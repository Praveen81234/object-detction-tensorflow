# Object Detection using TensorFlow

## Overview

This project was completed as part of the **1Stop AI Training Program**. It demonstrates how TensorFlow and Computer Vision techniques can be used to detect and classify objects in images. The project includes dataset preparation, model training, evaluation, and prediction.

## Features

- Object detection in images
- Image preprocessing
- TensorFlow-based model training
- Model evaluation
- Prediction on custom images
- Bounding box detection
- Confidence score generation

## Technologies Used

- Python
- TensorFlow
- OpenCV
- NumPy

## Project Structure

```
object-detection-tensorflow/
│── data_preparation.py
│── train.py
│── evaluate.py
│── predict.py
│── model.py
│── requirements.txt
│── README.md
```

## Setup

1. Install the required dependencies:

```bash
pip install -r requirements.txt
```

2. Download the required object detection dataset.

3. Place the dataset inside:

```
data/all_images/
```

organized according to the project requirements.

4. Prepare the dataset:

```bash
python data_preparation.py
```

5. Train the model:

```bash
python train.py
```

6. Evaluate the trained model:

```bash
python evaluate.py
```

7. Predict objects in a new image:

```bash
python predict.py path_to_image.jpg
```

## Learning Outcomes

- Learned image preprocessing techniques.
- Understood the TensorFlow object detection workflow.
- Explored model training and evaluation.
- Learned how object detection models identify and classify objects.
- Gained experience working with Computer Vision concepts.

## Note

This is a **guided project** completed during the **1Stop AI Training Program** for educational and learning purposes. The project demonstrates the complete workflow of an object detection system using TensorFlow.
