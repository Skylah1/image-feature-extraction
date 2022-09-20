import os
import cv2
import subprocess
import ffmpeg
import time



filenames=[ "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4",
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/1_logo.mp4",
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/2_caption.mp4",
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/3_severe.avi",
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/4_codec.mp4",          
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/5_ratio.mp4",          
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/6_resolution.mp4",          
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/7_frame.mp4",          
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/8_rotation.mp4",          
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/9_flip.mp4",          
            "C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/10_gray.mp4",          
]



def get_frame_types(video_fn):
    # command_IDR = 'ffprobe -skip_frame nokey -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    # command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split() # frame type을 알아내기 위한 커멘드
    out = subprocess.check_output(command + [video_fn]).decode() # command + [video_fn] 를 문자열로 변환
    # command+[video_fn] 실행한 후 pict_type 알아내기
    frame_types = out.replace('pict_type=','').split() # frames.frame.388.pict_type="I" -> frames.frame.388.pict_type=""
    # out=command + video_fn
    # frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types) # len(frame_types)와 frame_types를 순서대로 첫번쨰부터 같이 (len(frame_types))_1, frame_types_1), ... ) 묶어줌.



def save_i_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        basename = os.path.splitext(os.path.basename(video_fn))[0] # original, 1_logo, ...
        # print(basename)
        cap = cv2.VideoCapture(video_fn)
        # cap_fps=cap.get(cv2.CAP_PROP_FPS) # video fps 출력
        # print('video fps >> ',cap_fps)
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no) # CAP_PROP_POS_FRAMES 동영상의 현재 프레임 수
            ret, frame = cap.read()
            outname = basename+'_i_frame_'+str(frame_no)+'.png'
            # print('outname >> ',outname)
            # outname = +'_i_frame_'+str(frame_no)+'.png'
            cv2.imwrite(outname, frame)
            print ('Saved: '+outname)
        cap.release()
    else:
        print ('No I-frames in '+video_fn) 
        


# def my_save_i_keyframes(video_fn):
#     command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
#     out = subprocess.check_output(command + [video_fn]).decode() # command + [video_fn]를 문자열로 변환



if __name__ == '__main__':
     
    for file_name in filenames:
        start=time.time()
        get_frame_types(file_name)
        save_i_keyframes(file_name)
        end=time.time()
    print(f"{end-start:.5f} sec")
    # get_frame_types(filenames)
    # save_i_keyframes(filename)
    
    
    # 프레임 순서 정보로 영상에서 원하는 프레임을 추출할 수 있다
