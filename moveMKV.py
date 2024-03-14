import os
import shutil

def move_mkv_files(source_dir, destination_dir):
    # Überprüfe, ob das Zielverzeichnis existiert, andernfalls erstellen
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Durchsuche des Quellverzeichnisses und seiner Unterordner
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.mkv'):
                source_file_path = os.path.join(root, file)
                destination_file_path = os.path.join(destination_dir, file)
                # Überprüfe, ob die Datei bereits existiert, und sie ggf. umbenennen
                if os.path.exists(destination_file_path):
                    filename, file_extension = os.path.splitext(file)
                    i = 1
                    while os.path.exists(os.path.join(destination_dir, f"{filename}_{i}{file_extension}")):
                        i += 1
                    destination_file_path = os.path.join(destination_dir, f"{filename}_{i}{file_extension}")
                # Verschieben der Datei in das Zielverzeichnis
                shutil.move(source_file_path, destination_file_path)
                print(f"Moved {file} to {destination_file_path}")

# Beispielaufruf
source_directory = '/path/to/subfolders'
destination_directory = '/path/destination'
move_mkv_files(source_directory, destination_directory)
