from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    ADMIN_EMAIL = 'admin@mail.com'
    ADMIN_PASSWORD = 'adminpassword'
    help = 'Update or create development admin user.'

    def handle(self, *args, **options):
        user_model = get_user_model()

        user, _ = user_model.objects.update_or_create(
            email=self.ADMIN_EMAIL,
            defaults={
                'is_staff': True,
                'is_active': True,
                'is_superuser': True,
            },
        )
        user.set_password(self.ADMIN_PASSWORD)
        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully create development admin user.\n'
                f'Email: {self.ADMIN_EMAIL}\n'
                f'Password: {self.ADMIN_PASSWORD}'
            )
        )
