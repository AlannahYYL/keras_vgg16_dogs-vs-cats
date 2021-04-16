import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import cv2 as cv
import os
from config import *

def img_draw(res,img_file=''):
    img = cv.imread(img_file)
    if res[0][0] >= 0.5:
        text = DOG_CATE
    else:
        text = CAT_CATE
    cv.putText(img, text, (40, 60), cv.FONT_HERSHEY_PLAIN, 4.0, (0, 0, 255), 4)
    return img

def test():
    '''
    预测
    :return:
    '''
    #模型加载
    if not os.path.exists(res_data_path):
        os.makedirs(res_data_path)
    model_path = os.path.join(saved_models,'model_07-0.99.hdf5')
    model = load_model(model_path)
    #测试图片加载
    for root, dirs, files in os.walk(test_data_path):
        for filename in files:
            save_path = os.path.join(res_data_path,filename.split('.')[0]+'_res.jpg')
            img_file = os.path.join(test_data_path,filename)
            img_arr = image.load_img(img_file,target_size=(img_height,img_width))
            img_arr = image.img_to_array(img_arr)
            img_arr = img_arr[np.newaxis,:]
            res = model.predict(img_arr)
            # print(res)
            res = img_draw(res,img_file)
            cv.imwrite(save_path,res)
    pass
if __name__ == '__main__':
    test()
