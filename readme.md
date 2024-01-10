# Face Frame - Basic Snap Studio
Face Frame is a desktop application created with the primary goal of refreshing Python skills and gaining practical experience with camera libraries. This project focuses on real-time face detection and age estimation, serving as a hands-on exploration of Python programming and camera-related libraries.

## Features

- Real-time Face Detection: Capture pictures with the added functionality of real-time face detection.

- Age Estimation: Capable to estimate user's age.

- User-Friendly Interface: The intuitive design and straightforward navigation make Face Frame accessible to users of all levels.

- OpenCV Integration: Powered by OpenCV for efficient image processing and reliable face detection.

## Required Packages

Make sure to install the following Python packages before running the application:

- [OpenCV](https://pypi.org/project/opencv-python/)

```bash
pip install opencv-python
```

- [Tkinter](https://docs.python.org/3/library/tkinter.html) (usually included with Python installations)

```bash
pip install tk
```

- [Numpy](https://numpy.org/)

```bash
pip install numpy
```

- [dlib](http://dlib.net/)```bash
pip install numpy

```bash
pip install dlib
```

## How to Run

Execute the following command in your terminal to start the Face Frame application:

Method 1 : Recommended (usual method)

```bash
cd app
python main.py
```

Method 2 : Docker

```bash
docker-compose build
docker-compose up
docker-compose down
```