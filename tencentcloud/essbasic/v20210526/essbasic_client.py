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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.essbasic.v20210526 import models


class EssbasicClient(AbstractClient):
    _apiVersion = '2021-05-26'
    _endpoint = 'essbasic.tencentcloudapi.com'
    _service = 'essbasic'


    def ChannelBatchCancelFlows(self, request):
        """指定需要批量撤销的签署流程Id，批量撤销合同
        客户指定需要撤销的签署流程Id，最多100个，超过100不处理；接口失败后返回错误信息
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人

        :param request: Request instance for ChannelBatchCancelFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelBatchCancelFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelBatchCancelFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelBatchCancelFlows", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelBatchCancelFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCancelFlow(self, request):
        """撤销签署流程接口，可以撤回：未全部签署完成；不可以撤回（终态）：已全部签署完成、已拒签、已过期、已撤回。
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人

        :param request: Request instance for ChannelCancelFlow.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCancelFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCancelFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCancelMultiFlowSignQRCode(self, request):
        """此接口（ChannelCancelMultiFlowSignQRCode）用于取消一码多扫二维码。该接口对传入的二维码ID，若还在有效期内，可以提前失效。

        :param request: Request instance for ChannelCancelMultiFlowSignQRCode.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelMultiFlowSignQRCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCancelMultiFlowSignQRCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCancelMultiFlowSignQRCode", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCancelMultiFlowSignQRCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateBatchCancelFlowUrl(self, request):
        """指定需要批量撤销的签署流程Id，获取批量撤销链接 - 不建议使用此接口，可使用ChannelBatchCancelFlows
        客户指定需要撤销的签署流程Id，最多100个，超过100不处理；
        接口调用成功返回批量撤销合同的链接，通过链接跳转到电子签小程序完成批量撤销;
        可以撤回：未全部签署完成；不可以撤回（终态）：已全部签署完成、已拒签、已过期、已撤回。
        注意:
        能撤回合同的只能是合同的发起人或者发起企业的超管、法人

        :param request: Request instance for ChannelCreateBatchCancelFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchCancelFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBatchCancelFlowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateBatchCancelFlowUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateBatchCancelFlowUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateBoundFlows(self, request):
        """此接口（ChannelCreateBoundFlows）用于子客领取合同，经办人需要有相应的角色，合同不能重复领取。

        :param request: Request instance for ChannelCreateBoundFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBoundFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateBoundFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateBoundFlows", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateBoundFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateConvertTaskApi(self, request):
        """创建文件转换任务

        :param request: Request instance for ChannelCreateConvertTaskApi.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateConvertTaskApiRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateConvertTaskApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateConvertTaskApi", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateConvertTaskApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateEmbedWebUrl(self, request):
        """本接口（ChannelCreateEmbedWebUrl）用于创建嵌入web的链接

        :param request: Request instance for ChannelCreateEmbedWebUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateEmbedWebUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateEmbedWebUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateEmbedWebUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateEmbedWebUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateFlowByFiles(self, request):
        """接口（ChannelCreateFlowByFiles）用于通过文件创建签署流程。此接口静默签能力不可直接使用，需要运营申请

        :param request: Request instance for ChannelCreateFlowByFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowByFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowByFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowByFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowByFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateFlowGroupByFiles(self, request):
        """接口（ChannelCreateFlowGroupByFiles）用于通过多文件创建合同组签署流程。

        :param request: Request instance for ChannelCreateFlowGroupByFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowGroupByFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowGroupByFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowGroupByFiles", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowGroupByFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateFlowReminds(self, request):
        """指定需要批量催办的签署流程Id，批量催办合同，最多100个；接口失败后返回错误信息
        注意:
        该接口不可直接调用，请联系电子签运营开通后方可调用。

        :param request: Request instance for ChannelCreateFlowReminds.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowRemindsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowRemindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowReminds", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowRemindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateFlowSignReview(self, request):
        """提交企业签署流程审批结果

        在通过接口(CreateFlowsByTemplates 或者ChannelCreateFlowByFiles)创建签署流程时，若指定了参数 NeedSignReview 为true,则可以调用此接口提交企业内部签署审批结果。
        若签署流程状态正常，且本企业存在签署方未签署，同一签署流程可以多次提交签署审批结果，签署时的最后一个“审批结果”有效。

        :param request: Request instance for ChannelCreateFlowSignReview.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignReviewRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignReviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowSignReview", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowSignReviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateFlowSignUrl(self, request):
        """创建签署链接，需要联系运营人员开白后才可使用

        :param request: Request instance for ChannelCreateFlowSignUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateFlowSignUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateFlowSignUrl", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateFlowSignUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateMultiFlowSignQRCode(self, request):
        """此接口（ChannelCreateMultiFlowSignQRCode）用于创建一码多扫签署流程二维码。
        适用的模版仅限于B2C（1、无序签署，2、顺序签署时B静默签署，3、顺序签署时B非首位签署）、单C的模版，且模版中发起方没有填写控件。

        :param request: Request instance for ChannelCreateMultiFlowSignQRCode.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateMultiFlowSignQRCodeRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateMultiFlowSignQRCodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateMultiFlowSignQRCode", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateMultiFlowSignQRCodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreatePrepareFlow(self, request):
        """创建预发起合同

        :param request: Request instance for ChannelCreatePrepareFlow.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreatePrepareFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreatePrepareFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreatePrepareFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreatePrepareFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateReleaseFlow(self, request):
        """发起解除协议，主要应用场景为：基于一份已经签署的合同，进行解除操作。
        合同发起人必须在电子签已经进行实名。

        :param request: Request instance for ChannelCreateReleaseFlow.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateReleaseFlowRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateReleaseFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateReleaseFlow", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateReleaseFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelCreateSealPolicy(self, request):
        """将指定印章授权给第三方平台子客企业下的某些员工

        :param request: Request instance for ChannelCreateSealPolicy.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateSealPolicyRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelCreateSealPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelCreateSealPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelCreateSealPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelDeleteSealPolicies(self, request):
        """删除指定印章下多个授权信息

        :param request: Request instance for ChannelDeleteSealPolicies.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteSealPoliciesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDeleteSealPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDeleteSealPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDeleteSealPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelDescribeEmployees(self, request):
        """查询企业员工列表

        :param request: Request instance for ChannelDescribeEmployees.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeEmployeesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeEmployeesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeEmployees", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeEmployeesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelDescribeOrganizationSeals(self, request):
        """查询子客企业电子印章，需要操作者具有管理印章权限
        客户指定需要获取的印章数量和偏移量，数量最多100，超过100按100处理；入参InfoType控制印章是否携带授权人信息，为1则携带，为0则返回的授权人信息为空数组。接口调用成功返回印章的信息列表还有企业印章的总数。

        :param request: Request instance for ChannelDescribeOrganizationSeals.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeOrganizationSealsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelDescribeOrganizationSealsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelDescribeOrganizationSeals", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelDescribeOrganizationSealsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelGetTaskResultApi(self, request):
        """查询转换任务状态

        :param request: Request instance for ChannelGetTaskResultApi.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelGetTaskResultApiRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelGetTaskResultApiResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelGetTaskResultApi", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelGetTaskResultApiResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelUpdateSealStatus(self, request):
        """本接口（ChannelUpdateSealStatus）用于第三方应用平台为子客企业更新印章状态

        :param request: Request instance for ChannelUpdateSealStatus.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelUpdateSealStatusRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelUpdateSealStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelUpdateSealStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelUpdateSealStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ChannelVerifyPdf(self, request):
        """合同文件验签

        :param request: Request instance for ChannelVerifyPdf.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ChannelVerifyPdfRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ChannelVerifyPdfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChannelVerifyPdf", params, headers=headers)
            response = json.loads(body)
            model = models.ChannelVerifyPdfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateChannelFlowEvidenceReport(self, request):
        """创建出证报告，返回报告 ID。需要配合出证套餐才能调用。
        出证需要一定时间，建议调用创建出证24小时之后再通过DescribeChannelFlowEvidenceReport进行查询。

        :param request: Request instance for CreateChannelFlowEvidenceReport.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateChannelFlowEvidenceReportRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateChannelFlowEvidenceReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChannelFlowEvidenceReport", params, headers=headers)
            response = json.loads(body)
            model = models.CreateChannelFlowEvidenceReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateConsoleLoginUrl(self, request):
        """此接口（CreateConsoleLoginUrl）用于创建第三方平台子客企业控制台Web/移动登录链接。登录链接是子客控制台的唯一入口。
        若子客企业未激活，会进入企业激活流程，首次参与激活流程的经办人会成为超管。（若企业激活过程中填写信息有误，需要重置激活流程，可以换一个经办人OpenId获取新的链接进入。）
        若子客企业已激活，使用了新的经办人OpenId进入，则会进入经办人的实名流程。
        若子客企业、经办人均已完成认证，则会直接进入子客Web控制台。

        :param request: Request instance for CreateConsoleLoginUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateConsoleLoginUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateConsoleLoginUrl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateConsoleLoginUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFlowsByTemplates(self, request):
        """接口（CreateFlowsByTemplates）用于使用多个模板批量创建签署流程。当前可批量发起合同（签署流程）数量最大为20个。
        如若在模板中配置了动态表格, 上传的附件必须为A4大小
        合同发起人必须在电子签已经进行实名。

        :param request: Request instance for CreateFlowsByTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateFlowsByTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowsByTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowsByTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSealByImage(self, request):
        """通过图片为子客企业代创建印章，图片最大5MB

        :param request: Request instance for CreateSealByImage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSealByImageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSealByImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSealByImage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSealByImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSignUrls(self, request):
        """创建跳转小程序查看或签署的链接。

        跳转小程序的几种方式：主要是设置不同的EndPoint
        1. 通过链接Url直接跳转到小程序，不需要返回
        设置EndPoint为WEIXINAPP，得到链接打开即可。（与短信提醒用户签署形式一样）。
        2. 通过链接Url打开H5引导页-->点击跳转到小程序-->签署完退出小程序-->回到H5引导页-->跳转到指定JumpUrl
        设置EndPoint为CHANNEL，指定JumpUrl，得到链接打开即可。
        3. 客户App直接跳转到小程序-->小程序签署完成-->返回App
        跳转到小程序的实现，参考官方文档（分为全屏、半屏两种方式）
        全屏方式：
        （https://developers.weixin.qq.com/miniprogram/dev/api/navigate/wx.navigateToMiniProgram.html）
        半屏方式：
        （https://developers.weixin.qq.com/miniprogram/dev/framework/open-ability/openEmbeddedMiniProgram.html）
        其中小程序的原始Id，请联系<对接技术人员>获取，或者查看小程序信息自助获取。
        使用CreateSignUrls，设置EndPoint为APP，得到path。
        4. 客户小程序直接跳到电子签小程序-->签署完成退出电子签小程序-->回到客户小程序
        实现方式同App跳小程序。

        :param request: Request instance for CreateSignUrls.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.CreateSignUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSignUrls", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSignUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeChannelFlowEvidenceReport(self, request):
        """查询出证报告，返回报告 URL。

        :param request: Request instance for DescribeChannelFlowEvidenceReport.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelFlowEvidenceReportRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeChannelFlowEvidenceReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeChannelFlowEvidenceReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeChannelFlowEvidenceReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExtendedServiceAuthInfo(self, request):
        """查询企业扩展服务授权信息，企业经办人需要是企业超管或者法人

        :param request: Request instance for DescribeExtendedServiceAuthInfo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeExtendedServiceAuthInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeExtendedServiceAuthInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExtendedServiceAuthInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExtendedServiceAuthInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowDetailInfo(self, request):
        """此接口（DescribeFlowDetailInfo）用于查询合同(签署流程)的详细信息。

        :param request: Request instance for DescribeFlowDetailInfo.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeFlowDetailInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowDetailInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowDetailInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceUrlsByFlows(self, request):
        """根据签署流程信息批量获取资源下载链接，可以下载签署中、签署完的合同，需合作企业先进行授权。
        此接口直接返回下载的资源的url，与接口GetDownloadFlowUrl跳转到控制台的下载方式不同。

        :param request: Request instance for DescribeResourceUrlsByFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeResourceUrlsByFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceUrlsByFlows", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceUrlsByFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplates(self, request):
        """通过此接口（DescribeTemplates）查询该第三方平台子客企业在电子签拥有的有效模板，不包括第三方平台模板

        :param request: Request instance for DescribeTemplates.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsage(self, request):
        """此接口（DescribeUsage）用于获取第三方平台所有合作企业流量消耗情况。
         注: 此接口每日限频2次，若要扩大限制次数,请提前与客服经理或邮件至e-contract@tencent.com进行联系。

        :param request: Request instance for DescribeUsage.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.DescribeUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetDownloadFlowUrl(self, request):
        """此接口（GetDownloadFlowUrl）用于创建电子签批量下载地址，让合作企业进入控制台直接下载，支持客户合同（流程）按照自定义文件夹形式 分类下载。
        当前接口限制最多合同（流程）50个.

        :param request: Request instance for GetDownloadFlowUrl.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.GetDownloadFlowUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDownloadFlowUrl", params, headers=headers)
            response = json.loads(body)
            model = models.GetDownloadFlowUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyExtendedService(self, request):
        """修改（操作）企业扩展服务 ，企业经办人需要是企业超管或者法人

        :param request: Request instance for ModifyExtendedService.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.ModifyExtendedServiceRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.ModifyExtendedServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExtendedService", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExtendedServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def OperateChannelTemplate(self, request):
        """此接口（OperateChannelTemplate）用于针对第三方应用平台模板库中的模板对子客企业可见性的查询和设置，不会直接分配第三方应用平台模板给子客企业。
        1、OperateType=select时：
        查询第三方应用平台模板库
        2、OperateType=update或者delete时：
        对子客企业进行模板库中模板可见性的修改、删除操作。

        :param request: Request instance for OperateChannelTemplate.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.OperateChannelTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OperateChannelTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.OperateChannelTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def PrepareFlows(self, request):
        """该接口 (PrepareFlows) 用于创建待发起文件
        用户通过该接口进入签署流程发起的确认页面，进行发起信息二次确认， 如果确认则进行正常发起。
        目前该接口只支持B2C，不建议使用，将会废弃。

        :param request: Request instance for PrepareFlows.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.PrepareFlowsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PrepareFlows", params, headers=headers)
            response = json.loads(body)
            model = models.PrepareFlowsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncProxyOrganization(self, request):
        """此接口（SyncProxyOrganization）用于同步第三方平台子客企业信息，主要是子客企业的营业执照，便于子客企业开通过程中不用手动上传。若有需要调用此接口，需要在创建控制链接CreateConsoleLoginUrl之后即刻进行调用。

        :param request: Request instance for SyncProxyOrganization.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncProxyOrganization", params, headers=headers)
            response = json.loads(body)
            model = models.SyncProxyOrganizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SyncProxyOrganizationOperators(self, request):
        """此接口（SyncProxyOrganizationOperators）用于同步 第三方平台子客企业经办人列表，主要是同步经办人的离职状态。子客Web控制台的组织架构管理，是依赖于第三方应用平台的，无法针对员工做新增/更新/离职等操作。
        若经办人信息有误，或者需要修改，也可以先将之前的经办人做离职操作，然后重新使用控制台链接CreateConsoleLoginUrl让经办人重新实名。

        :param request: Request instance for SyncProxyOrganizationOperators.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.SyncProxyOrganizationOperatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SyncProxyOrganizationOperators", params, headers=headers)
            response = json.loads(body)
            model = models.SyncProxyOrganizationOperatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UploadFiles(self, request):
        """此接口（UploadFiles）用于文件上传。
        调用时需要设置Domain, 正式环境为 file.ess.tencent.cn。
        代码示例：
        HttpProfile httpProfile = new HttpProfile();
        httpProfile.setEndpoint("file.test.ess.tencent.cn");

        :param request: Request instance for UploadFiles.
        :type request: :class:`tencentcloud.essbasic.v20210526.models.UploadFilesRequest`
        :rtype: :class:`tencentcloud.essbasic.v20210526.models.UploadFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UploadFiles", params, headers=headers)
            response = json.loads(body)
            model = models.UploadFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)