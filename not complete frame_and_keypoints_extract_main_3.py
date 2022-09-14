#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import argparse
import ffmpeg
import sys
import random
# import numpy
import cv2
import subprocess



# def read_frame_as_jpeg(in_filename, frame_num):
#     out, err = (
#         ffmpeg
#         .input(in_filename) # input file url
#         .filter('select','eq(pict_type\,PICT_TYPE_I)')
#         # .filter('select', 'gte(n,{})'.format(frame_num)) # 0~frame_num까지 세면 frame_num+1의 값은 frame_num
#         # => .filter를 command로 바꾸면 -> ffmpeg -i video.mp4 -vf "select=gte(n\,200)" %d.jpg
#         .output('output.png') # codec : a media bitstream format // -vcodec : set the video codec
#         .run()
#     )
#     return out



# def print_frame():
#     for i in range()



# out_filename=print_frame()

input_video = (
    ffmpeg
    .input('./original.mp4') # input file url
    .filter('select','eq(pict_type\\,PICT_TYPE_I)')
    # .filter('select', 'gte(n,{})'.format(frame_num)) # 0~frame_num까지 세면 frame_num+1의 값은 frame_num
    # => .filter를 command로 바꾸면 -> ffmpeg -i video.mp4 -vf "select=gte(n\,200)" %d.jpg
    .output('frame_%4d',f='png')
    # .run()
)

def get_video_info(in_filename):

  try:
    probe = ffmpeg.probe(in_filename)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
      print('No video stream found', file=sys.stderr)
      sys.exit(1)
    return video_stream
  except ffmpeg.Error as err:
    print(str(err.stderr, encoding='utf8'))
    sys.exit(1)
    
    

if __name__ == '__main__':
    # file_path='C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4'
    file_path='./original.mp4'
    video_information=get_video_info(file_path)
    total_frames=int(video_information['nb_frames'])
    print('total_frames：' + str(total_frames))
    
    # random_frame = random.randint(1, total_frames)
    # print('random_frame：' + str(random_frame))
    # out = read_frame_as_jpeg(file_path, random_frame)
    print('input_video type >> ',type(input_video))
    print('input_video >> ', input_video)
    
    # print('out type >> ',type(out))
    # print('out >> ',out)
    # print('out length' + len(out))
    
    # image_array = numpy.asarray(bytearray(out), dtype="uint8")
    # print('image_array type >> ',type(image_array))
    # print('image_array >> ',image_array)
    # image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    # print('image >> ',type(image))
    # cv2.imshow('frame', image)
    # cv2.imwrite('./output_frame.png', image)
    # cv2.waitKey()
