import os
import shutil
import numpy as np

def split_train_test(path, ratio,output_dir_path): #列出当前文件从夹下的所有文件名称,包括文件跟文件夹 
    files = os.listdir(path) 
    train_path = os.path.join(output_dir_path, 'train') 
    test_path = os.path.join(output_dir_path, 'test') 
    if not os.path.isdir(train_path): #已存在的目录新建会报错 
        os.mkdir(train_path) 
    if not os.path.isdir(test_path): 
        os.mkdir(test_path) 
    np.random.shuffle (files) 
    test_num= int(len(files)*ratio) 
    test_files = files [test_num:] 
    train_files = files[:test_num]
    for file in train_files:
        shutil.copy(os.path.join(path,file),train_path)
    for file in test_files:
        shutil.copy(os.path.join(path,file),test_path)

    
split_train_test('img',0.8,'1')

