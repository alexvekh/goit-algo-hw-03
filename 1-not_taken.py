import os
import argparse
import shutil

def copy_files(source_dir, dest_dir=None):
  """ Функція рекурсивно копіює файли з вихідної директорії до нової директорії, сортуючи їх у піддиректорії за розширенням.
      Args:  source_dir: Шлях до вихідної директорії.
             dest_dir: Шлях до директорії призначення (за замовчуванням ./dist).  """
  
  if not os.path.exists(source_dir):
    print(f'Sorry. Directory {source_dir} does not exist.')

  if not dest_dir:
    dest_dir = os.path.join(os.path.dirname(source_dir), 'dist')

  os.makedirs(dest_dir, exist_ok=True)

  # The nested loop structure ensures that the os.walk function is called recursively for each subdirectory encountered
  for root, _, files in os.walk(source_dir):
    for file in files:
      # Отримання розширення файлу
      filename, extension = os.path.splitext(file)

      # Створення шляху до піддиректорії
      sub_dir = os.path.join(dest_dir, extension[1:])
      os.makedirs(sub_dir, exist_ok=True)

      # Копіювання файлу
      source_path = os.path.join(root, file)
      dest_path = os.path.join(sub_dir, file)
      try:
        shutil.copy(source_path, dest_path)
        print(f"File {file} copied to {sub_dir} successfully")
      except OSError as e:
        print(f'Error copying file {source_path}: {e}')

if __name__ == '__main__':
  # Створення об'єкта аргументів командного рядка
  parser = argparse.ArgumentParser(description='Script to copy files.')
  # Додавання аргументів
  parser.add_argument('source_dir', help='Path to the source directory.')
  parser.add_argument('dest_dir', nargs='?', help='Path to the destination directory. Default: ./dist', default='./dist')
  # Обробка аргументів
  args = parser.parse_args()
  # Виклик функції копіювання файлів
  copy_files(args.source_dir, args.dest_dir)