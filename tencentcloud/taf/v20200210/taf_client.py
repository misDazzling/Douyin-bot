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
from tencentcloud.taf.v20200210 import models


class TafClient(AbstractClient):
    _apiVersion = '2020-02-10'
    _endpoint = 'taf.tencentcloudapi.com'
    _service = 'taf'


    def RecognizeCustomizedAudience(self, request):
        """流量反欺诈-流量验准定制版

        :param request: Request instance for RecognizeCustomizedAudience.
        :type request: :class:`tencentcloud.taf.v20200210.models.RecognizeCustomizedAudienceRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.RecognizeCustomizedAudienceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeCustomizedAudience", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeCustomizedAudienceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecognizePreciseTargetAudience(self, request):
        """流量反欺诈-流量验准高级版

        :param request: Request instance for RecognizePreciseTargetAudience.
        :type request: :class:`tencentcloud.taf.v20200210.models.RecognizePreciseTargetAudienceRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.RecognizePreciseTargetAudienceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizePreciseTargetAudience", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizePreciseTargetAudienceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecognizeTargetAudience(self, request):
        """流量反欺诈-流量验准

        :param request: Request instance for RecognizeTargetAudience.
        :type request: :class:`tencentcloud.taf.v20200210.models.RecognizeTargetAudienceRequest`
        :rtype: :class:`tencentcloud.taf.v20200210.models.RecognizeTargetAudienceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecognizeTargetAudience", params, headers=headers)
            response = json.loads(body)
            model = models.RecognizeTargetAudienceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)