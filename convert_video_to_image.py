import cv2

video = cv2.VideoCapture('./videos/Thanksgiving drawing major traffic on LA roads.mp4')
success, image = video.read()

count=0 

delay = 3000

while video.isOpened():
    success, image = video.read()

    if not success:
        break

    video.set(cv2.CAP_PROP_POS_MSEC, (count * delay))

    success, image = video.read()

    if not success:
        break

    cv2.imwrite('./images2/102600700261111%d.png' % count, image)
    count+=1