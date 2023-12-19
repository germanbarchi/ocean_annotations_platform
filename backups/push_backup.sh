#!/bin/bash

cp /home/ubuntu/ocean_annotations_platform/pair_comparison/management/commands/data.pkl /home/ubuntu/ocean_annotations_platform/backups
python manage.py dumpdata pair_comparison > /home/ubuntu/ocean_annotations_platform/backups/updated_data.pkl

cd /home/ubuntu/ocean_annotations_platform
git add . 
git commit -m 'update_backup'
git push origin main