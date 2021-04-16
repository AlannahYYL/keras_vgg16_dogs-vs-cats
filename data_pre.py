'''
数据预处理，将数据分为训练集、测试集
原train文件中共有猫狗图片各12500，将其中前10000用作训练集，2500用作测试集
'''
from config import *
import os
import shutil
def div_dataset(ori_path,val_path,train_path):
    '''
    划分数据集
    :param ori_path:
    :param test_path:
    :param train_path:
    :return:
    '''
    cat_num=0
    dog_num=0
    train_num=0
    test_num=0
    cat_val_path =os.path.join(val_path,CAT_CATE)
    dog_val_path =os.path.join(val_path,DOG_CATE)
    cat_train_path =os.path.join(train_path,CAT_CATE)
    dog_train_path =os.path.join(train_path,DOG_CATE)
    if not os.path.exists(cat_val_path):
        os.makedirs(cat_val_path)
    if not os.path.exists(dog_val_path):
        os.makedirs(dog_val_path)
    if not os.path.exists(cat_train_path):
        os.makedirs(cat_train_path)
    if not os.path.exists(dog_train_path):
        os.makedirs(dog_train_path)
    for root, dirs, files in os.walk(ori_path):
        for filename in files:
            # print(filename)
            ori_file = os.path.join(ori_path, filename)
            filename_l = filename.split('.')
            cate = filename_l[0]
            if cate==CAT_CATE:
                cat_num+=1
            else:
                dog_num+=1
            nums = filename_l[1]
            if int(nums)<11000:
                train_num+=1
                train_file = os.path.join(train_path, cate, filename)
                print(train_file)
                shutil.copy(ori_file,train_file)
            else:
                test_num+=1
                val_file = os.path.join(val_path, cate, filename)
                print(val_file)
                shutil.copy(ori_file,val_file)
    print('cat总共{}张'.format(cat_num))
    print('dog总共{}张'.format(dog_num))
    print('train总共{}张'.format(train_num))
    print('val总共{}张'.format(test_num))
    print('Done')


if __name__ == '__main__':
    if not os.path.exists(valdata_dir):
        os.makedirs(valdata_dir)
    if not os.path.exists(traindata_dir):
        os.makedirs(traindata_dir)
    div_dataset(ori_data_path,valdata_dir,traindata_dir)