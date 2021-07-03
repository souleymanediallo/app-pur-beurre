from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from PIL import Image


# CustomUser
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("L'email est obligatoire")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=100, unique=True, verbose_name="Pseudo")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    objects = MyUserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default="user.png", upload_to="photos", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 80 or img.width > 80:
            output_size = (80, 80)
            img.thumbnail(output_size)
            img.save(self.image.path)


def post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(post_save_receiver, sender=CustomUser)
