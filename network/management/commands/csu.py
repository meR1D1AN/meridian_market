from django.core.management import BaseCommand
from django.contrib.auth import get_user_model
from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):
    help = "Создание учётки админа"

    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="admin",
            first_name="Admin",
            email=os.getenv("ADMIN_EMAIL"),
            is_active=True,
            password=os.getenv("ADMIN_PASS"),
        )
        user.save()
