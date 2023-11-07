from django.core.management.base import BaseCommand, CommandError
from pair_comparison.models import Audio, Annotation
from django.contrib.auth.models import User

import numpy as np
import pandas as pd
from tqdm import tqdm
import os
import joblib

class Command(BaseCommand):
    help = ''
        
    def add_arguments(self, parser):
        parser.add_argument('--N', help='Amount of audios per user', type=int, required=True)
    
    def handle(self, *args, **options):
        """
        - Hacer que contemple anotaciones de free speech o de lectura
        (por ahora lo hacemos solo con free speech)
        - Hacer que revise si no hay usuarios nuevos. Si hay, agregarlos
        """
        data_path = os.path.join(os.getcwd(), 'pair_comparison', 'management', 'commands', 'data.pkl')
        if os.path.exists(data_path):
            self.stdout.write(self.style.SUCCESS("Using existing data.pkl"))
            data = pd.read_pickle(data_path)            
        else:
            pairs = []
            audios = list(Audio.objects.all())
            
            #from IPython import embed; embed()

            for i in range(len(audios)-1):
                for j in range(i+1, len(audios)):
                    pair_id = f"{audios[i].name.split('_')[3]}_{audios[j].name.split('_')[3]}"
                    print(pair_id)
                    pairs.append({'user' : None, 
                                    'audio_A' : audios[i],
                                    'audio_B' : audios[j], 
                                    'order' : None, 
                                    'pair_id': pair_id, 
                                    'annotated': False})
            data = pd.DataFrame(pairs)
            data = data.set_index('pair_id')
        for user in tqdm(User.objects.all()):
            if user.is_superuser:
                continue
            while len(data[data.annotated == False]) < options['N']:
                options['N'] -= 1
                if options['N'] == 0:
                    self.stdout.write(self.style.ERROR(f"There is no more data to annotate for user {user.username}"))
                    continue
            for i in range(1, options['N']+1):
                this_pair = data[data.annotated == False].sample()
                this_pair = data.loc[this_pair.index].squeeze()
                order = data[(data.annotated == True)&(data.user == user)].count().min() + 1
                form = Annotation.objects.create(user = user,
                                                 audio_A = this_pair.audio_A,
                                                 audio_B = this_pair.audio_B,
                                                 order = order)
                form.save()
                data.loc[this_pair.name, 'annotated'] = True
                data.loc[this_pair.name, 'user'] = user
                data.loc[this_pair.name, 'order'] = order      
        data.to_pickle(data_path)
        joblib.dump(data,'/home/ubuntu/ocean_annotations_platform/pair_comparison/management/commands/data_joblib.pkl')