

# 将视频和音乐剪辑在一起
# 剪辑音频
import csv
import sys
import time

import numpy as np
import os
from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips, CompositeAudioClip


def making_video(video_clips, musicFile, best_music_beats, best_video_beats, file_name):

    # 开始剪辑视频
    video = video_clips
    audio = AudioFileClip(musicFile)
    print(video.duration)

    audio_use = audio.subclip(best_music_beats[0], best_music_beats[-1])
    print("audio_time:", audio_use.duration)

    print("best_video_beats", best_video_beats)
    print('best_music_beats', best_music_beats)

    #统一剪辑 - 快/不精确
    #change_size = best_music_beats[-1]/best_video_beats[-1]
    change_size = audio_use.duration/video.duration
    video_noaudio = video.fl_time(
        lambda t: t/change_size, apply_to=['video', 'audio']).set_end(best_video_beats[-1]*change_size)
    # video_noaudio.write_videofile('./temp/'+file_name.split('/')[-1]+"_111.mp4")

    #分段剪辑 - 慢/但更精确
    #video_clips = []
    #time = 0
    # for i in range(1,len(best_video_beats)):
    #	video_clip = 0
    #	#获取视频片段
    #	video_1 = video.subclip(best_video_beats[i-1],best_video_beats[i])
    #	#变速
    #	video_time = best_video_beats[i]-best_video_beats[i-1]
    #	music_time = best_music_beats[i]-best_music_beats[i-1]
    #	change_size = music_time/video_time #选择快进或者慢放
    #	video_clip = video_1.fl_time(lambda t:t/change_size,apply_to=['video','audio']).set_end(video_1.duration*change_size)
    #	print("change_size",change_size)
    #	video_clip.write_videofile('./temp/'+file_name.split('/')[-1]+str(i)+".mp4")
    #	path = './temp/'+file_name.split('/')[-1]+str(i)+".mp4"
    #	clips = VideoFileClip(path)
    #	time += clips.duration
    #	video_clips.append(clips)
    # print(time)
    #video_noaudio = concatenate_videoclips(video_clips)

    # 添加音乐
    video_result = video_noaudio.set_audio(audio_use)
    video_result.write_videofile(file_name, audio_codec="aac")


def main_make(fname, music_name, style):
    # 需要传入的参数：
    # 音乐文件 music_name
    # 生成类型 style

    # style = "china"
    # music_name = "0_0_wxd_6_TCOM_0_T4_P018_AccChord0.mp3"

    process = open("./list/"+fname+"/process.txt", "w")
    print("0", file=process, end="")
    process.close()

    # videoFile = "./data/input_video/test/clips.mp4"

    # style = sys.argv[1]
    # music_name = sys.argv[2]

    videoFile = "./data/input_video/"+fname+".mp4"
    video_clips = VideoFileClip(videoFile)
    # musicFile = "/Users/try/Desktop/input/data/musics/535_Track4_1290_471_Temp22.mid.mp3"
    musicFile = "./data/music/" + style + "/" + music_name
    name = musicFile.split('/')[-1]

    # 获取转场点
    data_file = open("./list/"+fname+"/output_data.csv", "r")
    data_reader = csv.reader(data_file)

    data = []
    for i in data_reader:
        i[1] = i[1][1:-1].split(',')
        i[2] = i[2][1:-1].split(',')
        data.append(i)

    for i in data:
        tmp = []
        for j in i[1]:
            j = float(j.strip())
            tmp.append(j)
        i[1] = tmp
        tmp = []
        for j in i[2]:
            j = float(j.strip())
            tmp.append(j)
        i[2] = tmp
        print(i)

    music_beats = []
    video_beats = []

    for i in data:
        if i[0] == name:
            music_beats = i[2]
            video_beats = i[1]

    process = open("./list/"+fname+"/process.txt", "w")
    print("10", file=process, end="")
    process.close()

    making_video(video_clips, musicFile, music_beats,
                 video_beats, './data/result_video/'+fname+'.mp4')

    process = open("./list/"+fname+"/process.txt", "w")
    print("100", file=process, end="")
    process.close()

    time.sleep(5)
    process = open("./list/"+fname+"/process.txt", "w")
    print("0", file=process, end="")
    process.close()


if __name__ == "__main__":

    # videoFile = "./data/input_video/test/11.mp4"
    # musicFile = "./data/musics/535_Track1_444_Temp18_2000.mp3"
    #
    # #获取转场点
    # video_beats = [0.0, 3.9, 20.55, 30.35, 31.35]
    # music_beats = [3.959002267573696, 8.103764172335602, 25.66965986394558, 34.7718820861678, 34.98086167800454]
    #
    # #best_music_beats = get_music_point(video_beats,music_beats)
    #
    # video_clips = VideoFileClip(videoFile)
    #
    # making_video(video_clips,musicFile,music_beats,video_beats,'111.mp4')

    # os.chdir("../rec/")

    # 需要传入的参数：
    # 音乐文件 music_name
    # 生成类型 style

    main_make("test10", "Pop12.mp3", "pop")
