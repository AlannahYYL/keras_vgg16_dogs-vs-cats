import os
#gpu
gpu_nums=1
# batchsize
batch_size = 4
# epoch
epochs = 15
#lr
lr=0.0001
momentum=0.9
# 样本数
train_samples = 22000
validation_samples = 3000
#pre_weight
pweight_path='pre_weight/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5'
#开始轮数
start_epoch=0
#尺寸
img_width=224
img_height=224
#训练冻结
freeze=10
#ouput neuron
OUTPUT_NUM=1
#类别
CAT_CATE='cat'
DOG_CATE='dog'
#是否训练
Train = True
#数据地址
# root_data_path = curPath = os.path.abspath(os.path.dirname(__file__))#项目路径
root_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))#获取项目的根目录
ori_data_path = r'/root/YYL/VGG16_cat_dog/data_VGG16_min_cats_dogs/ori/train'#原始数据文件路径
val_data_path = r'data/val'
train_data_path = r'data/train'
test_data_path = r'test_img'
res_data_path = r'res_img'
# logs_path = 'logs'
saved_models = 'saved_models'
data_dir='data_VGG16_min_cats_dogs'
# 训练集目录
traindata_dir = os.path.join(root_data_path,data_dir,train_data_path)
# 验证集目录
valdata_dir = os.path.join(root_data_path,data_dir,val_data_path)