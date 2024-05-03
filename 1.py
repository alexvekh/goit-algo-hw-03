# python 1.py source_dir dest_dir

from pathlib import Path
import os
import argparse
import shutil

def copy_files_by_ext(source_path: Path, dest_dir: Path) -> None:
  for child in source_path.iterdir():
    if child.is_dir():
      copy_files_by_ext(child, dest_dir)    ###   <---  Рекурсія   
    else:
      ext = child.suffix[1:]

      sub_dir = dest_dir/ext.lower()

      if not os.path.exists(sub_dir):
        os.makedirs(sub_dir, exist_ok=True)

      # Копіювання файлу
      source_file = source_path/child.name
      dest_file = sub_dir / child.name

      if not os.path.exists(dest_file):
        try:
          shutil.copy(source_file, dest_file)
          print(f"File '{child.name}' copied to '{sub_dir}' successfully.")
        except OSError as e:
          print(f'Error copying file {child}: {e}')
      else:
        print(f"File '{child.name}' already exists in '{sub_dir}'. Skipping copy.")


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