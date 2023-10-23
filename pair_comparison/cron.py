
from django.core import management
from django.conf import settings
from pathlib import Path
import subprocess, datetime


def annotations_backup():
    backup_path = Path(settings.BASE_DIR, 'backups')
    curr_backup = Path(backup_path, datetime.datetime.now().strftime("%Y_%m_%d__%H:%M:%S.json"))
    management.call_command('dumpdata', 'annotations' , 'auth', 'annotations', indent = 4, output= curr_backup)
    #rc = subprocess.call(Path(backup_path, "push_backup.sh"))
    
    

