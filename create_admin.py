import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sayt.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'adminjon'
password = 'Uzbekistan_2026!'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email='', password=password)
    print("=== SUPERUSER RAILWAY'DA MUVAFFAQIYATLI YARATILDI ===")
else:
    print("=== BU SUPERUSER ALLAQACHON MAVJUD ===")