from django.db.models.signals import post_save  # It is get To Exextute Query at Save method
from django.contrib.auth.models import User
from django.dispatch import receiver    # Recivers For Signals 
from .models import profile # Importing profile Model from models.py

# This Function Will run Everytime user gets created
@receiver(post_save, sender=User)    # 
def create_profile(sender, instance, created, **kwargs) :   # **kwargs accepts any Extra Keywords we Provide
    if created :
        profile.objects.create(user=instance)


# This Function Will run Everytime user gets created
#
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs) :
    instance.profile.save()

