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


class AudioResult(AbstractModel):
    """音频输出参数

    """

    def __init__(self):
        r"""
        :param HitFlag: 该字段用于返回审核内容是否命中审核模型；取值：0（**未命中**）、1（**命中**）。
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高** ），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Text: 该字段用于返回音频文件经ASR识别后的文本信息。最长可识别**5小时**的音频文件，若超出时长限制，接口将会报错。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Url: 该字段用于返回音频片段存储的链接地址，该地址有效期为1天。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Duration: 该字段用于返回音频文件的时长，单位为毫秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: str
        :param Extra: 该字段用于返回输入参数中的额外附加信息（Extra），如未配置则默认返回值为空。<br>备注：不同客户或Biztype下返回信息不同，如需配置该字段请提交工单咨询或联系售后专员处理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param TextResults: 该字段用于返回音频文件经ASR识别后产生的文本的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type TextResults: list of AudioResultDetailTextResult
        :param MoanResults: 该字段用于返回音频文件呻吟检测的详细审核结果。具体结果内容请参见AudioResultDetailMoanResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type MoanResults: list of AudioResultDetailMoanResult
        :param LanguageResults: 该字段用于返回音频小语种检测的详细审核结果。具体结果内容请参见AudioResultDetailLanguageResult数据结构的细节描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type LanguageResults: list of AudioResultDetailLanguageResult
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param RecognitionResults: 识别类标签结果信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognitionResults: list of RecognitionResult
        """
        self.HitFlag = None
        self.Label = None
        self.Suggestion = None
        self.Score = None
        self.Text = None
        self.Url = None
        self.Duration = None
        self.Extra = None
        self.TextResults = None
        self.MoanResults = None
        self.LanguageResults = None
        self.SubLabel = None
        self.RecognitionResults = None


    def _deserialize(self, params):
        self.HitFlag = params.get("HitFlag")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        self.Text = params.get("Text")
        self.Url = params.get("Url")
        self.Duration = params.get("Duration")
        self.Extra = params.get("Extra")
        if params.get("TextResults") is not None:
            self.TextResults = []
            for item in params.get("TextResults"):
                obj = AudioResultDetailTextResult()
                obj._deserialize(item)
                self.TextResults.append(obj)
        if params.get("MoanResults") is not None:
            self.MoanResults = []
            for item in params.get("MoanResults"):
                obj = AudioResultDetailMoanResult()
                obj._deserialize(item)
                self.MoanResults.append(obj)
        if params.get("LanguageResults") is not None:
            self.LanguageResults = []
            for item in params.get("LanguageResults"):
                obj = AudioResultDetailLanguageResult()
                obj._deserialize(item)
                self.LanguageResults.append(obj)
        self.SubLabel = params.get("SubLabel")
        if params.get("RecognitionResults") is not None:
            self.RecognitionResults = []
            for item in params.get("RecognitionResults"):
                obj = RecognitionResult()
                obj._deserialize(item)
                self.RecognitionResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailLanguageResult(AbstractModel):
    """音频小语种检测结果

    """

    def __init__(self):
        r"""
        :param Label: 语种
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param StartTime: 开始时间
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param EndTime: 结束时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        :param SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabelCode = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailMoanResult(AbstractModel):
    """音频呻吟审核结果

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回检测结果需要检测的内容类型，此处固定为**Moan**（呻吟）以调用呻吟检测功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Score: 该字段用于返回呻吟检测的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表音频越有可能属于呻吟内容。
        :type Score: int
        :param StartTime: 该字段用于返回对应呻吟标签的片段在音频文件内的开始时间，单位为毫秒。
        :type StartTime: float
        :param EndTime: 该字段用于返回对应呻吟标签的片段在音频文件内的结束时间，单位为毫秒。
        :type EndTime: float
        :param SubLabelCode: *内测中，敬请期待*
        :type SubLabelCode: str
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
        :type SubLabel: str
        :param Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
        :type Suggestion: str
        """
        self.Label = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None
        self.SubLabelCode = None
        self.SubLabel = None
        self.Suggestion = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.SubLabelCode = params.get("SubLabelCode")
        self.SubLabel = params.get("SubLabel")
        self.Suggestion = params.get("Suggestion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioResultDetailTextResult(AbstractModel):
    """音频ASR文本审核结果

    """

    def __init__(self):
        r"""
        :param Label: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Normal**：正常，**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Keywords: 该字段用于返回ASR识别出的文本内容命中的关键词信息，用于标注内容违规的具体原因（如：加我微信）。该参数可能会有多个返回值，代表命中的多个关键词；若返回值为空，Score不为空，则代表识别结果所对应的恶意标签（Label）来自于语义模型判断的返回值。
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param LibId: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的ID，以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 该字段**仅当Label为Custom：自定义关键词时该参数有效**,用于返回自定义库的名称,以方便自定义库管理和配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Score: 该字段用于返回当前标签下的置信度，取值范围：0（**置信度最低**）-100（**置信度最高**），越高代表文本越有可能属于当前返回的标签；如：*色情 99*，则表明该文本非常有可能属于色情内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param LibType: 该字段用于返回自定义关键词对应的词库类型，取值为**1**（黑白库）和**2**（自定义关键词库），若未配置自定义关键词库,则默认值为1（黑白库匹配）。
注意：此字段可能返回 null，表示取不到有效值。
        :type LibType: int
        :param Suggestion: 该字段用于返回后续操作建议。当您获取到判定结果后，返回值表示具体的后续建议操作。<br>
返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param SubLabel: 该字段用于返回当前标签（Lable）下的二级标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        """
        self.Label = None
        self.Keywords = None
        self.LibId = None
        self.LibName = None
        self.Score = None
        self.LibType = None
        self.Suggestion = None
        self.SubLabel = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Keywords = params.get("Keywords")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Score = params.get("Score")
        self.LibType = params.get("LibType")
        self.Suggestion = params.get("Suggestion")
        self.SubLabel = params.get("SubLabel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AudioSegments(AbstractModel):
    """声音段信息

    """

    def __init__(self):
        r"""
        :param OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
注意：此字段可能返回 null，表示取不到有效值。
        :type OffsetTime: str
        :param Result: 结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.vm.v20210922.models.AudioResult`
        """
        self.OffsetTime = None
        self.Result = None


    def _deserialize(self, params):
        self.OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self.Result = AudioResult()
            self.Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BucketInfo(AbstractModel):
    """文件桶信息
    参考腾讯云存储相关说明 https://cloud.tencent.com/document/product/436/44352

    """

    def __init__(self):
        r"""
        :param Bucket: 腾讯云对象存储，存储桶名称
        :type Bucket: str
        :param Region: 地域
        :type Region: str
        :param Object: 对象Key
        :type Object: str
        """
        self.Bucket = None
        self.Region = None
        self.Object = None


    def _deserialize(self, params):
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        self.Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskRequest(AbstractModel):
    """CancelTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
        :type TaskId: str
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelTaskResponse(AbstractModel):
    """CancelTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVideoModerationTaskRequest(AbstractModel):
    """CreateVideoModerationTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param BizType: 业务类型, 定义 模版策略，输出存储配置。如果没有BizType，可以先参考 【创建业务配置】接口进行创建
        :type BizType: str
        :param Type: 任务类型：可选VIDEO（点播视频），LIVE_VIDEO（直播视频）
        :type Type: str
        :param Tasks: 输入的任务信息，最多可以同时创建10个任务
        :type Tasks: list of TaskInput
        :param Seed: 回调签名key，具体可以查看签名文档。
        :type Seed: str
        :param CallbackUrl: 接收审核信息回调地址，如果设置，则审核过程中产生的违规音频片段和画面截帧发送此接口
        :type CallbackUrl: str
        :param Priority: 审核排队优先级。当您有多个视频审核任务排队时，可以根据这个参数控制排队优先级。用于处理插队等逻辑。默认该参数为0
        :type Priority: int
        """
        self.BizType = None
        self.Type = None
        self.Tasks = None
        self.Seed = None
        self.CallbackUrl = None
        self.Priority = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInput()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.Seed = params.get("Seed")
        self.CallbackUrl = params.get("CallbackUrl")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoModerationTaskResponse(AbstractModel):
    """CreateVideoModerationTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param Results: 任务创建结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of TaskResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = TaskResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskDetailRequest(AbstractModel):
    """DescribeTaskDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID，创建任务后返回的TaskId字段
        :type TaskId: str
        :param ShowAllSegments: 是否展示所有分片，默认只展示命中规则的分片
        :type ShowAllSegments: bool
        """
        self.TaskId = None
        self.ShowAllSegments = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ShowAllSegments = params.get("ShowAllSegments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskDetailResponse(AbstractModel):
    """DescribeTaskDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 该字段用于返回创建视频审核任务后返回的任务ID（在Results参数中），用于标识需要查询任务详情的审核任务。
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param DataId: 该字段用于返回调用视频审核接口时传入的数据ID参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param BizType: 该字段用于返回调用视频审核接口时传入的BizType参数，方便数据的辨别和管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param Name: 该字段用于返回调用视频审核接口时传入的TaskInput参数中的任务名称，方便任务的识别与管理。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 该字段用于返回所查询内容的任务状态。
<br>取值：**FINISH**（任务已完成）、**PENDING** （任务等待中）、**RUNNING** （任务进行中）、**ERROR** （任务出错）、**CANCELLED** （任务已取消）。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 该字段用于返回调用视频审核接口时输入的视频审核类型，取值为：**VIDEO**（点播视频）和**LIVE_VIDEO**（直播视频），默认值为VIDEO。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Suggestion: 该字段用于返回基于恶意标签的后续操作建议。当您获取到判定结果后，返回值表示系统推荐的后续操作；建议您按照业务所需，对不同违规类型与建议值进行处理。<br>返回值：**Block**：建议屏蔽，**Review** ：建议人工复审，**Pass**：建议通过
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Labels: 该字段用于返回检测结果所对应的恶意标签。<br>返回值：**Porn**：色情，**Abuse**：谩骂，**Ad**：广告，**Custom**：自定义违规；以及其他令人反感、不安全或不适宜的内容类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param MediaInfo: 该字段用于返回输入媒体文件的详细信息，包括编解码格式、分片时长等信息。详细内容敬请参考MediaInfo数据结构的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.vm.v20210922.models.MediaInfo`
        :param InputInfo: 该字段用于返回审核服务的媒体内容信息，主要包括传入文件类型和访问地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.vm.v20210922.models.InputInfo`
        :param CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 该字段用于返回被查询任务最后更新时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param TryInSeconds: 在秒后重试
注意：此字段可能返回 null，表示取不到有效值。
        :type TryInSeconds: int
        :param ImageSegments: 该字段用于返回视频中截帧审核的结果，详细返回内容敬请参考ImageSegments数据结构的描述。<br>备注：数据有效期为24小时，如需要延长存储时间，请在已配置的COS储存桶中设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageSegments: list of ImageSegments
        :param AudioSegments: 该字段用于返回视频中音频审核的结果，详细返回内容敬请参考AudioSegments数据结构的描述。<br>备注：数据有效期为24小时，如需要延长存储时间，请在已配置的COS储存桶中设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioSegments: list of AudioSegments
        :param ErrorType: 当任务状态为Error时，返回对应错误的类型，取值：**DECODE_ERROR**: 解码失败。（输入资源中可能包含无法解码的视频）
**URL_ERROR**：下载地址验证失败。
**TIMEOUT_ERROR**：处理超时。任务状态非Error时默认返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorType: str
        :param ErrorDescription: 当任务状态为Error时，该字段用于返回对应错误的详细描述，任务状态非Error时默认返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorDescription: str
        :param Label: 该字段用于返回检测结果所对应的标签。如果未命中恶意，返回Normal，如果命中恶意，则返回Labels中优先级最高的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param AudioText: 该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
注意：此字段可能返回 null，表示取不到有效值。
        :type AudioText: str
        :param Asrs: 该字段用于返回音频文件识别出的对应文本内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Asrs: list of RcbAsr
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.DataId = None
        self.BizType = None
        self.Name = None
        self.Status = None
        self.Type = None
        self.Suggestion = None
        self.Labels = None
        self.MediaInfo = None
        self.InputInfo = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.TryInSeconds = None
        self.ImageSegments = None
        self.AudioSegments = None
        self.ErrorType = None
        self.ErrorDescription = None
        self.Label = None
        self.AudioText = None
        self.Asrs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("InputInfo") is not None:
            self.InputInfo = InputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.TryInSeconds = params.get("TryInSeconds")
        if params.get("ImageSegments") is not None:
            self.ImageSegments = []
            for item in params.get("ImageSegments"):
                obj = ImageSegments()
                obj._deserialize(item)
                self.ImageSegments.append(obj)
        if params.get("AudioSegments") is not None:
            self.AudioSegments = []
            for item in params.get("AudioSegments"):
                obj = AudioSegments()
                obj._deserialize(item)
                self.AudioSegments.append(obj)
        self.ErrorType = params.get("ErrorType")
        self.ErrorDescription = params.get("ErrorDescription")
        self.Label = params.get("Label")
        self.AudioText = params.get("AudioText")
        if params.get("Asrs") is not None:
            self.Asrs = []
            for item in params.get("Asrs"):
                obj = RcbAsr()
                obj._deserialize(item)
                self.Asrs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTasksRequest(AbstractModel):
    """DescribeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 该参数表示任务列表每页展示的任务条数，**默认值为10**（每页展示10条任务）。
        :type Limit: int
        :param Filter: 该参数表示任务筛选器的输入参数，可根据业务类型、审核文件类型、处理建议及任务状态筛选想要查看的审核任务，具体参数内容请参见TaskFilter数据结构的详细描述。
        :type Filter: :class:`tencentcloud.vm.v20210922.models.TaskFilter`
        :param PageToken: 该参数表示翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
        :type PageToken: str
        :param StartTime: 该参数表示任务列表的开始时间，格式为ISO8601标准的时间戳。**默认值为最近3天**，若传入该参数，则在这一时间到EndTime之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :type StartTime: str
        :param EndTime: 该参数表示任务列表的结束时间，格式为ISO8601标准的时间戳。**默认值为空**，若传入该参数，则在这StartTime到这一时间之间的任务将会被筛选出来。<br>备注：该参数与Filter共同起到任务筛选作用，二者作用无先后顺序。
        :type EndTime: str
        """
        self.Limit = None
        self.Filter = None
        self.PageToken = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        if params.get("Filter") is not None:
            self.Filter = TaskFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.PageToken = params.get("PageToken")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTasksResponse(AbstractModel):
    """DescribeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 该字段用于返回当前查询的任务总量，格式为int字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: str
        :param Data: 该字段用于返回当前页的任务详细数据，具体输出内容请参见TaskData数据结构的详细描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of TaskData
        :param PageToken: 该字段用于返回翻页时使用的Token信息，由系统自动生成，并在翻页时向下一个生成的页面传递此参数，以方便快速翻页功能的实现。当到最后一页时，该字段为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type PageToken: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Data = None
        self.PageToken = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TaskData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.PageToken = params.get("PageToken")
        self.RequestId = params.get("RequestId")


class ImageResult(AbstractModel):
    """Result结果详情

    """

    def __init__(self):
        r"""
        :param HitFlag: 违规标志
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Label: 命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Results: 画面截帧图片结果集
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of ImageResultResult
        :param Url: 图片URL地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Extra: 附加字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        """
        self.HitFlag = None
        self.Label = None
        self.Suggestion = None
        self.Score = None
        self.Results = None
        self.Url = None
        self.Extra = None


    def _deserialize(self, params):
        self.HitFlag = params.get("HitFlag")
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = ImageResultResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.Url = params.get("Url")
        self.Extra = params.get("Extra")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultResult(AbstractModel):
    """图片输出结果的子结果

    """

    def __init__(self):
        r"""
        :param Scene: 场景
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Scene: str
        :param HitFlag: 是否命中
0 未命中
1 命中
注意：此字段可能返回 null，表示取不到有效值。
        :type HitFlag: int
        :param Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param SubLabel: 子标签
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabel: str
        :param Score: 分数
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param Names: 如果命中场景为涉政，则该数据为人物姓名列表，否则null
注意：此字段可能返回 null，表示取不到有效值。
        :type Names: list of str
        :param Text: 图片OCR文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Details: 其他详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: list of ImageResultsResultDetail
        """
        self.Scene = None
        self.HitFlag = None
        self.Suggestion = None
        self.Label = None
        self.SubLabel = None
        self.Score = None
        self.Names = None
        self.Text = None
        self.Details = None


    def _deserialize(self, params):
        self.Scene = params.get("Scene")
        self.HitFlag = params.get("HitFlag")
        self.Suggestion = params.get("Suggestion")
        self.Label = params.get("Label")
        self.SubLabel = params.get("SubLabel")
        self.Score = params.get("Score")
        self.Names = params.get("Names")
        self.Text = params.get("Text")
        if params.get("Details") is not None:
            self.Details = []
            for item in params.get("Details"):
                obj = ImageResultsResultDetail()
                obj._deserialize(item)
                self.Details.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetail(AbstractModel):
    """具体场景下的图片识别结果

    """

    def __init__(self):
        r"""
        :param Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Text: OCR识别文本
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param Location: 位置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Location: :class:`tencentcloud.vm.v20210922.models.ImageResultsResultDetailLocation`
        :param Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param LibId: 库ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LibId: str
        :param LibName: 库名称
注意：此字段可能返回 null，表示取不到有效值。
        :type LibName: str
        :param Keywords: 命中的关键词
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of str
        :param Suggestion: 建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 得分
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param SubLabelCode: 子标签码
注意：此字段可能返回 null，表示取不到有效值。
        :type SubLabelCode: str
        """
        self.Name = None
        self.Text = None
        self.Location = None
        self.Label = None
        self.LibId = None
        self.LibName = None
        self.Keywords = None
        self.Suggestion = None
        self.Score = None
        self.SubLabelCode = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Text = params.get("Text")
        if params.get("Location") is not None:
            self.Location = ImageResultsResultDetailLocation()
            self.Location._deserialize(params.get("Location"))
        self.Label = params.get("Label")
        self.LibId = params.get("LibId")
        self.LibName = params.get("LibName")
        self.Keywords = params.get("Keywords")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        self.SubLabelCode = params.get("SubLabelCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageResultsResultDetailLocation(AbstractModel):
    """图片详情位置信息

    """

    def __init__(self):
        r"""
        :param X: x坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type X: float
        :param Y: y坐标
注意：此字段可能返回 null，表示取不到有效值。
        :type Y: float
        :param Width: 宽度
注意：此字段可能返回 null，表示取不到有效值。
        :type Width: int
        :param Height: 高度
注意：此字段可能返回 null，表示取不到有效值。
        :type Height: int
        :param Rotate: 旋转角度
注意：此字段可能返回 null，表示取不到有效值。
        :type Rotate: float
        """
        self.X = None
        self.Y = None
        self.Width = None
        self.Height = None
        self.Rotate = None


    def _deserialize(self, params):
        self.X = params.get("X")
        self.Y = params.get("Y")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Rotate = params.get("Rotate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageSegments(AbstractModel):
    """图片段信息

    """

    def __init__(self):
        r"""
        :param OffsetTime: 截帧时间。
点播文件：该值为相对于视频偏移时间，单位为秒，例如：0，5，10
直播流：该值为时间戳，例如：1594650717
        :type OffsetTime: str
        :param Result: 画面截帧结果详情
        :type Result: :class:`tencentcloud.vm.v20210922.models.ImageResult`
        """
        self.OffsetTime = None
        self.Result = None


    def _deserialize(self, params):
        self.OffsetTime = params.get("OffsetTime")
        if params.get("Result") is not None:
            self.Result = ImageResult()
            self.Result._deserialize(params.get("Result"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InputInfo(AbstractModel):
    """输入信息详情

    """

    def __init__(self):
        r"""
        :param Type: 传入的类型可选：URL，COS
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Url: Url地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param BucketInfo: 桶信息。当输入当时COS时，该字段不为空
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketInfo: str
        """
        self.Type = None
        self.Url = None
        self.BucketInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        self.BucketInfo = params.get("BucketInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MediaInfo(AbstractModel):
    """媒体类型

    """

    def __init__(self):
        r"""
        :param Codecs: 编码格式
        :type Codecs: str
        :param Duration: 流检测时分片时长
注意：此字段可能返回 0，表示取不到有效值。
        :type Duration: int
        :param Width: 宽，单位为像素
        :type Width: int
        :param Height: 高，单位为像素
        :type Height: int
        :param Thumbnail: 封面
        :type Thumbnail: str
        """
        self.Codecs = None
        self.Duration = None
        self.Width = None
        self.Height = None
        self.Thumbnail = None


    def _deserialize(self, params):
        self.Codecs = params.get("Codecs")
        self.Duration = params.get("Duration")
        self.Width = params.get("Width")
        self.Height = params.get("Height")
        self.Thumbnail = params.get("Thumbnail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RcbAsr(AbstractModel):
    """审核切片asr文本信息

    """

    def __init__(self):
        r"""
        :param Text: 该字段用于返回音频文件识别出的对应文本内容，最大支持**前1000个字符**。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param CreatedAt: 该字段用于返回被查询任务创建的时间，格式采用 ISO 8601标准。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        """
        self.Text = None
        self.CreatedAt = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecognitionResult(AbstractModel):
    """识别类标签结果信息

    """

    def __init__(self):
        r"""
        :param Label: 可能的取值有：Teenager 、Gender
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Tags: 识别标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.Label = None
        self.Tags = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """数据存储信息

    """

    def __init__(self):
        r"""
        :param Type: 类型 可选：
URL 资源链接类型
COS 腾讯云对象存储类型
        :type Type: str
        :param Url: 资源链接
        :type Url: str
        :param BucketInfo: 腾讯云存储桶信息
        :type BucketInfo: :class:`tencentcloud.vm.v20210922.models.BucketInfo`
        """
        self.Type = None
        self.Url = None
        self.BucketInfo = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Url = params.get("Url")
        if params.get("BucketInfo") is not None:
            self.BucketInfo = BucketInfo()
            self.BucketInfo._deserialize(params.get("BucketInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """音频切片识别标签

    """

    def __init__(self):
        r"""
        :param Name: 根据Label字段确定具体名称：
当Label 为Teenager 时 Name可能取值有：Teenager 
当Label 为Gender 时 Name可能取值有：Male 、Female
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Score: 置信分：0～100，数值越大表示置信度越高
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        :param StartTime: 识别开始偏移时间，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: float
        :param EndTime: 识别结束偏移时间，单位：毫秒
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: float
        """
        self.Name = None
        self.Score = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Score = params.get("Score")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskData(AbstractModel):
    """任务数据

    """

    def __init__(self):
        r"""
        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param DataId: 输入的数据ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param BizType: 业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BizType: str
        :param Name: 任务名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Status: 状态，可选：PENDING，RUNNING，ERROR，FINISH，CANCELLED
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param Type: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param Suggestion: 处理建议
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Labels: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of TaskLabel
        :param MediaInfo: 媒体信息
注意：此字段可能返回 null，表示取不到有效值。
        :type MediaInfo: :class:`tencentcloud.vm.v20210922.models.MediaInfo`
        :param InputInfo: 输入信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InputInfo: :class:`tencentcloud.vm.v20210922.models.InputInfo`
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        """
        self.TaskId = None
        self.DataId = None
        self.BizType = None
        self.Name = None
        self.Status = None
        self.Type = None
        self.Suggestion = None
        self.Labels = None
        self.MediaInfo = None
        self.InputInfo = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DataId = params.get("DataId")
        self.BizType = params.get("BizType")
        self.Name = params.get("Name")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        if params.get("Labels") is not None:
            self.Labels = []
            for item in params.get("Labels"):
                obj = TaskLabel()
                obj._deserialize(item)
                self.Labels.append(obj)
        if params.get("MediaInfo") is not None:
            self.MediaInfo = MediaInfo()
            self.MediaInfo._deserialize(params.get("MediaInfo"))
        if params.get("InputInfo") is not None:
            self.InputInfo = InputInfo()
            self.InputInfo._deserialize(params.get("InputInfo"))
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskFilter(AbstractModel):
    """Cos TaskFilter

    """

    def __init__(self):
        r"""
        :param BizType: 任务业务类型
        :type BizType: str
        :param Type: 任务类型，可选：VIDEO，AUDIO， LIVE_VIDEO, LIVE_AUDIO
        :type Type: str
        :param Suggestion: 建议，可选：Pass, Review,Block
        :type Suggestion: str
        :param TaskStatus: 状态，可选：PENDING，RUNNING，ERROR，FINISH，CANCELLED
        :type TaskStatus: str
        """
        self.BizType = None
        self.Type = None
        self.Suggestion = None
        self.TaskStatus = None


    def _deserialize(self, params):
        self.BizType = params.get("BizType")
        self.Type = params.get("Type")
        self.Suggestion = params.get("Suggestion")
        self.TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """音视频任务结构

    """

    def __init__(self):
        r"""
        :param DataId: 数据ID
        :type DataId: str
        :param Name: 任务名
        :type Name: str
        :param Input: 任务输入
        :type Input: :class:`tencentcloud.vm.v20210922.models.StorageInfo`
        """
        self.DataId = None
        self.Name = None
        self.Input = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.Name = params.get("Name")
        if params.get("Input") is not None:
            self.Input = StorageInfo()
            self.Input._deserialize(params.get("Input"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskLabel(AbstractModel):
    """任务输出标签

    """

    def __init__(self):
        r"""
        :param Label: 命中的标签
Porn 色情
Sexy 性感
Polity 政治
Illegal 违法
Abuse 谩骂
Terror 暴恐
Ad 广告
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Suggestion: 审核建议，可选值：
Pass 通过，
Review 建议人审，
Block 确认违规
注意：此字段可能返回 null，表示取不到有效值。
        :type Suggestion: str
        :param Score: 得分，分数是 0 ～ 100
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: int
        """
        self.Label = None
        self.Suggestion = None
        self.Score = None


    def _deserialize(self, params):
        self.Label = params.get("Label")
        self.Suggestion = params.get("Suggestion")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskResult(AbstractModel):
    """创建任务时的返回结果

    """

    def __init__(self):
        r"""
        :param DataId: 请求时传入的DataId
注意：此字段可能返回 null，表示取不到有效值。
        :type DataId: str
        :param TaskId: TaskId，任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param Code: 错误码。如果code为OK，则表示创建成功，其他则参考公共错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: str
        :param Message: 如果错误，该字段表示错误详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.DataId = None
        self.TaskId = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.DataId = params.get("DataId")
        self.TaskId = params.get("TaskId")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        