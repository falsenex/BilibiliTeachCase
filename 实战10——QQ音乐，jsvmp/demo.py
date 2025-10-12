import re
from hashlib import sha1
from base64 import b64encode
import requests

def get_sign(mingwen_str):
    arr1 = [23, 14, 6, 36, 16, 7, 19]
    arr2 = [16, 1, 32, 12, 19, 27, 8, 5]
    arr3 = [89, 39, 179, 150, 218, 82, 58, 252, 177, 52, 186, 123, 120, 64, 242, 133, 143, 161, 121, 179]
    dict_hex = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,'F': 15}
    sha1_str = sha1(mingwen_str.encode()).hexdigest().upper()

    first_str = ''.join(map(lambda i: sha1_str[i], arr1))
    last_str = ''.join(map(lambda i: sha1_str[i], arr2))
    result = []
    i = 0
    while i < len(sha1_str):
        result.append(((dict_hex[sha1_str[i]] * 16) + dict_hex[sha1_str[i+1]]) ^ arr3[i//2])
        i += 2
    medium_str = re.sub(r'[\\+/=]', '', b64encode(bytes(result)).decode())
    return ('zzc' + first_str + medium_str + last_str).lower()

cookies = {
    'RK': '44CQhb0/Sk',
    'ptcz': '990a4028ea6a126b87637c8f02dc7e5f929a5d380b92a024e541bd2d2ffe8ebf',
    'pgv_pvid': '1078949012',
    'fqm_pvqid': '134f521e-e9f2-417f-b6c3-ad5b0d04d053',
    'ts_refer': 'www.baidu.com/link',
    'ts_uid': '2574765000',
    'tmeLoginType': '2',
    'wxunionid': '',
    'euin': 'oK-koenA7wvq7z**',
    'qqmusic_key': 'Q_H_L_63k3NsBPmlTmKt0lVvUicMDE6EJE0hwHogL9Tpg8oPMwPsqpHcBWgIGHUFX_SHPgOKDnrEZlSP6G8TRKF6y5G9Q',
    'psrf_qqaccess_token': '6521830AB9CDF2E909C16E5D5BF69AE6',
    'qm_keyst': 'Q_H_L_63k3NsBPmlTmKt0lVvUicMDE6EJE0hwHogL9Tpg8oPMwPsqpHcBWgIGHUFX_SHPgOKDnrEZlSP6G8TRKF6y5G9Q',
    'psrf_qqunionid': 'F681AD9098CCCC80CC09D0A7845197FE',
    'music_ignore_pskey': '202306271436Hn@vBj',
    'uin': '1250026497',
    'psrf_access_token_expiresAt': '1735723503',
    'psrf_qqrefresh_token': '56563E947861C3DA182B6C5EE6C1F003',
    'psrf_musickey_createtime': '1727947503',
    'wxopenid': '',
    'psrf_qqopenid': 'A26C1F8431CA0F23DCF2377095FF27FD',
    'wxrefresh_token': '',
    'fqm_sessionid': 'fb098062-d794-41bd-8305-3d7f17fbaf25',
    'pgv_info': 'ssid=s5592408332',
    'ts_last': 'y.qq.com/n/ryqq/player',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'RK=44CQhb0/Sk; ptcz=990a4028ea6a126b87637c8f02dc7e5f929a5d380b92a024e541bd2d2ffe8ebf; pgv_pvid=1078949012; fqm_pvqid=134f521e-e9f2-417f-b6c3-ad5b0d04d053; ts_refer=www.baidu.com/link; ts_uid=2574765000; tmeLoginType=2; wxunionid=; euin=oK-koenA7wvq7z**; qqmusic_key=Q_H_L_63k3NsBPmlTmKt0lVvUicMDE6EJE0hwHogL9Tpg8oPMwPsqpHcBWgIGHUFX_SHPgOKDnrEZlSP6G8TRKF6y5G9Q; psrf_qqaccess_token=6521830AB9CDF2E909C16E5D5BF69AE6; qm_keyst=Q_H_L_63k3NsBPmlTmKt0lVvUicMDE6EJE0hwHogL9Tpg8oPMwPsqpHcBWgIGHUFX_SHPgOKDnrEZlSP6G8TRKF6y5G9Q; psrf_qqunionid=F681AD9098CCCC80CC09D0A7845197FE; music_ignore_pskey=202306271436Hn@vBj; uin=1250026497; psrf_access_token_expiresAt=1735723503; psrf_qqrefresh_token=56563E947861C3DA182B6C5EE6C1F003; psrf_musickey_createtime=1727947503; wxopenid=; psrf_qqopenid=A26C1F8431CA0F23DCF2377095FF27FD; wxrefresh_token=; fqm_sessionid=fb098062-d794-41bd-8305-3d7f17fbaf25; pgv_info=ssid=s5592408332; ts_last=y.qq.com/n/ryqq/player',
    'origin': 'https://y.qq.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Microsoft Edge";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0',
}

params = {
    '_': '1728004438745',
    # 'sign': 'zzc721de17oenph9drx9hqq6pcjk6hluemogge16f7e0c',
}

data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":1250026497,"g_tk_new_20200303":884997523,"g_tk":884997523},"req_1":{"module":"userInfo.VipQueryServer","method":"SRFVipQuery_V2","param":{"uin_list":["1250026497"]}},"req_2":{"module":"userInfo.BaseUserInfoServer","method":"get_user_baseinfo_v2","param":{"vec_uin":["1250026497"]}},"req_3":{"module":"music.lvz.VipIconUiShowSvr","method":"GetVipIconUiV2","param":{"PID":3}},"req_4":{"module":"music.musicasset.SongFavRead","method":"IsSongFanByMid","param":{"v_songMid":["001PiWfo2pSlN8"]}},"req_5":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"001PiWfo2pSlN8","songID":517907086}},"req_6":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"517907086","biz_sub_type":0}]}},"req_7":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"002SqSOg44hr7c"}},"req_8":{"module":"music.vkey.GetVkey","method":"GetUrl","param":{"guid":"3753685201","songmid":["001PiWfo2pSlN8"],"songtype":[0],"uin":"1250026497","loginflag":1,"platform":"20"}}}'
params['sign'] = get_sign(data)
print(get_sign(data))
response = requests.post('https://u6.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers, data=data)

print(response.text)


