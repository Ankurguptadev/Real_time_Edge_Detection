import cv2 as cv

video = cv.VideoCapture(0)

while True:
    ret, frame = video.read()

    if not ret:
        break


    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (3, 3), 0)
    canny = cv.Canny(blur, 100, 200)

    cv.imshow("Original", frame)
    cv.imshow("Edges", canny)

    if cv.waitKey(1) & 0xFF == 27:
        break

video.release()
cv.destroyAllWindows()
