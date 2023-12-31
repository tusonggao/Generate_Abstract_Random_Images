# https://gamedev.stackexchange.com/questions/32274/how-can-i-create-beautiful-random-abstract-images
# code adapted from https://www.reedbeta.com/blog/generating-abstract-images-with-random-functions/

import os
import random
import time
import numpy as np 
import cv2
import matplotlib
import matplotlib.pyplot as plt

def load_image(img_file_path):
    img_data = cv2.imread(img_file_path)[...,::-1].copy()
    return img_data

def show_image(img_data, img_title=None):
    plt.imshow(img_data)
    if img_title is not None and type(img_title)==str:
        plt.title(img_title)
    plt.axis('off')
    plt.show()

def save_image(img_data, save_file_name='saved_img.jpg'):
    matplotlib.image.imsave(save_file_name, img_data)
    
dX, dY, NC = 256, 256, 3
depthMin, depthMax = 3, 10
xArray, yArray = None, None

def randColor():
    global NC, dX, dY
    randv = np.array([random.random() for i in range(NC)]).reshape((1, 1, NC))
    randv = np.repeat(randv, dX, axis=0)
    randv = np.repeat(randv, dY, axis=1)
    assert randv.shape==(dX, dY, NC)
    return randv

def getX(): 
    global xArray
    assert xArray is not None
    return xArray

def getY(): 
    global yArray
    assert yArray is not None
    return yArray

def scale(x):
    scale_ratio = random.random() * 2 - 1.0
    return x * scale_ratio

def sigmoid(x, T=1):
    return 1 / (1 + np.exp(-x*T))

def safeDivide(a, b):
    b = np.where(np.logical_and(b>0, b<1e-5), 1e-5, b)
    b = np.where(np.logical_and(b<0, b>-1e-5), -1e-5, b)
    outcome = np.divide(a, b)
    return outcome

functions = [(0, randColor),
             (0, getX),
             (0, getY),
             (1, scale),
             (1, np.tanh),
             (1, np.sin),
             (1, np.cos),
             (1, sigmoid),
             (1, np.abs),
             (2, np.add),
             (2, np.subtract),
             (2, np.multiply),
             (2, safeDivide),
]

def buildImg(depth=0):
    funcs = [f for f in functions if 
                (f[0] > 0 and depth < depthMax) or
                (f[0] == 0 and depth >= depthMin)]
    nArgs, func = random.choice(funcs)
    args = [buildImg(depth + 1) for n in range(nArgs)]
    return func(*args)

# if you want grayscale image, set channel_num=1
def generate_abstract_img(x_dim=256, y_dim=256, channel_num=3, seed=None):
    global xArray, yArray, dX, dY, NC 
    dX, dY, NC = x_dim, y_dim, channel_num
    
    if seed is not None:
        random.seed(seed)

    start_t = time.time()
    xArray = np.linspace(-1.0, 1.0, dX).reshape((1, dX, 1))
    xArray = np.repeat(xArray, NC, axis=2)
    xArray = np.repeat(xArray, dY, axis=0)
    yArray = np.linspace(-1.0, 1.0, dY).reshape((dY, 1, 1))
    yArray = np.repeat(yArray, NC, axis=2)
    yArray = np.repeat(yArray, dX, axis=1)
    assert xArray.shape == yArray.shape == (dX, dY, NC)
    
    try_cnt = 0
    while True:
        try_cnt += 1
        img = buildImg(depth=0)
        img = sigmoid(img)
        img = np.round(img.clip(0.0, 1.0) * 255.0).astype('uint8')
        # if the pixel values in a very small range, not an interesting image,
        # loop to generate another one
        if (img.max() - img.min()) >= 15:  
            break
            
    if channel_num == 1:
        img = img.squeeze(-1)  # squeeze the last axis of grayscale image
    print(f'in generate_abstract_img() img.shape: {img.shape}, img.min: {img.min()}, img.max: {img.max()} '
          f'try_cnt: {try_cnt} cost time: {time.time()-start_t:.5f} sec')
    return img


if __name__ == '__main__':
    generate_num = 200

    images_output_dir = './color_images_outcome/'
    if not os.path.exists(images_output_dir):
        os.makedirs(images_output_dir)
        
    for seed in range(generate_num):
        img = generate_abstract_img(channel_num=3, seed=seed)
        save_image(img, save_file_name=f'{images_output_dir}/saved_img_seed{seed}.jpg')
        print(f'color image with seed {seed} generated !!!')

    images_output_dir = './grayscale_images_outcome/'
    if not os.path.exists(images_output_dir):
        os.makedirs(images_output_dir)
        
    for seed in range(generate_num):
        img = generate_abstract_img(channel_num=1, seed=seed)
        save_image(img, save_file_name=f'{images_output_dir}/saved_img_seed{seed}.jpg')
        print(f'grayscale image with seed {seed} generated !!!')



