#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from gtts import gTTS
from playsound import playsound

if __name__ == '__main__':
    tts = gTTS(
    text = '화장실로 출발하겠습니다',
    lang = 'ko', slow = False
    )
    tts.save('/home/kim/catkin_ws/src/whisper/speeches/toilet.wav')
    playsound('/home/kim/catkin_ws/src/whisper/speeches/ex_ko.mp3')


