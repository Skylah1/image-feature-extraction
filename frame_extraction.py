import subprocess


original_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./original_iframe/original_%04d.png"'
logo_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/1_logo.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./1_iframe/1_logo_%04d.png"'
caption_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/2_caption.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./2_iframe/2_caption_%04d.png"'
severe_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/3_severe.avi" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./3_iframe/3_severe_%04d.png"'
codec_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/4_codec.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./4_iframe/4_codec_%04d.png"'
ratio_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/5_ratio.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./5_iframe/5_ratio_%04d.png"'
resolution_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/6_resolution.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./6_iframe/6_resolution_%04d.png"'
frame_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/7_frame.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./7_iframe/7_frame_%04d.png"'
rotation_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/8_rotation.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./8_iframe/8_rotation_%04d.png"'
flip_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/9_flip.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./9_iframe/flip_%04d.png"'
gray_cmd='ffmpeg -ss 00:00:00.000 -i "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/10_gray.mp4" -vf select=eq(pict_type\,PICT_TYPE_I) -vsync vfr -t 00:00:30.000 "./10_iframe/gray_%04d.png"'


command_list=[
    original_cmd,
    logo_cmd,
    caption_cmd,
    severe_cmd,
    codec_cmd,
    ratio_cmd,
    resolution_cmd,
    frame_cmd,
    rotation_cmd,
    flip_cmd,
    gray_cmd,
]

convert_image_name_list=[
    'original',
    'logo',
    'caption',
    'severe',
    'codec',
    'ratio',
    'resolution',
    'frame',
    'rotation',
    'flip',
    'gray',
]


        
convert_image_order=0
for convert_image_name_of_extract_frame in convert_image_name_list:
        # convert_image_order=0
        convert_image_name_of_extract_frame=subprocess.run(command_list[convert_image_order])
        print('**********', '{0}_'.format(convert_image_order),convert_image_name_of_extract_frame, '**********')
        convert_image_order+=1
        print()

