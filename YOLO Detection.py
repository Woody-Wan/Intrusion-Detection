# -*- coding: utf-8 -*-
import cv2 as cv
import time
import numpy as np

tpPointsChoose = []
drawing = False
tempFlag = False
global detectnotation #检测坐标

def draw_ROI(event, x, y, flags, param):
	global point1,pts,drawing,tempFlag
	# 对鼠标按下的点坐标进行存储
	global tpPointsChoose
	if event == cv.EVENT_LBUTTONDOWN:
		tempFlag = True
		drawing = False
		point1 = (x, y)
		# 画点
		tpPointsChoose.append((x, y))  
	if event == cv.EVENT_RBUTTONDOWN:
		tempFlag = True
		drawing = True
		pts = np.array([tpPointsChoose], np.int32)
		pts1 = tpPointsChoose[1:len(tpPointsChoose)]
		print(pts1)
	if event == cv.EVENT_MBUTTONDOWN:
		tempFlag = False
		drawing = True
		tpPointsChoose = []

def isPoiWithinPoly(poi,poly):
    #输入：点，多边形三维数组
    #poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组
	sinsc=0 #交点个数
	#循环每条边->epoly 是二维数组[[x1,y1],…[xn,yn]]
	for epoly in poly: 
		for i in range(len(epoly)): #[0,len-1]
			s_poi=epoly[i]
			s_poi_bf = epoly[i-1]
		if i < (len(epoly)-2):  #限制下标范围，防止溢出
				e_poi = epoly[i + 1]
				e_poi_af = epoly[i + 2]
		elif i == len(epoly)-2: # 若超出循环，则设置为起始值
				e_poi = epoly[-1]
				e_poi_af = epoly[0]
		elif i == len(epoly)-1: # 若超出循环，则设置为起始值
				e_poi = epoly[0]
				e_poi_af = epoly[1]
		if poi[1] == s_poi[1] == e_poi[1]: # 判断平行线段，是否位于区域中间位置，若位于，则+1
				if ((s_poi[1]-s_poi_bf[1])*(e_poi_af[1]-s_poi[1]) > 0):
					sinsc += 1
					continue
		elif poi[1] == s_poi[1] != e_poi[1]: # 点
				if ((s_poi_bf[1]-s_poi[1])*(s_poi[1]-e_poi[1])>0):
					sinsc += 1
					continue 
		elif s_poi[1] > poi[1] and e_poi[1] > poi[1]:  # 线段在射线上边
			continue
		elif s_poi[1] < poi[1] and e_poi[1] < poi[1]:  # 线段在射线下边
			continue
		elif s_poi[0] < poi[0] and e_poi[1] < poi[1]:  # 线段在射线左边
			continue
		else:
			xseg = e_poi - (e_poi - s_poi) * (e_poi - poi[1]) / (e_poi - s_poi)  # 求交
			if all(xseg < poi[0]):  # 交点在射线起点的左侧
				continue
			else:
				sinsc += 1  # 排除上述情况之后
	return True if sinsc%2==1 else  False

cv.namedWindow('detection')
cv.setMouseCallback('detection',draw_ROI)

#创建模型net
net = cv.dnn_DetectionModel('yolov4.cfg', 'yolov4.weights')
net.setInputSize(320, 320)
net.setInputScale(1.0 / 255)
net.setInputSwapRB(True)

#创建类别names
with open('coco.names', 'rt') as f:
	names = f.read().rstrip('\n').split('\n')

#读入图像开展目标检测处理
#cap = cv.VideoCapture(0)
cap = cv.VideoCapture('其他人员4_1.mp4')
size=(cap.get(cv.CAP_PROP_FRAME_WIDTH),cap.get(cv.CAP_PROP_FRAME_HEIGHT))
while cap.isOpened():
	#读取帧数据
	ok, frame = cap.read()
	#显示方向
	#frame = cv.flip(frame,1)
	classes, confidences, boxes = net.detect(frame, confThreshold=0.1, nmsThreshold=0.4)
	
	#按键“q”作为退出指令
	c = cv.waitKey(10)
	if c & 0xFF == ord('q'):
		break
	
	#若画面内无识别需要进行判断以免出现参数缺少错误
	if (len(classes)==0):
		cv.imshow('detection', frame)
		continue

	#对识别目标进行标注
	for classId, confidence, box in zip(classes.flatten(), confidences.flatten(), boxes):
		if confidence>0.5:
			#(x,y,w,h)中心坐标偏移量，长宽偏移量
			left, top, w, h = box
			cv.rectangle(frame, (left, top), (left + w, top + h), (0,255,0),2 )
			
			#距离检测
			Xs = w
			Ys = h
			Warning = 15
			Alert = 14
			d1 = 16
			d2 = 7
			w1 = 100
			w2 = 200
			h1 = 200
			h2 = 420
			Dh = (d1-d2)*h/(h1-h2)+(d2*h1-d1*h2)/(h1-h2)
			Dw = (d1-d2)*w/(w1-w2)+(d2*w1-d1*w2)/(w1-w2)
			D = (Dh*11+Dw*9)/20
			DT = str(D)
			#坐标检测
			XL = left
			YT = top
			XR = left + w
			YB = top + h	
			OX = (XL+XR)/2
			OY = (YT+YB)/2
			sign = 0
			if (tempFlag == True and drawing == False) :  # 鼠标左击
				cv.circle(frame, point1, 5, (0, 255, 0), 2)
				for i in range(len(tpPointsChoose) - 1):
					cv.line(frame, tpPointsChoose[i], tpPointsChoose[i + 1], (255, 0, 0), 2)
			if (tempFlag == True and drawing == True):  #鼠标右击
				cv.polylines(frame, pts, True, (0, 0, 255), thickness=2)
				sign = isPoiWithinPoly([XL,YT], pts)
				if (sign == True):
					cv.putText(frame, 'Alert! Invasion!', (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
			if (tempFlag == False and drawing == True):  # 鼠标中键
				for i in range(len(tpPointsChoose) - 1):
					cv.line(frame, tpPointsChoose[i], tpPointsChoose[i + 1], (0, 0, 255), 2)
			if (D < Warning and D > Alert or D == Warning and sign == False):
				cv.putText(frame, 'Warning!', (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
			if (D < Alert or D == Alert and sign == False):
				cv.putText(frame, 'Alert! Invasion!', (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
			if (D > Warning and sign == False):
				cv.putText(frame, DT, (left, top), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

	cv.imshow('detection', frame)
	

cv.waitKey(0)