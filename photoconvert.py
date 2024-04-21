import cv2

capture = cv2.VideoCapture('vid/video.mp4')

frameNr = 0
count = 0

while True:
    success, frame = capture.read()
    count += 1
    capture.set(cv2.CAP_PROP_POS_FRAMES, count * 10)

    if success:
        cv2.imwrite(f'img/trash/frame_{frameNr}.jpg', frame)

    else: break

    frameNr = frameNr + 1

capture.release()
