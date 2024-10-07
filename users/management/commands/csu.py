from django.core.management import BaseCommand
from users.models import User
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):
    help = "Создание учётки админа"

    def handle(self, *args, **options):
        user = User.objects.create(
            name="Admin",
            email="admin@admin.ru",
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )
        user.set_password(os.getenv("ADMIN_PASS"))
        user.save()
