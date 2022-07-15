# -*- coding: utf-8 -*-
# @Time : 2022/6/24 15:09
# @Author : 武梓龙
# @File : FFMPEG.py
# @Software: PyCharm
import cv2
import subprocess as sp

way = 'rtmp'
push_url = "rtmp://localhost:1935/live/test"
camera_path = 0

cap = cv2.VideoCapture(camera_path)

# Get video information
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps, width, height)
# ffmpeg command
command = ['ffmpeg',
            '-y',
            '-f', 'rawvideo',
            '-vcodec', 'rawvideo',
            '-pix_fmt', 'bgr24',
            '-s', "{}x{}".format(width, height),
            '-r', str(fps),
            '-i', '-',
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            '-preset', 'ultrafast',
            '-f', 'flv',
            push_url]

# 管道配置
p = sp.Popen(command, stdin=sp.PIPE)
while (cap.isOpened()):
    ret, frame = cap.read()
    # print("running......")
    if not ret:
        print("Opening camera is failed")
        break
    p.stdin.write(frame.tobytes())

return_value, frame = cap.read()
