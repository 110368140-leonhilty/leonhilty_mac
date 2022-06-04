import glob
# glob 可以過濾資料
def print_dir_scores(dirname):
    for filename in glob.glob(dirname+r'/*.json'):
        print('讀取檔案：',filename)



print_dir_scores('F1750_exercises/py/data/scores')