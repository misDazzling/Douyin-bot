# encoding:utf-8
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sys
import random
import time
from PIL import Image
import argparse
import requests
# 从SKD包导入相应产品模块
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.iai.v20200303 import iai_client, models
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.iai.v20200303 import iai_client, models
import base64


if sys.version_info.major != 3:
    print('Please run under Python3')
    exit(1)
try:
    from common import debug, config, screenshot, UnicodeStreamFilter
    from common.auto_adb import auto_adb
    from common import apiutil
    from common.compression import resize_image
except Exception as ex:
    print(ex)
    print('请将脚本放在项目根目录中运行')
    print('请检查项目根目录中的 common 文件夹是否存在')
    exit(1)

VERSION = "0.0.1"

# 我申请的 Key，随便用，嘻嘻嘻
# 申请地址 http://ai.qq.com  下面的AppID和AppKey不需要填，只要填secretID和secretKey
AppID = '1305234700'
AppKey = 'gFmDUZO5vaer0zmNxONFwdDmOqWFtSub'
# 填入自己新建的访问密钥和图片的详细地址
secretId = '***'  #一定要填，需要先在购买腾讯云ai人脸识别的套餐 ，购买链接https://buy.cloud.tencent.com/iai_face?chargeMode=invoke
secretKey = '***' #一定要填，需要先在购买腾讯云ai人脸识别的套餐
img_dir = rb"optimized.png"
DEBUG_SWITCH = True
FACE_PATH = 'face/'

adb = auto_adb()
adb.test_device()
config = config.open_accordant_config()

# 审美标准
BEAUTY_THRESHOLD = 80

# 最小年龄
GIRL_MIN_AGE = 16


def yes_or_no():
    """
    检查是否已经为启动程序做好了准备
    """
    while True:
        yes_or_no = str(input('请确保手机打开了 ADB 并连接了电脑，'
                              '然后打开手机软件，确定开始？[y/n]:'))
        if yes_or_no == 'y':
            break
        elif yes_or_no == 'n':
            print('谢谢使用')
            exit(0)
        else:
            print('请重新输入')


def _random_bias(num):
    """
    random bias
    :param num:
    :return:
    """
    return random.randint(-num, num)


def next_page():
    """
    翻到下一页
    :return:
    """
    print('翻页')
    #cmd = 'shell input touchscreen swipe{x1} {y1} {x2} {y2} {duration}'.format(
        #x1=config['center_point']['x'],
        #y1=config['center_point']['y']+config['center_point']['ry'],
       # x2=config['center_point']['x'],
       # y2=config['center_point']['y'],
       # #duration=200
    #)
    cmd ='shell input touchscreen swipe 529 1664 529 800'
    adb.run(cmd)
    time.sleep(1.5)


def follow_user():
    """
    关注用户
    :return:
    """
    cmd = 'shell input tap {x} {y}'.format(
        x=config['follow_bottom']['x'] + _random_bias(10),
        y=config['follow_bottom']['y'] + _random_bias(10)
    )
    adb.run(cmd)
    time.sleep(0.5)


def thumbs_up():
    """
    点赞
    :return:
    """
    cmd = 'shell input tap {x} {y}'.format(
        x=config['star_bottom']['x'] + _random_bias(10),
        y=config['star_bottom']['y'] + _random_bias(10)
    )
    print('点赞一波！')
    adb.run(cmd)
    time.sleep(0.5)


def tap(x, y):
    cmd = 'shell input tap {x} {y}'.format(
        x=x + _random_bias(10),
        y=y + _random_bias(10)
    )
    adb.run(cmd)


def auto_reply():

    msg = "垆边人似月，皓腕凝霜雪。就在刚刚，我的心动了一下，小姐姐你好可爱呀_Powered_By_Python"


    # 点击右侧评论按钮
    tap(config['comment_bottom']['x'], config['comment_bottom']['y'])
    time.sleep(1)
    #弹出评论列表后点击输入评论框
    tap(config['comment_text']['x'], config['comment_text']['y'])
    time.sleep(1)
    #输入上面msg内容 ，注意要使用ADB keyboard  否则不能自动输入，参考： https://www.jianshu.com/p/2267adf15595
    cmd = "shell am broadcast -a ADB_INPUT_TEXT --es msg {text}".format(text=msg)
    #cmd = "shell am broadcast -a ADB_INPUT_TEXT --es '垆边人似月，皓腕凝霜雪。就在刚刚，我的心动了一下，小姐姐你好可爱呀-Powered_By_Python'"
    adb.run(cmd)
    time.sleep(1)
    # 点击发送按钮
    tap(config['comment_send']['x'], config['comment_send']['y'])
    time.sleep(0.5)

    # 触发返回按钮, keyevent 4 对应安卓系统的返回键，参考KEY 对应按钮操作：  https://www.cnblogs.com/chengchengla1990/p/4515108.html
    cmd = 'shell input keyevent 4'
    adb.run(cmd)


def parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-r", "--reply", action='store_true',
                    help="auto reply")
    args = vars(ap.parse_args())
    return args

def get_json(img_dir):
    with open(img_dir, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        base64_code = base64_data.decode()
    try:
        # 实例化一个请求-响应协议
        httpProfile = HttpProfile()
        httpProfile.endpoint = "iai.tencentcloudapi.com" # 接口请求域名
        # 实例化一个客户端配置对象
        clientProfile = ClientProfile()
        clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
        # 实例化一个认证对象
        cred = credential.Credential(secretId,secretKey) # 传入腾讯云账户 secretId，secretKey
        client = iai_client.IaiClient(cred,"ap-beijing",clientProfile) #传入地域参数
        # 实例化一个请求对象
        req = models.DetectFaceRequest()

        # 人脸检测参数
        req.MaxFaceNum = 1
        req.Image = base64_code
        req.NeedFaceAttributes = 1
        req.NeedQualityDetection = 1

        # 通过 client 对象调用想要访问的接口，需要传入请求对象
        resp = client.DetectFace(req)
        # 输出 JSON 格式的字符串回包
        json_data = resp.to_json_string()
        return json_data

    except TencentCloudSDKException as err:
     print(err)
    return None

def main():
    """
    main
    :return:
    """
    print('程序版本号：{}'.format(VERSION))
    print('激活窗口并按 CONTROL + C 组合键退出')
    debug.dump_device_info()
    screenshot.check_screenshot()

    cmd_args = parser()

    while True:
        next_page()

        time.sleep(1)
        screenshot.pull_screenshot()

        resize_image('autojump.png', 'optimized.png', 540*1200)

        json_data = get_json(img_dir)

        if json_data ==None:
            print('没有人脸，开始撤退！')
            continue
        #print(json_data)
        beauty = 0
        str = json.loads(json_data)
        #print(str['FaceInfos'][0]['FaceAttributesInfo']['Beauty'])


        dict1 = str['FaceInfos'][0]


        #print(dict1) #输出详细信息
        major_total = 0
        minor_total = 0
        #print(rsp)




        msg_log = '[INFO] gender: {gender} age: {age} expression: {expression} beauty: {beauty}'.format(
                    gender=dict1['FaceAttributesInfo']['Gender'],
                    age=dict1['FaceAttributesInfo']['Age'],
                    expression=dict1['FaceAttributesInfo']['Expression'],
                    beauty=dict1['FaceAttributesInfo']['Beauty'],
        )
        print(msg_log) #输出简略信息
        face_area = (dict1['X'], dict1['Y'], dict1['X']+dict1['Width'], dict1['Y']+dict1['Height'])
        img = Image.open("optimized.png")
        cropped_img = img.crop(face_area).convert('RGB')
        cropped_img.save(FACE_PATH + str['RequestId'] + '.png')
        # 性别判断
        if dict1['FaceAttributesInfo']['Gender'] > 50:
            print("是个小哥哥，撤退！")
            continue
        if dict1['FaceAttributesInfo']['Beauty']> beauty and dict1['FaceAttributesInfo']['Gender'] < 50:
            beauty =dict1['FaceAttributesInfo']['Beauty']

        if dict1['FaceAttributesInfo']['Age'] > GIRL_MIN_AGE:
            major_total += 1
        else:
            minor_total += 1

        # 是个美人儿~关注点赞走一波
        if beauty > BEAUTY_THRESHOLD and major_total > minor_total:
            print('发现漂亮妹子！！！')
            thumbs_up()#点赞
            auto_reply()#评论
            next_page()#下一页，不要删，不然会出bug
            #follow_user()


            if cmd_args['reply']:
                auto_reply()
        else:
            print('下一个')



if __name__ == '__main__':
    try:
        # yes_or_no()
        main()
    except KeyboardInterrupt:
        adb.run('kill-server')
        print('谢谢使用')
        exit(0)
