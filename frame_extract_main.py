'''
FFMPEG을 사용하므로 클래스 파일인 frame_extraction.py와 기타 input data, ffmpeg.exe 실행파일이 하나의 폴더 안에 있어야 함.
즉, 같은 경로에 있어야 한다는 의미.
그래야 프레임을 추출할 수 있음.
이 파일은 클래스를 가져와서 클래스 객체를 생성하면 바로 프레임 추출을 실행할 수 있음.

'''

import subprocess
from frame_extraction import FrameExtraction


# 클래스 객체 생성
# 프레임 추출 전체 과정
get_frame=FrameExtraction()
