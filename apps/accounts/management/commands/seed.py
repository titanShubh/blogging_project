from django.core.management.base import BaseCommand
from apps.accounts.models import User

class Command(BaseCommand):
    help = "Seed default admin user"

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@example.com", "adminpass", role="admin")
            self.stdout.write(self.style.SUCCESS("Created admin/adminpass"))
        else:
            self.stdout.write("admin exists")
