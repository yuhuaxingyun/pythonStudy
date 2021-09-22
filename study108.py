#
# 语音识别
# 
import Speech
import SDKfrom
from aip import AipSpeech

class HumanInteraction(object):
    def __init__(self):
        # 能够识别语音的用户配置
        self.APP_ID = '24219284'
        self.APP_KEY = 'MMmGK7rqex5cjlZiNuNokNHq'
        self.SECRET_KEY = 'ZALFt67GpQgmGPDcHHwXKrVgusyFZYeb'
        self.client = AipSpeech(self.APP_ID,self.APP_KEY,self.SECRET_KEY) # 定义一个用户


        # 能够将文字合成语音的用户配置
        self.SpeechAPP_ID = '24219302'
        self.SpeechAPI_KEY = 'eqdpzNiPaj85Lp5Yo79h5Mwz'
        self.SpeechSECRET_KEY = 'k9uf2rAxH4L8LGtmkgwXSlW5cXIpMwec'
        self.Speechclient = AipSpeech(self.SpeechAPP_ID,self.SpeechAPI_KEY,self.SpeechSECRET_KEY) # 定义一个能合成用户

        self.r = sr.Recognizer()

        
        