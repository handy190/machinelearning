#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import cv2

cap = cv2.VideoCapture("xxx.mp4")

while(1):
    #ret��frame���Ƿ���ֵ�����ߴ���֡��
    ret,frame = cap.read()
    #����ɫ��ͼ��ת���ɻҶȣ��Ӵ˿��Կ���read����Ӧ����ÿһ֡��ͼ��frame��ͼƬ
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("capture",gray)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

