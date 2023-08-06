import cv2
import numpy as np 
from ultralytics import YOLO
import pandas as pd

model = YOLO('./Model.pt')

my_file = open("coco.txt", "r")
data = my_file.read()
class_list = data.split("\n")

video1 = cv2.VideoCapture('./video5.mp4')
video2 = cv2.VideoCapture('./Second_part.mp4')
video3 = cv2.VideoCapture('./video6.mp4')
video4 = cv2.VideoCapture('./second_part-2.mp4')

isopen = True

while isopen:

    for i in range(3):
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()
        ret3, frame3 = video3.read()
        ret4, frame4 = video4.read()


    new_size_frame1 = cv2.resize(frame1, (820, 420))
    new_size_frame2 = cv2.resize(frame2, (820, 420))
    new_size_frame3 = cv2.resize(frame3, (820, 420))
    new_size_frame4 = cv2.resize(frame4, (820, 420))

    new_size_frame1 = new_size_frame1[:, :600]
    new_size_frame2 = new_size_frame2[:, :-120]
    new_size_frame3 = new_size_frame3[:, 140:-30]
    new_size_frame4 = new_size_frame4[:, 140:-30]

    area1 = [(0,418), (0, 233), (255,0), (429,1), (569,204), (592, 417)]
    area2 = [(600,418), (600,304), (880,50), (1030,40), (1300,416)]

    area3 = [(0,418), (0, 212), (228,0), (595,0), (648,418)]
    area4 = [(652,416), (653,194), (895,0), (1217,0), (1300,418)]


    combine_frame1 = np.concatenate((new_size_frame1, new_size_frame2), axis=1)
    combine_frame2 = np.concatenate((new_size_frame3, new_size_frame4), axis=1)

    result1 = model.predict(combine_frame1)
    result2 = model.predict(combine_frame2)

    b=result1[0].boxes.data

    px2=pd.DataFrame(b).astype("float")

    count = []

    for index,row in px2.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])
        c=class_list[d]

        cx = int(x1+x2) // 2
        cy = int(y1+y2) // 2

        results1 = cv2.pointPolygonTest(np.array(area1, np.int32), (cx, cy), False)
        results2 = cv2.pointPolygonTest(np.array(area2, np.int32), (cx, cy), False)

        if results1 >= 0 or results2 >= 0:

            cv2.rectangle(combine_frame1,(x1,y1),(x2,y2),(0,255,0),2) 
            cv2.circle(combine_frame1, (cx, cy), 3, (0, 0, 255), -1)
                
            # cv2.putText(combine_frame1,str(c),(x1,y1),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
            count.append(d)

    k = len(count)
    print('objects in frame 1 is: ', k)
    print(f'frame 1 has {k} seconds')
    print('frame 1 is green\nframe 2 is red')
    print('==========================================================')

    cv2.polylines(combine_frame1, [np.array(area1, np.int32)], True, (255, 0, 0), 2)
    cv2.polylines(combine_frame1, [np.array(area2, np.int32)], True, (255, 0, 0), 2)
    

    cv2.imshow('frame1', combine_frame1)

    cv2.waitKey((k) * 1000)

    # if cv2.waitKey(0) == ord('q'):
    #     isopen = False
    #     break

    # if isopen == False:
    #     break

    cv2.destroyAllWindows()



    a=result2[0].boxes.data

    px1=pd.DataFrame(a).astype("float")

    count2 = []

    for index,row in px1.iterrows():
        x1=int(row[0])
        y1=int(row[1])
        x2=int(row[2])
        y2=int(row[3])
        d=int(row[5])

        cx = int(x1+x2) // 2
        cy = int(y1+y2) // 2

        results3 = cv2.pointPolygonTest(np.array(area3, np.int32), (cx, cy), False)
        results4 = cv2.pointPolygonTest(np.array(area4, np.int32), (cx, cy), False)

        if results3 >=0 or results4 >= 0:
       
            cv2.rectangle(combine_frame2,(x1,y1),(x2,y2),(0,255,0),2) 
            cv2.circle(combine_frame2, (cx, cy), 3, (0, 0, 255), -1)


            # cv2.putText(combine_frame2,str(c),(x1,y1),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0),2)
            count2.append(d)

    p = len(count2)

    print('objects in frame 2 is: ', p)
    print(f'frame 2 has {p} seconds')
    print('frame 2 is green\nframe 1 is red')
    print('==========================================================')

    cv2.polylines(combine_frame2, [np.array(area3, np.int32)], True, (255, 0, 0), 2)
    cv2.polylines(combine_frame2, [np.array(area4, np.int32)], True, (255, 0, 0), 2)

    cv2.imshow('frame2', combine_frame2)

    cv2.waitKey((p) * 1000)

    cv2.destroyAllWindows()


