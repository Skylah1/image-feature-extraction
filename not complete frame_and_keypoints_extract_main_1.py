from __future__ import unicode_literals
import os
import sys
import getopt
import time
import subprocess as sp
import ffmpeg
# from frame_extraction import FrameExtraction
import argparse # Command-line parsing library
import cv2
from matplotlib import pyplot as plt
import numpy as np



# command=['ffmpeg',
#          '-ss', '00:00:00.000',
#          '-i', '"C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4"',
#          '-vf', 'select=eq(pict_type\,PICT_TYPE_I)',
#          '-vsync', 'vfr', '-t', ',00:00:30.000',
#          '"./original_iframe/original_%04d.png"']
command=['ffmpeg',
         '-i', 'original.mp4'
         ]

pipe=sp.Popen(command, stdout=sp.PIPE, bufsize=10**8)
while True:
    raw_image = pipe.stdout
   # transform the byte read into a numpy array
    image =  np.fromstring(raw_image, dtype='uint8')
    # image = image.reshape((360,420,3))
    # cv2.imshow('hello',image)
    cv2.imwrite('./ex_output.png',image)
    cv2.waitKey()
    # throw away the data in the pipe's buffer.
    pipe.stdout.flush()
    

"""
filename='./original.mp4'

def get_frame_types(video_fn):
    # command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    command='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./original_iframe/original_%04d.png"'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types)

def save_i_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        basename = os.path.splitext(os.path.basename(video_fn))[0]
        cap = cv2.VideoCapture(video_fn)
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            outname = basename+'_i_frame_'+str(frame_no)+'.jpg'
            cv2.imwrite(outname, frame)
            print ('Saved: '+outname)
        cap.release()
    else:
        print ('No I-frames in '+video_fn)

if __name__ == '__main__':
    save_i_keyframes(filename)
    
"""

"""
parser = argparse.ArgumentParser(
    description='Read individual video frame into memory as jpeg and write to stdout')
parser.add_argument('in_filename', help='Input filename')
# parser.add_argument('frame_num', help='Frame number')



def read_frame_as_jpeg(in_filename):
    out, err = (
        ffmpeg
        .input(in_filename)
        .output('pipe:', vframes=1, format='image2', vcodec='mjpeg')
        .run(capture_stdout=True)
    )
    return out

input_file_path='./original.mp4'
if __name__ == '__main__':
    
    # original_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./original_iframe/original_%04d.png"'

    args = parser.parse_args()
    out = read_frame_as_jpeg(input_file_path)
    sys.stdout.buffer.write(out)




# def get_keypoints():
#     # path='C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original_iframe'
#     # file_list=os.listdir(path)
#     # print(len(file_list))
#     # for number_of_iframe in range(len(file_list)):
#         # 같은 시간에서의 query frame과 train frame 비교
#         src = cv2.imread("./original_iframe/original_0001.png") # queryImage
#         target = cv2.imread("./1_iframe/1_logo_0001.png") # trainImage

#         # Initiate ORB detector
#         orb = cv2.ORB_create()

#         # find the keypoints and descriptors with ORB
#         kp1, des1 = orb.detectAndCompute(src,None)
#         print('kp1 length >> ', len(kp1))
#         kp2, des2 = orb.detectAndCompute(target,None)
#         print('kp2 length >> ',len(kp2))


#         # BFMatcher with default params
#         matcher = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
#         matches = matcher.match(des1,des2)
#         print('matches length >> ', len(matches))

#         matching_ratio=(len(matches)/len(des2))*100
#         print(f'matching_ratio >> {matching_ratio: .2f}')
#         convert_image_result = cv2.drawMatches(src,kp1,target,kp2,matches,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

#         print('convert_image_result result >> ',convert_image_result.shape)
#         cv2.imshow("result", convert_image_result)
#         cv2.imwrite('./ex_output.png',convert_image_result)


#         cv2.waitKey() 
"""
