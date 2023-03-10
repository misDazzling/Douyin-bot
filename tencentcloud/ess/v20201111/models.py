# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Admin(AbstractModel):
    """企业超管信息

    """

    def __init__(self):
        r"""
        :param Name: 超管名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Mobile: 超管手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type Mobile: str
        """
        self.Name = None
        self.Mobile = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Agent(AbstractModel):
    """代理相关应用信息，如集团主企业代子企业操作

    """

    def __init__(self):
        r"""
        :param AppId: 代理机构的应用编号,32位字符串，一般不用传
        :type AppId: str
        :param ProxyAppId: 被代理机构的应用号，一般不用传
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyAppId: str
        :param ProxyOrganizationId: 被代理机构在电子签平台的机构编号，集团代理下场景必传
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOrganizationId: str
        :param ProxyOperator: 被代理机构的经办人，一般不用传
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyOperator: str
        """
        self.AppId = None
        self.ProxyAppId = None
        self.ProxyOrganizationId = None
        self.ProxyOperator = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ProxyAppId = params.get("ProxyAppId")
        self.ProxyOrganizationId = params.get("ProxyOrganizationId")
        self.ProxyOperator = params.get("ProxyOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverInfo(AbstractModel):
    """参与者信息

    """

    def __init__(self):
        r"""
        :param ApproverType: 参与者类型：
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。静默签署仅进行盖章操作，不能自动签名。
        :type ApproverType: int
        :param ApproverName: 本环节需要操作人的名字
        :type ApproverName: str
        :param ApproverMobile: 本环节需要操作人的手机号
        :type ApproverMobile: str
        :param SignComponents: 本环节操作人签署控件配置
        :type SignComponents: list of Component
        :param OrganizationName: 如果是企业,则为企业的名字
        :type OrganizationName: str
        :param ApproverIdCardNumber: 身份证号
        :type ApproverIdCardNumber: str
        :param ApproverIdCardType: 证件类型 
ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type ApproverIdCardType: str
        :param NotifyType: sms--短信，none--不通知
        :type NotifyType: str
        :param ApproverRole: 1--收款人、2--开具人、3--见证人
        :type ApproverRole: int
        :param VerifyChannel: 签署意愿确认渠道,WEIXINAPP:人脸识别
        :type VerifyChannel: list of str
        :param PreReadTime: 合同的强制预览时间：3~300s，未指定则按合同页数计算
        :type PreReadTime: int
        :param UserId: 签署人userId，传此字段则不用传姓名、手机号
        :type UserId: str
        :param ApproverSource: 签署人用户来源,企微侧用户请传入：WEWORKAPP
        :type ApproverSource: str
        :param CustomApproverTag: 客户自定义签署人标识，64位长度，保证唯一，非企微场景不使用此字段
        :type CustomApproverTag: str
        :param ApproverOption: 签署人个性化能力值
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        """
        self.ApproverType = None
        self.ApproverName = None
        self.ApproverMobile = None
        self.SignComponents = None
        self.OrganizationName = None
        self.ApproverIdCardNumber = None
        self.ApproverIdCardType = None
        self.NotifyType = None
        self.ApproverRole = None
        self.VerifyChannel = None
        self.PreReadTime = None
        self.UserId = None
        self.ApproverSource = None
        self.CustomApproverTag = None
        self.ApproverOption = None


    def _deserialize(self, params):
        self.ApproverType = params.get("ApproverType")
        self.ApproverName = params.get("ApproverName")
        self.ApproverMobile = params.get("ApproverMobile")
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.OrganizationName = params.get("OrganizationName")
        self.ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self.ApproverIdCardType = params.get("ApproverIdCardType")
        self.NotifyType = params.get("NotifyType")
        self.ApproverRole = params.get("ApproverRole")
        self.VerifyChannel = params.get("VerifyChannel")
        self.PreReadTime = params.get("PreReadTime")
        self.UserId = params.get("UserId")
        self.ApproverSource = params.get("ApproverSource")
        self.CustomApproverTag = params.get("CustomApproverTag")
        if params.get("ApproverOption") is not None:
            self.ApproverOption = ApproverOption()
            self.ApproverOption._deserialize(params.get("ApproverOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverOption(AbstractModel):
    """签署人个性化能力信息

    """

    def __init__(self):
        r"""
        :param NoRefuse: 是否可以拒签 false-可以拒签,默认 true-不可以拒签
        :type NoRefuse: bool
        :param NoTransfer: 是否可以转发 false-可以转发,默认 true-不可以转发
        :type NoTransfer: bool
        """
        self.NoRefuse = None
        self.NoTransfer = None


    def _deserialize(self, params):
        self.NoRefuse = params.get("NoRefuse")
        self.NoTransfer = params.get("NoTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproverRestriction(AbstractModel):
    """指定签署人限制项

    """

    def __init__(self):
        r"""
        :param Name: 指定签署人名字
        :type Name: str
        :param Mobile: 指定签署人手机号
        :type Mobile: str
        :param IdCardType: 指定签署人证件类型
        :type IdCardType: str
        :param IdCardNumber: 指定签署人证件号码
        :type IdCardNumber: str
        """
        self.Name = None
        self.Mobile = None
        self.IdCardType = None
        self.IdCardNumber = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizedUser(AbstractModel):
    """授权用户

    """

    def __init__(self):
        r"""
        :param UserId: 用户id
        :type UserId: str
        """
        self.UserId = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSignConfig(AbstractModel):
    """自动签开启、签署相关配置

    """

    def __init__(self):
        r"""
        :param UserInfo: 自动签开通个人用户的三要素
注意：此字段可能返回 null，表示取不到有效值。
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        :param CallbackUrl: 回调链接
注意：此字段可能返回 null，表示取不到有效值。
        :type CallbackUrl: str
        :param CertInfoCallback: 是否回调证书信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfoCallback: bool
        :param UserDefineSeal: 是否支持用户自定义签名印章
注意：此字段可能返回 null，表示取不到有效值。
        :type UserDefineSeal: bool
        :param SealImgCallback: 是否需要回调的时候返回印章(签名) 图片的 base64
注意：此字段可能返回 null，表示取不到有效值。
        :type SealImgCallback: bool
        :param VerifyChannels: 开通时候的验证方式，取值：WEIXINAPP（微信人脸识别），INSIGHT（慧眼人脸认别），TELECOM（运营商三要素验证）。如果是小程序开通链接，支持传 WEIXINAPP / TELECOM。如果是 H5 开通链接，支持传 INSIGHT / TELECOM。默认值 WEIXINAPP / INSIGHT。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyChannels: list of str
        """
        self.UserInfo = None
        self.CallbackUrl = None
        self.CertInfoCallback = None
        self.UserDefineSeal = None
        self.SealImgCallback = None
        self.VerifyChannels = None


    def _deserialize(self, params):
        if params.get("UserInfo") is not None:
            self.UserInfo = UserThreeFactor()
            self.UserInfo._deserialize(params.get("UserInfo"))
        self.CallbackUrl = params.get("CallbackUrl")
        self.CertInfoCallback = params.get("CertInfoCallback")
        self.UserDefineSeal = params.get("UserDefineSeal")
        self.SealImgCallback = params.get("SealImgCallback")
        self.VerifyChannels = params.get("VerifyChannels")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Caller(AbstractModel):
    """此结构体 (Caller) 用于描述调用方属性。

    """

    def __init__(self):
        r"""
        :param ApplicationId: 应用号
        :type ApplicationId: str
        :param OrganizationId: 主机构ID
        :type OrganizationId: str
        :param OperatorId: 经办人的用户ID
        :type OperatorId: str
        :param SubOrganizationId: 下属机构ID
        :type SubOrganizationId: str
        """
        self.ApplicationId = None
        self.OrganizationId = None
        self.OperatorId = None
        self.SubOrganizationId = None


    def _deserialize(self, params):
        self.ApplicationId = params.get("ApplicationId")
        self.OrganizationId = params.get("OrganizationId")
        self.OperatorId = params.get("OperatorId")
        self.SubOrganizationId = params.get("SubOrganizationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowRequest(AbstractModel):
    """CancelFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程id
        :type FlowId: str
        :param CancelMessage: 撤销原因，最长200个字符；
        :type CancelMessage: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowId = None
        self.CancelMessage = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.CancelMessage = params.get("CancelMessage")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelFlowResponse(AbstractModel):
    """CancelFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelMultiFlowSignQRCodeRequest(AbstractModel):
    """CancelMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param QrCodeId: 二维码id
        :type QrCodeId: str
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.QrCodeId = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.QrCodeId = params.get("QrCodeId")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelMultiFlowSignQRCodeResponse(AbstractModel):
    """CancelMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CcInfo(AbstractModel):
    """抄送信息

    """

    def __init__(self):
        r"""
        :param Mobile: 被抄送人手机号
        :type Mobile: str
        """
        self.Mobile = None


    def _deserialize(self, params):
        self.Mobile = params.get("Mobile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Component(AbstractModel):
    """模板控件信息

    """

    def __init__(self):
        r"""
        :param ComponentType: 如果是Component控件类型，则可选的字段为：
TEXT - 普通文本控件，输入文本字符串；
MULTI_LINE_TEXT - 多行文本控件，输入文本字符串；
CHECK_BOX - 勾选框控件，若选中填写ComponentValue 填写 true或者 false 字符串；
FILL_IMAGE - 图片控件，ComponentValue 填写图片的资源 ID；
DYNAMIC_TABLE - 动态表格控件；
ATTACHMENT - 附件控件,ComponentValue 填写福建图片的资源 ID列表，以逗号分割；
SELECTOR - 选择器控件，ComponentValue填写选择的字符串内容；
DATE - 日期控件；默认是格式化为xxxx年xx月xx日字符串；
DISTRICT - 省市区行政区划控件，ComponentValue填写省市区行政区划字符串内容；

如果是SignComponent控件类型，则可选的字段为
SIGN_SEAL - 签署印章控件；
SIGN_DATE - 签署日期控件；
SIGN_SIGNATURE - 用户签名控件；
SIGN_PERSONAL_SEAL - 个人签署印章控件（使用文件发起暂不支持此类型）；
SIGN_PAGING_SEAL - 骑缝章；若文件发起，需要对应填充ComponentPosY、ComponentWidth、ComponentHeight
SIGN_OPINION - 签署意见控件，用户需要根据配置的签署意见内容，完成对意见内容的确认；
SIGN_LEGAL_PERSON_SEAL - 企业法定代表人控件。

表单域的控件不能作为印章和签名控件
        :type ComponentType: str
        :param FileIndex: 控件所属文件的序号（模板中的resourceId排列序号，取值为：0-N）
        :type FileIndex: int
        :param ComponentHeight: 参数控件高度，单位pt
        :type ComponentHeight: float
        :param ComponentWidth: 参数控件宽度，单位pt
        :type ComponentWidth: float
        :param ComponentPage: 参数控件所在页码，取值为：1-N
        :type ComponentPage: int
        :param ComponentPosX: 参数控件X位置，单位pt
        :type ComponentPosX: float
        :param ComponentPosY: 参数控件Y位置，单位pt
        :type ComponentPosY: float
        :param ComponentId: GenerateMode==KEYWORD 指定关键字
        :type ComponentId: str
        :param ComponentName: GenerateMode==FIELD 指定表单域名称
        :type ComponentName: str
        :param ComponentRequired: 是否必选，默认为false
        :type ComponentRequired: bool
        :param ComponentRecipientId: 控件关联的签署人ID
        :type ComponentRecipientId: str
        :param ComponentExtra: 扩展参数：
为JSON格式。

ComponentType为FILL_IMAGE时，支持以下参数：
NotMakeImageCenter：bool。是否设置图片居中。false：居中（默认）。 true: 不居中
FillMethod: int. 填充方式。0-铺满（默认）；1-等比例缩放

ComponentType为SIGN_SIGNATURE类型可以控制签署方式
{“ComponentTypeLimit”: [“xxx”]}
xxx可以为：
HANDWRITE – 手写签名
BORDERLESS_ESIGN – 自动生成无边框腾讯体
OCR_ESIGN -- AI智能识别手写签名
ESIGN -- 个人印章类型
如：{“ComponentTypeLimit”: [“BORDERLESS_ESIGN”]}
        :type ComponentExtra: str
        :param IsFormType: 是否是表单域类型，默认不存在
        :type IsFormType: bool
        :param ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
DATE - 默认是格式化为xxxx年xx月xx日
SIGN_SEAL - 印章ID，于控制台查询获取
SIGN_PAGING_SEAL - 可以指定印章ID，于控制台查询获取

控件值约束说明：
企业全称控件：
  约束：企业名称中文字符中文括号
  检查正则表达式：/^[\u3400-\u4dbf\u4e00-\u9fa5（）]+$/

统一社会信用代码控件：
  检查正则表达式：/^[A-Z0-9]{1,18}$/

法人名称控件：
  约束：最大50个字符，2到25个汉字或者1到50个字母
  检查正则表达式：/^([\u3400-\u4dbf\u4e00-\u9fa5.·]{2,25}|[a-zA-Z·,\s-]{1,50})$/

签署意见控件：
  约束：签署意见最大长度为50字符

签署人手机号控件：
  约束：国内手机号 13,14,15,16,17,18,19号段长度11位

签署人身份证控件：
  约束：合法的身份证号码检查

控件名称：
  约束：控件名称最大长度为20字符

单行文本控件：
  约束：只允许输入中文，英文，数字，中英文标点符号

多行文本控件：
  约束：只允许输入中文，英文，数字，中英文标点符号

勾选框控件：
  约束：选择填字符串true，不选填字符串false

选择器控件：
  约束：同单行文本控件约束，填写选择值中的字符串

数字控件：
  约束：请输入有效的数字(可带小数点) 
  检查正则表达式：/^(-|\+)?\d+(\.\d+)?$/

日期控件：
  约束：格式：yyyy年mm月dd日

附件控件：
  约束：JPG或PNG图片，上传数量限制，1到6个，最大6个附件

图片控件：
  约束：JPG或PNG图片，填写上传的图片资源ID

邮箱控件：
  约束：请输入有效的邮箱地址, w3c标准
  检查正则表达式：/^([A-Za-z0-9_\-.!#$%&])+@([A-Za-z0-9_\-.])+\.([A-Za-z]{2,4})$/
  参考：https://emailregex.com/

地址控件：
  同单行文本控件约束

省市区控件：
  同单行文本控件约束

性别控件：
  同单行文本控件约束，填写选择值中的字符串

学历控件：
  同单行文本控件约束，填写选择值中的字符串
        :type ComponentValue: str
        :param GenerateMode: NORMAL 正常模式，使用坐标制定签署控件位置
FIELD 表单域，需使用ComponentName指定表单域名称
KEYWORD 关键字，使用ComponentId指定关键字
        :type GenerateMode: str
        :param ComponentDateFontSize: 日期签署控件的字号，默认为 12
        :type ComponentDateFontSize: int
        :param ChannelComponentId: 渠道版控件 id 标识
        :type ChannelComponentId: str
        :param OffsetX: 指定关键字时横坐标偏移量，单位pt
        :type OffsetX: float
        :param OffsetY: 指定关键字时纵坐标偏移量，单位pt
        :type OffsetY: float
        :param ChannelComponentSource: //渠道子客控件来源。0-渠道指定；1-用户自定义
        :type ChannelComponentSource: int
        :param KeywordOrder: 指定关键字排序规则，Positive-正序，Reverse-倒序。传入Positive时会根据关键字在PDF文件内的顺序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的第一个关键字。
传入Reverse时会根据关键字在PDF文件内的反序进行排列。在指定KeywordIndexes时，0代表在PDF内查找内容时，查找到的最后一个关键字。
        :type KeywordOrder: str
        :param KeywordPage: 指定关键字页码，可选参数，指定页码后，将只在指定的页码内查找关键字，非该页码的关键字将不会查询出来
        :type KeywordPage: int
        :param RelativeLocation: 关键字位置模式，Middle-居中，Below-正下方，Right-正右方，LowerRight-右上角，UpperRight-右下角。示例：如果设置Middle的关键字盖章，则印章的中心会和关键字的中心重合，如果设置Below，则印章在关键字的正下方
        :type RelativeLocation: str
        :param KeywordIndexes: 关键字索引，可选参数，如果一个关键字在PDF文件中存在多个，可以通过关键字索引指定使用第几个关键字作为最后的结果，可指定多个索引。示例：[0,2]，说明使用PDF文件内第1个和第3个关键字位置。
        :type KeywordIndexes: list of int
        """
        self.ComponentType = None
        self.FileIndex = None
        self.ComponentHeight = None
        self.ComponentWidth = None
        self.ComponentPage = None
        self.ComponentPosX = None
        self.ComponentPosY = None
        self.ComponentId = None
        self.ComponentName = None
        self.ComponentRequired = None
        self.ComponentRecipientId = None
        self.ComponentExtra = None
        self.IsFormType = None
        self.ComponentValue = None
        self.GenerateMode = None
        self.ComponentDateFontSize = None
        self.ChannelComponentId = None
        self.OffsetX = None
        self.OffsetY = None
        self.ChannelComponentSource = None
        self.KeywordOrder = None
        self.KeywordPage = None
        self.RelativeLocation = None
        self.KeywordIndexes = None


    def _deserialize(self, params):
        self.ComponentType = params.get("ComponentType")
        self.FileIndex = params.get("FileIndex")
        self.ComponentHeight = params.get("ComponentHeight")
        self.ComponentWidth = params.get("ComponentWidth")
        self.ComponentPage = params.get("ComponentPage")
        self.ComponentPosX = params.get("ComponentPosX")
        self.ComponentPosY = params.get("ComponentPosY")
        self.ComponentId = params.get("ComponentId")
        self.ComponentName = params.get("ComponentName")
        self.ComponentRequired = params.get("ComponentRequired")
        self.ComponentRecipientId = params.get("ComponentRecipientId")
        self.ComponentExtra = params.get("ComponentExtra")
        self.IsFormType = params.get("IsFormType")
        self.ComponentValue = params.get("ComponentValue")
        self.GenerateMode = params.get("GenerateMode")
        self.ComponentDateFontSize = params.get("ComponentDateFontSize")
        self.ChannelComponentId = params.get("ChannelComponentId")
        self.OffsetX = params.get("OffsetX")
        self.OffsetY = params.get("OffsetY")
        self.ChannelComponentSource = params.get("ChannelComponentSource")
        self.KeywordOrder = params.get("KeywordOrder")
        self.KeywordPage = params.get("KeywordPage")
        self.RelativeLocation = params.get("RelativeLocation")
        self.KeywordIndexes = params.get("KeywordIndexes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchCancelFlowUrlRequest(AbstractModel):
    """CreateBatchCancelFlowUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowIds: 需要执行撤回的签署流程id数组，最多100个
        :type FlowIds: list of str
        """
        self.Operator = None
        self.FlowIds = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowIds = params.get("FlowIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBatchCancelFlowUrlResponse(AbstractModel):
    """CreateBatchCancelFlowUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param BatchCancelFlowUrl: 批量撤回签署流程链接
        :type BatchCancelFlowUrl: str
        :param FailMessages: 签署流程撤回失败信息
        :type FailMessages: list of str
        :param UrlExpireOn: 签署连接过期时间字符串：年月日-时分秒
        :type UrlExpireOn: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BatchCancelFlowUrl = None
        self.FailMessages = None
        self.UrlExpireOn = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BatchCancelFlowUrl = params.get("BatchCancelFlowUrl")
        self.FailMessages = params.get("FailMessages")
        self.UrlExpireOn = params.get("UrlExpireOn")
        self.RequestId = params.get("RequestId")


class CreateConvertTaskApiRequest(AbstractModel):
    """CreateConvertTaskApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceType: 资源类型 取值范围doc,docx,html,xls,xlsx之一
        :type ResourceType: str
        :param ResourceName: 资源名称，长度限制为256字符
        :type ResourceName: str
        :param ResourceId: 资源Id，通过UploadFiles获取
        :type ResourceId: str
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Agent: 应用号信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param Organization: 暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        """
        self.ResourceType = None
        self.ResourceName = None
        self.ResourceId = None
        self.Operator = None
        self.Agent = None
        self.Organization = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceName = params.get("ResourceName")
        self.ResourceId = params.get("ResourceId")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateConvertTaskApiResponse(AbstractModel):
    """CreateConvertTaskApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 转换任务Id
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateDocumentRequest(AbstractModel):
    """CreateDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号,由CreateFlow接口返回
        :type FlowId: str
        :param TemplateId: 用户上传的模板ID
        :type TemplateId: str
        :param FileNames: 文件名列表，单个文件名最大长度200个字符，暂时仅支持单文件发起
        :type FileNames: list of str
        :param FormFields: 内容控件信息数组
        :type FormFields: list of FormField
        :param NeedPreview: 是否需要生成预览文件 默认不生成；
预览链接有效期300秒；
        :type NeedPreview: bool
        :param PreviewType: 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效,
        :type PreviewType: int
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        """
        self.Operator = None
        self.FlowId = None
        self.TemplateId = None
        self.FileNames = None
        self.FormFields = None
        self.NeedPreview = None
        self.PreviewType = None
        self.Agent = None
        self.ClientToken = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.TemplateId = params.get("TemplateId")
        self.FileNames = params.get("FileNames")
        if params.get("FormFields") is not None:
            self.FormFields = []
            for item in params.get("FormFields"):
                obj = FormField()
                obj._deserialize(item)
                self.FormFields.append(obj)
        self.NeedPreview = params.get("NeedPreview")
        self.PreviewType = params.get("PreviewType")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocumentResponse(AbstractModel):
    """CreateDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param DocumentId: 签署流程电子文档ID
        :type DocumentId: str
        :param PreviewFileUrl: 签署流程文件的预览地址, 5分钟内有效。仅当NeedPreview为true 时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewFileUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DocumentId = None
        self.PreviewFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DocumentId = params.get("DocumentId")
        self.PreviewFileUrl = params.get("PreviewFileUrl")
        self.RequestId = params.get("RequestId")


class CreateFlowApproversRequest(AbstractModel):
    """CreateFlowApprovers请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param Approvers: 补充签署人信息
        :type Approvers: list of FillApproverInfo
        :param Initiator: 企微消息中的发起人
        :type Initiator: str
        """
        self.Operator = None
        self.FlowId = None
        self.Approvers = None
        self.Initiator = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = FillApproverInfo()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.Initiator = params.get("Initiator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowApproversResponse(AbstractModel):
    """CreateFlowApprovers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFlowByFilesRequest(AbstractModel):
    """CreateFlowByFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId 代发合同
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowName: 签署流程名称,最大长度200个字符
        :type FlowName: str
        :param Approvers: 签署参与者信息，最大限制50方
        :type Approvers: list of ApproverInfo
        :param FileIds: 签署pdf文件的资源编号列表，通过UploadFiles接口获取，暂时仅支持单文件发起
        :type FileIds: list of str
        :param FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
        :type FlowType: str
        :param Components: 经办人内容控件配置
        :type Components: list of Component
        :param CcInfos: 被抄送人的信息列表。
注:此功能为白名单功能，若有需要，请联系电子签客服开白使用
        :type CcInfos: list of CcInfo
        :param NeedPreview: 是否需要预览，true：预览模式，false：非预览（默认）；
预览链接有效期300秒；

注：如果使用“预览模式”，出参会返回合同预览链接 PreviewUrl，不会正式发起合同，且出参不会返回签署流程编号 FlowId；如果使用“非预览”，则会正常返回签署流程编号 FlowId，不会生成合同预览链接 PreviewUrl。
        :type NeedPreview: bool
        :param PreviewType: 预览链接类型 默认:0-文件流, 1- H5链接 注意:此参数在NeedPreview 为true 时有效,
        :type PreviewType: int
        :param Deadline: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type Deadline: int
        :param Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签）
        :type Unordered: bool
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。
若设置为true，审核结果需通过接口 CreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        :param UserData: 用户自定义字段，回调的时候会进行透传，长度需要小于20480
        :type UserData: str
        :param ApproverVerifyType: 签署人校验方式
VerifyCheck: 人脸识别（默认）
MobileCheck：手机号验证
参数说明：可选人脸识别或手机号验证两种方式，若选择后者，未实名个人签署方在签署合同时，无需经过实名认证和意愿确认两次人脸识别，该能力仅适用于个人签署方。
        :type ApproverVerifyType: str
        :param FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param SignBeanTag: 标识是否允许发起后添加控件。0为不允许1为允许。如果为1，创建的时候不能有签署控件，只能创建后添加。注意发起后添加控件功能不支持添加骑缝章和签批控件
        :type SignBeanTag: int
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowName = None
        self.Approvers = None
        self.FileIds = None
        self.FlowType = None
        self.Components = None
        self.CcInfos = None
        self.NeedPreview = None
        self.PreviewType = None
        self.Deadline = None
        self.Unordered = None
        self.CustomShowMap = None
        self.NeedSignReview = None
        self.UserData = None
        self.ApproverVerifyType = None
        self.FlowDescription = None
        self.SignBeanTag = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = ApproverInfo()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.FileIds = params.get("FileIds")
        self.FlowType = params.get("FlowType")
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        if params.get("CcInfos") is not None:
            self.CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self.CcInfos.append(obj)
        self.NeedPreview = params.get("NeedPreview")
        self.PreviewType = params.get("PreviewType")
        self.Deadline = params.get("Deadline")
        self.Unordered = params.get("Unordered")
        self.CustomShowMap = params.get("CustomShowMap")
        self.NeedSignReview = params.get("NeedSignReview")
        self.UserData = params.get("UserData")
        self.ApproverVerifyType = params.get("ApproverVerifyType")
        self.FlowDescription = params.get("FlowDescription")
        self.SignBeanTag = params.get("SignBeanTag")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowByFilesResponse(AbstractModel):
    """CreateFlowByFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 签署流程编号。

注：如入参 是否需要预览 NeedPreview 设置为 true，不会正式发起合同，此处不会有值返回；如入参 是否需要预览 NeedPreview 设置为 false，此处会正常返回签署流程编号 FlowId。
        :type FlowId: str
        :param PreviewUrl: 合同预览链接。

注：如入参 是否需要预览 NeedPreview 设置为 true，会开启“预览模式”，此处会返回预览链接；如入参 是否需要预览 NeedPreview 设置为 false，此处不会有值返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.PreviewUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.PreviewUrl = params.get("PreviewUrl")
        self.RequestId = params.get("RequestId")


class CreateFlowEvidenceReportRequest(AbstractModel):
    """CreateFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号
        :type FlowId: str
        """
        self.Operator = None
        self.FlowId = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowEvidenceReportResponse(AbstractModel):
    """CreateFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportId: 出证报告 ID，用于查询出证报告DescribeFlowEvidenceReport接口时用到
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param Status: 执行中：EvidenceStatusExecuting
成功：EvidenceStatusSuccess
失败：EvidenceStatusFailed
        :type Status: str
        :param ReportUrl: 废除，字段无效
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportId = None
        self.Status = None
        self.ReportUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportId = params.get("ReportId")
        self.Status = params.get("Status")
        self.ReportUrl = params.get("ReportUrl")
        self.RequestId = params.get("RequestId")


class CreateFlowRemindsRequest(AbstractModel):
    """CreateFlowReminds请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowIds: 需要执行催办的签署流程id数组，最多100个
        :type FlowIds: list of str
        """
        self.Operator = None
        self.FlowIds = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowIds = params.get("FlowIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowRemindsResponse(AbstractModel):
    """CreateFlowReminds返回参数结构体

    """

    def __init__(self):
        r"""
        :param RemindFlowRecords: 签署连接过期时间字符串：年月日-时分秒
        :type RemindFlowRecords: list of RemindFlowRecords
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RemindFlowRecords = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RemindFlowRecords") is not None:
            self.RemindFlowRecords = []
            for item in params.get("RemindFlowRecords"):
                obj = RemindFlowRecords()
                obj._deserialize(item)
                self.RemindFlowRecords.append(obj)
        self.RequestId = params.get("RequestId")


class CreateFlowRequest(AbstractModel):
    """CreateFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowName: 签署流程名称,最大长度200个字符
        :type FlowName: str
        :param Approvers: 签署流程参与者信息，最大限制50方
        :type Approvers: list of FlowCreateApprover
        :param FlowType: 签署流程的类型(如销售合同/入职合同等)，最大长度200个字符
        :type FlowType: str
        :param ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param RelatedFlowId: 暂未开放
        :type RelatedFlowId: str
        :param DeadLine: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type DeadLine: int
        :param UserData: 用户自定义字段，回调的时候会进行透传，长度需要小于20480
        :type UserData: str
        :param FlowDescription: 签署流程描述,最大长度1000个字符
        :type FlowDescription: str
        :param Unordered: 发送类型：
true：无序签
false：有序签
注：默认为false（有序签），请和模板中的配置保持一致
        :type Unordered: bool
        :param CustomShowMap: 合同显示的页卡模板，说明：只支持{合同名称}, {发起方企业}, {发起方姓名}, {签署方N企业}, {签署方N姓名}，且N不能超过签署人的数量，N从1开始
        :type CustomShowMap: str
        :param NeedSignReview: 发起方企业的签署人进行签署操作是否需要企业内部审批。使用此功能需要发起方企业有参与签署。
若设置为true，审核结果需通过接口 CreateFlowSignReview 通知电子签，审核通过后，发起方企业签署人方可进行签署操作，否则会阻塞其签署操作。

注：企业可以通过此功能与企业内部的审批流程进行关联，支持手动、静默签署合同。
        :type NeedSignReview: bool
        :param CallbackUrl: 暂未开放
        :type CallbackUrl: str
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param CcInfos: 被抄送人的信息列表。
注: 此功能为白名单功能，若有需要，请联系电子签客服开白使用。
        :type CcInfos: list of CcInfo
        """
        self.Operator = None
        self.FlowName = None
        self.Approvers = None
        self.FlowType = None
        self.ClientToken = None
        self.RelatedFlowId = None
        self.DeadLine = None
        self.UserData = None
        self.FlowDescription = None
        self.Unordered = None
        self.CustomShowMap = None
        self.NeedSignReview = None
        self.CallbackUrl = None
        self.Agent = None
        self.CcInfos = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowName = params.get("FlowName")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.FlowType = params.get("FlowType")
        self.ClientToken = params.get("ClientToken")
        self.RelatedFlowId = params.get("RelatedFlowId")
        self.DeadLine = params.get("DeadLine")
        self.UserData = params.get("UserData")
        self.FlowDescription = params.get("FlowDescription")
        self.Unordered = params.get("Unordered")
        self.CustomShowMap = params.get("CustomShowMap")
        self.NeedSignReview = params.get("NeedSignReview")
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("CcInfos") is not None:
            self.CcInfos = []
            for item in params.get("CcInfos"):
                obj = CcInfo()
                obj._deserialize(item)
                self.CcInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowResponse(AbstractModel):
    """CreateFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateFlowSignReviewRequest(AbstractModel):
    """CreateFlowSignReview请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号
        :type FlowId: str
        :param ReviewType: 企业内部审核结果
PASS: 通过 
REJECT: 拒绝
        :type ReviewType: str
        :param ReviewMessage: 审核原因 
当ReviewType 是REJECT 时此字段必填,字符串长度不超过200
        :type ReviewMessage: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowId = None
        self.ReviewType = None
        self.ReviewMessage = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.ReviewType = params.get("ReviewType")
        self.ReviewMessage = params.get("ReviewMessage")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowSignReviewResponse(AbstractModel):
    """CreateFlowSignReview返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFlowSignUrlRequest(AbstractModel):
    """CreateFlowSignUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 流程编号
        :type FlowId: str
        :param FlowApproverInfos: 流程签署人，其中ApproverName，ApproverMobile和ApproverType必传，其他可不传，ApproverType目前只支持个人类型的签署人。还需注意签署人只能有手写签名和时间类型的签署控件，其他类型的填写控件和签署控件暂时都未支持。
        :type FlowApproverInfos: list of FlowCreateApprover
        :param Organization: 机构信息，暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param Operator: 用户信息，此结构体UserId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        """
        self.FlowId = None
        self.FlowApproverInfos = None
        self.Organization = None
        self.Operator = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("FlowApproverInfos") is not None:
            self.FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self.FlowApproverInfos.append(obj)
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFlowSignUrlResponse(AbstractModel):
    """CreateFlowSignUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowApproverUrlInfos: 签署人签署链接信息
        :type FlowApproverUrlInfos: list of FlowApproverUrlInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowApproverUrlInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowApproverUrlInfos") is not None:
            self.FlowApproverUrlInfos = []
            for item in params.get("FlowApproverUrlInfos"):
                obj = FlowApproverUrlInfo()
                obj._deserialize(item)
                self.FlowApproverUrlInfos.append(obj)
        self.RequestId = params.get("RequestId")


class CreateIntegrationEmployeesRequest(AbstractModel):
    """CreateIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Employees: 待创建员工的信息，Mobile和DisplayName必填
        :type Employees: list of Staff
        """
        self.Operator = None
        self.Employees = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Employees") is not None:
            self.Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self.Employees.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIntegrationEmployeesResponse(AbstractModel):
    """CreateIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param CreateEmployeeResult: 创建员工的结果
        :type CreateEmployeeResult: :class:`tencentcloud.ess.v20201111.models.CreateStaffResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CreateEmployeeResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CreateEmployeeResult") is not None:
            self.CreateEmployeeResult = CreateStaffResult()
            self.CreateEmployeeResult._deserialize(params.get("CreateEmployeeResult"))
        self.RequestId = params.get("RequestId")


class CreateMultiFlowSignQRCodeRequest(AbstractModel):
    """CreateMultiFlowSignQRCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param FlowName: 签署流程名称，最大长度不超过200字符
        :type FlowName: str
        :param MaxFlowNum: 最大可发起签署流程份数，默认5份 
发起流程数量超过此上限后二维码自动失效
        :type MaxFlowNum: int
        :param FlowEffectiveDay: 签署流程有效天数 默认7天 最高设置不超过30天
        :type FlowEffectiveDay: int
        :param QrEffectiveDay: 二维码有效天数 默认7天 最高设置不超过90天
        :type QrEffectiveDay: int
        :param Restrictions: 限制二维码用户条件
        :type Restrictions: list of ApproverRestriction
        :param UserData: 用户自定义字段，回调的时候会进行透传，长度需要小于20480
        :type UserData: str
        :param CallbackUrl: 回调地址,最大长度1000字符串
回调时机：
用户通过签署二维码发起签署流程时，企业额度不足导致失败
        :type CallbackUrl: str
        :param Agent: 应用信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param ApproverRestrictions: 限制二维码用户条件（已弃用）
        :type ApproverRestrictions: :class:`tencentcloud.ess.v20201111.models.ApproverRestriction`
        """
        self.Operator = None
        self.TemplateId = None
        self.FlowName = None
        self.MaxFlowNum = None
        self.FlowEffectiveDay = None
        self.QrEffectiveDay = None
        self.Restrictions = None
        self.UserData = None
        self.CallbackUrl = None
        self.Agent = None
        self.ApproverRestrictions = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.TemplateId = params.get("TemplateId")
        self.FlowName = params.get("FlowName")
        self.MaxFlowNum = params.get("MaxFlowNum")
        self.FlowEffectiveDay = params.get("FlowEffectiveDay")
        self.QrEffectiveDay = params.get("QrEffectiveDay")
        if params.get("Restrictions") is not None:
            self.Restrictions = []
            for item in params.get("Restrictions"):
                obj = ApproverRestriction()
                obj._deserialize(item)
                self.Restrictions.append(obj)
        self.UserData = params.get("UserData")
        self.CallbackUrl = params.get("CallbackUrl")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("ApproverRestrictions") is not None:
            self.ApproverRestrictions = ApproverRestriction()
            self.ApproverRestrictions._deserialize(params.get("ApproverRestrictions"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMultiFlowSignQRCodeResponse(AbstractModel):
    """CreateMultiFlowSignQRCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param QrCode: 签署二维码对象
        :type QrCode: :class:`tencentcloud.ess.v20201111.models.SignQrCode`
        :param SignUrls: 签署链接对象
        :type SignUrls: :class:`tencentcloud.ess.v20201111.models.SignUrl`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QrCode = None
        self.SignUrls = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QrCode") is not None:
            self.QrCode = SignQrCode()
            self.QrCode._deserialize(params.get("QrCode"))
        if params.get("SignUrls") is not None:
            self.SignUrls = SignUrl()
            self.SignUrls._deserialize(params.get("SignUrls"))
        self.RequestId = params.get("RequestId")


class CreatePrepareFlowRequest(AbstractModel):
    """CreatePrepareFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param ResourceId: 资源Id，通过多文件上传（UploadFiles）接口获得
        :type ResourceId: str
        :param FlowName: 合同名称
        :type FlowName: str
        :param Unordered: 是否顺序签署(true:无序签,false:顺序签)
        :type Unordered: bool
        :param Deadline: 签署流程的签署截止时间。
值为unix时间戳,精确到秒,不传默认为当前时间一年后
        :type Deadline: int
        :param UserFlowTypeId: 用户自定义合同类型
        :type UserFlowTypeId: str
        :param Approvers: 签署流程参与者信息，最大限制50方
        :type Approvers: list of FlowCreateApprover
        :param IntelligentStatus: 打开智能添加填写区(默认开启，打开:"OPEN" 关闭："CLOSE")
        :type IntelligentStatus: str
        """
        self.Operator = None
        self.ResourceId = None
        self.FlowName = None
        self.Unordered = None
        self.Deadline = None
        self.UserFlowTypeId = None
        self.Approvers = None
        self.IntelligentStatus = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.ResourceId = params.get("ResourceId")
        self.FlowName = params.get("FlowName")
        self.Unordered = params.get("Unordered")
        self.Deadline = params.get("Deadline")
        self.UserFlowTypeId = params.get("UserFlowTypeId")
        if params.get("Approvers") is not None:
            self.Approvers = []
            for item in params.get("Approvers"):
                obj = FlowCreateApprover()
                obj._deserialize(item)
                self.Approvers.append(obj)
        self.IntelligentStatus = params.get("IntelligentStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrepareFlowResponse(AbstractModel):
    """CreatePrepareFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 快速发起预览链接
        :type Url: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.RequestId = params.get("RequestId")


class CreateSchemeUrlRequest(AbstractModel):
    """CreateSchemeUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param OrganizationName: 企业名称
        :type OrganizationName: str
        :param Name: 姓名,最大长度50个字符
        :type Name: str
        :param Mobile: 手机号，大陆手机号11位
        :type Mobile: str
        :param EndPoint: 链接类型
HTTP：跳转电子签小程序的http_url，
APP：第三方APP或小程序跳转电子签小程序的path。
默认为HTTP类型
        :type EndPoint: str
        :param FlowId: 签署流程编号 (PathType=1时必传)
        :type FlowId: str
        :param PathType: 跳转页面 1: 小程序合同详情 2: 小程序合同列表页 0: 不传, 默认主页
        :type PathType: int
        :param AutoJumpBack: 是否自动回跳 true：是， false：否。该参数只针对"APP" 类型的签署链接有效
        :type AutoJumpBack: bool
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.OrganizationName = None
        self.Name = None
        self.Mobile = None
        self.EndPoint = None
        self.FlowId = None
        self.PathType = None
        self.AutoJumpBack = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.OrganizationName = params.get("OrganizationName")
        self.Name = params.get("Name")
        self.Mobile = params.get("Mobile")
        self.EndPoint = params.get("EndPoint")
        self.FlowId = params.get("FlowId")
        self.PathType = params.get("PathType")
        self.AutoJumpBack = params.get("AutoJumpBack")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchemeUrlResponse(AbstractModel):
    """CreateSchemeUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param SchemeUrl: 小程序链接地址
        :type SchemeUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SchemeUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SchemeUrl = params.get("SchemeUrl")
        self.RequestId = params.get("RequestId")


class CreateSealPolicyRequest(AbstractModel):
    """CreateSealPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 授权发起人在平台信息，具体参考UserInfo结构体
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Users: 用户在电子文件签署平台标识信息，具体参考UserInfo结构体。可跟下面的UserIds可叠加起作用
        :type Users: list of UserInfo
        :param SealId: 印章ID
        :type SealId: str
        :param Expired: 授权有效期。时间戳秒级
        :type Expired: int
        :param Policy: 印章授权内容
        :type Policy: str
        :param Agent: 应用相关
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param UserIds: 需要授权的用户UserId集合。跟上面的SealId参数配合使用。选填，跟上面的Users同时起作用
        :type UserIds: list of str
        """
        self.Operator = None
        self.Users = None
        self.SealId = None
        self.Expired = None
        self.Policy = None
        self.Agent = None
        self.UserIds = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self.Users.append(obj)
        self.SealId = params.get("SealId")
        self.Expired = params.get("Expired")
        self.Policy = params.get("Policy")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSealPolicyResponse(AbstractModel):
    """CreateSealPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param UserIds: 最终授权成功的。其他的跳过的是已经授权了的
        :type UserIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UserIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UserIds = params.get("UserIds")
        self.RequestId = params.get("RequestId")


class CreateStaffResult(AbstractModel):
    """创建员工的结果

    """

    def __init__(self):
        r"""
        :param SuccessEmployeeData: 创建员工的成功列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessEmployeeData: list of SuccessCreateStaffData
        :param FailedEmployeeData: 创建员工的失败列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedEmployeeData: list of FailedCreateStaffData
        """
        self.SuccessEmployeeData = None
        self.FailedEmployeeData = None


    def _deserialize(self, params):
        if params.get("SuccessEmployeeData") is not None:
            self.SuccessEmployeeData = []
            for item in params.get("SuccessEmployeeData"):
                obj = SuccessCreateStaffData()
                obj._deserialize(item)
                self.SuccessEmployeeData.append(obj)
        if params.get("FailedEmployeeData") is not None:
            self.FailedEmployeeData = []
            for item in params.get("FailedEmployeeData"):
                obj = FailedCreateStaffData()
                obj._deserialize(item)
                self.FailedEmployeeData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAutoSignEnableUrlRequest(AbstractModel):
    """CreateUserAutoSignEnableUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param AutoSignConfig: 自动签开通，签署相关配置
        :type AutoSignConfig: :class:`tencentcloud.ess.v20201111.models.AutoSignConfig`
        :param UrlType: 链接类型，空-默认小程序端链接，H5SIGN-h5端链接
        :type UrlType: str
        """
        self.Operator = None
        self.SceneKey = None
        self.AutoSignConfig = None
        self.UrlType = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.SceneKey = params.get("SceneKey")
        if params.get("AutoSignConfig") is not None:
            self.AutoSignConfig = AutoSignConfig()
            self.AutoSignConfig._deserialize(params.get("AutoSignConfig"))
        self.UrlType = params.get("UrlType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserAutoSignEnableUrlResponse(AbstractModel):
    """CreateUserAutoSignEnableUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Url: 跳转短链
        :type Url: str
        :param AppId: 小程序AppId
        :type AppId: str
        :param AppOriginalId: 小程序 原始 Id
        :type AppOriginalId: str
        :param Path: 跳转路径
        :type Path: str
        :param QrCode: base64格式跳转二维码
        :type QrCode: str
        :param UrlType: 链接类型，空-默认小程序端链接，H5SIGN-h5端链接
        :type UrlType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Url = None
        self.AppId = None
        self.AppOriginalId = None
        self.Path = None
        self.QrCode = None
        self.UrlType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.AppId = params.get("AppId")
        self.AppOriginalId = params.get("AppOriginalId")
        self.Path = params.get("Path")
        self.QrCode = params.get("QrCode")
        self.UrlType = params.get("UrlType")
        self.RequestId = params.get("RequestId")


class DeleteIntegrationEmployeesRequest(AbstractModel):
    """DeleteIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Employees: 待移除员工的信息，userId和openId二选一，必填一个
        :type Employees: list of Staff
        """
        self.Operator = None
        self.Employees = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Employees") is not None:
            self.Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self.Employees.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIntegrationEmployeesResponse(AbstractModel):
    """DeleteIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeleteEmployeeResult: 员工删除数据
        :type DeleteEmployeeResult: :class:`tencentcloud.ess.v20201111.models.DeleteStaffsResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeleteEmployeeResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeleteEmployeeResult") is not None:
            self.DeleteEmployeeResult = DeleteStaffsResult()
            self.DeleteEmployeeResult._deserialize(params.get("DeleteEmployeeResult"))
        self.RequestId = params.get("RequestId")


class DeleteSealPoliciesRequest(AbstractModel):
    """DeleteSealPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作撤销的用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param PolicyIds: 印章授权编码数组。这个参数跟下面的SealId其中一个必填，另外一个可选填
        :type PolicyIds: list of str
        :param Agent: 应用相关
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param SealId: 印章ID。这个参数跟上面的PolicyIds其中一个必填，另外一个可选填
        :type SealId: str
        :param UserIds: 待授权的员工ID
        :type UserIds: list of str
        """
        self.Operator = None
        self.PolicyIds = None
        self.Agent = None
        self.SealId = None
        self.UserIds = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.PolicyIds = params.get("PolicyIds")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.SealId = params.get("SealId")
        self.UserIds = params.get("UserIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSealPoliciesResponse(AbstractModel):
    """DeleteSealPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteStaffsResult(AbstractModel):
    """删除员工结果

    """

    def __init__(self):
        r"""
        :param SuccessEmployeeData: 删除员工的成功数据
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessEmployeeData: list of SuccessDeleteStaffData
        :param FailedEmployeeData: 删除员工的失败数据
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedEmployeeData: list of FailedDeleteStaffData
        """
        self.SuccessEmployeeData = None
        self.FailedEmployeeData = None


    def _deserialize(self, params):
        if params.get("SuccessEmployeeData") is not None:
            self.SuccessEmployeeData = []
            for item in params.get("SuccessEmployeeData"):
                obj = SuccessDeleteStaffData()
                obj._deserialize(item)
                self.SuccessEmployeeData.append(obj)
        if params.get("FailedEmployeeData") is not None:
            self.FailedEmployeeData = []
            for item in params.get("FailedEmployeeData"):
                obj = FailedDeleteStaffData()
                obj._deserialize(item)
                self.FailedEmployeeData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Department(AbstractModel):
    """集成版员工部门信息

    """

    def __init__(self):
        r"""
        :param DepartmentId: 部门id
        :type DepartmentId: str
        :param DepartmentName: 部门名称
        :type DepartmentName: str
        """
        self.DepartmentId = None
        self.DepartmentName = None


    def _deserialize(self, params):
        self.DepartmentId = params.get("DepartmentId")
        self.DepartmentName = params.get("DepartmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileUrlsRequest(AbstractModel):
    """DescribeFileUrls请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，UserId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param BusinessType: 文件对应的业务类型，目前支持：
- 流程 "FLOW"，如需下载合同文件请选择此项
- 模板 "TEMPLATE"
- 文档 "DOCUMENT"
- 印章  “SEAL”
        :type BusinessType: str
        :param BusinessIds: 业务编号的数组，如流程编号、模板编号、文档编号、印章编号。如需下载合同文件请传入FlowId
最大支持20个资源
        :type BusinessIds: list of str
        :param FileName: 下载后的文件命名，只有FileType为zip的时候生效
        :type FileName: str
        :param FileType: 文件类型，"JPG", "PDF","ZIP"等
        :type FileType: str
        :param Offset: 指定资源起始偏移量，默认0
        :type Offset: int
        :param Limit: 指定资源数量，查询全部资源则传入-1
        :type Limit: int
        :param UrlTtl: 下载url过期时间，单位秒。0: 按默认值5分钟，允许范围：1s~24x60x60s(1天)
        :type UrlTtl: int
        :param CcToken: 暂不开放
        :type CcToken: str
        :param Scene: 暂不开放
        :type Scene: str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.BusinessType = None
        self.BusinessIds = None
        self.FileName = None
        self.FileType = None
        self.Offset = None
        self.Limit = None
        self.UrlTtl = None
        self.CcToken = None
        self.Scene = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.BusinessType = params.get("BusinessType")
        self.BusinessIds = params.get("BusinessIds")
        self.FileName = params.get("FileName")
        self.FileType = params.get("FileType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.UrlTtl = params.get("UrlTtl")
        self.CcToken = params.get("CcToken")
        self.Scene = params.get("Scene")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFileUrlsResponse(AbstractModel):
    """DescribeFileUrls返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileUrls: URL信息
        :type FileUrls: list of FileUrl
        :param TotalCount: URL数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileUrls = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FileUrls") is not None:
            self.FileUrls = []
            for item in params.get("FileUrls"):
                obj = FileUrl()
                obj._deserialize(item)
                self.FileUrls.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeFlowBriefsRequest(AbstractModel):
    """DescribeFlowBriefs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowIds: 需要查询的流程ID列表，限制最大20个
        :type FlowIds: list of str
        :param Agent: 应用相关信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowIds = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowIds = params.get("FlowIds")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowBriefsResponse(AbstractModel):
    """DescribeFlowBriefs返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowBriefs: 流程列表
        :type FlowBriefs: list of FlowBrief
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowBriefs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowBriefs") is not None:
            self.FlowBriefs = []
            for item in params.get("FlowBriefs"):
                obj = FlowBrief()
                obj._deserialize(item)
                self.FlowBriefs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowEvidenceReportRequest(AbstractModel):
    """DescribeFlowEvidenceReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param ReportId: 出证报告编号
        :type ReportId: str
        """
        self.Operator = None
        self.ReportId = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.ReportId = params.get("ReportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowEvidenceReportResponse(AbstractModel):
    """DescribeFlowEvidenceReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param ReportUrl: 报告 URL
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportUrl: str
        :param Status: 执行中：EvidenceStatusExecuting
成功：EvidenceStatusSuccess
失败：EvidenceStatusFailed
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ReportUrl = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportUrl = params.get("ReportUrl")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeFlowInfoRequest(AbstractModel):
    """DescribeFlowInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowIds: 需要查询的流程ID列表，限制最大100个
        :type FlowIds: list of str
        :param Operator: 调用方用户信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.FlowIds = None
        self.Operator = None
        self.Agent = None


    def _deserialize(self, params):
        self.FlowIds = params.get("FlowIds")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowInfoResponse(AbstractModel):
    """DescribeFlowInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowDetailInfos: 签署流程信息
        :type FlowDetailInfos: list of FlowDetailInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowDetailInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowDetailInfos") is not None:
            self.FlowDetailInfos = []
            for item in params.get("FlowDetailInfos"):
                obj = FlowDetailInfo()
                obj._deserialize(item)
                self.FlowDetailInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowTemplatesRequest(AbstractModel):
    """DescribeFlowTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Organization: 企业组织相关信息，一般不用填
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param Offset: 查询偏移位置，默认0
        :type Offset: int
        :param Limit: 查询个数，默认20，最大200
        :type Limit: int
        :param Filters: 搜索条件，具体参考Filter结构体。本接口取值：template-id：按照【 **模板唯一标识** 】进行过滤
        :type Filters: list of Filter
        :param ApplicationId: 这个参数跟下面的IsChannel参数配合使用。
IsChannel=false时，ApplicationId参数不起任何作用。
IsChannel=true时，ApplicationId为空，查询所有渠道模板列表；ApplicationId不为空，查询指定渠道下的模板列表
ApplicationId为空，查询渠道模板列表
        :type ApplicationId: str
        :param IsChannel: 默认为false，查询SaaS模板库列表；
为true，查询渠道模板库管理列表
        :type IsChannel: bool
        :param GenerateSource: 暂未开放
        :type GenerateSource: int
        :param ContentType: 查询内容：0-模板列表及详情（默认），1-仅模板列表
        :type ContentType: int
        """
        self.Operator = None
        self.Organization = None
        self.Agent = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ApplicationId = None
        self.IsChannel = None
        self.GenerateSource = None
        self.ContentType = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ApplicationId = params.get("ApplicationId")
        self.IsChannel = params.get("IsChannel")
        self.GenerateSource = params.get("GenerateSource")
        self.ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowTemplatesResponse(AbstractModel):
    """DescribeFlowTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Templates: 模板详情列表
        :type Templates: list of TemplateInfo
        :param TotalCount: 查询到的总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Templates = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Templates") is not None:
            self.Templates = []
            for item in params.get("Templates"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.Templates.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationEmployeesRequest(AbstractModel):
    """DescribeIntegrationEmployees请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Limit: 返回最大数量，最大为20
        :type Limit: int
        :param Filters: 查询过滤实名用户，Key为Status，Values为["IsVerified"]
根据第三方系统openId过滤查询员工时,Key为StaffOpenId,Values为["OpenId","OpenId",...]
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        """
        self.Operator = None
        self.Limit = None
        self.Filters = None
        self.Offset = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationEmployeesResponse(AbstractModel):
    """DescribeIntegrationEmployees返回参数结构体

    """

    def __init__(self):
        r"""
        :param Employees: 员工数据列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Employees: list of Staff
        :param Offset: 偏移量，默认为0，最大为20000
注意：此字段可能返回 null，表示取不到有效值。
        :type Offset: int
        :param Limit: 返回最大数量，最大为20
        :type Limit: int
        :param TotalCount: 符合条件的员工数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Employees = None
        self.Offset = None
        self.Limit = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Employees") is not None:
            self.Employees = []
            for item in params.get("Employees"):
                obj = Staff()
                obj._deserialize(item)
                self.Employees.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeIntegrationMainOrganizationUserRequest(AbstractModel):
    """DescribeIntegrationMainOrganizationUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        """
        self.Operator = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIntegrationMainOrganizationUserResponse(AbstractModel):
    """DescribeIntegrationMainOrganizationUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param IntegrationMainOrganizationUser: 主企业员工账号信息
注意：此字段可能返回 null，表示取不到有效值。
        :type IntegrationMainOrganizationUser: :class:`tencentcloud.ess.v20201111.models.IntegrationMainOrganizationUser`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IntegrationMainOrganizationUser = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IntegrationMainOrganizationUser") is not None:
            self.IntegrationMainOrganizationUser = IntegrationMainOrganizationUser()
            self.IntegrationMainOrganizationUser._deserialize(params.get("IntegrationMainOrganizationUser"))
        self.RequestId = params.get("RequestId")


class DescribeOrganizationGroupOrganizationsRequest(AbstractModel):
    """DescribeOrganizationGroupOrganizations请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息，userId必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Limit: 单次查询成员企业最大返回数量
        :type Limit: int
        :param Offset: 页面偏移量
        :type Offset: int
        :param Name: 查询成员企业的企业名，模糊匹配
        :type Name: str
        :param Status: 成员企业加入集团的当前状态:1-待授权;2-已授权待激活;3-拒绝授权;4-已解除;5-已加入
        :type Status: int
        :param Export: 是否到处当前成员企业数据
        :type Export: bool
        :param Id: 成员企业id
        :type Id: str
        """
        self.Operator = None
        self.Limit = None
        self.Offset = None
        self.Name = None
        self.Status = None
        self.Export = None
        self.Id = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Export = params.get("Export")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationGroupOrganizationsResponse(AbstractModel):
    """DescribeOrganizationGroupOrganizations返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 查询到的符合条件的成员企业总数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param JoinedTotal: 已授权待激活的企业数量
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinedTotal: int
        :param ActivedTotal: 已加入的企业数量
注意：此字段可能返回 null，表示取不到有效值。
        :type ActivedTotal: int
        :param ExportUrl: 导出文件的url
注意：此字段可能返回 null，表示取不到有效值。
        :type ExportUrl: str
        :param List: 成员企业信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type List: list of GroupOrganization
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.JoinedTotal = None
        self.ActivedTotal = None
        self.ExportUrl = None
        self.List = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.JoinedTotal = params.get("JoinedTotal")
        self.ActivedTotal = params.get("ActivedTotal")
        self.ExportUrl = params.get("ExportUrl")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = GroupOrganization()
                obj._deserialize(item)
                self.List.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOrganizationSealsRequest(AbstractModel):
    """DescribeOrganizationSeals请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Limit: 返回最大数量，最大为100
        :type Limit: int
        :param Offset: 偏移量，默认为0，最大为20000
        :type Offset: int
        :param InfoType: 查询信息类型，为0时不返回授权用户，为1时返回
        :type InfoType: int
        :param SealId: 印章id（没有输入返回所有）
        :type SealId: str
        :param SealTypes: 印章类型列表（都是组织机构印章）。
为空时查询所有类型的印章。
目前支持以下类型：
OFFICIAL：企业公章；
CONTRACT：合同专用章；
ORGANIZATION_SEAL：企业印章(图片上传创建)；
LEGAL_PERSON_SEAL：法定代表人章
        :type SealTypes: list of str
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.Limit = None
        self.Offset = None
        self.InfoType = None
        self.SealId = None
        self.SealTypes = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.InfoType = params.get("InfoType")
        self.SealId = params.get("SealId")
        self.SealTypes = params.get("SealTypes")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationSealsResponse(AbstractModel):
    """DescribeOrganizationSeals返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 在设置了SealId时返回0或1，没有设置时返回公司的总印章数量，可能比返回的印章数组数量多
        :type TotalCount: int
        :param Seals: 查询到的印章结果数组
        :type Seals: list of OccupiedSeal
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Seals = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Seals") is not None:
            self.Seals = []
            for item in params.get("Seals"):
                obj = OccupiedSeal()
                obj._deserialize(item)
                self.Seals.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeThirdPartyAuthCodeRequest(AbstractModel):
    """DescribeThirdPartyAuthCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param AuthCode: 电子签小程序跳转客户小程序时携带的授权查看码
        :type AuthCode: str
        """
        self.AuthCode = None


    def _deserialize(self, params):
        self.AuthCode = params.get("AuthCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeThirdPartyAuthCodeResponse(AbstractModel):
    """DescribeThirdPartyAuthCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param VerifyStatus: 用户是否实名，VERIFIED 为实名，UNVERIFIED 未实名
        :type VerifyStatus: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VerifyStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VerifyStatus = params.get("VerifyStatus")
        self.RequestId = params.get("RequestId")


class DescribeUserAutoSignStatusRequest(AbstractModel):
    """DescribeUserAutoSignStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param UserInfo: 查询开启状态的用户信息
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        """
        self.Operator = None
        self.SceneKey = None
        self.UserInfo = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self.UserInfo = UserThreeFactor()
            self.UserInfo._deserialize(params.get("UserInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserAutoSignStatusResponse(AbstractModel):
    """DescribeUserAutoSignStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsOpen: 是否开通
        :type IsOpen: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsOpen = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsOpen = params.get("IsOpen")
        self.RequestId = params.get("RequestId")


class DisableUserAutoSignRequest(AbstractModel):
    """DisableUserAutoSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param SceneKey: 自动签场景:
E_PRESCRIPTION_AUTO_SIGN 电子处方
        :type SceneKey: str
        :param UserInfo: 关闭自动签的个人的三要素
        :type UserInfo: :class:`tencentcloud.ess.v20201111.models.UserThreeFactor`
        """
        self.Operator = None
        self.SceneKey = None
        self.UserInfo = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.SceneKey = params.get("SceneKey")
        if params.get("UserInfo") is not None:
            self.UserInfo = UserThreeFactor()
            self.UserInfo._deserialize(params.get("UserInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableUserAutoSignResponse(AbstractModel):
    """DisableUserAutoSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FailedCreateStaffData(AbstractModel):
    """创建员工的失败数据

    """

    def __init__(self):
        r"""
        :param DisplayName: 员工名
        :type DisplayName: str
        :param Mobile: 员工手机号
        :type Mobile: str
        :param Reason: 失败原因
        :type Reason: str
        """
        self.DisplayName = None
        self.Mobile = None
        self.Reason = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Mobile = params.get("Mobile")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FailedDeleteStaffData(AbstractModel):
    """删除员工失败数据

    """

    def __init__(self):
        r"""
        :param UserId: 员工在电子签的userId
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: str
        :param OpenId: 员工在第三方平台的openId
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Reason: 失败原因
        :type Reason: str
        """
        self.UserId = None
        self.OpenId = None
        self.Reason = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.OpenId = params.get("OpenId")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileInfo(AbstractModel):
    """二期接口返回的模板中文件的信息结构

    """

    def __init__(self):
        r"""
        :param FileId: 文件Id
        :type FileId: str
        :param FileName: 文件名
        :type FileName: str
        :param FileSize: 文件大小，单位为Byte
        :type FileSize: int
        :param CreatedOn: 文件上传时间，10位时间戳（精确到秒）
        :type CreatedOn: int
        """
        self.FileId = None
        self.FileName = None
        self.FileSize = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.FileId = params.get("FileId")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FileUrl(AbstractModel):
    """下载文件的URL信息

    """

    def __init__(self):
        r"""
        :param Url: 下载文件的URL
        :type Url: str
        :param Option: 下载文件的附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Option: str
        """
        self.Url = None
        self.Option = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Option = params.get("Option")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FillApproverInfo(AbstractModel):
    """补充签署人信息

    """

    def __init__(self):
        r"""
        :param RecipientId: 签署人签署Id
        :type RecipientId: str
        :param ApproverSource: 签署人来源
WEWORKAPP: 企业微信
        :type ApproverSource: str
        :param CustomUserId: 企业自定义账号Id
WEWORKAPP场景下指企业自有应用获取企微明文的userid
        :type CustomUserId: str
        """
        self.RecipientId = None
        self.ApproverSource = None
        self.CustomUserId = None


    def _deserialize(self, params):
        self.RecipientId = params.get("RecipientId")
        self.ApproverSource = params.get("ApproverSource")
        self.CustomUserId = params.get("CustomUserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤条件

    """

    def __init__(self):
        r"""
        :param Key: 查询过滤条件的Key
        :type Key: str
        :param Values: 查询过滤条件的Value列表
        :type Values: list of str
        """
        self.Key = None
        self.Values = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverDetail(AbstractModel):
    """签署人详情信息

    """

    def __init__(self):
        r"""
        :param ApproveMessage: 签署人信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveMessage: str
        :param ApproveName: 签署人名字
        :type ApproveName: str
        :param ApproveStatus: 签署人的状态
0：还没有发起
1：流程中 没有开始处理
2：待处理
3：签署态
4：拒绝态
5：过期没人处理
6：取消态
7：还没有预发起
8：待填写
9：因为各种原因而终止
        :type ApproveStatus: int
        :param ReceiptId: 模板配置时候的签署人id,与控件绑定
        :type ReceiptId: str
        :param CustomUserId: 客户自定义userId
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomUserId: str
        :param Mobile: 签署人手机号
        :type Mobile: str
        :param SignOrder: 签署顺序
        :type SignOrder: int
        :param ApproveTime: 签署人签署时间
        :type ApproveTime: int
        :param ApproveType: 参与者类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproveType: str
        :param ApproverSource: 签署人侧用户来源
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverSource: str
        :param CustomApproverTag: 客户自定义签署人标识
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomApproverTag: str
        :param OrganizationId: 签署人企业Id
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param OrganizationName: 签署人企业名称
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        """
        self.ApproveMessage = None
        self.ApproveName = None
        self.ApproveStatus = None
        self.ReceiptId = None
        self.CustomUserId = None
        self.Mobile = None
        self.SignOrder = None
        self.ApproveTime = None
        self.ApproveType = None
        self.ApproverSource = None
        self.CustomApproverTag = None
        self.OrganizationId = None
        self.OrganizationName = None


    def _deserialize(self, params):
        self.ApproveMessage = params.get("ApproveMessage")
        self.ApproveName = params.get("ApproveName")
        self.ApproveStatus = params.get("ApproveStatus")
        self.ReceiptId = params.get("ReceiptId")
        self.CustomUserId = params.get("CustomUserId")
        self.Mobile = params.get("Mobile")
        self.SignOrder = params.get("SignOrder")
        self.ApproveTime = params.get("ApproveTime")
        self.ApproveType = params.get("ApproveType")
        self.ApproverSource = params.get("ApproverSource")
        self.CustomApproverTag = params.get("CustomApproverTag")
        self.OrganizationId = params.get("OrganizationId")
        self.OrganizationName = params.get("OrganizationName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowApproverUrlInfo(AbstractModel):
    """签署链接信息

    """

    def __init__(self):
        r"""
        :param SignUrl: 签署链接，注意该链接有效期为30分钟，同时需要注意保密，不要外泄给无关用户。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignUrl: str
        :param ApproverMobile: 签署人手机号
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverMobile: str
        :param ApproverName: 签署人姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverName: str
        :param ApproverType: 签署人类型 1-个人
注意：此字段可能返回 null，表示取不到有效值。
        :type ApproverType: int
        """
        self.SignUrl = None
        self.ApproverMobile = None
        self.ApproverName = None
        self.ApproverType = None


    def _deserialize(self, params):
        self.SignUrl = params.get("SignUrl")
        self.ApproverMobile = params.get("ApproverMobile")
        self.ApproverName = params.get("ApproverName")
        self.ApproverType = params.get("ApproverType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowBrief(AbstractModel):
    """流程信息摘要

    """

    def __init__(self):
        r"""
        :param FlowId: 流程的编号
        :type FlowId: str
        :param FlowName: 流程的名称
        :type FlowName: str
        :param FlowDescription: 流程的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param FlowType: 流程的类型
        :type FlowType: str
        :param FlowStatus: 流程状态
- `0`  还没有发起
- `1`  未签署
- `2`  部分签署
- `3`  已退回
- `4`  完成签署
- `5`  已过期
- `6`  已取消
- `7`  还没有预发起
- `8`  等待填写
- `9`  部分填写
- `10`  拒填
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowStatus: int
        :param CreatedOn: 流程创建的时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedOn: int
        :param FlowMessage: 拒签或者取消的原因描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        """
        self.FlowId = None
        self.FlowName = None
        self.FlowDescription = None
        self.FlowType = None
        self.FlowStatus = None
        self.CreatedOn = None
        self.FlowMessage = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.FlowDescription = params.get("FlowDescription")
        self.FlowType = params.get("FlowType")
        self.FlowStatus = params.get("FlowStatus")
        self.CreatedOn = params.get("CreatedOn")
        self.FlowMessage = params.get("FlowMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowCreateApprover(AbstractModel):
    """创建流程的签署方信息

    """

    def __init__(self):
        r"""
        :param ApproverType: 参与者类型：
0：企业
1：个人
3：企业静默签署
注：类型为3（企业静默签署）时，此接口会默认完成该签署方的签署。静默签署仅进行盖章操作，不能自动签名。
        :type ApproverType: int
        :param OrganizationName: 如果签署方为企业，需要填入企业全称
        :type OrganizationName: str
        :param ApproverName: 签署方经办人姓名
        :type ApproverName: str
        :param ApproverMobile: 签署方经办人手机号码
        :type ApproverMobile: str
        :param ApproverIdCardType: 签署方经办人证件类型ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
        :type ApproverIdCardType: str
        :param ApproverIdCardNumber: 签署方经办人证件号码
        :type ApproverIdCardNumber: str
        :param RecipientId: 签署方经办人在模板中的角色ID
        :type RecipientId: str
        :param VerifyChannel: 签署意愿确认渠道,WEIXINAPP:人脸识别
        :type VerifyChannel: list of str
        :param NotifyType: 是否发送短信，sms--短信通知，none--不通知，默认为sms；发起方=签署方时不发送短信
        :type NotifyType: str
        :param IsFullText: 签署前置条件：是否需要阅读全文，默认为不需要
        :type IsFullText: bool
        :param PreReadTime: 签署前置条件：阅读时长限制，单位秒，默认为不需要
        :type PreReadTime: int
        :param UserId: 签署方经办人的用户ID,和签署方经办人姓名+手机号+证件必须有一个。
        :type UserId: str
        :param Required: 当前只支持true，默认为true
        :type Required: bool
        :param ApproverSource: 签署人用户来源,企微侧用户请传入：WEWORKAPP
        :type ApproverSource: str
        :param CustomApproverTag: 客户自定义签署人标识，64位长度，保证唯一。非企微场景不使用此字段
        :type CustomApproverTag: str
        :param RegisterInfo: 快速注册相关信息，目前暂未开放！
        :type RegisterInfo: :class:`tencentcloud.ess.v20201111.models.RegisterInfo`
        :param ApproverOption: 签署人个性化能力值
        :type ApproverOption: :class:`tencentcloud.ess.v20201111.models.ApproverOption`
        """
        self.ApproverType = None
        self.OrganizationName = None
        self.ApproverName = None
        self.ApproverMobile = None
        self.ApproverIdCardType = None
        self.ApproverIdCardNumber = None
        self.RecipientId = None
        self.VerifyChannel = None
        self.NotifyType = None
        self.IsFullText = None
        self.PreReadTime = None
        self.UserId = None
        self.Required = None
        self.ApproverSource = None
        self.CustomApproverTag = None
        self.RegisterInfo = None
        self.ApproverOption = None


    def _deserialize(self, params):
        self.ApproverType = params.get("ApproverType")
        self.OrganizationName = params.get("OrganizationName")
        self.ApproverName = params.get("ApproverName")
        self.ApproverMobile = params.get("ApproverMobile")
        self.ApproverIdCardType = params.get("ApproverIdCardType")
        self.ApproverIdCardNumber = params.get("ApproverIdCardNumber")
        self.RecipientId = params.get("RecipientId")
        self.VerifyChannel = params.get("VerifyChannel")
        self.NotifyType = params.get("NotifyType")
        self.IsFullText = params.get("IsFullText")
        self.PreReadTime = params.get("PreReadTime")
        self.UserId = params.get("UserId")
        self.Required = params.get("Required")
        self.ApproverSource = params.get("ApproverSource")
        self.CustomApproverTag = params.get("CustomApproverTag")
        if params.get("RegisterInfo") is not None:
            self.RegisterInfo = RegisterInfo()
            self.RegisterInfo._deserialize(params.get("RegisterInfo"))
        if params.get("ApproverOption") is not None:
            self.ApproverOption = ApproverOption()
            self.ApproverOption._deserialize(params.get("ApproverOption"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowDetailInfo(AbstractModel):
    """此结构体(FlowDetailInfo)描述的是合同(流程)的详细信息

    """

    def __init__(self):
        r"""
        :param FlowId: 合同(流程)的Id
        :type FlowId: str
        :param FlowName: 合同(流程)的名字
        :type FlowName: str
        :param FlowType: 合同(流程)的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowType: str
        :param FlowStatus: 合同(流程)的状态
1：未签署
2：部分签署
3：已退回
4：完成签署
5：已过期
6：已取消
        :type FlowStatus: int
        :param FlowMessage: 合同(流程)的信息
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowMessage: str
        :param FlowDescription: 流程的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowDescription: str
        :param CreatedOn: 合同(流程)的创建时间戳
        :type CreatedOn: int
        :param FlowApproverInfos: 合同(流程)的签署人数组
        :type FlowApproverInfos: list of FlowApproverDetail
        """
        self.FlowId = None
        self.FlowName = None
        self.FlowType = None
        self.FlowStatus = None
        self.FlowMessage = None
        self.FlowDescription = None
        self.CreatedOn = None
        self.FlowApproverInfos = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.FlowName = params.get("FlowName")
        self.FlowType = params.get("FlowType")
        self.FlowStatus = params.get("FlowStatus")
        self.FlowMessage = params.get("FlowMessage")
        self.FlowDescription = params.get("FlowDescription")
        self.CreatedOn = params.get("CreatedOn")
        if params.get("FlowApproverInfos") is not None:
            self.FlowApproverInfos = []
            for item in params.get("FlowApproverInfos"):
                obj = FlowApproverDetail()
                obj._deserialize(item)
                self.FlowApproverInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FormField(AbstractModel):
    """电子文档的控件填充信息。按照控件类型进行相应的填充。

    【数据表格传参说明】
    当模板的 ComponentType='DYNAMIC_TABLE'时（渠道版或集成版），FormField.ComponentValue需要传递json格式的字符串参数，用于确定表头&填充数据表格（支持内容的单元格合并）
    输入示例1：

    ```
    {
        "headers":[
            {
                "content":"head1"
            },
            {
                "content":"head2"
            },
            {
                "content":"head3"
            }
        ],
        "rowCount":3,
        "body":{
            "cells":[
                {
                    "rowStart":1,
                    "rowEnd":1,
                    "columnStart":1,
                    "columnEnd":1,
                    "content":"123"
                },
                {
                    "rowStart":2,
                    "rowEnd":3,
                    "columnStart":1,
                    "columnEnd":2,
                    "content":"456"
                },
                {
                    "rowStart":3,
                    "rowEnd":3,
                    "columnStart":3,
                    "columnEnd":3,
                    "content":"789"
                }
            ]
        }
    }

    ```

    输入示例2（表格表头宽度比例配置）：

    ```
    {
        "headers":[
            {
                "content":"head1",
                "widthPercent": 30
            },
            {
                "content":"head2",
                "widthPercent": 30
            },
            {
                "content":"head3",
                "widthPercent": 40
            }
        ],
        "rowCount":3,
        "body":{
            "cells":[
                {
                    "rowStart":1,
                    "rowEnd":1,
                    "columnStart":1,
                    "columnEnd":1,
                    "content":"123"
                },
                {
                    "rowStart":2,
                    "rowEnd":3,
                    "columnStart":1,
                    "columnEnd":2,
                    "content":"456"
                },
                {
                    "rowStart":3,
                    "rowEnd":3,
                    "columnStart":3,
                    "columnEnd":3,
                    "content":"789"
                }
            ]
        }
    }

    ```
    表格参数说明

    | 名称                | 类型    | 描述                                              |
    | ------------------- | ------- | ------------------------------------------------- |
    | headers             | Array   | 表头：不超过10列，不支持单元格合并，字数不超过100 |
    | rowCount            | Integer | 表格内容最大行数                                  |
    | cells.N.rowStart    | Integer | 单元格坐标：行起始index                           |
    | cells.N.rowEnd      | Integer | 单元格坐标：行结束index                           |
    | cells.N.columnStart | Integer | 单元格坐标：列起始index                           |
    | cells.N.columnEnd   | Integer | 单元格坐标：列结束index                           |
    | cells.N.content     | String  | 单元格内容，字数不超过100                         |

    表格参数headers说明
    widthPercent Integer 表头单元格列占总表头的比例，例如1：30表示 此列占表头的30%，不填写时列宽度平均拆分；例如2：总2列，某一列填写40，剩余列可以为空，按照60计算。；例如3：总3列，某一列填写30，剩余2列可以为空，分别为(100-30)/2=35
    content String 表头单元格内容，字数不超过100

    """

    def __init__(self):
        r"""
        :param ComponentValue: 控件填充vaule，ComponentType和传入值类型对应关系：
TEXT - 文本内容
MULTI_LINE_TEXT - 文本内容
CHECK_BOX - true/false
FILL_IMAGE、ATTACHMENT - 附件的FileId，需要通过UploadFiles接口上传获取
SELECTOR - 选项值
DYNAMIC_TABLE - 传入json格式的表格内容，具体见数据结构FlowInfo：https://cloud.tencent.com/document/api/1420/61525#FlowInfo
        :type ComponentValue: str
        :param ComponentId: 控件id，和ComponentName选择一项传入即可
        :type ComponentId: str
        :param ComponentName: 控件名字，最大长度不超过30字符，和ComponentId选择一项传入即可
        :type ComponentName: str
        """
        self.ComponentValue = None
        self.ComponentId = None
        self.ComponentName = None


    def _deserialize(self, params):
        self.ComponentValue = params.get("ComponentValue")
        self.ComponentId = params.get("ComponentId")
        self.ComponentName = params.get("ComponentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskResultApiRequest(AbstractModel):
    """GetTaskResultApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id，通过CreateConvertTaskApi得到
        :type TaskId: str
        :param Operator: 操作人信息
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param Agent: 应用号信息
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        :param Organization: 暂未开放
        :type Organization: :class:`tencentcloud.ess.v20201111.models.OrganizationInfo`
        """
        self.TaskId = None
        self.Operator = None
        self.Agent = None
        self.Organization = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        if params.get("Organization") is not None:
            self.Organization = OrganizationInfo()
            self.Organization._deserialize(params.get("Organization"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskResultApiResponse(AbstractModel):
    """GetTaskResultApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务Id
        :type TaskId: str
        :param TaskStatus: 任务状态，需要关注的状态
0  :NeedTranform   - 任务已提交
4  :Processing     - 文档转换中
8  :TaskEnd        - 任务处理完成
-2 :DownloadFailed - 下载失败
-6 :ProcessFailed  - 转换失败
-13:ProcessTimeout - 转换文件超时
        :type TaskStatus: int
        :param TaskMessage: 状态描述，需要关注的状态
NeedTranform   - 任务已提交
Processing     - 文档转换中
TaskEnd        - 任务处理完成
DownloadFailed - 下载失败
ProcessFailed  - 转换失败
ProcessTimeout - 转换文件超时
        :type TaskMessage: str
        :param ResourceId: 资源Id，也是FileId，用于文件发起使用
        :type ResourceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.TaskStatus = None
        self.TaskMessage = None
        self.ResourceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskStatus = params.get("TaskStatus")
        self.TaskMessage = params.get("TaskMessage")
        self.ResourceId = params.get("ResourceId")
        self.RequestId = params.get("RequestId")


class GroupOrganization(AbstractModel):
    """成员企业信息

    """

    def __init__(self):
        r"""
        :param Name: 成员企业名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Alias: 成员企业别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param OrganizationId: 成员企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationId: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param Status: 成员企业状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param IsMainOrganization: 是否为集团主企业
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMainOrganization: bool
        :param IdCardNumber: 企业社会信用代码
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        :param AdminInfo: 企业超管信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminInfo: :class:`tencentcloud.ess.v20201111.models.Admin`
        :param License: 企业许可证
注意：此字段可能返回 null，表示取不到有效值。
        :type License: str
        :param LicenseExpireTime: 企业许可证过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LicenseExpireTime: int
        :param JoinTime: 成员企业加入集团时间
注意：此字段可能返回 null，表示取不到有效值。
        :type JoinTime: int
        :param FlowEngineEnable: 是否可以使用审批流引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowEngineEnable: bool
        """
        self.Name = None
        self.Alias = None
        self.OrganizationId = None
        self.UpdateTime = None
        self.Status = None
        self.IsMainOrganization = None
        self.IdCardNumber = None
        self.AdminInfo = None
        self.License = None
        self.LicenseExpireTime = None
        self.JoinTime = None
        self.FlowEngineEnable = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Alias = params.get("Alias")
        self.OrganizationId = params.get("OrganizationId")
        self.UpdateTime = params.get("UpdateTime")
        self.Status = params.get("Status")
        self.IsMainOrganization = params.get("IsMainOrganization")
        self.IdCardNumber = params.get("IdCardNumber")
        if params.get("AdminInfo") is not None:
            self.AdminInfo = Admin()
            self.AdminInfo._deserialize(params.get("AdminInfo"))
        self.License = params.get("License")
        self.LicenseExpireTime = params.get("LicenseExpireTime")
        self.JoinTime = params.get("JoinTime")
        self.FlowEngineEnable = params.get("FlowEngineEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IntegrationMainOrganizationUser(AbstractModel):
    """主企业员工账号信息

    """

    def __init__(self):
        r"""
        :param MainOrganizationId: 主企业id
注意：此字段可能返回 null，表示取不到有效值。
        :type MainOrganizationId: str
        :param MainUserId: 主企业员工UserId
注意：此字段可能返回 null，表示取不到有效值。
        :type MainUserId: str
        :param UserName: 主企业员工名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        """
        self.MainOrganizationId = None
        self.MainUserId = None
        self.UserName = None


    def _deserialize(self, params):
        self.MainOrganizationId = params.get("MainOrganizationId")
        self.MainUserId = params.get("MainUserId")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApplicationCallbackInfoRequest(AbstractModel):
    """ModifyApplicationCallbackInfo请求参数结构体

    """


class ModifyApplicationCallbackInfoResponse(AbstractModel):
    """ModifyApplicationCallbackInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OccupiedSeal(AbstractModel):
    """持有的电子印章信息

    """

    def __init__(self):
        r"""
        :param SealId: 电子印章编号
        :type SealId: str
        :param SealName: 电子印章名称
        :type SealName: str
        :param CreateOn: 电子印章授权时间戳
        :type CreateOn: int
        :param Creator: 电子印章授权人
        :type Creator: str
        :param SealPolicyId: 电子印章策略Id
        :type SealPolicyId: str
        :param SealStatus: 印章状态，有以下六种：CHECKING（审核中）SUCCESS（已启用）FAIL（审核拒绝）CHECKING-SADM（待超管审核）DISABLE（已停用）STOPPED（已终止）
        :type SealStatus: str
        :param FailReason: 审核失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type FailReason: str
        :param Url: 印章图片url，5分钟内有效
        :type Url: str
        :param SealType: 印章类型
        :type SealType: str
        :param IsAllTime: 用印申请是否为永久授权
        :type IsAllTime: bool
        :param AuthorizedUsers: 授权人列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedUsers: list of AuthorizedUser
        """
        self.SealId = None
        self.SealName = None
        self.CreateOn = None
        self.Creator = None
        self.SealPolicyId = None
        self.SealStatus = None
        self.FailReason = None
        self.Url = None
        self.SealType = None
        self.IsAllTime = None
        self.AuthorizedUsers = None


    def _deserialize(self, params):
        self.SealId = params.get("SealId")
        self.SealName = params.get("SealName")
        self.CreateOn = params.get("CreateOn")
        self.Creator = params.get("Creator")
        self.SealPolicyId = params.get("SealPolicyId")
        self.SealStatus = params.get("SealStatus")
        self.FailReason = params.get("FailReason")
        self.Url = params.get("Url")
        self.SealType = params.get("SealType")
        self.IsAllTime = params.get("IsAllTime")
        if params.get("AuthorizedUsers") is not None:
            self.AuthorizedUsers = []
            for item in params.get("AuthorizedUsers"):
                obj = AuthorizedUser()
                obj._deserialize(item)
                self.AuthorizedUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationInfo(AbstractModel):
    """机构信息

    """

    def __init__(self):
        r"""
        :param OrganizationId: 机构在平台的编号
        :type OrganizationId: str
        :param Channel: 用户渠道
        :type Channel: str
        :param OrganizationOpenId: 用户在渠道的机构编号
        :type OrganizationOpenId: str
        :param ClientIp: 用户真实的IP
        :type ClientIp: str
        :param ProxyIp: 机构的代理IP
        :type ProxyIp: str
        """
        self.OrganizationId = None
        self.Channel = None
        self.OrganizationOpenId = None
        self.ClientIp = None
        self.ProxyIp = None


    def _deserialize(self, params):
        self.OrganizationId = params.get("OrganizationId")
        self.Channel = params.get("Channel")
        self.OrganizationOpenId = params.get("OrganizationOpenId")
        self.ClientIp = params.get("ClientIp")
        self.ProxyIp = params.get("ProxyIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PdfVerifyResult(AbstractModel):
    """合同文件验签单个结果结构体

    """

    def __init__(self):
        r"""
        :param VerifyResult: 验签结果
        :type VerifyResult: int
        :param SignPlatform: 签署平台
        :type SignPlatform: str
        :param SignerName: 签署人名称
        :type SignerName: str
        :param SignTime: 签署时间
        :type SignTime: int
        :param SignAlgorithm: 签名算法
        :type SignAlgorithm: str
        :param CertSn: 签名证书序列号
        :type CertSn: str
        :param CertNotBefore: 证书起始时间
        :type CertNotBefore: int
        :param CertNotAfter: 证书过期时间
        :type CertNotAfter: int
        :param ComponentPosX: 签名域横坐标
        :type ComponentPosX: float
        :param ComponentPosY: 签名域纵坐标
        :type ComponentPosY: float
        :param ComponentWidth: 签名域宽度
        :type ComponentWidth: float
        :param ComponentHeight: 签名域高度
        :type ComponentHeight: float
        :param ComponentPage: 签名域所在页码
        :type ComponentPage: int
        """
        self.VerifyResult = None
        self.SignPlatform = None
        self.SignerName = None
        self.SignTime = None
        self.SignAlgorithm = None
        self.CertSn = None
        self.CertNotBefore = None
        self.CertNotAfter = None
        self.ComponentPosX = None
        self.ComponentPosY = None
        self.ComponentWidth = None
        self.ComponentHeight = None
        self.ComponentPage = None


    def _deserialize(self, params):
        self.VerifyResult = params.get("VerifyResult")
        self.SignPlatform = params.get("SignPlatform")
        self.SignerName = params.get("SignerName")
        self.SignTime = params.get("SignTime")
        self.SignAlgorithm = params.get("SignAlgorithm")
        self.CertSn = params.get("CertSn")
        self.CertNotBefore = params.get("CertNotBefore")
        self.CertNotAfter = params.get("CertNotAfter")
        self.ComponentPosX = params.get("ComponentPosX")
        self.ComponentPosY = params.get("ComponentPosY")
        self.ComponentWidth = params.get("ComponentWidth")
        self.ComponentHeight = params.get("ComponentHeight")
        self.ComponentPage = params.get("ComponentPage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Recipient(AbstractModel):
    """签署参与者信息

    """

    def __init__(self):
        r"""
        :param RecipientId: 签署参与者ID
        :type RecipientId: str
        :param RecipientType: 参与者类型（ENTERPRISE/INDIVIDUAL）
        :type RecipientType: str
        :param Description: 描述信息
        :type Description: str
        :param RoleName: 角色名称
        :type RoleName: str
        :param RequireValidation: 是否需要验证，默认为false
        :type RequireValidation: bool
        :param RequireSign: 是否需要签署，默认为true
        :type RequireSign: bool
        :param RoutingOrder: 添加序列
        :type RoutingOrder: int
        :param RequireDelivery: 是否需要发送，默认为true
        :type RequireDelivery: bool
        :param Email: 邮箱地址
        :type Email: str
        :param Mobile: 电话号码
        :type Mobile: str
        :param UserId: 关联的用户ID
        :type UserId: str
        :param DeliveryMethod: 发送方式（EMAIL/MOBILE）
        :type DeliveryMethod: str
        :param RecipientExtra: 附属信息
        :type RecipientExtra: str
        """
        self.RecipientId = None
        self.RecipientType = None
        self.Description = None
        self.RoleName = None
        self.RequireValidation = None
        self.RequireSign = None
        self.RoutingOrder = None
        self.RequireDelivery = None
        self.Email = None
        self.Mobile = None
        self.UserId = None
        self.DeliveryMethod = None
        self.RecipientExtra = None


    def _deserialize(self, params):
        self.RecipientId = params.get("RecipientId")
        self.RecipientType = params.get("RecipientType")
        self.Description = params.get("Description")
        self.RoleName = params.get("RoleName")
        self.RequireValidation = params.get("RequireValidation")
        self.RequireSign = params.get("RequireSign")
        self.RoutingOrder = params.get("RoutingOrder")
        self.RequireDelivery = params.get("RequireDelivery")
        self.Email = params.get("Email")
        self.Mobile = params.get("Mobile")
        self.UserId = params.get("UserId")
        self.DeliveryMethod = params.get("DeliveryMethod")
        self.RecipientExtra = params.get("RecipientExtra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterInfo(AbstractModel):
    """发起流程快速注册相关信息

    """

    def __init__(self):
        r"""
        :param LegalName: 法人姓名
        :type LegalName: str
        :param Uscc: 社会统一信用代码
        :type Uscc: str
        """
        self.LegalName = None
        self.Uscc = None


    def _deserialize(self, params):
        self.LegalName = params.get("LegalName")
        self.Uscc = params.get("Uscc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemindFlowRecords(AbstractModel):
    """催办接口返回详细信息

    """

    def __init__(self):
        r"""
        :param CanRemind: 是否能够催办
        :type CanRemind: bool
        :param FlowId: 合同id
        :type FlowId: str
        :param RemindMessage: 催办详情
        :type RemindMessage: str
        """
        self.CanRemind = None
        self.FlowId = None
        self.RemindMessage = None


    def _deserialize(self, params):
        self.CanRemind = params.get("CanRemind")
        self.FlowId = params.get("FlowId")
        self.RemindMessage = params.get("RemindMessage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignQrCode(AbstractModel):
    """一码多扫签署二维码对象

    """

    def __init__(self):
        r"""
        :param QrCodeId: 二维码id
        :type QrCodeId: str
        :param QrCodeUrl: 二维码url
        :type QrCodeUrl: str
        :param ExpiredTime: 二维码过期时间
        :type ExpiredTime: int
        """
        self.QrCodeId = None
        self.QrCodeUrl = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.QrCodeId = params.get("QrCodeId")
        self.QrCodeUrl = params.get("QrCodeUrl")
        self.ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignUrl(AbstractModel):
    """一码多扫签署二维码签署信息

    """

    def __init__(self):
        r"""
        :param AppSignUrl: 小程序签署链接
        :type AppSignUrl: str
        :param EffectiveTime: 签署链接有效时间
        :type EffectiveTime: str
        :param HttpSignUrl: 移动端签署链接
        :type HttpSignUrl: str
        """
        self.AppSignUrl = None
        self.EffectiveTime = None
        self.HttpSignUrl = None


    def _deserialize(self, params):
        self.AppSignUrl = params.get("AppSignUrl")
        self.EffectiveTime = params.get("EffectiveTime")
        self.HttpSignUrl = params.get("HttpSignUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Staff(AbstractModel):
    """企业员工信息

    """

    def __init__(self):
        r"""
        :param UserId: 用户在电子签平台的id
        :type UserId: str
        :param DisplayName: 显示的用户名/昵称
        :type DisplayName: str
        :param Mobile: 用户手机号
        :type Mobile: str
        :param Email: 用户邮箱
注意：此字段可能返回 null，表示取不到有效值。
        :type Email: str
        :param OpenId: 用户在第三方平台id
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param Roles: 员工角色
注意：此字段可能返回 null，表示取不到有效值。
        :type Roles: list of StaffRole
        :param Department: 员工部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Department: :class:`tencentcloud.ess.v20201111.models.Department`
        :param Verified: 员工是否实名
        :type Verified: bool
        :param CreatedOn: 员工创建时间戳
        :type CreatedOn: int
        :param VerifiedOn: 员工实名时间戳
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifiedOn: int
        :param QuiteJob: 员工是否离职：0-未离职，1-离职
注意：此字段可能返回 null，表示取不到有效值。
        :type QuiteJob: int
        """
        self.UserId = None
        self.DisplayName = None
        self.Mobile = None
        self.Email = None
        self.OpenId = None
        self.Roles = None
        self.Department = None
        self.Verified = None
        self.CreatedOn = None
        self.VerifiedOn = None
        self.QuiteJob = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.DisplayName = params.get("DisplayName")
        self.Mobile = params.get("Mobile")
        self.Email = params.get("Email")
        self.OpenId = params.get("OpenId")
        if params.get("Roles") is not None:
            self.Roles = []
            for item in params.get("Roles"):
                obj = StaffRole()
                obj._deserialize(item)
                self.Roles.append(obj)
        if params.get("Department") is not None:
            self.Department = Department()
            self.Department._deserialize(params.get("Department"))
        self.Verified = params.get("Verified")
        self.CreatedOn = params.get("CreatedOn")
        self.VerifiedOn = params.get("VerifiedOn")
        self.QuiteJob = params.get("QuiteJob")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaffRole(AbstractModel):
    """集成版企业角色信息

    """

    def __init__(self):
        r"""
        :param RoleId: 角色id
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleId: str
        :param RoleName: 角色名称
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleName: str
        """
        self.RoleId = None
        self.RoleName = None


    def _deserialize(self, params):
        self.RoleId = params.get("RoleId")
        self.RoleName = params.get("RoleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartFlowRequest(AbstractModel):
    """StartFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param Operator: 调用方用户信息，userId 必填。支持填入集团子公司经办人 userId代发合同。
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        :param FlowId: 签署流程编号，由CreateFlow接口返回
        :type FlowId: str
        :param ClientToken: 客户端Token，保持接口幂等性,最大长度64个字符
        :type ClientToken: str
        :param Agent: 代理相关应用信息，如集团主企业代子企业操作的场景中ProxyOrganizationId必填
        :type Agent: :class:`tencentcloud.ess.v20201111.models.Agent`
        """
        self.Operator = None
        self.FlowId = None
        self.ClientToken = None
        self.Agent = None


    def _deserialize(self, params):
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        self.FlowId = params.get("FlowId")
        self.ClientToken = params.get("ClientToken")
        if params.get("Agent") is not None:
            self.Agent = Agent()
            self.Agent._deserialize(params.get("Agent"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartFlowResponse(AbstractModel):
    """StartFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 返回描述，START-发起成功， REVIEW-提交审核成功，EXECUTING-已提交发起任务
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class SuccessCreateStaffData(AbstractModel):
    """创建员工的成功数据

    """

    def __init__(self):
        r"""
        :param DisplayName: 员工名
        :type DisplayName: str
        :param Mobile: 员工手机号
        :type Mobile: str
        :param UserId: 员工在电子签平台的id
        :type UserId: str
        """
        self.DisplayName = None
        self.Mobile = None
        self.UserId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Mobile = params.get("Mobile")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessDeleteStaffData(AbstractModel):
    """删除员工的成功数据

    """

    def __init__(self):
        r"""
        :param DisplayName: 员工名
        :type DisplayName: str
        :param Mobile: 员工手机号
        :type Mobile: str
        :param UserId: 员工在电子签平台的id
        :type UserId: str
        """
        self.DisplayName = None
        self.Mobile = None
        self.UserId = None


    def _deserialize(self, params):
        self.DisplayName = params.get("DisplayName")
        self.Mobile = params.get("Mobile")
        self.UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateInfo(AbstractModel):
    """二期接口返回的模板的信息结构

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param TemplateName: 模板名字
        :type TemplateName: str
        :param Description: 模板描述信息
        :type Description: str
        :param DocumentResourceIds: 模板关联的资源IDs
        :type DocumentResourceIds: list of str
        :param FileInfos: 返回的文件信息结构
        :type FileInfos: list of FileInfo
        :param AttachmentResourceIds: 附件关联的资源ID是
        :type AttachmentResourceIds: list of str
        :param SignOrder: 签署顺序
        :type SignOrder: list of int
        :param Recipients: 签署参与者的信息
        :type Recipients: list of Recipient
        :param Components: 模板信息结构
        :type Components: list of Component
        :param SignComponents: 签署区模板信息结构
        :type SignComponents: list of Component
        :param Status: 模板状态(-1:不可用；0:草稿态；1:正式态)
        :type Status: int
        :param Creator: 模板的创建人
        :type Creator: str
        :param CreatedOn: 模板创建的时间戳（精确到秒）
        :type CreatedOn: int
        :param Promoter: 发起人角色信息
        :type Promoter: :class:`tencentcloud.ess.v20201111.models.Recipient`
        :param OrganizationId: 模板创建组织id
        :type OrganizationId: str
        :param PreviewUrl: 模板预览链接
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewUrl: str
        :param TemplateVersion: 模板版本。默认为空时，全数字字符，初始版本为yyyyMMdd001。
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateVersion: str
        :param Published: 模板是否已发布。true-已发布；false-未发布
注意：此字段可能返回 null，表示取不到有效值。
        :type Published: bool
        """
        self.TemplateId = None
        self.TemplateName = None
        self.Description = None
        self.DocumentResourceIds = None
        self.FileInfos = None
        self.AttachmentResourceIds = None
        self.SignOrder = None
        self.Recipients = None
        self.Components = None
        self.SignComponents = None
        self.Status = None
        self.Creator = None
        self.CreatedOn = None
        self.Promoter = None
        self.OrganizationId = None
        self.PreviewUrl = None
        self.TemplateVersion = None
        self.Published = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateName = params.get("TemplateName")
        self.Description = params.get("Description")
        self.DocumentResourceIds = params.get("DocumentResourceIds")
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        self.AttachmentResourceIds = params.get("AttachmentResourceIds")
        self.SignOrder = params.get("SignOrder")
        if params.get("Recipients") is not None:
            self.Recipients = []
            for item in params.get("Recipients"):
                obj = Recipient()
                obj._deserialize(item)
                self.Recipients.append(obj)
        if params.get("Components") is not None:
            self.Components = []
            for item in params.get("Components"):
                obj = Component()
                obj._deserialize(item)
                self.Components.append(obj)
        if params.get("SignComponents") is not None:
            self.SignComponents = []
            for item in params.get("SignComponents"):
                obj = Component()
                obj._deserialize(item)
                self.SignComponents.append(obj)
        self.Status = params.get("Status")
        self.Creator = params.get("Creator")
        self.CreatedOn = params.get("CreatedOn")
        if params.get("Promoter") is not None:
            self.Promoter = Recipient()
            self.Promoter._deserialize(params.get("Promoter"))
        self.OrganizationId = params.get("OrganizationId")
        self.PreviewUrl = params.get("PreviewUrl")
        self.TemplateVersion = params.get("TemplateVersion")
        self.Published = params.get("Published")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFile(AbstractModel):
    """此结构体 (UploadFile) 用于描述多文件上传的文件信息。

    """

    def __init__(self):
        r"""
        :param FileBody: Base64编码后的文件内容
        :type FileBody: str
        :param FileName: 文件名，最大长度不超过200字符
        :type FileName: str
        """
        self.FileBody = None
        self.FileName = None


    def _deserialize(self, params):
        self.FileBody = params.get("FileBody")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesRequest(AbstractModel):
    """UploadFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param BusinessType: 文件对应业务类型
1. TEMPLATE - 模板； 文件类型：.pdf/.doc/.docx/.html
2. DOCUMENT - 签署过程及签署后的合同文档/图片控件 文件类型：.pdf/.doc/.docx/.jpg/.png/.xls.xlsx/.html
3. SEAL - 印章； 文件类型：.jpg/.jpeg/.png
        :type BusinessType: str
        :param Caller: 调用方信息，其中OperatorId为必填字段，即用户的UserId
        :type Caller: :class:`tencentcloud.ess.v20201111.models.Caller`
        :param FileInfos: 上传文件内容数组，最多支持20个文件
        :type FileInfos: list of UploadFile
        :param FileType: 文件类型， 默认通过文件内容解析得到文件类型，客户可以显示的说明上传文件的类型。
如：PDF 表示上传的文件 xxx.pdf的文件类型是 PDF
        :type FileType: str
        :param CoverRect: 此参数只对 PDF 文件有效。是否将pdf灰色矩阵置白
true--是，处理置白
默认为false--否，不处理
        :type CoverRect: bool
        :param CustomIds: 用户自定义ID数组，与上传文件一一对应
        :type CustomIds: list of str
        :param FileUrls: 不再使用，上传文件链接数组，最多支持20个URL
        :type FileUrls: str
        """
        self.BusinessType = None
        self.Caller = None
        self.FileInfos = None
        self.FileType = None
        self.CoverRect = None
        self.CustomIds = None
        self.FileUrls = None


    def _deserialize(self, params):
        self.BusinessType = params.get("BusinessType")
        if params.get("Caller") is not None:
            self.Caller = Caller()
            self.Caller._deserialize(params.get("Caller"))
        if params.get("FileInfos") is not None:
            self.FileInfos = []
            for item in params.get("FileInfos"):
                obj = UploadFile()
                obj._deserialize(item)
                self.FileInfos.append(obj)
        self.FileType = params.get("FileType")
        self.CoverRect = params.get("CoverRect")
        self.CustomIds = params.get("CustomIds")
        self.FileUrls = params.get("FileUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFilesResponse(AbstractModel):
    """UploadFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileIds: 文件id数组
        :type FileIds: list of str
        :param TotalCount: 上传成功文件数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileIds = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileIds = params.get("FileIds")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param UserId: 用户在平台的编号
        :type UserId: str
        :param Channel: 用户的来源渠道
        :type Channel: str
        :param OpenId: 用户在渠道的编号
        :type OpenId: str
        :param ClientIp: 用户真实IP
        :type ClientIp: str
        :param ProxyIp: 用户代理IP
        :type ProxyIp: str
        """
        self.UserId = None
        self.Channel = None
        self.OpenId = None
        self.ClientIp = None
        self.ProxyIp = None


    def _deserialize(self, params):
        self.UserId = params.get("UserId")
        self.Channel = params.get("Channel")
        self.OpenId = params.get("OpenId")
        self.ClientIp = params.get("ClientIp")
        self.ProxyIp = params.get("ProxyIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserThreeFactor(AbstractModel):
    """用户的三要素：姓名，证件号，证件类型

    """

    def __init__(self):
        r"""
        :param Name: 姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param IdCardType: 证件类型: 
ID_CARD 身份证
HONGKONG_AND_MACAO 港澳居民来往内地通行证
HONGKONG_MACAO_AND_TAIWAN 港澳台居民居住证(格式同居民身份证)
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardType: str
        :param IdCardNumber: 证件号，如果有 X 请大写
注意：此字段可能返回 null，表示取不到有效值。
        :type IdCardNumber: str
        """
        self.Name = None
        self.IdCardType = None
        self.IdCardNumber = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.IdCardType = params.get("IdCardType")
        self.IdCardNumber = params.get("IdCardNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyPdfRequest(AbstractModel):
    """VerifyPdf请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 合同Id，流程Id
        :type FlowId: str
        :param Operator: 调用方用户信息，userId 必填
        :type Operator: :class:`tencentcloud.ess.v20201111.models.UserInfo`
        """
        self.FlowId = None
        self.Operator = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        if params.get("Operator") is not None:
            self.Operator = UserInfo()
            self.Operator._deserialize(params.get("Operator"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyPdfResponse(AbstractModel):
    """VerifyPdf返回参数结构体

    """

    def __init__(self):
        r"""
        :param VerifyResult: 验签结果，1-文件未被篡改，全部签名在腾讯电子签完成； 2-文件未被篡改，部分签名在腾讯电子签完成；3-文件被篡改；4-异常：文件内没有签名域；5-异常：文件签名格式错误
        :type VerifyResult: int
        :param PdfVerifyResults: 验签结果详情,内部状态1-验签成功，在电子签签署；2-验签成功，在其他平台签署；3-验签失败；4-pdf文件没有签名域
；5-文件签名格式错误
        :type PdfVerifyResults: list of PdfVerifyResult
        :param VerifySerialNo: 验签序列号
        :type VerifySerialNo: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VerifyResult = None
        self.PdfVerifyResults = None
        self.VerifySerialNo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.VerifyResult = params.get("VerifyResult")
        if params.get("PdfVerifyResults") is not None:
            self.PdfVerifyResults = []
            for item in params.get("PdfVerifyResults"):
                obj = PdfVerifyResult()
                obj._deserialize(item)
                self.PdfVerifyResults.append(obj)
        self.VerifySerialNo = params.get("VerifySerialNo")
        self.RequestId = params.get("RequestId")