#
# 语音合成
# 

from aip import AipSpeech

APP_ID = '24219302'
APP_KEY = 'eqdpzNiPaj85Lp5Yo79h5Mwz'
SECRET_KEY = 'k9uf2rAxH4L8LGtmkgwXSlW5cXIpMwec'
# 与百度进行一次加密校验,认证你是合法用户合法的应用
# AipSpeech是百度语音的客户端,认证成功之后,客户端将被开启,这里的client就是已经开启的百度语音的客户端了
client = AipSpeech(APP_ID,APP_KEY,SECRET_KEY)
str = '今天天气怎么样？'
result = client.synthesis(
    str,  # text:合成的文本,使用UTF-8编码,请注意文本长度必须小于1024字节
    'zh',           # lang:语言,中文:zh,英文:en
    1,              # ctp:客户端信息这里就写1,写别的不好使,至于为什么咱们以后再解释
    {
        'vol':5,    # 合成音频文件的准音量
        'spd':4,    # 语速取值0-9,默认为5中语速
        'pit':8,    # 语调音量,取值0-9,默认为5中语调
        'per':4     # 发音人选择,0为女声,1为男生,3为情感合成-度逍遥,4为情感合成-度丫丫,默认为普通女
    } # options:这是一个dict类型的参数,里面的键值对才是关键.
)
# 如果上面的三个参数APP_ID,APP_KEY,SECRET_KEY填写正确的话
# result就是音频文件的二进制文件流,如果返回失败的话,result就会是个字典
print(result)

if not isinstance(result,dict):
    with open('audio.mp3','wb') as f:
        f.write(result)


# 识别正确返回语音二进制文件流,错误则返回dict,参照下面错误代码.
"""
result = {
            'err_detail': 'Tex length exceeds limit.', 
            'err_msg': 'parameter error.', 
            'err_no': 501, 
            'err_subcode': 10, 
            'tts_logid': 3257246120
        }
"""