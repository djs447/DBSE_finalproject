import os
import shutil

def backup_store(nodeid):
    source_folder = 'chaindata%s/' % (nodeid)
    destination_folder = 'backup_chaindata%s/' % (nodeid)
    #check that the backup folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    clear_contents(destination_folder)

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

def clear_contents(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                clear_contents(file_path)
        except:
            print(f"Failed to delete {file_path}.")