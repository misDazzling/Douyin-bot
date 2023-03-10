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
from tencentcloud.wedata.v20210820 import models


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'


    def BatchCreateIntegrationTaskAlarms(self, request):
        """批量创建任务告警规则

        :param request: Request instance for BatchCreateIntegrationTaskAlarms.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchCreateIntegrationTaskAlarmsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchCreateIntegrationTaskAlarmsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchCreateIntegrationTaskAlarms", params, headers=headers)
            response = json.loads(body)
            model = models.BatchCreateIntegrationTaskAlarmsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeleteIntegrationTasks(self, request):
        """批量删除集成任务

        :param request: Request instance for BatchDeleteIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchDeleteTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量删除任务，仅对任务状态为”已停止“有效；

        :param request: Request instance for BatchDeleteTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchDeleteTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchDeleteTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.BatchDeleteTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchForceSuccessIntegrationTaskInstances(self, request):
        """批量置成功集成任务实例

        :param request: Request instance for BatchForceSuccessIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchForceSuccessIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchForceSuccessIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchForceSuccessIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchForceSuccessIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchKillIntegrationTaskInstances(self, request):
        """批量终止集成任务实例

        :param request: Request instance for BatchKillIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchKillIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchKillIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchKillIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchKillIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchMakeUpIntegrationTasks(self, request):
        """对集成离线任务执行批量补数据操作

        :param request: Request instance for BatchMakeUpIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchMakeUpIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchMakeUpIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchMakeUpIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchMakeUpIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchModifyOwnersNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量修改任务责任人

        :param request: Request instance for BatchModifyOwnersNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOwnersNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchModifyOwnersNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchModifyOwnersNew", params, headers=headers)
            response = json.loads(body)
            model = models.BatchModifyOwnersNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchRerunIntegrationTaskInstances(self, request):
        """批量重跑集成任务实例

        :param request: Request instance for BatchRerunIntegrationTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchRerunIntegrationTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchRerunIntegrationTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchRerunIntegrationTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.BatchRerunIntegrationTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchResumeIntegrationTasks(self, request):
        """批量继续执行集成实时任务

        :param request: Request instance for BatchResumeIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchResumeIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchResumeIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchResumeIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchResumeIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchStartIntegrationTasks(self, request):
        """批量运行集成任务

        :param request: Request instance for BatchStartIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStartIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStartIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStartIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStartIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchStopIntegrationTasks(self, request):
        """批量停止集成任务

        :param request: Request instance for BatchStopIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchStopTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        仅对任务状态为”调度中“和”已暂停“有效，对所选任务的任务实例进行终止，并停止调度

        :param request: Request instance for BatchStopTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchStopTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchStopTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchStopTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.BatchStopTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchSuspendIntegrationTasks(self, request):
        """批量暂停集成任务

        :param request: Request instance for BatchSuspendIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchSuspendIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchSuspendIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchSuspendIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchSuspendIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BatchUpdateIntegrationTasks(self, request):
        """批量更新集成任务（暂时仅支持批量更新责任人）

        :param request: Request instance for BatchUpdateIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.BatchUpdateIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BatchUpdateIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.BatchUpdateIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckAlarmRegularNameExist(self, request):
        """判断告警规则重名

        :param request: Request instance for CheckAlarmRegularNameExist.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckAlarmRegularNameExistRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckAlarmRegularNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAlarmRegularNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAlarmRegularNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckDuplicateRuleName(self, request):
        """检查规则名称是否重复

        :param request: Request instance for CheckDuplicateRuleName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateRuleNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateRuleNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDuplicateRuleName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDuplicateRuleNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckDuplicateTemplateName(self, request):
        """检查规则模板名称是否重复

        :param request: Request instance for CheckDuplicateTemplateName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateTemplateNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckDuplicateTemplateNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDuplicateTemplateName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDuplicateTemplateNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckIntegrationNodeNameExists(self, request):
        """判断集成节点名称是否存在

        :param request: Request instance for CheckIntegrationNodeNameExists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationNodeNameExistsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationNodeNameExistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntegrationNodeNameExists", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntegrationNodeNameExistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckIntegrationTaskNameExists(self, request):
        """判断集成任务名称是否存在

        :param request: Request instance for CheckIntegrationTaskNameExists.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationTaskNameExistsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckIntegrationTaskNameExistsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckIntegrationTaskNameExists", params, headers=headers)
            response = json.loads(body)
            model = models.CheckIntegrationTaskNameExistsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckTaskNameExist(self, request):
        """离线任务重名校验

        :param request: Request instance for CheckTaskNameExist.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CheckTaskNameExistResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTaskNameExist", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTaskNameExistResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommitExportTask(self, request):
        """提交数据导出任务

        :param request: Request instance for CommitExportTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitExportTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommitIntegrationTask(self, request):
        """提交集成任务

        :param request: Request instance for CommitIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommitRuleGroupExecResult(self, request):
        """Runner 规则检测结果上报

        :param request: Request instance for CommitRuleGroupExecResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupExecResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupExecResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitRuleGroupExecResult", params, headers=headers)
            response = json.loads(body)
            model = models.CommitRuleGroupExecResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CommitRuleGroupTask(self, request):
        """提交规则组运行任务接口

        :param request: Request instance for CommitRuleGroupTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CommitRuleGroupTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CommitRuleGroupTask", params, headers=headers)
            response = json.loads(body)
            model = models.CommitRuleGroupTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCustomFunction(self, request):
        """创建用户自定义函数

        :param request: Request instance for CreateCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDataSource(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建数据源

        :param request: Request instance for CreateDataSource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建文件夹

        :param request: Request instance for CreateFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFolder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHiveTable(self, request):
        """建hive表

        :param request: Request instance for CreateHiveTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHiveTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHiveTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHiveTableByDDL(self, request):
        """创建hive表，返回表名称

        :param request: Request instance for CreateHiveTableByDDL.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableByDDLRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateHiveTableByDDLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHiveTableByDDL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHiveTableByDDLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInLongAgent(self, request):
        """注册采集器

        :param request: Request instance for CreateInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIntegrationNode(self, request):
        """创建集成节点

        :param request: Request instance for CreateIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIntegrationTask(self, request):
        """创建集成任务

        :param request: Request instance for CreateIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOfflineTask(self, request):
        """创建离线任务

        :param request: Request instance for CreateOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateOrUpdateResource(self, request):
        """资源管理需要先将资源上传到cos中，然后调用该接口，将cos资源绑定到wedata

        :param request: Request instance for CreateOrUpdateResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateOrUpdateResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateOrUpdateResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateOrUpdateResource", params, headers=headers)
            response = json.loads(body)
            model = models.CreateOrUpdateResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateResourcePath(self, request):
        """文件路径的根目录为 /datastudio/resource，如果要在根目录下创建 aaa 文件夹，FilePath的值应该为 /datastudio/resource，如果根目录下已经创建了 aaa 文件夹，要在 aaa 下创建  bbb 文件夹，FilePath的值应该为 /datastudio/resource/aaa

        :param request: Request instance for CreateResourcePath.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateResourcePathRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateResourcePathResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourcePath", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourcePathResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRule(self, request):
        """创建质量规则接口

        :param request: Request instance for CreateRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRuleTemplate(self, request):
        """创建规则模版

        :param request: Request instance for CreateRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建任务

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTaskAlarmRegular(self, request):
        """创建任务告警规则

        :param request: Request instance for CreateTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        创建工作流

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCustomFunction(self, request):
        """删除用户自定义函数

        :param request: Request instance for DeleteCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDataSources(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除数据源

        :param request: Request instance for DeleteDataSources.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteDataSourcesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除文件夹

        :param request: Request instance for DeleteFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFolder", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteInLongAgent(self, request):
        """删除采集器

        :param request: Request instance for DeleteInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIntegrationNode(self, request):
        """删除集成节点

        :param request: Request instance for DeleteIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIntegrationTask(self, request):
        """删除集成任务

        :param request: Request instance for DeleteIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteOfflineTask(self, request):
        """删除任务

        :param request: Request instance for DeleteOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteResource(self, request):
        """资源管理删除资源

        :param request: Request instance for DeleteResource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteResourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResource", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRule(self, request):
        """删除质量规则接口

        :param request: Request instance for DeleteRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRuleTemplate(self, request):
        """删除规则模版

        :param request: Request instance for DeleteRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTaskAlarmRegular(self, request):
        """删除任务告警规则

        :param request: Request instance for DeleteTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWorkflowNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        删除工作流

        :param request: Request instance for DeleteWorkflowNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DeleteWorkflowNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkflowNew", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkflowNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmEvents(self, request):
        """告警事件列表

        :param request: Request instance for DescribeAlarmEvents.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmEventsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAlarmReceiver(self, request):
        """告警接收人详情

        :param request: Request instance for DescribeAlarmReceiver.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmReceiverRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeAlarmReceiverResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAlarmReceiver", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAlarmReceiverResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClusterNamespaceList(self, request):
        """获取集群命名空间列表

        :param request: Request instance for DescribeClusterNamespaceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeClusterNamespaceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeClusterNamespaceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterNamespaceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterNamespaceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataBases(self, request):
        """查询数据来源列表

        :param request: Request instance for DescribeDataBases.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataBasesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataBasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataBases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataBasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataCheckStat(self, request):
        """数据质量的概览页面数据监测情况接口

        :param request: Request instance for DescribeDataCheckStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataCheckStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataCheckStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataCheckStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataCheckStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataObjects(self, request):
        """查询规则组数据对象列表

        :param request: Request instance for DescribeDataObjects.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataObjectsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataSourceInfoList(self, request):
        """获取数据源信息-数据源分页列表

        :param request: Request instance for DescribeDataSourceInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataSourceList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        数据源详情

        :param request: Request instance for DescribeDataSourceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataSourceWithoutInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        数据源列表

        :param request: Request instance for DescribeDataSourceWithoutInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceWithoutInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataSourceWithoutInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataSourceWithoutInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataSourceWithoutInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataTypes(self, request):
        """获取字段类型列表

        :param request: Request instance for DescribeDataTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDataTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDataTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabaseInfoList(self, request):
        """获取数据库信息

        :param request: Request instance for DescribeDatabaseInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatabaseInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatasource(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        数据源详情

        :param request: Request instance for DescribeDatasource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDatasourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDatasourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasource", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDependTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        根据层级查找上/下游任务节点

        :param request: Request instance for DescribeDependTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDependTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDependTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDependTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDimensionScore(self, request):
        """质量报告-查询质量评分

        :param request: Request instance for DescribeDimensionScore.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeDimensionScoreRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeDimensionScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDimensionScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDimensionScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeExecStrategy(self, request):
        """查询规则组执行策略

        :param request: Request instance for DescribeExecStrategy.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeExecStrategyRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeExecStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeExecStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeExecStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFolderList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        拉取文件夹目录

        :param request: Request instance for DescribeFolderList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFolderListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFolderWorkflowList(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        拉取文件夹下的工作流

        :param request: Request instance for DescribeFolderWorkflowList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFolderWorkflowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFolderWorkflowList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFolderWorkflowListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFunctionKinds(self, request):
        """查询函数分类

        :param request: Request instance for DescribeFunctionKinds.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionKindsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionKindsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionKinds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionKindsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFunctionTypes(self, request):
        """查询函数类型

        :param request: Request instance for DescribeFunctionTypes.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionTypesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeFunctionTypesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFunctionTypes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFunctionTypesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInLongAgentList(self, request):
        """获取采集器列表

        :param request: Request instance for DescribeInLongAgentList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongAgentList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongAgentListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInLongAgentTaskList(self, request):
        """查询采集器关联的任务列表

        :param request: Request instance for DescribeInLongAgentTaskList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentTaskListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongAgentTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongAgentTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInLongAgentVpcList(self, request):
        """获取采集器所在集群的VPC列表

        :param request: Request instance for DescribeInLongAgentVpcList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentVpcListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongAgentVpcListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongAgentVpcList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongAgentVpcListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInLongTkeClusterList(self, request):
        """获取TKE集群列表

        :param request: Request instance for DescribeInLongTkeClusterList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongTkeClusterListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInLongTkeClusterListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInLongTkeClusterList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInLongTkeClusterListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceLastLog(self, request):
        """日志获取详情页面

        :param request: Request instance for DescribeInstanceLastLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLastLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLastLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLastLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLastLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceList(self, request):
        """获取实例列表

        :param request: Request instance for DescribeInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceLog(self, request):
        """获取实例运行日志

        :param request: Request instance for DescribeInstanceLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceLogList(self, request):
        """离线任务实例运行日志列表

        :param request: Request instance for DescribeInstanceLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstanceLogs(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        获取实例日志列表

        :param request: Request instance for DescribeInstanceLogs.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstanceLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeInstances(self, request):
        """数据质量，查询调度任务的实例列表

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationNode(self, request):
        """查询集成节点

        :param request: Request instance for DescribeIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationStatistics(self, request):
        """数据集成大屏概览

        :param request: Request instance for DescribeIntegrationStatistics.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationStatisticsAgentStatus(self, request):
        """数据集成大屏采集器状态分布统计

        :param request: Request instance for DescribeIntegrationStatisticsAgentStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsAgentStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsAgentStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsAgentStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsAgentStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationStatisticsInstanceTrend(self, request):
        """数据集成大屏实例状态统计趋势

        :param request: Request instance for DescribeIntegrationStatisticsInstanceTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsInstanceTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsInstanceTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsInstanceTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsInstanceTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationStatisticsRecordsTrend(self, request):
        """数据集成大屏同步条数统计趋势

        :param request: Request instance for DescribeIntegrationStatisticsRecordsTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRecordsTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsRecordsTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsRecordsTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsRecordsTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationStatisticsTaskStatus(self, request):
        """数据集成大屏任务状态分布统计

        :param request: Request instance for DescribeIntegrationStatisticsTaskStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationStatisticsTaskStatusTrend(self, request):
        """数据集成大屏任务状态统计趋势

        :param request: Request instance for DescribeIntegrationStatisticsTaskStatusTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationStatisticsTaskStatusTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationStatisticsTaskStatusTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationStatisticsTaskStatusTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationTask(self, request):
        """查询集成任务

        :param request: Request instance for DescribeIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationTasks(self, request):
        """查询集成任务列表

        :param request: Request instance for DescribeIntegrationTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIntegrationVersionNodesInfo(self, request):
        """查询集成任务版本节点信息

        :param request: Request instance for DescribeIntegrationVersionNodesInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationVersionNodesInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeIntegrationVersionNodesInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIntegrationVersionNodesInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIntegrationVersionNodesInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKafkaTopicInfo(self, request):
        """获取kafka的topic信息

        :param request: Request instance for DescribeKafkaTopicInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeKafkaTopicInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeKafkaTopicInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKafkaTopicInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKafkaTopicInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMonitorsByPage(self, request):
        """分页查询质量监控组

        :param request: Request instance for DescribeMonitorsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeMonitorsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeMonitorsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMonitorsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMonitorsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOfflineTaskToken(self, request):
        """获取离线任务长连接Token

        :param request: Request instance for DescribeOfflineTaskToken.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOfflineTaskTokenRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOfflineTaskTokenResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOfflineTaskToken", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOfflineTaskTokenResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrganizationalFunctions(self, request):
        """查询全量函数

        :param request: Request instance for DescribeOrganizationalFunctions.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeOrganizationalFunctionsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeOrganizationalFunctionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrganizationalFunctions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrganizationalFunctionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProdTasks(self, request):
        """数据质量获取生产调度任务列表

        :param request: Request instance for DescribeProdTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProdTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProdTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProdTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProdTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProject(self, request):
        """获取项目信息

        :param request: Request instance for DescribeProject.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProject", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeQualityScore(self, request):
        """质量报告-质量评分

        :param request: Request instance for DescribeQualityScore.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityScore", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeQualityScoreTrend(self, request):
        """质量报告-质量分周期趋势

        :param request: Request instance for DescribeQualityScoreTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeQualityScoreTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeQualityScoreTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeQualityScoreTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealTimeTaskInstanceNodeInfo(self, request):
        """查询实时任务实例节点信息

        :param request: Request instance for DescribeRealTimeTaskInstanceNodeInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealTimeTaskMetricOverview(self, request):
        """实时任务运行指标概览

        :param request: Request instance for DescribeRealTimeTaskMetricOverview.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskMetricOverviewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskMetricOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskMetricOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskMetricOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRealTimeTaskSpeed(self, request):
        """实时任务同步速度趋势

        :param request: Request instance for DescribeRealTimeTaskSpeed.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskSpeedRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRealTimeTaskSpeedResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRealTimeTaskSpeed", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRealTimeTaskSpeedResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRelatedInstances(self, request):
        """查询任务实例的关联实例列表

        :param request: Request instance for DescribeRelatedInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRelatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRelatedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRelatedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceManagePathTrees(self, request):
        """获取资源管理目录树

        :param request: Request instance for DescribeResourceManagePathTrees.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeResourceManagePathTreesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeResourceManagePathTreesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceManagePathTrees", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceManagePathTreesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRule(self, request):
        """查询规则详情

        :param request: Request instance for DescribeRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRule", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleDataSources(self, request):
        """查询质量规则数据源

        :param request: Request instance for DescribeRuleDataSources.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDataSourcesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDataSourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleDataSources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleDataSourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleDimStat(self, request):
        """数据质量概览页面触发维度分布统计接口

        :param request: Request instance for DescribeRuleDimStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDimStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleDimStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleDimStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleDimStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecDetail(self, request):
        """查询规则执行结果详情

        :param request: Request instance for DescribeRuleExecDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecExportResult(self, request):
        """查询规则执行导出结果

        :param request: Request instance for DescribeRuleExecExportResult.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecExportResultRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecExportResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecExportResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecExportResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecHistory(self, request):
        """查询规则执行历史， 最近30条

        :param request: Request instance for DescribeRuleExecHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecLog(self, request):
        """规则执行日志查询

        :param request: Request instance for DescribeRuleExecLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecResults(self, request):
        """规则执行结果列表查询

        :param request: Request instance for DescribeRuleExecResults.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecResults", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecResultsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecResultsByPage(self, request):
        """分页查询规则执行结果列表

        :param request: Request instance for DescribeRuleExecResultsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecResultsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecResultsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecResultsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleExecStat(self, request):
        """数据质量概览页面规则运行情况接口

        :param request: Request instance for DescribeRuleExecStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleExecStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleExecStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleExecStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleGroup(self, request):
        """查询规则组详情接口

        :param request: Request instance for DescribeRuleGroup.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleGroupExecResultsByPage(self, request):
        """规则组执行结果分页查询接口

        :param request: Request instance for DescribeRuleGroupExecResultsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupExecResultsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupExecResultsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleGroupExecResultsByPageWithoutAuth(self, request):
        """规则组执行结果分页查询接口不带鉴权

        :param request: Request instance for DescribeRuleGroupExecResultsByPageWithoutAuth.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageWithoutAuthRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupExecResultsByPageWithoutAuthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupExecResultsByPageWithoutAuth", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupExecResultsByPageWithoutAuthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleGroupSubscription(self, request):
        """查询规则组订阅信息

        :param request: Request instance for DescribeRuleGroupSubscription.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupSubscriptionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleGroupTable(self, request):
        """查询表绑定执行规则组信息

        :param request: Request instance for DescribeRuleGroupTable.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupTableRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleGroupsByPage(self, request):
        """【过滤条件】
        {表名称TableName,支持模糊匹配}       {表负责人TableOwnerName,支持模糊匹配}      {监控方式MonitorTypes，1.未配置 2.关联生产调度 3.离线周期检测,支持多选}  {订阅人ReceiverUin}
        【必要字段】
        {数据来源DatasourceId}

        :param request: Request instance for DescribeRuleGroupsByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupsByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleGroupsByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleGroupsByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleGroupsByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleHistoryByPage(self, request):
        """过滤条件【必要字段】{ruleId}

        :param request: Request instance for DescribeRuleHistoryByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleHistoryByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleHistoryByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleHistoryByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleHistoryByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleTablesByPage(self, request):
        """获取表列表

        :param request: Request instance for DescribeRuleTablesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTablesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTablesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTablesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTablesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleTemplate(self, request):
        """查询模板详情

        :param request: Request instance for DescribeRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleTemplates(self, request):
        """查询规则模版列表

        :param request: Request instance for DescribeRuleTemplates.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRuleTemplatesByPage(self, request):
        """过滤条件】 {模版名称Name,支持模糊匹配} {模版类型type，1.系统模版 2.自定义模版} {质量检测维度QualityDims, 1.准确性 2.唯一性 3.完整性 4.一致性 5.及时性 6.有效性} 【排序字段】 { 引用数排序类型CitationOrderType，根据引用数量排序 ASC DESC}

        :param request: Request instance for DescribeRuleTemplatesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRuleTemplatesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRuleTemplatesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRuleTemplatesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRules(self, request):
        """查询质量规则列表

        :param request: Request instance for DescribeRules.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRulesByPage(self, request):
        """分页查询质量规则

        :param request: Request instance for DescribeRulesByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeRulesByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRulesByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRulesByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStandardRuleDetailInfoList(self, request):
        """获取数据标准规则详情

        :param request: Request instance for DescribeStandardRuleDetailInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStandardRuleDetailInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStandardRuleDetailInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStandardRuleDetailInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStandardRuleDetailInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStreamTaskLogList(self, request):
        """查询实时任务日志列表

        :param request: Request instance for DescribeStreamTaskLogList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeStreamTaskLogListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeStreamTaskLogListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStreamTaskLogList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStreamTaskLogListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableInfoList(self, request):
        """获取数据表信息

        :param request: Request instance for DescribeTableInfoList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableInfoListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableInfoListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableInfoList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableInfoListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableQualityDetails(self, request):
        """质量报告-查询表质量详情

        :param request: Request instance for DescribeTableQualityDetails.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableQualityDetailsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableQualityDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableQualityDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableQualityDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableSchemaInfo(self, request):
        """获取表schema信息

        :param request: Request instance for DescribeTableSchemaInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableSchemaInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableSchemaInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableSchemaInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableSchemaInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTableScoreTrend(self, request):
        """查询表得分趋势

        :param request: Request instance for DescribeTableScoreTrend.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTableScoreTrendRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTableScoreTrendResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTableScoreTrend", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableScoreTrendResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskAlarmRegulations(self, request):
        """查询任务告警规则列表

        :param request: Request instance for DescribeTaskAlarmRegulations.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskAlarmRegulationsRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskAlarmRegulationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskAlarmRegulations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskAlarmRegulationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskDetail(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        查询任务具体详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskInstance(self, request):
        """离线任务实例详情

        :param request: Request instance for DescribeTaskInstance.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskInstanceReportDetail(self, request):
        """离线任务实例统计明细

        :param request: Request instance for DescribeTaskInstanceReportDetail.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceReportDetailRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstanceReportDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstanceReportDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInstanceReportDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskInstances(self, request):
        """查询任务实例列表

        :param request: Request instance for DescribeTaskInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskLockStatus(self, request):
        """查看任务锁状态信息

        :param request: Request instance for DescribeTaskLockStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLockStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskLockStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLockStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLockStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskReport(self, request):
        """按起止日期统计离线任务的所有实例的运行指标总和

        :param request: Request instance for DescribeTaskReport.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskReport", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskReportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskReportDetailList(self, request):
        """离线任务周期统计明细

        :param request: Request instance for DescribeTaskReportDetailList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportDetailListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskReportDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskReportDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskReportDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskScript(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        查询任务脚本

        :param request: Request instance for DescribeTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasksByPage(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        根据工作流分页查询任务

        :param request: Request instance for DescribeTasksByPage.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksByPageRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTasksByPageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksByPage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksByPageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplateDimCount(self, request):
        """查询规则模版维度分布情况

        :param request: Request instance for DescribeTemplateDimCount.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateDimCountRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateDimCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateDimCount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateDimCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplateHistory(self, request):
        """查询规则模版操作记录

        :param request: Request instance for DescribeTemplateHistory.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateHistoryRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTemplateHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateHistory", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTopTableStat(self, request):
        """数据质量概览页面表排行接口

        :param request: Request instance for DescribeTopTableStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTopTableStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTopTableStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTopTableStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTopTableStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTrendStat(self, request):
        """数据质量概览页面趋势变化接口

        :param request: Request instance for DescribeTrendStat.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DescribeTrendStatRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DescribeTrendStatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrendStat", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrendStatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DryRunDIOfflineTask(self, request):
        """调试运行集成任务

        :param request: Request instance for DryRunDIOfflineTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.DryRunDIOfflineTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.DryRunDIOfflineTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DryRunDIOfflineTask", params, headers=headers)
            response = json.loads(body)
            model = models.DryRunDIOfflineTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ForceSucInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量置成功

        :param request: Request instance for ForceSucInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ForceSucInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ForceSucInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ForceSucInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ForceSucInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FreezeTasks(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        批量冻结任务

        :param request: Request instance for FreezeTasks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def FreezeTasksByMultiWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        基于多个工作流进行批量冻结任务操作

        :param request: Request instance for FreezeTasksByMultiWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByMultiWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.FreezeTasksByMultiWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FreezeTasksByMultiWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.FreezeTasksByMultiWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenHiveTableDDLSql(self, request):
        """生成建hive表的sql

        :param request: Request instance for GenHiveTableDDLSql.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GenHiveTableDDLSqlRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GenHiveTableDDLSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenHiveTableDDLSql", params, headers=headers)
            response = json.loads(body)
            model = models.GenHiveTableDDLSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetIntegrationNodeColumnSchema(self, request):
        """提取数据集成节点字段Schema

        :param request: Request instance for GetIntegrationNodeColumnSchema.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetIntegrationNodeColumnSchemaRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetIntegrationNodeColumnSchemaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetIntegrationNodeColumnSchema", params, headers=headers)
            response = json.loads(body)
            model = models.GetIntegrationNodeColumnSchemaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetOfflineDIInstanceList(self, request):
        """获取离线任务实例列表(新)

        :param request: Request instance for GetOfflineDIInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetOfflineDIInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetOfflineDIInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOfflineDIInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetOfflineDIInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetOfflineInstanceList(self, request):
        """获取离线任务实例

        :param request: Request instance for GetOfflineInstanceList.
        :type request: :class:`tencentcloud.wedata.v20210820.models.GetOfflineInstanceListRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.GetOfflineInstanceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOfflineInstanceList", params, headers=headers)
            response = json.loads(body)
            model = models.GetOfflineInstanceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def KillInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量终止操作

        :param request: Request instance for KillInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.KillInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.KillInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillInstances", params, headers=headers)
            response = json.loads(body)
            model = models.KillInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LockIntegrationTask(self, request):
        """锁定集成任务

        :param request: Request instance for LockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.LockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.LockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.LockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MakeUpTasksNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        任务批量补录，调度状态任务才可以补录；



        :param request: Request instance for MakeUpTasksNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpTasksNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpTasksNew", params, headers=headers)
            response = json.loads(body)
            model = models.MakeUpTasksNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MakeUpWorkflowNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        工作流下所有任务的补录

        :param request: Request instance for MakeUpWorkflowNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.MakeUpWorkflowNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.MakeUpWorkflowNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MakeUpWorkflowNew", params, headers=headers)
            response = json.loads(body)
            model = models.MakeUpWorkflowNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDataSource(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        修改数据源

        :param request: Request instance for ModifyDataSource.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDataSourceRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDataSourceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataSource", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataSourceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDimensionWeight(self, request):
        """质量报告-修改维度权限

        :param request: Request instance for ModifyDimensionWeight.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyDimensionWeightRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyDimensionWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDimensionWeight", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDimensionWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyExecStrategy(self, request):
        """更新规则组执行策略

        :param request: Request instance for ModifyExecStrategy.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyExecStrategyRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyExecStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyExecStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyExecStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFolder(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        文件夹更新

        :param request: Request instance for ModifyFolder.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyFolderRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyFolderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFolder", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFolderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIntegrationNode(self, request):
        """更新集成节点

        :param request: Request instance for ModifyIntegrationNode.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationNodeRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationNodeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntegrationNode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntegrationNodeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIntegrationTask(self, request):
        """更新集成任务

        :param request: Request instance for ModifyIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMonitorStatus(self, request):
        """更新监控状态

        :param request: Request instance for ModifyMonitorStatus.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyMonitorStatusRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyMonitorStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMonitorStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMonitorStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRule(self, request):
        """更新质量规则接口

        :param request: Request instance for ModifyRule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRuleGroupSubscription(self, request):
        """更新规则组订阅信息

        :param request: Request instance for ModifyRuleGroupSubscription.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleGroupSubscriptionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleGroupSubscriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleGroupSubscription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleGroupSubscriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRuleTemplate(self, request):
        """编辑规则模版

        :param request: Request instance for ModifyRuleTemplate.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleTemplateRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyRuleTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRuleTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRuleTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskAlarmRegular(self, request):
        """修改任务告警规则

        :param request: Request instance for ModifyTaskAlarmRegular.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskAlarmRegularRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskAlarmRegularResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskAlarmRegular", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskAlarmRegularResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新任务

        :param request: Request instance for ModifyTaskInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskLinks(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        添加父任务依赖

        :param request: Request instance for ModifyTaskLinks.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskLinksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskLinks", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskLinksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskName(self, request):
        """重命名任务（任务编辑）

        :param request: Request instance for ModifyTaskName.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskNameRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTaskScript(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        修改任务脚本

        :param request: Request instance for ModifyTaskScript.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyTaskScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTaskScript", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTaskScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWorkflowInfo(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新工作流

        :param request: Request instance for ModifyWorkflowInfo.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowInfo", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkflowInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWorkflowSchedule(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        更新工作流调度

        :param request: Request instance for ModifyWorkflowSchedule.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ModifyWorkflowScheduleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkflowSchedule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkflowScheduleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterEvent(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        注册事件

        :param request: Request instance for RegisterEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEvent", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RegisterEventListener(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        注册事件监听器

        :param request: Request instance for RegisterEventListener.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RegisterEventListenerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterEventListener", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterEventListenerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RerunInstances(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        实例批量重跑

        :param request: Request instance for RerunInstances.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RerunInstancesRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RerunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RerunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartInLongAgent(self, request):
        """重启采集器

        :param request: Request instance for RestartInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RestartInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RestartInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResumeIntegrationTask(self, request):
        """继续集成任务

        :param request: Request instance for ResumeIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.ResumeIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.ResumeIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RobAndLockIntegrationTask(self, request):
        """抢占锁定集成任务

        :param request: Request instance for RobAndLockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RobAndLockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RobAndLockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RobAndLockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.RobAndLockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        运行任务

        :param request: Request instance for RunTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.RunTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.RunTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunTask", params, headers=headers)
            response = json.loads(body)
            model = models.RunTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SaveCustomFunction(self, request):
        """保存用户自定义函数

        :param request: Request instance for SaveCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SaveCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SaveCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SaveCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.SaveCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetTaskAlarmNew(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        设置任务告警，新建/更新告警信息（最新）

        :param request: Request instance for SetTaskAlarmNew.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SetTaskAlarmNewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetTaskAlarmNew", params, headers=headers)
            response = json.loads(body)
            model = models.SetTaskAlarmNewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartIntegrationTask(self, request):
        """启动集成任务

        :param request: Request instance for StartIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StartIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StartIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StartIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopIntegrationTask(self, request):
        """停止集成任务

        :param request: Request instance for StopIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.StopIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.StopIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitCustomFunction(self, request):
        """提交自定义函数

        :param request: Request instance for SubmitCustomFunction.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitCustomFunctionRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitCustomFunctionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitCustomFunction", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitCustomFunctionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitTask(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        提交任务

        :param request: Request instance for SubmitTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTask", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SubmitWorkflow(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        提交工作流

        :param request: Request instance for SubmitWorkflow.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SubmitWorkflowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitWorkflow", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitWorkflowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SuspendIntegrationTask(self, request):
        """暂停集成任务

        :param request: Request instance for SuspendIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.SuspendIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.SuspendIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SuspendIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.SuspendIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TaskLog(self, request):
        """查询Inlong manager日志

        :param request: Request instance for TaskLog.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TaskLogRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TaskLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TaskLog", params, headers=headers)
            response = json.loads(body)
            model = models.TaskLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TriggerEvent(self, request):
        """<p style="color:red;">[注意：该Beta版本只满足广州区部分白名单客户使用]</p>
        触发事件

        :param request: Request instance for TriggerEvent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.TriggerEventRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.TriggerEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TriggerEvent", params, headers=headers)
            response = json.loads(body)
            model = models.TriggerEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnlockIntegrationTask(self, request):
        """解锁集成任务

        :param request: Request instance for UnlockIntegrationTask.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UnlockIntegrationTaskRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UnlockIntegrationTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockIntegrationTask", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockIntegrationTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateInLongAgent(self, request):
        """更新采集器

        :param request: Request instance for UpdateInLongAgent.
        :type request: :class:`tencentcloud.wedata.v20210820.models.UpdateInLongAgentRequest`
        :rtype: :class:`tencentcloud.wedata.v20210820.models.UpdateInLongAgentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateInLongAgent", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateInLongAgentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)