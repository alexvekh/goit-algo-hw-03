# python 1.py source_dir dest_dir

from pathlib import Path
import os
import argparse
import shutil

def copy_files_by_ext(source_dir, dest_dir) -> None:
  files = os.listdir(source_dir)
  print(source_dir, files)
  for file in files:
    if os.path.isdir(os.path.join(source_dir, file)):
      print(f"Found directory: {file}")
      copy_files_by_ext(os.path.join(source_dir, file), dest_dir)    ###   <---  Рекурсія   
    else:
      filename, extension = os.path.splitext(file)
      print(f"Processing file: {filename}{extension}")
      sub_dir = os.path.join(dest_dir, extension[1:])
      if not os.path.exists(sub_dir):
        os.makedirs(sub_dir, exist_ok=True)

      # Копіювання файлу
      source_path = os.path.join(source_dir, file)
      dest_path = os.path.join(sub_dir, file)

      if not os.path.exists(dest_path):
        try:
          shutil.copy(source_path, dest_path)
          print(f"File '{file}' copied to '{sub_dir}' successfully.")
        except OSError as e:
          print(f'Error copying file {source_path}: {e}')
      else:
        print(f"File '{file}' already exists in '{sub_dir}'. Skipping copy.")


if __name__ == '__main__':
  # Парсинг аргументів командного рядка
  parser = argparse.ArgumentParser(description='Script to copy files.')
  parser.add_argument('source_dir', help='Path to the source directory.')
  parser.add_argument('dest_dir', nargs='?', help='Path to the destination directory. Default: ./dist', default='./dist')
  args = parser.parse_args()

  source_dir = Path(args.source_dir)
  dest_dir = Path(args.dest_dir)

  # Check for exist source dir
  if not os.path.exists(source_dir):
    print(f'Sorry. Directory {source_dir} does not exist.')
  
  # Create dest dir(if need)
  try:
    os.makedirs(dest_dir, exist_ok=True)
    print(f"Directory {dest_dir} is ready.")
  except OSError as e:
    print(f"Error creating directory: {e}")
  
  # Call copy func
  copy_files_by_ext(source_dir, dest_dir)