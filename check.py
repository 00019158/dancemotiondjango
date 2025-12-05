import django
from django.conf import settings

django.setup()

print("BASE_DIR =", settings.BASE_DIR)
print("INSTALLED_APPS =", settings.INSTALLED_APPS)
