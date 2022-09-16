#####        파일 정보 읽어오는 역할       #####
##### pict_type을 커스텀하기는 어려워보임. #####

import ffmpeg


filename="C:/Users/bt_dev/Downloads/feature_extraction/FFMPEG/original.mp4" # file path

def test_ffprobe(file_path):
    test=ffmpeg.probe(file_path)
    print('test type >> ',type(test)) # dictionary type
    print('test output >> ',test)
    return test


if __name__ == '__main__':
    test_ffprobe(filename)
