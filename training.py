import os
os.environ["CUDA_VISIBLE_DEVICES"] = '0'
from keras import optimizers
from keras import applications
from keras.models import Sequential, Model
from keras.callbacks import ModelCheckpoint
from keras.layers import Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.losses import binary_crossentropy
# from keras.utils import multi_gpu_model
# from keras.optimizers import Adam
from config import *

opt=optimizers.SGD(lr=lr, momentum=momentum)

def training():
    '''
    training
    :return:
    '''
    base_model = applications.VGG16(weights=pweight_path, include_top=False,
                                input_shape=(img_width, img_height, 3))  # 预训练的VGG16网络
    #固定前几层权值
    for layer in base_model.layers[:freeze]: layer.trainable = False
    #自定义网络
    top_model = Sequential()  # 自定义顶层网络
    top_model.add(Flatten(input_shape=base_model.output_shape[1:]))  # 展平
    top_model.add(Dense(4096, activation='relu')) #全连接层
    top_model.add(Dropout(0.5))  # Dropout概率0.5
    top_model.add(Dense(4096, activation='relu'))
    top_model.add(Dropout(0.5))  # Dropout概率0.5
    top_model.add(Dense(OUTPUT_NUM, activation='sigmoid'))  # 二分类
    #组装网络
    model = Model(inputs=base_model.input, outputs=top_model(inputs=base_model.output))
    #损失函数与优化器
    model.compile(loss=binary_crossentropy, optimizer=opt,
                  metrics=['accuracy'])
    print(base_model.summary())
    # 数据预处理器
    train_datagen = ImageDataGenerator(rescale=1. / 255, #归一化
                                       width_shift_range=0.1,
                                       height_shift_range=0.1,
                                       horizontal_flip=True)
    val_datagen = ImageDataGenerator(rescale=1. / 255)
    #数据生成器
    train_generator = train_datagen.flow_from_directory(traindata_dir, target_size=(img_height, img_width),
                                                        batch_size=batch_size, class_mode='binary')
    val_generator = val_datagen.flow_from_directory(valdata_dir, target_size=(img_height, img_width),
                                                            batch_size=batch_size, class_mode='binary',
                                                            shuffle=False)
    # 保存模型
    filepath = os.path.join(saved_models, "model_{epoch:02d}-{val_acc:.2f}.hdf5")
    checkpointer = ModelCheckpoint(filepath=filepath, monitor='val_acc', verbose=1, save_best_only=True)
    #模型训练
    model.fit_generator(train_generator,
                        steps_per_epoch=train_samples // batch_size,
                        epochs=epochs,
                        validation_data=val_generator,
                        validation_steps=validation_samples // batch_size,
                        verbose=2,
                        callbacks=[checkpointer],
                        initial_epoch=start_epoch)

if __name__ == '__main__':
    training()



