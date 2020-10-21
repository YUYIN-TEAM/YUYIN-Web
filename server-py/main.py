# encoding:utf-8

# 输入：经过前端得到的视频
# 工作：1.判断视频数量（多个合并）；2.启动不同的操作
# 输出：得到不同的视频结果
import csv
import os
import shutil

import pandas
import numpy as np
import scene_cut
from keras.models import load_model
from moviepy.editor import *
import time

import video_demo as video_para_getter
import vis_match
import recommend
import making
import tools


# 初始化
# def inite(music_path):
#
# 	music_name = tools.get_music_name(music_path)
#
# 	music_beats = np.load('./list/100_music_beats.npy', allow_pickle=True) #导入音乐节奏保存文件 - 来自tool.py get_music_beats
#
# 	music_features = np.load('./list/100_music_features.npy', allow_pickle=True)
#
# 	music_vis_pred = np.load('./list/music_vis_pred.npy', allow_pickle=True)
#
# 	return music_name,music_beats,music_features,music_vis_pred

def inite(music_path, style):
    music_name = tools.get_music_name(music_path)

    music_beats = np.load('./list/music_beats_' + style + '.npy', allow_pickle=True)  # 导入音乐节奏保存文件 - 来自tool.py get_music_beats

    music_features = np.load('./list/music_features_' + style + '.npy', allow_pickle=True)

    music_vis_pred = np.load('./list/music_vis_pred_' + style + '.npy', allow_pickle=True)

    return music_name, music_beats, music_features, music_vis_pred


def create_models():
    vis_model = vis_match.init_tri_model()

    mood_model = load_model('./models/model_recommendation.h5')

    return vis_model, mood_model


# 获取视频信息
def get_video_info(video_path):
    video = VideoFileClip(video_path)

    # 获取视频转场点
    video_beats = []

    scenes_list, rate = scene_cut.get_scene_time(video_path)
    for i in scenes_list:
        video_beats.append(i / rate)

    time = video.duration
    video_beats.append(time)

    # 获取视频C3D特征参数
    video_features = []

    c_model = video_para_getter.init_model()
    video_para_tmp = video_para_getter.get_features(c_model, video_path, scenes_list)

    video_features.append(np.array(video_para_tmp))
    video_features = np.array(video_features)

    return video_beats, video_features


def match_vis_features(vis_model, video_features, music_vis_pred, music_index, num):
    # 得到视频预测特征
    video_pred = vis_match.get_video_features(video_features, vis_model)

    # 预测
    recom_vis_music_index = vis_match.cal_dist(video_pred, music_vis_pred, music_index, num)

    return recom_vis_music_index


def match_mood_features(mood_model, video_features, music_features, music_index, num):
    # 获得当前音乐预测特征
    now_music_features = []
    for i in music_index:
        now_music_features.append(music_features[i])

    # 预测
    pred_ls = []
    for i in now_music_features:
        pred = mood_model.predict(x=[np.array([i]), video_features])
        pred_ls.append(pred[0][0])

    remd_list = np.argsort(pred_ls)
    recom_mood_music_index = []
    for i in remd_list[:num]:
        recom_mood_music_index.append(music_index[i])

    return recom_mood_music_index


def match_beat_features(video_beats, music_beats, music_index, num):
    print(music_beats)
    # 获得当前的音乐节奏
    now_music_beats_list = []

    for i in music_index:
        now_music_beats = music_beats[i]
        now_music_beats = sorted(set(now_music_beats))
        now_music_beats_list.append(now_music_beats)

    min_dist = []
    music_best_beats = []
    for i in now_music_beats_list:
        min_dist_each, music_best_beats_each = recommend.match_beats(len(video_beats), video_beats, i)
        min_dist.append(min_dist_each)
        music_best_beats.append(music_best_beats_each)
    min_dist = np.array(min_dist)
    beats_music_index = np.argsort(min_dist)[:num]

    recom_beats_music_index = []
    for i in beats_music_index:
        recom_beats_music_index.append(music_index[i])

    return recom_beats_music_index, music_best_beats


def main_rec(name, style):
    # 需要传入的参数：
    # 项目名称 project_name : test
    # 生成风格 style
    # name = sys.argv[1]
    # style = sys.argv[2]
    # name = "test"
    # style = "pop"
    #try:
    #    os.mkdir("./list/"+name+"/")
    #except:
    #    pass
    while True:
        try:
            os.mkdir("./list/"+name+"/")
            break
        except Exception as e:
            print(e)
            continue

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("0", file=process, end="")
    process.close()

    music_path = './data/music/' + style

    # music_path = './data/musics' #音乐文件名称

    # 初始化变量 - 在页面打开，点击进入视频生成页面后就开始执行
    music_name, music_beats, music_features, music_vis_pred = inite(music_path, style)

    vis_model, mood_model = create_models()

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("15", file=process, end="")
    process.close()

    print("初始化完成，正式开始进行视频生成……")

    # 注意：此处需要在前端对上传文件类型进行限制。//TODO

    # 参数1:video_files_path - 前端放置上传视频的文件夹地址,test一般为前端设置的文件夹名称
    video_files_path = './data/input_video/' + name + '/'
    files_basenames = os.listdir(video_files_path)
    try:
        files_basenames.remove(".DS_Store")
    except:
        pass
    print('files to process:', files_basenames)  # 提示上传成功，返回用户上传视频名称

    #try:
    #    os.remove("./data/input_video/clips.mp4")
    #except:
    #    pass

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("28", file=process, end="")
    process.close()

    # 若传入了多个视频，则将多个视频拼接剪辑在一起
    # video_basename  - 需要生成的视频 //TODO - 对长视频做摘要处理
    if len(files_basenames) > 1:
        L = []
        for video_path in files_basenames:
            video = VideoFileClip(os.path.join(video_files_path, video_path))
            L.append(video)
        finalclip = concatenate_videoclips(L)
        finalclip.to_videofile(os.path.join(video_files_path, '../'+name+'.mp4'), audio_codec="aac")
        video_basename = os.path.join(video_files_path, '../'+name+'.mp4')
    else:
        video_basename = os.path.join(video_files_path, files_basenames[0])
        finalclip = VideoFileClip(os.path.join(video_basename))
        shutil.copy(video_basename, "./data/input_video/"+name+".mp4")

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("39", file=process, end="")
    process.close()

    video_beats, video_features = get_video_info("./data/input_video/"+name+".mp4")  # 得到视频的相关信息

    # 开始运行

    start = time.time()
    print("Start: " + str(start))

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("58", file=process, end="")
    process.close()

    # 根据视觉推荐音乐 num=推荐数量
    num_vis = 5
    vis_music_index = range(0, len(music_name))
    recom_vis_music_index = match_vis_features(vis_model, video_features, music_vis_pred, vis_music_index, num_vis)
    recom_vis_music_name = []

    for i in recom_vis_music_index:
        recom_vis_music_name.append(music_name[i])
    print("根据视觉效果推荐的" + str(num_vis) + "首音乐：")
    print(recom_vis_music_name)

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("88", file=process, end="")
    process.close()

    # 根据情感推荐音乐
    num_mood = 3
    mood_music_index = recom_vis_music_index
    recom_mood_music_index = match_mood_features(mood_model, video_features, music_features, mood_music_index, num_mood)

    recom_mood_music_name = []
    for i in recom_mood_music_index:
        recom_mood_music_name.append(music_name[i])

    print("根据情感效果推荐的" + str(num_mood) + "首音乐：")
    print(recom_mood_music_name)

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("93", file=process, end="")
    process.close()

    # 根据节奏推荐音乐
    num_beats = 3
    beats_music_index = recom_mood_music_index
    recom_beats_music_index, recom_music_beats = match_beat_features(video_beats, music_beats, beats_music_index,
                                                                     num_beats)

    recom_beats_music_name = []
    for i in recom_beats_music_index:
        recom_beats_music_name.append(music_name[i])
    print("根据节奏推荐的" + str(num_beats) + "首音乐：")
    print(recom_beats_music_name)

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("97", file=process, end="")
    process.close()

    output_data = []
    for i in range(3):
        temp_output = []
        temp_output.append(recom_beats_music_name[i])
        temp_output.append(video_beats)
        temp_output.append(recom_music_beats[i])
        temp_output.append(video_basename)
        output_data.append(temp_output)

    with open('./list/'+name+'/output_data.csv', 'w') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(output_data)

    music_name = open("./list/"+name+"/rec_music.txt", "w")
    rec_all = []

    for j in recom_beats_music_name:
        if j not in rec_all:
            rec_all.append(j)

    for j in rec_all:
        print(j, file=music_name, end=",")

    process = open("./list/"+name+"/rec_process.txt", "w")
    print("100", file=process, end="")
    process.close()

    process = open("./list/"+name+"/rec_result.txt", "w")
    print(recom_beats_music_name, file=process, end="")
    process.close()

    time.sleep(5)
    process = open("./list/"+name+"/rec_process.txt", "w")
    print("0", file=process, end="")
    process.close()

    return recom_beats_music_name


# 单例测试代码
if __name__ == "__main__":

    # 需要传入的参数：
    # 项目名称 project_name : test
    # 生成风格 style
    # name = sys.argv[1]
    # style = sys.argv[2]
    name = "test1019"
    style = "country"

    main_rec(name,style)

    # music_path = './data/music/' + style
    #
    # # music_path = './data/musics' #音乐文件名称
    #
    # # 初始化变量 - 在页面打开，点击进入视频生成页面后就开始执行
    # music_name, music_beats, music_features, music_vis_pred = inite(music_path, style)
    #
    # vis_model, mood_model = create_models()
    #
    # print("初始化完成，正式开始进行视频生成……")
    #
    # # 注意：此处需要在前端对上传文件类型进行限制。//TODO
    #
    # # 参数1:video_files_path - 前端放置上传视频的文件夹地址,test一般为前端设置的文件夹名称
    # video_files_path = './data/input_video/' + name + '/'
    # files_basenames = os.listdir(video_files_path)
    # try:
    #     files_basenames.remove(".DS_Store")
    # except:
    #     pass
    # print('files to process:', files_basenames)  # 提示上传成功，返回用户上传视频名称
    #
    # try:
    #     os.remove("./data/input_video/clips.mp4")
    # except:
    #     pass
    #
    # # 若传入了多个视频，则将多个视频拼接剪辑在一起
    # # video_basename  - 需要生成的视频 //TODO - 对长视频做摘要处理
    # if len(files_basenames) > 1:
    #     L = []
    #     for video_path in files_basenames:
    #         video = VideoFileClip(os.path.join(video_files_path, video_path))
    #         L.append(video)
    #     finalclip = concatenate_videoclips(L)
    #     finalclip.to_videofile(os.path.join(video_files_path, '../clips.mp4'), audio_codec="aac")
    #     video_basename = os.path.join(video_files_path, '../clips.mp4')
    # else:
    #     video_basename = os.path.join(video_files_path, files_basenames[0])
    #     finalclip = VideoFileClip(os.path.join(video_basename))
    #     shutil.copy(video_basename, "./data/input_video/clips.mp4")
    #
    # video_beats, video_features = get_video_info(video_basename)  # 得到视频的相关信息
    #
    # # 开始运行
    #
    # start = time()
    # print("Start: " + str(start))
    #
    # # 根据视觉推荐音乐 num=推荐数量
    # num_vis = 20
    # vis_music_index = range(0, len(music_name))
    # recom_vis_music_index = match_vis_features(vis_model, video_features, music_vis_pred, vis_music_index, num_vis)
    # recom_vis_music_name = []
    #
    # for i in recom_vis_music_index:
    #     recom_vis_music_name.append(music_name[i])
    # print("根据视觉效果推荐的" + str(num_vis) + "首音乐：")
    # print(recom_vis_music_name)
    #
    # # 根据情感推荐音乐
    # num_mood = 15
    # mood_music_index = recom_vis_music_index
    # recom_mood_music_index = match_mood_features(mood_model, video_features, music_features, mood_music_index, num_mood)
    #
    # recom_mood_music_name = []
    # for i in recom_mood_music_index:
    #     recom_mood_music_name.append(music_name[i])
    #
    # print("根据情感效果推荐的" + str(num_mood) + "首音乐：")
    # print(recom_mood_music_name)
    #
    # # 根据节奏推荐音乐
    # num_beats = 3
    # beats_music_index = recom_mood_music_index
    # recom_beats_music_index, recom_music_beats = match_beat_features(video_beats, music_beats, beats_music_index,
    #                                                                  num_beats)
    #
    # recom_beats_music_name = []
    # for i in recom_beats_music_index:
    #     recom_beats_music_name.append(music_name[i])
    # print("根据节奏推荐的" + str(num_beats) + "首音乐：")
    # print(recom_beats_music_name)
    #
    # output_data = []
    # for i in range(3):
    #     temp_output = []
    #     temp_output.append(recom_beats_music_name[i])
    #     temp_output.append(video_beats)
    #     temp_output.append(recom_music_beats[i])
    #     temp_output.append(video_basename)
    #     output_data.append(temp_output)
    #
    # with open('output_data.csv', 'w') as f:
    #     f_csv = csv.writer(f)
    #     f_csv.writerows(output_data)
    #
    # music_name = open("./rec_music.txt", "w")
    # rec_all = []
    #
    # for j in recom_beats_music_name:
    #     if j not in rec_all:
    #         rec_all.append(j)
    #
    # for j in rec_all:
    #     print(j, file=music_name, end=",")

# 生成视频
# for i in range(0,1):
#
# 	index = recom_beats_music_index[i]
# 	recom_music_beats_i = recom_music_beats[i]
#
# 	print("生成背景音乐为"+music_name[index]+"的视频...")
#
# 	musicFile = os.path.join(music_path, music_name[index])
#
# 	result_file = os.path.join("./data/result_video/", "result.mp4") #输出视频的名称
#
# 	making.making_video(finalclip,musicFile,recom_music_beats_i,video_beats,result_file)
#
# 	stop = time()
#
# 	print("视频生成成功，用时：" + str(stop-start))