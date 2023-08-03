import os
from os.path import join, getsize
import json
import csv
import pickle

def file_size():  # функция для определения размеров файлов
    dict_file = {}  # словарь: путь к файлу - размер
    for root, dirs, files in os.walk('.'):
        for file_name in files:
            size_file = os.path.getsize(os.path.join(root, file_name))
            dict_file[f'File{os.path.join(root, file_name)}'] = size_file
    return dict_file


def dir_size():                                 # функция для определения размеров папок
    dict_dir = {}                                  # словарь: путь к папке - размер
    for root, dirs, files in os.walk('.', topdown=False):
        size = sum(getsize(join(root, f)) for f in files)
        size += sum(dict_dir[f'Directory{join(root, d)}'] for d in dirs)
        dict_dir[f'Directory{root}'] = size
    for path, total_size in sorted(dict_dir.items(), key=lambda x: x[0]):
        return dict_dir


general_dict = dict(list(file_size().items()) + list(dir_size().items()))  # словарь из файлов и папок
list_general_dict = list(general_dict)

with open('result.json', 'w') as fp:
    json.dump(general_dict, fp, indent=2)

with open('result.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in general_dict.items():
        writer.writerow([key, value])

with open('result.pickle', 'wb') as pic_file:
    pickle.dump(general_dict, pic_file, protocol=pickle.HIGHEST_PROTOCOL)

print(general_dict)

