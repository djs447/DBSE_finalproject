import os
import shutil

def backup_store():
    source_folder = 'chaindata/'
    destination_folder = 'backup_chaindata/'
    #check that the backup folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")

def backup_load():
    source_folder = 'backup_chaindata/'
    destination_folder = 'chaindata/'
    #check that the backup folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")