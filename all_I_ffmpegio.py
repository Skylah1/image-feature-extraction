import ffmpegio
from ffmpegio import ffmpeg, ffmpegprocess
from subprocess import PIPE
from ffmpegio.utils import filter as filter_utils
from pprint import pprint
import time



start=time.time()

file_path='C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4'
start_time='00:00:00.000'
end_time='00:00:10.000'
output_save_path='./iframe_output/original'
output_file=output_save_path+'_%04d.png'

ffmpeg(['-i', file_path, '-ss', start_time, '-vf', "select='eq(pict_type\,PICT_TYPE_I)", '-vsync', 'vfr', '-t', end_time, output_file])
# extract=ffmpeg(['-i', file_path, '-ss', start_time, '-vf', "select='eq(pict_type\,PICT_TYPE_I)", '-vsync', 'vfr', '-t', end_time, output_file])

end=time.time()
print(f"{end-start:.5f} sec")
