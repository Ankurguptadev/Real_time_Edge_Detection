# Real-Time Edge Detection using OpenCV

## Overview
This project demonstrates real-time edge detection using a webcam and OpenCV. It captures live video and processes each frame to detect edges using basic image processing techniques.

---

## What This Project Does

The application performs the following steps continuously:

1. Capture video from the webcam  
2. Convert each frame to grayscale  
3. Apply Gaussian Blur to reduce noise  
4. Perform edge detection using the Canny algorithm  
5. Display both original and processed frames in real-time  

---

## Techniques Used

- Video Capture using OpenCV  
- Grayscale Conversion  
- Gaussian Blur  
- Canny Edge Detection  

---

## How It Works

- The webcam captures frames continuously  
- Each frame is processed instantly  
- Edge detection is applied on the blurred grayscale image  
- The result is displayed in a separate window  

---

## How to Run

1. Install required libraries:

```
pip install opencv-contrib-python
```

2. Run the script:

```
python main.py
```

3. Press `ESC` to exit the application  

---

## Output

The program opens two windows:

- Original webcam feed  
- Edge-detected output  

---

## Applications

- Real-time video processing  
- Surveillance systems  
- Object boundary detection  
- Basic computer vision understanding  

---

## Conclusion

This project shows how edge detection can be applied in real-time using live video input. It helps in understanding how computer vision techniques work on dynamic data.

---