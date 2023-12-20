# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import shutil


def desktop_clean():
    # returns the desktop path
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

    # list of type files and folders names
    file_types = {
        'Applications': ('.exe',),
        'ExcelSheets': ('.xlsx', '.csv'),
        'Documents': ('.docx', '.txt', '.pdf', '.odt'),
        'ZipFolders': ('.zip', '.rar'),
        'SqlFiles': ('.sql',),
        'Images': ('.jpg', '.jpeg', '.png', '.gif'),
        'Videos': ('.mp4', '.mov', '.mkv'),
        'Music': ('.mp3', '.wav', '.flac'),
        'Folders': (),
        'Others': ()
    }

    # making folders if not exist
    for folder_name in file_types.keys():
        folder_path = os.path.join(desktop_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    new_folders = set([folder_name.lower() for folder_name, ex in file_types.items()])

    # put file to good folder
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        moved = False
        # Sprawdz, czy to jest folder i nie jest ukryty
        if (os.path.isdir(file_path)) and (not filename.startswith('.')) and (filename.lower() not in new_folders):
            destination_folder = os.path.join(desktop_path, 'Folders')
            shutil.move(file_path, destination_folder)
            print(f'Moved FOLDER: {filename} to *Folders*')
            moved = True
        else:
            for folder_name, extensions in file_types.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    destination_folder = os.path.join(desktop_path, folder_name)
                    shutil.move(file_path, destination_folder)
                    print(f'Moved: {filename} to *{folder_name}*')
                    moved = True
                    break

        # Jeśli nie pasuje do żadnej kategorii, przenieś do foldera "Others"
        if not moved and (filename.lower() not in new_folders):
            destination_folder = os.path.join(desktop_path, 'Others')
            shutil.move(file_path, destination_folder)
            print(f'Moved: {filename} to *Others*')


if __name__ == '__main__':
    desktop_clean()
