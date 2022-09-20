from __future__ import unicode_literals
import argparse
import sys
import ffmpeg
import time
import argparse
import numpy as np


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
    
    in_filename="C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/9_flip.mp4"
   
    start=time.time()
    output_save_path='./iframe_output/output_%4d-I.png'
   
    (
      ffmpeg
      .input(in_filename,ss=('00:00:00'),t=('00:00:10'))
      # .addExtraArgs('select','eq(pict_type,I)') # java version
      # .filter('vf',"select='eq(pict_type\,PICT_TYPE_I)'")
      .filter('select','eq(pict_type\\,I)')
      .filter('')
      # .output('./iframe_output/output_%4d_I.png')
      # .output('output_%4d_I.png')
      # .output(output_save_path+'output_I_%4d.png')
      .output(output_save_path)
      .overwrite_output()
      # .output('./iframe_output/output_%4d-I.png',select='eq(pict_type\,I)')
      # .output('fix_original.mp4')
      # .run()
      .run_async(pipe_stdout=True, pipe_stderr=False)
    )
    
    
    '''(
          ffmpeg
          # .input(in_filename,ss=('00:00:00'),t=('00:00:05'))
          .input(in_filename,ss=('00:00:00'),t=('00:00:05'))
          .filter('select','eq(pict_type,I)')
          # .filter('print_format','flat')
          # .filter('select', 'eq(pict_type,PICT_TYPE_I)')
          .output('./extract_result/output_I_%4d.png')
          # .output('./     /output_%4d-P.png')
          # .output('pipe:', format='rawvideo', pix_fmt='png', vframes=1)
          # .output('pipe:')
          .run()
          # .run_async(pipe_stdout=True, pipe_stderr=False)
          # .run_async(pipe_stdout=True)
        )
        '''
  
    '''
    assert out_file.get_args()==['-i',
                                 'in_filename',
                                 '-ss',
                                 '00:00:00',
                                #  '-vsync',
                                #  'vfr',
                                 '-t',
                                 '00:00:10',
                                 '-vf',
                                 "select='eq(pict_type\,PICT_TYPE_I)",
                                #  "select='eq(pict_type,I)'",
                                "./output_%4d_I.png",
    ]
    # get_keyframe=get_frame()
    # print(get_keyframe)
    # print(out_file)
    out_file.get_args().run()
    '''
    
    end=time.time()
    print(f"{end-start:.5f} sec")



'''
def print_frame():
    out_file=(
      ffmpeg
      .input(in_filename,ss=('00:00:00'),t=('00:00:10'))
      .filter('select','eq(pict_type,I)')
      # ._get_filter_arg('select',)
      .output('./iframe_output/output_%4d-I.png')
      # .output('./iframe_output/output_%4d-I.png',vf=("select='eq(pict_type,I)'"))
      # .output('fix_original.mp4')
      # .run()
      # .run_async(pipe_stdout=True, pipe_stderr=True)
    )
    assert out_file.get_args()==['-vf',
                                 "select='eq(pict_type,I)'",
    ]
    '''
    
