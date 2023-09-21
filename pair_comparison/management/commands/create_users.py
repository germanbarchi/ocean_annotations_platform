from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create user for test the app'

    def add_arguments(self, parser):
        parser.add_argument('-user','--username', help='Username to create')
        parser.add_argument('-pass','--password', help='Password for the user')
        parser.add_argument('-l', '--list', help='List the existing users', action='store_true')

    def handle(self, *args, **options):
        if (not options['username']) or (not options['password']):
            self.stdout.write(self.style.ERROR("You have to to specify both username and password. Try create_users --help"))
        else:
            user, created = User.objects.get_or_create(username=options['username'])
            if not created:
                self.stdout.write(self.style.ERROR('User '+options['username']+' already exist'))
            else:
                user.set_password(options['password'])
                user.save()
                self.stdout.write(self.style.SUCCESS('User '+options['username']+' has been created.'))
        if options['list']:
            self.stdout.write('#'*10+' List of users '+'#'*10)
            _ = [self.stdout.write('- '+user.username) for user in User.objects.all()]