Multimedia Project
===================

This project is made to implement 2 image processing algorithm: Gaussian filter and Sobel Edge Detection.

## 1. Gaussian filter

#### Description

Gaussian filtering is used to blur images and remove noise and detail.

#### Steps Involved
- Calculate the Gaussian kernel using the fomula of ["normal distribution"](https://en.wikipedia.org/wiki/Normal_distribution)
- Apply Grayscale to the image
- Add padding to the image (padding size is according to the kernel size)
- Convolve the padded image with gaussian kernel

#### Result

![canny result](https://github.com/tranvanthanh99/mutimedia-project/blob/master/static/img/gaussian-result.png)


#### How to run
-------------

This program depends on the following packages:

 - opencv-python
 - Matplotlib
 - NumPy
 - argparse

Execute the script with:
```bash
python gaussian_smoothing.py -i/--image <input image path>
```

## 2 Sobel edge detection

#### Description

Sobel edge detection is used in image processing and computer vision, particularly within edge detection algorithms where it creates an image emphasising edges.

#### Steps Involved
- Apply Gaussian filter to smooth out the image
- Convole the given image with vertical and horizontal derivative kernel
- Find intensity gradients by combining both the vertical and horizontal edges (derivatives)

#### Result

![canny result](https://github.com/tranvanthanh99/mutimedia-project/blob/master/static/img/sobel-result.png)


#### How to run
-------------

This program depends on the following packages:

 - opencv-python
 - Matplotlib
 - NumPy
 - argparse

Execute the script with:
```bash
python sobel.py -i/--image <input image path>
```

## 3. Demo web

#### Description

A demo web page for the two algorithm

#### Result

![canny result](https://github.com/tranvanthanh99/mutimedia-project/blob/master/static/img/demo-result.png)


#### How to run
-------------

This program depends on the following packages:

 - Flask (framework)
 - opencv-python
 - Matplotlib
 - NumPy
 - argparse

Run the web on localhost:8000 with:
```bash
python app.py
```
