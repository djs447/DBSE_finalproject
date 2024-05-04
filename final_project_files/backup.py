import os
import shutil

def backup_store(nodeid):
    source_folder = 'chaindata%s/' % (nodeid)
    destination_folder = 'backup_chaindata%s/' % (nodeid)
    #check that the backup folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")

def backup_load(nodeid):
    source_folder = 'backup_chaindata%s/' % (nodeid)
    destination_folder = 'chaindata%s/' % (nodeid)
    #check that the backup folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_file = os.path.join(source_folder, filename)
        destination_file = os.path.join(destination_folder, filename)

        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")