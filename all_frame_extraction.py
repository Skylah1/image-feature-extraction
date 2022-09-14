from __future__ import unicode_literals
import argparse
import ffmpeg
import sys


# parser = argparse.ArgumentParser(
#     description='Read individual video frame into memory as jpeg and write to stdout')
# parser.add_argument('in_filename', help='Input filename')
# parser.add_argument('frame_num', help='Frame number')

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
    
    
    
def read_frame_as_jpeg(in_filename, frame_num):
    out, err = (
        ffmpeg
        .input(in_filename)
        .filter('select', 'eq(pict_type\\,I)')
        .output('pipe:',format='png')
        .run()
    )
    return out




if __name__ == '__main__':
    
    in_filename="C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4"
    input_file=ffmpeg.input(in_filename)
    filter_file=ffmpeg.filter(input_file,'select','eq(pict_type\,I)')
    video_information=get_video_info(in_filename)
    total_frames=int(video_information['nb_frames'])
    print('total_frames：' + str(total_frames))
    for i in range(total_frames):
        output_file=ffmpeg.output(filter_file,'output_%4d.png')
        # print(output_file)
        ffmpeg.run(output_file)
        i+=1
