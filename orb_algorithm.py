import time
import math
import numpy as np
import cv2
from matplotlib import pyplot as plt
from math import sqrt


start=time.time()
src = cv2.imread("input dataset/0_original.png") # queryImage
target = cv2.imread("input dataset/5_lotation.png") # trainImage

'''bgr2rgb -> rgb2gray'''
# opencv 는 image 가 BGR 로 되어있음.
# src = cv2.cvtColor(src,cv2.COLOR_BGR2RGB) # queryImage
# target = cv2.imread("image dataset/image data/original.png",cv2.COLOR_BGR2RGB) # trainImage
# target = cv2.cvtColor(target,cv2.COLOR_RGB2GRAY) # trainImage
# print('rgb2gray >> ',target.shape)

"""
orb = cv2.ORB_create(
    nfeatures=10000,                # 최대 피처 수 : ORB 객체가 한 번에 검출하고자 하는 특징점의 개수
    scaleFactor=1.5,                # 스케일 계수 : 이미지 피라미드 설정
    nlevels=8,                      # 피라미드 레벨 : 이미지 피라미드 레벨 수
    edgeThreshold=31,               # 엣지 임계값 : 이미지 테두리에서 발생하는 특징점을 무시하기 위한 경계의 크기
    firstLevel=0,                   # 시작 피라미드 레벨
    WTA_K=2,                        # 비교점
    scoreType=cv2.ORB_HARRIS_SCORE, # 점수 방식
    patchSize=31,                   # 패치 크기
    fastThreshold=20,               # FAST 임계값
)
"""

# Initiate ORB detector
orb = cv2.ORB_create()

# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(src,None)
print('kp1 >> ',type(kp1))
print('kp1 length >> ', len(kp1))
print('des1 >> ',des1.shape)
kp2, des2 = orb.detectAndCompute(target,None)
print('kp2 >> ',type(kp2))
print('kp2 length >> ',len(kp2))
print('des2 >> ',des2.shape)


# BFMatcher with default params
matcher = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
matches = matcher.match(des1,des2)
print('matches type >> ',type(matches))
print('matcheds length >> ',len(matches))

matching_ratio=(len(matches)/len(des2))*100
print(f'matching_ratio = {matching_ratio: .2f}')
convert_image_result = cv2.drawMatches(src,kp1,target,kp2,matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)


# BFMatcher with default params
# matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
# matches = matcher.match(des1,des2,2)
# print('matches length >> ',len(matches))
#matches=matcher.knnMatch(queryDescriptors,trainDescriptors,k,mask,compactResult)



# print('\ntrain image index >> ',matches[0][0].imgIdx, matches[0][1].imgIdx)
# print('\nquery descriptor index >> ',matches[0][0].queryIdx, matches[0][1].queryIdx)
# print('\ntrain descriptor index >> ',matches[0][0].trainIdx, matches[0][1].trainIdx)
# print('\ndistance >> ',matches[0][0].distance, matches[0][1].distance)


'''
# Apply ratio test
good = []
# matched1=[]
# matched2=[]
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append([m])
        # matched1.append(kp1[m.queryIdx])
        # matched2.append(kp2[m.trainIdx])
#  print(type(good))
    # print('good >> \n',good)
print('\nhow many good >> ',len(good))
# print('\nhow many matched1 >> ',len(matched1))
# print('\nhow many matched2 >> ',len(matched2))
    # print('matched1 >>\n',matched1)
    # print('matched2 >>\n',matched2)
'''


# cv.drawMatchesKnn expects list of lists as matches.
# convert_image_result = cv2.drawMatchesKnn(src,kp1,target,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
print('convert_image_result result >> ',convert_image_result.shape)
cv2.imshow("result", convert_image_result)
cv2.imwrite('image output/output5.png',convert_image_result)


cv2.waitKey() 

end=time.time()
print(f"{end-start:.5f} sec")
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = bf.match(des1, des2)
# matches = sorted(matches, key=lambda x: x.distance)

# for i in matches[:100]:
#     idx = i.queryIdx
#     x1, y1 = kp1[idx].pt
#     cv2.circle(src, (int(x1), int(y1)), 3, (255, 0, 0), 3)

# img3=cv2.drawMatches(src,kp1,target,kp2,)
# cv2.imshow("src | box_in_scene", src)
# cv2.imshow("target | box", target)
