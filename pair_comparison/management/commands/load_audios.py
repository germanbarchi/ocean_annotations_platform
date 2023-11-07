import glob
import os
from pathlib import Path
from tqdm import tqdm
import pandas as pd
import soundfile as sf
from django.core.files import File
from django.core.management.base import BaseCommand

from pair_comparison.models import Audio


class Command(BaseCommand):
    """
    TODO:
    - Sumar la opción de que se pueda elegir si se quieren cargar audios de lectura o de free speech
    """
    help = 'Load audio files to database'

    def add_arguments(self, parser):
        parser.add_argument('--path', help='Path to audios', type=str, required=True)

    def handle(self, *args, **options):
        speech_type = 'free' # 'lecture' or 'free'
        discard_ids = [1, 9, 13, 18, 29, 32, 33, 34, 46, 65, 82, 12, 14, 15, 16, 28, 58, 27, 69, 22, 41, 38, 54, 7, 53, 52]
        paths = glob.glob(os.path.join(options['path'],'*.wav'), recursive=True)
        for path in paths:
            if (speech_type not in path) or (int(path.split('/')[-1].split('_')[-3]) in discard_ids):
                self.stdout.write(self.style.ERROR(f'discarding audio {path}'))
                continue
            audio, sr = sf.read(path)
            sf.write('tmp.wav', audio, sr)
            name = f"{path.split('/')[-1]}"
            
            #from IPython import embed; embed()
            
            audio_object, created = Audio.objects.get_or_create(name=name)
            if created:
                with open('tmp.wav', mode='rb') as f:
                    audio_object.audiofile = File(f, name=name)
                    audio_object.speaker_id =  int(path.split('/')[-1].split('_')[-3])
                    audio_object.save()
            else:
                self.stdout.write(self.style.ERROR(f'"{name}" file already exist'))
        if Path('tmp.wav').is_file(): 
            os.remove('tmp.wav')
        n_files = len(glob.glob(os.path.join(os.getcwd(),'media','audios', '*.wav')))
        self.stdout.write(self.style.SUCCESS(f'Successfully loaded {n_files} audio files'))