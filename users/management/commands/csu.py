from django.core.management import BaseCommand
from pathlib import Path
from dotenv import load_dotenv
import os
from users.models import User

BASE_DIR = Path(__file__).resolve().parent.parent

dot_env = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=dot_env)


class Command(BaseCommand):
    help = "Создание учётки админа"

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("ADMIN_EMAIL"),
            is_active=True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(os.getenv("ADMIN_PASS"))
        user.save()
