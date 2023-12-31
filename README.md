##  Generate Abstract Random Images with Python

When we study image processing or computer vision algorithms, sometimes we may want to test them on unnatural abstarct synthetic images.

This repo shows a way to generate interesting abstract random images in python.

Run the following command line, then you will get 200 color images under ```./color_images_outcome/``` and 200 grayscale images under ```./grayscale_images_outcome/```:
```
python ./generate_abstract_images.py
```
Some interesting images generated are displayed as below.

### Generated Color Images 

<img src="color_images_outcome/saved_img_seed40.jpg" alt="seed 40" width="240" height="240"> <img src="color_images_outcome/saved_img_seed41.jpg" alt="seed 41" width="240" height="240">  <img src="color_images_outcome/saved_img_seed37.jpg" alt="seed 37" width="240" height="240">  
<img src="color_images_outcome/saved_img_seed23.jpg" alt="seed 23" width="240" height="240"> <img src="color_images_outcome/saved_img_seed139.jpg" alt="seed 139" width="240" height="240">  <img src="color_images_outcome/saved_img_seed35.jpg" alt="seed 35" width="240" height="240">     
<img src="color_images_outcome/saved_img_seed6.jpg" alt="seed 6" width="240" height="240"> <img src="color_images_outcome/saved_img_seed15.jpg" alt="seed 15" width="240" height="240">  <img src="color_images_outcome/saved_img_seed146.jpg" alt="seed 146" width="240" height="240">      
<img src="color_images_outcome/saved_img_seed97.jpg" alt="seed 97" width="240" height="240"> <img src="color_images_outcome/saved_img_seed101.jpg" alt="seed 101" width="240" height="240">  <img src="color_images_outcome/saved_img_seed107.jpg" alt="seed 107" width="240" height="240">      
<img src="color_images_outcome/saved_img_seed0.jpg" alt="seed 0" width="240" height="240"> <img src="color_images_outcome/saved_img_seed77.jpg" alt="seed 77" width="240" height="240">  <img src="color_images_outcome/saved_img_seed133.jpg" alt="seed 133" width="240" height="240">      
<img src="color_images_outcome/saved_img_seed128.jpg" alt="seed 128" width="240" height="240"> <img src="color_images_outcome/saved_img_seed166.jpg" alt="seed 166" width="240" height="240">  <img src="color_images_outcome/saved_img_seed81.jpg" alt="seed 81" width="240" height="240">     

### Generated Grayscale Images

<img src="grayscale_images_outcome/saved_img_seed5.jpg" alt="seed 5" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed6.jpg" alt="seed 6" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed18.jpg" alt="seed 18" width="240" height="240">    
<img src="grayscale_images_outcome/saved_img_seed26.jpg" alt="seed 26" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed27.jpg" alt="seed 27" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed33.jpg" alt="seed 33" width="240" height="240">   
<img src="grayscale_images_outcome/saved_img_seed30.jpg" alt="seed 30" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed47.jpg" alt="seed 47" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed49.jpg" alt="seed 49" width="240" height="240">  
<img src="grayscale_images_outcome/saved_img_seed55.jpg" alt="seed 55" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed51.jpg" alt="seed 51" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed57.jpg" alt="seed 57" width="240" height="240">  
<img src="grayscale_images_outcome/saved_img_seed190.jpg" alt="seed 190" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed158.jpg" alt="seed 158" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed71.jpg" alt="seed 71" width="240" height="240">   
<img src="grayscale_images_outcome/saved_img_seed90.jpg" alt="seed 90" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed107.jpg" alt="seed 107" width="240" height="240"> <img src="grayscale_images_outcome/saved_img_seed166.jpg" alt="seed 166" width="240" height="240">   

Looks not bad, euh?    

**NOTE:  Above are just picked from those 200 images generated with random seed from 0 to 199. To try more different random seeds will surely get many more interesting and appealing images.**    

[Reference1] code adapted from https://www.reedbeta.com/blog/generating-abstract-images-with-random-functions/     
[Reference2] https://gamedev.stackexchange.com/questions/32274/how-can-i-create-beautiful-random-abstract-images

