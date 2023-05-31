import os
import shutil

print(len(os.listdir('./CNN/datasets/train')))

for i in os.listdir('./CNN/datasets/train'):
  if i == 'cat' or i == 'dog':
    continue
  if 'cat' in i:
    shutil.move('./CNN/datasets/train/' + i, './CNN/datasets/train/cat/' + i)
  elif 'dog' in i:
    shutil.move('./CNN/datasets/train/' + i, './CNN/datasets/train/dog/' + i)