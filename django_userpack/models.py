"""
userpack user models
"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class AdvancedBaseUser(AbstractUser):
    def avatar_upload_path(instance,filename):
        return f"users/avatars/{filename}"
    email = models.EmailField(verbose_name=_("email"),unique=True)
    phone_number = models.CharField(verbose_name=_("Phone number"),blank=True,null=True,unique=True)
    national_code = models.CharField(verbose_name=_("National code"),blank=True,null=True,unique=True)
    verify_date = models.DateTimeField(verbose_name=_("Verify date"))
    is_verify = models.BooleanField(verbose_name=_("Verify"),default=False)
    bio = models.TextField(verbose_name=_("Bio"),blank=True,null=True)
    short_bio = models.CharField(verbose_name=_("Short bio"),max_length=70)
    avatar = models.ImageField(verbose_name=_("Avatar"),upload_to=avatar_upload_path)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_short_name(self):
        return f"{self.first_name}"
    def get_advanced_name(self):
        return f"{self.first_name} {self.last_name}-{self.short_bio}"

    def __str__(self):
        return f"{self.first_name}"
    
    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        abstract = True
        ordering = ["first_name","last_name","-date_joined","-last_login","-verify_date"]