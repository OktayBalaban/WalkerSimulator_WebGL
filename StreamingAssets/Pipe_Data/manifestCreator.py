import os

def create_manifest(directory):
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    manifest_path = os.path.join(directory, 'CSV_List.txt')

    with open(manifest_path, 'w') as manifest_file:
        for file in csv_files:
            manifest_file.write(file + '\n')

    print(f'Manifest created with {len(csv_files)} files.')

# Use the current directory
directory_path = os.getcwd()
create_manifest(directory_path)
