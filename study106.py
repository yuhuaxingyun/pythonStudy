import requests
import json
import os

def allmusic(name):
    headers = {"Cookie": "eas_sid=h1u5a6D7N0u089l4P8g4S1o9N5; pgv_pvi=1399294976; pgv_pvid=3522250322; RK=RaCE+Qw87C; ptcz=645f699f302818f2aa4fb78a5bf7f75fd0d90f1c95db5a5d0acb695283fdc8b7; tvfe_boss_uuid=306cd91a9af78b43; LW_uid=11f5K7a8I9K0K2E7d6G2B4q7P1; LW_sid=K1o518v1X5U1h0o5J6i4x9g0n9; o_cookie=229554158; pac_uid=1_229554158; uin_cookie=o0229554158; ied_qq=o0229554158; ptui_loginuin=2863778213; luin=o0229554158; lskey=00010000161fb2266a89bdbedc615f48e2b88d65a280a1be4207429dee5c429e0fcb7e0da641297e832f0555",
               "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}
    search_url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=52176551238941872&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w={}&g_tk_new_20200303=5381&g_tk=5381&loginUin=229554158&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(name)
    json_html = requests.get(search_url).text  #json格式转化为字典格式 转化的类型必须是字符串型
    dict_html = json.loads(json_html)
    file_address = "./music/"
    music_list = dict_html["data"]["song"]["list"]  #获取搜索到的所有歌曲的列表
    for music in music_list:
        per_songmid = music["mid"]  #歌曲的songmid
        per_songname = music["name"]  #歌曲名称
        singer = music["singer"][0]["name"]  #歌手名称
        music_document_url_part = "https://u.y.qq.com/cgi-bin/musicu.fcg?format=json&data=%7B%22req_0%22%3A%7B%22module%22%3A%22vkey.GetVkeyServer%22%2C%22method%22%3A%22CgiGetVkey%22%2C%22param%22%3A%7B%22guid%22%3A%22358840384%22%2C%22songmid%22%3A%5B%22{}%22%5D%2C%22songtype%22%3A%5B0%5D%2C%22uin%22%3A%221443481947%22%2C%22loginflag%22%3A1%2C%22platform%22%3A%2220%22%7D%7D%2C%22comm%22%3A%7B%22uin%22%3A%2218585073516%22%2C%22format%22%3A%22json%22%2C%22ct%22%3A24%2C%22cv%22%3A0%7D%7D".format(per_songmid)
        music_document_html_json = requests.get(music_document_url_part).text
        music_document_html_dict = json.loads(music_document_html_json)  #将文件从json格式转化为字典格式
        music_url_part = music_document_html_dict["req_0"]["data"]["midurlinfo"][0]["purl"]  #歌曲下载地址的后部分
        if music_url_part == "":  #有的没有版权的歌曲应该是没有地址的 所以为空的话 就直接重新循环下一首就行了
            continue
        music_url = "https://isure.stream.qqmusic.qq.com/" + music_url_part  #歌曲完整下载地址
        music_url_content = requests.get(music_url,headers=headers).content  #将歌曲下载地址转化为二进制格式
        music_file_name = per_songname + "---" + singer + ".mp3"  #歌曲保存的名称  歌曲名+歌手名
        try:
            if not os.path.exists(file_address):
                os.mkdir(file_address)
            if not os.path.exists(file_address + music_file_name):
                print("正在下载     %s" % music_file_name)
                with open(file_address + music_file_name,"wb") as f:  #保存语句
                    f.write(music_url_content)
                print(music_file_name,"   下载成功")
            else:
                print(music_file_name,"   文件已存在")
        except:
            print("下载失败")

allmusic("夏天的风")