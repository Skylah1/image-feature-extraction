#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import argparse
import ffmpeg
import sys
import random
import numpy
import cv2
import subprocess
import os


filename = 'C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4'

def get_frame_types(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    # print('out type >> ', type(out))
    # print('out result >> ', out)
    frame_types = out.replace('pict_type=','').split()
    print(len(frame_types))
    # print('frame_types >> ', type(frame_types))
    # print('frame_types result >> ', frame_types)
    # return zip(range(len(frame_types)), frame_types)
    # original_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./original_iframe/original_%04d.png"'
    # out = subprocess.check_output(original_cmd).decode() # python에서 decode() 디폴트는 utf-8
    # print('out type >> ', type(out))
    # print('out result >> ', out)
    # frame_types = out.replace('pict_type\\','').split()
    # print('frame_types >> ', type(frame_types))
    # print('frame_types result >> ', frame_types)
    return zip(range(len(frame_types)), frame_types)

# def save_i_keyframes(video_fn):
#     frame_types = get_frame_types(video_fn)
#     i_frames = [x[0] for x in frame_types if x[1]=='I']
#     if i_frames:
#         basename = os.path.splitext(os.path.basename(video_fn))[0]
#         cap = cv2.VideoCapture(video_fn)
#         for frame_no in i_frames:
#             cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
#             ret, frame = cap.read()
#             outname = basename+'_i_frame_'+str(frame_no)+'.jpg'
#             cv2.imwrite(outname, frame)
#             # print ('Saved: '+outname)
#         cap.release()
#     else:
#         print ('No I-frames in '+video_fn)
#     print ('I-frames 개수 >> ', len(i_frames))
    

def save_p_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    p_frames = [x[0] for x in frame_types if x[1]=='p']
    if p_frames:
        basename = os.path.splitext(os.path.basename(video_fn))[0]
        cap = cv2.VideoCapture(video_fn)
        for frame_no in p_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            outname = basename+'_p_frames_'+str(frame_no)+'.jpg'
            cv2.imwrite(outname, frame)
            # print ('Saved: '+outname)
        cap.release()
    else:
        print ('No P-frames in '+video_fn)
    
    print ('P-frames 개수 >> ', len(p_frames))
    

if __name__ == '__main__':
    # save_i_keyframes(filename)
    save_p_keyframes(filename)
