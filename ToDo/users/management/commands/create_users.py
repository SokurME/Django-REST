from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        super_user = User.objects.create_superuser('admin', 'admin@dfr.local', '123', firstname='admin',
                                                   lastname='admin')
        for i in range(3):
            user = User.objects.create_user(f'user{i}', f'user{i}@mail.ru', firstname=f'user{i}', lastname=f'user{i}')
