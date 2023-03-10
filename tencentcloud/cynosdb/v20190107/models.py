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


class Ability(AbstractModel):
    """集群支持的功能

    """

    def __init__(self):
        r"""
        :param IsSupportSlaveZone: 是否支持从可用区
        :type IsSupportSlaveZone: str
        :param NonsupportSlaveZoneReason: 不支持从可用区的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type NonsupportSlaveZoneReason: str
        :param IsSupportRo: 是否支持RO实例
        :type IsSupportRo: str
        :param NonsupportRoReason: 不支持RO实例的原因
注意：此字段可能返回 null，表示取不到有效值。
        :type NonsupportRoReason: str
        """
        self.IsSupportSlaveZone = None
        self.NonsupportSlaveZoneReason = None
        self.IsSupportRo = None
        self.NonsupportRoReason = None


    def _deserialize(self, params):
        self.IsSupportSlaveZone = params.get("IsSupportSlaveZone")
        self.NonsupportSlaveZoneReason = params.get("NonsupportSlaveZoneReason")
        self.IsSupportRo = params.get("IsSupportRo")
        self.NonsupportRoReason = params.get("NonsupportRoReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Account(AbstractModel):
    """数据库账号信息

    """

    def __init__(self):
        r"""
        :param AccountName: 数据库账号名
        :type AccountName: str
        :param Description: 数据库账号描述
        :type Description: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Host: 主机
        :type Host: str
        :param MaxUserConnections: 用户最大连接数
        :type MaxUserConnections: int
        """
        self.AccountName = None
        self.Description = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Host = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.Host = params.get("Host")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountParam(AbstractModel):
    """账号参数

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名称，当前仅支持参数：max_user_connections
        :type ParamName: str
        :param ParamValue: 参数值
        :type ParamValue: str
        """
        self.ParamName = None
        self.ParamValue = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.ParamValue = params.get("ParamValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceRequest(AbstractModel):
    """ActivateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 实例 ID 列表，单个实例 ID 格式如：cynosdbmysql-ins-n7ocdslw，与TDSQL-C MySQL数据库控制台页面中显示的实例 ID 相同，可使用 查询实例列表 接口获取，其值为输出参数中字段 InstanceId 的值。
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateInstanceResponse(AbstractModel):
    """ActivateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class AddClusterSlaveZoneRequest(AbstractModel):
    """AddClusterSlaveZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SlaveZone: 从可用区
        :type SlaveZone: str
        """
        self.ClusterId = None
        self.SlaveZone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddClusterSlaveZoneResponse(AbstractModel):
    """AddClusterSlaveZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步FlowId
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class AddInstancesRequest(AbstractModel):
    """AddInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Cpu: Cpu核数
        :type Cpu: int
        :param Memory: 内存，单位为GB
        :type Memory: int
        :param ReadOnlyCount: 新增只读实例数，取值范围为[0,4]
        :type ReadOnlyCount: int
        :param InstanceGrpId: 实例组ID，在已有RO组中新增实例时使用，不传则新增RO组。当前版本不建议传输该值。
        :type InstanceGrpId: str
        :param VpcId: 所属VPC网络ID，该参数已废弃
        :type VpcId: str
        :param SubnetId: 所属子网ID，如果设置了VpcId，则SubnetId必填。该参数已废弃。
        :type SubnetId: str
        :param Port: 新增RO组时使用的Port，取值范围为[0,65535)
        :type Port: int
        :param InstanceName: 实例名称，字符串长度范围为[0,64)，取值范围为大小写字母，0-9数字，'_','-','.'
        :type InstanceName: str
        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param OrderSource: 订单来源，字符串长度范围为[0,64)
        :type OrderSource: str
        :param DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        :param ParamTemplateId: 参数模版ID
        :type ParamTemplateId: int
        :param InstanceParams: 参数列表，ParamTemplateId 传入时InstanceParams才有效
        :type InstanceParams: list of ModifyParamItem
        """
        self.ClusterId = None
        self.Cpu = None
        self.Memory = None
        self.ReadOnlyCount = None
        self.InstanceGrpId = None
        self.VpcId = None
        self.SubnetId = None
        self.Port = None
        self.InstanceName = None
        self.AutoVoucher = None
        self.DbType = None
        self.OrderSource = None
        self.DealMode = None
        self.ParamTemplateId = None
        self.InstanceParams = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.ReadOnlyCount = params.get("ReadOnlyCount")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Port = params.get("Port")
        self.InstanceName = params.get("InstanceName")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
        self.OrderSource = params.get("OrderSource")
        self.DealMode = params.get("DealMode")
        self.ParamTemplateId = params.get("ParamTemplateId")
        if params.get("InstanceParams") is not None:
            self.InstanceParams = []
            for item in params.get("InstanceParams"):
                obj = ModifyParamItem()
                obj._deserialize(item)
                self.InstanceParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddInstancesResponse(AbstractModel):
    """AddInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TranId: 冻结流水，一次开通一个冻结流水。
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param DealNames: 后付费订单号。
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param ResourceIds: 发货资源id列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.DealNames = None
        self.ResourceIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")


class Addr(AbstractModel):
    """数据库地址

    """

    def __init__(self):
        r"""
        :param IP: IP
        :type IP: str
        :param Port: 端口
        :type Port: int
        """
        self.IP = None
        self.Port = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例组ID数组
        :type InstanceIds: list of str
        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组Id组成的数组。
        :type SecurityGroupIds: list of str
        :param Zone: 可用区
        :type Zone: str
        """
        self.InstanceIds = None
        self.SecurityGroupIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AuditLog(AbstractModel):
    """审计日志详细信息

    """

    def __init__(self):
        r"""
        :param AffectRows: 影响行数。
        :type AffectRows: int
        :param ErrCode: 错误码。
        :type ErrCode: int
        :param SqlType: SQL类型。
        :type SqlType: str
        :param TableName: 表名称。
        :type TableName: str
        :param InstanceName: 实例名称。
        :type InstanceName: str
        :param PolicyName: 审计策略名称。
        :type PolicyName: str
        :param DBName: 数据库名称。
        :type DBName: str
        :param Sql: SQL语句。
        :type Sql: str
        :param Host: 客户端地址。
        :type Host: str
        :param User: 用户名。
        :type User: str
        :param ExecTime: 执行时间。
        :type ExecTime: int
        :param Timestamp: 时间戳。
        :type Timestamp: str
        :param SentRows: 发送行数。
        :type SentRows: int
        :param ThreadId: 执行线程ID。
        :type ThreadId: int
        """
        self.AffectRows = None
        self.ErrCode = None
        self.SqlType = None
        self.TableName = None
        self.InstanceName = None
        self.PolicyName = None
        self.DBName = None
        self.Sql = None
        self.Host = None
        self.User = None
        self.ExecTime = None
        self.Timestamp = None
        self.SentRows = None
        self.ThreadId = None


    def _deserialize(self, params):
        self.AffectRows = params.get("AffectRows")
        self.ErrCode = params.get("ErrCode")
        self.SqlType = params.get("SqlType")
        self.TableName = params.get("TableName")
        self.InstanceName = params.get("InstanceName")
        self.PolicyName = params.get("PolicyName")
        self.DBName = params.get("DBName")
        self.Sql = params.get("Sql")
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.ExecTime = params.get("ExecTime")
        self.Timestamp = params.get("Timestamp")
        self.SentRows = params.get("SentRows")
        self.ThreadId = params.get("ThreadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFile(AbstractModel):
    """审计日志文件

    """

    def __init__(self):
        r"""
        :param FileName: 审计日志文件名称
        :type FileName: str
        :param CreateTime: 审计日志文件创建时间。格式为 : "2019-03-20 17:09:13"。
        :type CreateTime: str
        :param Status: 文件状态值。可能返回的值为：
"creating" - 生成中;
"failed" - 创建失败;
"success" - 已生成;
        :type Status: str
        :param FileSize: 文件大小，单位为 KB。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        :param DownloadUrl: 审计日志下载地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param ErrMsg: 错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        """
        self.FileName = None
        self.CreateTime = None
        self.Status = None
        self.FileSize = None
        self.DownloadUrl = None
        self.ErrMsg = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.FileSize = params.get("FileSize")
        self.DownloadUrl = params.get("DownloadUrl")
        self.ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogFilter(AbstractModel):
    """审计日志过滤条件。查询审计日志时，用户过滤返回的审计日志。

    """

    def __init__(self):
        r"""
        :param Host: 客户端地址。
        :type Host: list of str
        :param User: 用户名。
        :type User: list of str
        :param DBName: 数据库名称。
        :type DBName: list of str
        :param TableName: 表名称。
        :type TableName: list of str
        :param PolicyName: 审计策略名称。
        :type PolicyName: list of str
        :param Sql: SQL 语句。支持模糊匹配。
        :type Sql: str
        :param SqlType: SQL 类型。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlType: str
        :param ExecTime: 执行时间。单位为：ms。表示筛选执行时间大于该值的审计日志。
        :type ExecTime: int
        :param AffectRows: 影响行数。表示筛选影响行数大于该值的审计日志。
        :type AffectRows: int
        :param SqlTypes: SQL 类型。支持多个类型同时查询。目前支持："SELECT", "INSERT", "UPDATE", "DELETE", "CREATE", "DROP", "ALTER", "SET", "REPLACE", "EXECUTE"。
        :type SqlTypes: list of str
        :param Sqls: SQL 语句。支持传递多个sql语句。
        :type Sqls: list of str
        :param SentRows: 返回行数。
        :type SentRows: int
        :param ThreadId: 线程ID。
        :type ThreadId: list of str
        """
        self.Host = None
        self.User = None
        self.DBName = None
        self.TableName = None
        self.PolicyName = None
        self.Sql = None
        self.SqlType = None
        self.ExecTime = None
        self.AffectRows = None
        self.SqlTypes = None
        self.Sqls = None
        self.SentRows = None
        self.ThreadId = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.User = params.get("User")
        self.DBName = params.get("DBName")
        self.TableName = params.get("TableName")
        self.PolicyName = params.get("PolicyName")
        self.Sql = params.get("Sql")
        self.SqlType = params.get("SqlType")
        self.ExecTime = params.get("ExecTime")
        self.AffectRows = params.get("AffectRows")
        self.SqlTypes = params.get("SqlTypes")
        self.Sqls = params.get("Sqls")
        self.SentRows = params.get("SentRows")
        self.ThreadId = params.get("ThreadId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleFilters(AbstractModel):
    """规则审计的过滤条件

    """

    def __init__(self):
        r"""
        :param RuleFilters: 单条审计规则。
        :type RuleFilters: list of RuleFilters
        """
        self.RuleFilters = None


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditRuleTemplateInfo(AbstractModel):
    """审计规则模版的详情

    """

    def __init__(self):
        r"""
        :param RuleTemplateId: 规则模版ID。
        :type RuleTemplateId: str
        :param RuleTemplateName: 规则模版名称。
        :type RuleTemplateName: str
        :param RuleFilters: 规则模版的过滤条件
        :type RuleFilters: list of RuleFilters
        :param Description: 规则模版描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreateAt: 规则模版创建时间。
        :type CreateAt: str
        """
        self.RuleTemplateId = None
        self.RuleTemplateName = None
        self.RuleFilters = None
        self.Description = None
        self.CreateAt = None


    def _deserialize(self, params):
        self.RuleTemplateId = params.get("RuleTemplateId")
        self.RuleTemplateName = params.get("RuleTemplateName")
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        self.Description = params.get("Description")
        self.CreateAt = params.get("CreateAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BackupFileInfo(AbstractModel):
    """备份文件信息

    """

    def __init__(self):
        r"""
        :param SnapshotId: 快照文件ID，已废弃，请使用BackupId
        :type SnapshotId: int
        :param FileName: 备份文件名
        :type FileName: str
        :param FileSize: 备份文件大小
        :type FileSize: int
        :param StartTime: 备份开始时间
        :type StartTime: str
        :param FinishTime: 备份完成时间
        :type FinishTime: str
        :param BackupType: 备份类型：snapshot，快照备份；logic，逻辑备份
        :type BackupType: str
        :param BackupMethod: 备份方式：auto，自动备份；manual，手动备份
        :type BackupMethod: str
        :param BackupStatus: 备份文件状态：success：备份成功；fail：备份失败；creating：备份文件创建中；deleting：备份文件删除中
        :type BackupStatus: str
        :param SnapshotTime: 备份文件时间
        :type SnapshotTime: str
        :param BackupId: 备份ID
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupId: int
        :param SnapShotType: 快照类型，可选值：full，全量；increment，增量
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapShotType: str
        :param BackupName: 备份文件备注
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupName: str
        """
        self.SnapshotId = None
        self.FileName = None
        self.FileSize = None
        self.StartTime = None
        self.FinishTime = None
        self.BackupType = None
        self.BackupMethod = None
        self.BackupStatus = None
        self.SnapshotTime = None
        self.BackupId = None
        self.SnapShotType = None
        self.BackupName = None


    def _deserialize(self, params):
        self.SnapshotId = params.get("SnapshotId")
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.BackupType = params.get("BackupType")
        self.BackupMethod = params.get("BackupMethod")
        self.BackupStatus = params.get("BackupStatus")
        self.SnapshotTime = params.get("SnapshotTime")
        self.BackupId = params.get("BackupId")
        self.SnapShotType = params.get("SnapShotType")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BillingResourceInfo(AbstractModel):
    """计费资源信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param DealName: 订单ID
        :type DealName: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.DealName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.DealName = params.get("DealName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BinlogItem(AbstractModel):
    """Binlog描述

    """

    def __init__(self):
        r"""
        :param FileName: Binlog文件名称
        :type FileName: str
        :param FileSize: 文件大小，单位：字节
        :type FileSize: int
        :param StartTime: 事务最早时间
        :type StartTime: str
        :param FinishTime: 事务最晚时间
        :type FinishTime: str
        :param BinlogId: Binlog文件ID
        :type BinlogId: int
        """
        self.FileName = None
        self.FileSize = None
        self.StartTime = None
        self.FinishTime = None
        self.BinlogId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.FileSize = params.get("FileSize")
        self.StartTime = params.get("StartTime")
        self.FinishTime = params.get("FinishTime")
        self.BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAuditServiceRequest(AbstractModel):
    """CloseAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseAuditServiceResponse(AbstractModel):
    """CloseAuditService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ClusterInstanceDetail(AbstractModel):
    """集群实例信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param InstanceType: 引擎类型
        :type InstanceType: str
        :param InstanceStatus: 实例状态
        :type InstanceStatus: str
        :param InstanceStatusDesc: 实例状态描述
        :type InstanceStatusDesc: str
        :param InstanceCpu: cpu核数
        :type InstanceCpu: int
        :param InstanceMemory: 内存
        :type InstanceMemory: int
        :param InstanceStorage: 硬盘
        :type InstanceStorage: int
        :param InstanceRole: 实例角色
        :type InstanceRole: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceType = None
        self.InstanceStatus = None
        self.InstanceStatusDesc = None
        self.InstanceCpu = None
        self.InstanceMemory = None
        self.InstanceStorage = None
        self.InstanceRole = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceType = params.get("InstanceType")
        self.InstanceStatus = params.get("InstanceStatus")
        self.InstanceStatusDesc = params.get("InstanceStatusDesc")
        self.InstanceCpu = params.get("InstanceCpu")
        self.InstanceMemory = params.get("InstanceMemory")
        self.InstanceStorage = params.get("InstanceStorage")
        self.InstanceRole = params.get("InstanceRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClusterParamModifyLog(AbstractModel):
    """参数修改记录

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名称
        :type ParamName: str
        :param CurrentValue: 当前值
        :type CurrentValue: str
        :param UpdateValue: 修改后的值
        :type UpdateValue: str
        :param Status: 修改状态
        :type Status: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.ParamName = None
        self.CurrentValue = None
        self.UpdateValue = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ClusterId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.CurrentValue = params.get("CurrentValue")
        self.UpdateValue = params.get("UpdateValue")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ClusterId = params.get("ClusterId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsRequest(AbstractModel):
    """CreateAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Accounts: 新账户列表
        :type Accounts: list of NewAccount
        """
        self.ClusterId = None
        self.Accounts = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Accounts") is not None:
            self.Accounts = []
            for item in params.get("Accounts"):
                obj = NewAccount()
                obj._deserialize(item)
                self.Accounts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAccountsResponse(AbstractModel):
    """CreateAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateAuditLogFileRequest(AbstractModel):
    """CreateAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param StartTime: 开始时间，格式为："2017-07-12 10:29:20"。
        :type StartTime: str
        :param EndTime: 结束时间，格式为："2017-07-12 10:29:20"。
        :type EndTime: str
        :param Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param Filter: 过滤条件。可按设置的过滤条件过滤日志。
        :type Filter: :class:`tencentcloud.cynosdb.v20190107.models.AuditLogFilter`
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = AuditLogFilter()
            self.Filter._deserialize(params.get("Filter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditLogFileResponse(AbstractModel):
    """CreateAuditLogFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileName: 审计日志文件名称。
        :type FileName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileName = params.get("FileName")
        self.RequestId = params.get("RequestId")


class CreateAuditRuleTemplateRequest(AbstractModel):
    """CreateAuditRuleTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleFilters: 审计规则。
        :type RuleFilters: list of RuleFilters
        :param RuleTemplateName: 规则模版名称。
        :type RuleTemplateName: str
        :param Description: 规则模版描述。
        :type Description: str
        """
        self.RuleFilters = None
        self.RuleTemplateName = None
        self.Description = None


    def _deserialize(self, params):
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        self.RuleTemplateName = params.get("RuleTemplateName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuditRuleTemplateResponse(AbstractModel):
    """CreateAuditRuleTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleTemplateId: 生成的规则模版ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTemplateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleTemplateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleTemplateId = params.get("RuleTemplateId")
        self.RequestId = params.get("RequestId")


class CreateBackupRequest(AbstractModel):
    """CreateBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param BackupType: 备份类型, 可选值：logic，逻辑备份；snapshot，物理备份
        :type BackupType: str
        :param BackupDatabases: 备份的库, 只在 BackupType 为 logic 时有效
        :type BackupDatabases: list of str
        :param BackupTables: 备份的表, 只在 BackupType 为 logic 时有效
        :type BackupTables: list of DatabaseTables
        :param BackupName: 备注名
        :type BackupName: str
        """
        self.ClusterId = None
        self.BackupType = None
        self.BackupDatabases = None
        self.BackupTables = None
        self.BackupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupType = params.get("BackupType")
        self.BackupDatabases = params.get("BackupDatabases")
        if params.get("BackupTables") is not None:
            self.BackupTables = []
            for item in params.get("BackupTables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self.BackupTables.append(obj)
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBackupResponse(AbstractModel):
    """CreateBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务流ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class CreateClustersRequest(AbstractModel):
    """CreateClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param VpcId: 所属VPC网络ID
        :type VpcId: str
        :param SubnetId: 所属子网ID
        :type SubnetId: str
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param DbVersion: 数据库版本，取值范围: 
<li> MYSQL可选值：5.7，8.0 </li>
        :type DbVersion: str
        :param ProjectId: 所属项目ID
        :type ProjectId: int
        :param Cpu: 当DbMode为NORMAL或不填时必选
普通实例Cpu核数
        :type Cpu: int
        :param Memory: 当DbMode为NORMAL或不填时必选
普通实例内存,单位G
        :type Memory: int
        :param Storage: 该参数无实际意义，已废弃。
存储大小，单位G。
        :type Storage: int
        :param ClusterName: 集群名称，长度小于64个字符，每个字符取值范围：大/小写字母，数字，特殊符号（'-','_','.'）
        :type ClusterName: str
        :param AdminPassword: 账号密码(8-64个字符，包含大小写英文字母、数字和符号~!@#$%^&*_-+=`|\(){}[]:;'<>,.?/中的任意三种)
        :type AdminPassword: str
        :param Port: 端口，默认3306，取值范围[0, 65535)
        :type Port: int
        :param PayMode: 计费模式，按量计费：0，包年包月：1。默认按量计费。
        :type PayMode: int
        :param Count: 购买集群数，可选值范围[1,50]，默认为1
        :type Count: int
        :param RollbackStrategy: 回档类型：
noneRollback：不回档；
snapRollback，快照回档；
timeRollback，时间点回档
        :type RollbackStrategy: str
        :param RollbackId: 快照回档，表示snapshotId；时间点回档，表示queryId，为0，表示需要判断时间点是否有效
        :type RollbackId: int
        :param OriginalClusterId: 回档时，传入源集群ID，用于查找源poolId
        :type OriginalClusterId: str
        :param ExpectTime: 时间点回档，指定时间；快照回档，快照时间
        :type ExpectTime: str
        :param ExpectTimeThresh: 该参数无实际意义，已废弃。
时间点回档，指定时间允许范围
        :type ExpectTimeThresh: int
        :param StorageLimit: 普通实例存储上限，单位GB
当DbType为MYSQL，且存储计费模式为预付费时，该参数需不大于cpu与memory对应存储规格上限
        :type StorageLimit: int
        :param InstanceCount: 实例数量，数量范围为(0,16]
        :type InstanceCount: int
        :param TimeSpan: 包年包月购买时长
        :type TimeSpan: int
        :param TimeUnit: 包年包月购买时长单位，['s','d','m','y']
        :type TimeUnit: str
        :param AutoRenewFlag: 包年包月购买是否自动续费，默认为0
        :type AutoRenewFlag: int
        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param HaCount: 实例数量（该参数已不再使用，只做存量兼容处理）
        :type HaCount: int
        :param OrderSource: 订单来源
        :type OrderSource: str
        :param ResourceTags: 集群创建需要绑定的tag数组信息
        :type ResourceTags: list of Tag
        :param DbMode: Db类型
当DbType为MYSQL时可选(默认NORMAL)：
<li>NORMAL</li>
<li>SERVERLESS</li>
        :type DbMode: str
        :param MinCpu: 当DbMode为SEVERLESS时必填
cpu最小值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MinCpu: float
        :param MaxCpu: 当DbMode为SEVERLESS时必填：
cpu最大值，可选范围参考DescribeServerlessInstanceSpecs接口返回
        :type MaxCpu: float
        :param AutoPause: 当DbMode为SEVERLESS时，指定集群是否自动暂停，可选范围
<li>yes</li>
<li>no</li>
默认值:yes
        :type AutoPause: str
        :param AutoPauseDelay: 当DbMode为SEVERLESS时，指定集群自动暂停的延迟，单位秒，可选范围[600,691200]
默认值:600
        :type AutoPauseDelay: int
        :param StoragePayMode: 集群存储计费模式，按量计费：0，包年包月：1。默认按量计费
当DbType为MYSQL时，在集群计算计费模式为后付费（包括DbMode为SERVERLESS）时，存储计费模式仅可为按量计费
回档与克隆均不支持包年包月存储
        :type StoragePayMode: int
        :param SecurityGroupIds: 安全组id数组
        :type SecurityGroupIds: list of str
        :param AlarmPolicyIds: 告警策略Id数组
        :type AlarmPolicyIds: list of str
        :param ClusterParams: 参数数组，暂时支持character_set_server （utf8｜latin1｜gbk｜utf8mb4） ，lower_case_table_names，1-大小写不敏感，0-大小写敏感
        :type ClusterParams: list of ParamItem
        :param DealMode: 交易模式，0-下单且支付，1-下单
        :type DealMode: int
        :param ParamTemplateId: 参数模版ID，可以通过查询参数模板信息DescribeParamTemplates获得参数模板ID
        :type ParamTemplateId: int
        :param SlaveZone: 多可用区地址
        :type SlaveZone: str
        :param InstanceInitInfos: 实例初始化配置信息，主要用于购买集群时选不同规格实例
        :type InstanceInitInfos: list of InstanceInitInfo
        """
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None
        self.DbType = None
        self.DbVersion = None
        self.ProjectId = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.ClusterName = None
        self.AdminPassword = None
        self.Port = None
        self.PayMode = None
        self.Count = None
        self.RollbackStrategy = None
        self.RollbackId = None
        self.OriginalClusterId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None
        self.StorageLimit = None
        self.InstanceCount = None
        self.TimeSpan = None
        self.TimeUnit = None
        self.AutoRenewFlag = None
        self.AutoVoucher = None
        self.HaCount = None
        self.OrderSource = None
        self.ResourceTags = None
        self.DbMode = None
        self.MinCpu = None
        self.MaxCpu = None
        self.AutoPause = None
        self.AutoPauseDelay = None
        self.StoragePayMode = None
        self.SecurityGroupIds = None
        self.AlarmPolicyIds = None
        self.ClusterParams = None
        self.DealMode = None
        self.ParamTemplateId = None
        self.SlaveZone = None
        self.InstanceInitInfos = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.ProjectId = params.get("ProjectId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.ClusterName = params.get("ClusterName")
        self.AdminPassword = params.get("AdminPassword")
        self.Port = params.get("Port")
        self.PayMode = params.get("PayMode")
        self.Count = params.get("Count")
        self.RollbackStrategy = params.get("RollbackStrategy")
        self.RollbackId = params.get("RollbackId")
        self.OriginalClusterId = params.get("OriginalClusterId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        self.StorageLimit = params.get("StorageLimit")
        self.InstanceCount = params.get("InstanceCount")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.AutoVoucher = params.get("AutoVoucher")
        self.HaCount = params.get("HaCount")
        self.OrderSource = params.get("OrderSource")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbMode = params.get("DbMode")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.AutoPause = params.get("AutoPause")
        self.AutoPauseDelay = params.get("AutoPauseDelay")
        self.StoragePayMode = params.get("StoragePayMode")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.AlarmPolicyIds = params.get("AlarmPolicyIds")
        if params.get("ClusterParams") is not None:
            self.ClusterParams = []
            for item in params.get("ClusterParams"):
                obj = ParamItem()
                obj._deserialize(item)
                self.ClusterParams.append(obj)
        self.DealMode = params.get("DealMode")
        self.ParamTemplateId = params.get("ParamTemplateId")
        self.SlaveZone = params.get("SlaveZone")
        if params.get("InstanceInitInfos") is not None:
            self.InstanceInitInfos = []
            for item in params.get("InstanceInitInfos"):
                obj = InstanceInitInfo()
                obj._deserialize(item)
                self.InstanceInitInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClustersResponse(AbstractModel):
    """CreateClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param ResourceIds: 资源ID列表（该字段已不再维护，请使用dealNames字段查询接口DescribeResourcesByDealName获取资源ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param ClusterIds: 集群ID列表（该字段已不再维护，请使用dealNames字段查询接口DescribeResourcesByDealName获取集群ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterIds: list of str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.DealNames = None
        self.ResourceIds = None
        self.ClusterIds = None
        self.BigDealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.DealNames = params.get("DealNames")
        self.ResourceIds = params.get("ResourceIds")
        self.ClusterIds = params.get("ClusterIds")
        self.BigDealIds = params.get("BigDealIds")
        self.RequestId = params.get("RequestId")


class CynosdbCluster(AbstractModel):
    """集群信息

    """

    def __init__(self):
        r"""
        :param Status: 集群状态， 可选值如下:
creating: 创建中
running:运行中
isolating:隔离中
isolated:已隔离
activating:解隔离中
offlining:下线中
offlined:已下线
deleting:删除中
deleted:已删除
        :type Status: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Zone: 可用区
        :type Zone: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Region: 地域
        :type Region: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceNum: 实例数
        :type InstanceNum: int
        :param Uin: 用户uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param DbType: 引擎类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DbType: str
        :param AppId: 用户appid
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param StatusDesc: 集群状态描述
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusDesc: str
        :param CreateTime: 集群创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param PayMode: 付费模式。0-按量计费，1-包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: int
        :param PeriodEndTime: 截止时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PeriodEndTime: str
        :param Vip: 集群读写vip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param Vport: 集群读写vport
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param ProjectID: 项目id
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectID: int
        :param VpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param SubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param CynosVersion: cynos内核版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CynosVersion: str
        :param StorageLimit: 存储容量
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: int
        :param RenewFlag: 续费标志
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param ProcessingTask: 正在处理的任务
注意：此字段可能返回 null，表示取不到有效值。
        :type ProcessingTask: str
        :param Tasks: 集群的任务数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        :param ResourceTags: 集群绑定的tag数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of Tag
        :param DbMode: Db类型(NORMAL, SERVERLESS)
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
pause
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerlessStatus: str
        :param Storage: 集群预付费存储值大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: int
        :param StorageId: 集群存储为预付费时的存储ID，用于预付费存储变配
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageId: str
        :param StoragePayMode: 集群存储付费模式。0-按量计费，1-包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePayMode: int
        :param MinStorageSize: 集群计算规格对应的最小存储值
注意：此字段可能返回 null，表示取不到有效值。
        :type MinStorageSize: int
        :param MaxStorageSize: 集群计算规格对应的最大存储值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStorageSize: int
        :param NetAddrs: 集群网络信息
注意：此字段可能返回 null，表示取不到有效值。
        :type NetAddrs: list of NetAddr
        :param PhysicalZone: 物理可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalZone: str
        :param MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: str
        :param HasSlaveZone: 是否有从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type HasSlaveZone: str
        :param SlaveZones: 从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: list of str
        :param BusinessType: 商业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param IsFreeze: 是否冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFreeze: str
        :param OrderSource: 订单来源
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderSource: str
        :param Ability: 能力
注意：此字段可能返回 null，表示取不到有效值。
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        """
        self.Status = None
        self.UpdateTime = None
        self.Zone = None
        self.ClusterName = None
        self.Region = None
        self.DbVersion = None
        self.ClusterId = None
        self.InstanceNum = None
        self.Uin = None
        self.DbType = None
        self.AppId = None
        self.StatusDesc = None
        self.CreateTime = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.Vip = None
        self.Vport = None
        self.ProjectID = None
        self.VpcId = None
        self.SubnetId = None
        self.CynosVersion = None
        self.StorageLimit = None
        self.RenewFlag = None
        self.ProcessingTask = None
        self.Tasks = None
        self.ResourceTags = None
        self.DbMode = None
        self.ServerlessStatus = None
        self.Storage = None
        self.StorageId = None
        self.StoragePayMode = None
        self.MinStorageSize = None
        self.MaxStorageSize = None
        self.NetAddrs = None
        self.PhysicalZone = None
        self.MasterZone = None
        self.HasSlaveZone = None
        self.SlaveZones = None
        self.BusinessType = None
        self.IsFreeze = None
        self.OrderSource = None
        self.Ability = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.UpdateTime = params.get("UpdateTime")
        self.Zone = params.get("Zone")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.DbVersion = params.get("DbVersion")
        self.ClusterId = params.get("ClusterId")
        self.InstanceNum = params.get("InstanceNum")
        self.Uin = params.get("Uin")
        self.DbType = params.get("DbType")
        self.AppId = params.get("AppId")
        self.StatusDesc = params.get("StatusDesc")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ProjectID = params.get("ProjectID")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.CynosVersion = params.get("CynosVersion")
        self.StorageLimit = params.get("StorageLimit")
        self.RenewFlag = params.get("RenewFlag")
        self.ProcessingTask = params.get("ProcessingTask")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.DbMode = params.get("DbMode")
        self.ServerlessStatus = params.get("ServerlessStatus")
        self.Storage = params.get("Storage")
        self.StorageId = params.get("StorageId")
        self.StoragePayMode = params.get("StoragePayMode")
        self.MinStorageSize = params.get("MinStorageSize")
        self.MaxStorageSize = params.get("MaxStorageSize")
        if params.get("NetAddrs") is not None:
            self.NetAddrs = []
            for item in params.get("NetAddrs"):
                obj = NetAddr()
                obj._deserialize(item)
                self.NetAddrs.append(obj)
        self.PhysicalZone = params.get("PhysicalZone")
        self.MasterZone = params.get("MasterZone")
        self.HasSlaveZone = params.get("HasSlaveZone")
        self.SlaveZones = params.get("SlaveZones")
        self.BusinessType = params.get("BusinessType")
        self.IsFreeze = params.get("IsFreeze")
        self.OrderSource = params.get("OrderSource")
        if params.get("Ability") is not None:
            self.Ability = Ability()
            self.Ability._deserialize(params.get("Ability"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbClusterDetail(AbstractModel):
    """集群详情详细信息

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param Region: 地域
        :type Region: str
        :param Status: 状态
        :type Status: str
        :param StatusDesc: 状态描述
        :type StatusDesc: str
        :param VpcName: VPC名称
        :type VpcName: str
        :param VpcId: vpc唯一id
        :type VpcId: str
        :param SubnetName: 子网名称
        :type SubnetName: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Charset: 字符集
        :type Charset: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param DbType: 数据库类型
        :type DbType: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param UsedStorage: 使用容量
        :type UsedStorage: int
        :param RoAddr: 读写分离Vport
        :type RoAddr: list of Addr
        :param InstanceSet: 实例信息
        :type InstanceSet: list of ClusterInstanceDetail
        :param PayMode: 付费模式
        :type PayMode: int
        :param PeriodEndTime: 到期时间
        :type PeriodEndTime: str
        :param Vip: vip地址
        :type Vip: str
        :param Vport: vport端口
        :type Vport: int
        :param ProjectID: 项目id
        :type ProjectID: int
        :param Zone: 可用区
        :type Zone: str
        :param ResourceTags: 实例绑定的tag数组信息
        :type ResourceTags: list of Tag
        :param ServerlessStatus: 当Db类型为SERVERLESS时，serverless集群状态，可选值:
resume
resuming
pause
pausing
        :type ServerlessStatus: str
        :param LogBin: binlog开关，可选值：ON, OFF
注意：此字段可能返回 null，表示取不到有效值。
        :type LogBin: str
        :param PitrType: pitr类型，可选值：normal, redo_pitr
注意：此字段可能返回 null，表示取不到有效值。
        :type PitrType: str
        :param PhysicalZone: 物理可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type PhysicalZone: str
        :param StorageId: 存储Id
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageId: str
        :param Storage: 存储大小，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: int
        :param MaxStorageSize: 最大存储规格，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStorageSize: int
        :param MinStorageSize: 最小存储规格，单位为G
注意：此字段可能返回 null，表示取不到有效值。
        :type MinStorageSize: int
        :param StoragePayMode: 存储付费类型，1为包年包月，0为按量计费
注意：此字段可能返回 null，表示取不到有效值。
        :type StoragePayMode: int
        :param DbMode: 数据库类型，normal，serverless
注意：此字段可能返回 null，表示取不到有效值。
        :type DbMode: str
        :param StorageLimit: 存储空间上限
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: int
        :param Ability: 集群支持的功能
注意：此字段可能返回 null，表示取不到有效值。
        :type Ability: :class:`tencentcloud.cynosdb.v20190107.models.Ability`
        :param CynosVersion: cynos版本
注意：此字段可能返回 null，表示取不到有效值。
        :type CynosVersion: str
        :param BusinessType: 商业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param HasSlaveZone: 是否有从可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type HasSlaveZone: str
        :param IsFreeze: 是否冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFreeze: str
        :param Tasks: 任务列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        :param MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: str
        :param SlaveZones: 从可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: list of str
        :param ProxyStatus: Proxy状态
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyStatus: str
        :param IsSkipTrade: 是否跳过交易
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSkipTrade: str
        :param IsOpenPasswordComplexity: 是否打开密码复杂度
注意：此字段可能返回 null，表示取不到有效值。
        :type IsOpenPasswordComplexity: str
        :param NetworkStatus: 网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkStatus: str
        """
        self.ClusterId = None
        self.ClusterName = None
        self.Region = None
        self.Status = None
        self.StatusDesc = None
        self.VpcName = None
        self.VpcId = None
        self.SubnetName = None
        self.SubnetId = None
        self.Charset = None
        self.CreateTime = None
        self.DbType = None
        self.DbVersion = None
        self.UsedStorage = None
        self.RoAddr = None
        self.InstanceSet = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.Vip = None
        self.Vport = None
        self.ProjectID = None
        self.Zone = None
        self.ResourceTags = None
        self.ServerlessStatus = None
        self.LogBin = None
        self.PitrType = None
        self.PhysicalZone = None
        self.StorageId = None
        self.Storage = None
        self.MaxStorageSize = None
        self.MinStorageSize = None
        self.StoragePayMode = None
        self.DbMode = None
        self.StorageLimit = None
        self.Ability = None
        self.CynosVersion = None
        self.BusinessType = None
        self.HasSlaveZone = None
        self.IsFreeze = None
        self.Tasks = None
        self.MasterZone = None
        self.SlaveZones = None
        self.ProxyStatus = None
        self.IsSkipTrade = None
        self.IsOpenPasswordComplexity = None
        self.NetworkStatus = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.SubnetId = params.get("SubnetId")
        self.Charset = params.get("Charset")
        self.CreateTime = params.get("CreateTime")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.UsedStorage = params.get("UsedStorage")
        if params.get("RoAddr") is not None:
            self.RoAddr = []
            for item in params.get("RoAddr"):
                obj = Addr()
                obj._deserialize(item)
                self.RoAddr.append(obj)
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ClusterInstanceDetail()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ProjectID = params.get("ProjectID")
        self.Zone = params.get("Zone")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.ServerlessStatus = params.get("ServerlessStatus")
        self.LogBin = params.get("LogBin")
        self.PitrType = params.get("PitrType")
        self.PhysicalZone = params.get("PhysicalZone")
        self.StorageId = params.get("StorageId")
        self.Storage = params.get("Storage")
        self.MaxStorageSize = params.get("MaxStorageSize")
        self.MinStorageSize = params.get("MinStorageSize")
        self.StoragePayMode = params.get("StoragePayMode")
        self.DbMode = params.get("DbMode")
        self.StorageLimit = params.get("StorageLimit")
        if params.get("Ability") is not None:
            self.Ability = Ability()
            self.Ability._deserialize(params.get("Ability"))
        self.CynosVersion = params.get("CynosVersion")
        self.BusinessType = params.get("BusinessType")
        self.HasSlaveZone = params.get("HasSlaveZone")
        self.IsFreeze = params.get("IsFreeze")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.MasterZone = params.get("MasterZone")
        self.SlaveZones = params.get("SlaveZones")
        self.ProxyStatus = params.get("ProxyStatus")
        self.IsSkipTrade = params.get("IsSkipTrade")
        self.IsOpenPasswordComplexity = params.get("IsOpenPasswordComplexity")
        self.NetworkStatus = params.get("NetworkStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstance(AbstractModel):
    """实例信息

    """

    def __init__(self):
        r"""
        :param Uin: 用户Uin
        :type Uin: str
        :param AppId: 用户AppId
        :type AppId: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param Status: 实例状态
        :type Status: str
        :param StatusDesc: 实例状态中文描述
        :type StatusDesc: str
        :param DbType: 数据库类型
        :type DbType: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param Cpu: Cpu，单位：核
        :type Cpu: int
        :param Memory: 内存，单位：GB
        :type Memory: int
        :param Storage: 存储量，单位：GB
        :type Storage: int
        :param InstanceType: 实例类型
        :type InstanceType: str
        :param InstanceRole: 实例当前角色
        :type InstanceRole: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param VpcId: VPC网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Vip: 实例内网IP
        :type Vip: str
        :param Vport: 实例内网端口
        :type Vport: int
        :param PayMode: 付费模式
        :type PayMode: int
        :param PeriodEndTime: 实例过期时间
        :type PeriodEndTime: str
        :param DestroyDeadlineText: 销毁期限
        :type DestroyDeadlineText: str
        :param IsolateTime: 隔离时间
        :type IsolateTime: str
        :param NetType: 网络类型
        :type NetType: int
        :param WanDomain: 外网域名
        :type WanDomain: str
        :param WanIP: 外网IP
        :type WanIP: str
        :param WanPort: 外网端口
        :type WanPort: int
        :param WanStatus: 外网状态
        :type WanStatus: str
        :param DestroyTime: 实例销毁时间
        :type DestroyTime: str
        :param CynosVersion: Cynos内核版本
        :type CynosVersion: str
        :param ProcessingTask: 正在处理的任务
        :type ProcessingTask: str
        :param RenewFlag: 续费标志
        :type RenewFlag: int
        :param MinCpu: serverless实例cpu下限
        :type MinCpu: float
        :param MaxCpu: serverless实例cpu上限
        :type MaxCpu: float
        :param ServerlessStatus: serverless实例状态, 可选值：
resume
pause
        :type ServerlessStatus: str
        :param StorageId: 预付费存储Id
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageId: str
        :param StoragePayMode: 存储付费类型
        :type StoragePayMode: int
        :param PhysicalZone: 物理区
        :type PhysicalZone: str
        :param BusinessType: 商业类型
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessType: str
        :param Tasks: 任务
注意：此字段可能返回 null，表示取不到有效值。
        :type Tasks: list of ObjectTask
        :param IsFreeze: 是否冻结
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFreeze: str
        :param ResourceTags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceTags: list of Tag
        :param MasterZone: 主可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type MasterZone: str
        :param SlaveZones: 备可用区
注意：此字段可能返回 null，表示取不到有效值。
        :type SlaveZones: list of str
        """
        self.Uin = None
        self.AppId = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.StatusDesc = None
        self.DbType = None
        self.DbVersion = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.InstanceType = None
        self.InstanceRole = None
        self.UpdateTime = None
        self.CreateTime = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vport = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.DestroyDeadlineText = None
        self.IsolateTime = None
        self.NetType = None
        self.WanDomain = None
        self.WanIP = None
        self.WanPort = None
        self.WanStatus = None
        self.DestroyTime = None
        self.CynosVersion = None
        self.ProcessingTask = None
        self.RenewFlag = None
        self.MinCpu = None
        self.MaxCpu = None
        self.ServerlessStatus = None
        self.StorageId = None
        self.StoragePayMode = None
        self.PhysicalZone = None
        self.BusinessType = None
        self.Tasks = None
        self.IsFreeze = None
        self.ResourceTags = None
        self.MasterZone = None
        self.SlaveZones = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceType = params.get("InstanceType")
        self.InstanceRole = params.get("InstanceRole")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.DestroyDeadlineText = params.get("DestroyDeadlineText")
        self.IsolateTime = params.get("IsolateTime")
        self.NetType = params.get("NetType")
        self.WanDomain = params.get("WanDomain")
        self.WanIP = params.get("WanIP")
        self.WanPort = params.get("WanPort")
        self.WanStatus = params.get("WanStatus")
        self.DestroyTime = params.get("DestroyTime")
        self.CynosVersion = params.get("CynosVersion")
        self.ProcessingTask = params.get("ProcessingTask")
        self.RenewFlag = params.get("RenewFlag")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.ServerlessStatus = params.get("ServerlessStatus")
        self.StorageId = params.get("StorageId")
        self.StoragePayMode = params.get("StoragePayMode")
        self.PhysicalZone = params.get("PhysicalZone")
        self.BusinessType = params.get("BusinessType")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.IsFreeze = params.get("IsFreeze")
        if params.get("ResourceTags") is not None:
            self.ResourceTags = []
            for item in params.get("ResourceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ResourceTags.append(obj)
        self.MasterZone = params.get("MasterZone")
        self.SlaveZones = params.get("SlaveZones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceDetail(AbstractModel):
    """实例详情

    """

    def __init__(self):
        r"""
        :param Uin: 用户Uin
        :type Uin: str
        :param AppId: 用户AppId
        :type AppId: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Region: 地域
        :type Region: str
        :param Zone: 可用区
        :type Zone: str
        :param Status: 实例状态
        :type Status: str
        :param StatusDesc: 实例状态中文描述
        :type StatusDesc: str
        :param DbType: 数据库类型
        :type DbType: str
        :param DbVersion: 数据库版本
        :type DbVersion: str
        :param Cpu: Cpu，单位：核
        :type Cpu: int
        :param Memory: 内存，单位：GB
        :type Memory: int
        :param Storage: 存储量，单位：GB
        :type Storage: int
        :param InstanceType: 实例类型
        :type InstanceType: str
        :param InstanceRole: 实例当前角色
        :type InstanceRole: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param PayMode: 付费模式
        :type PayMode: int
        :param PeriodEndTime: 实例过期时间
        :type PeriodEndTime: str
        :param NetType: 网络类型
        :type NetType: int
        :param VpcId: VPC网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Vip: 实例内网IP
        :type Vip: str
        :param Vport: 实例内网端口
        :type Vport: int
        :param WanDomain: 实例外网域名
        :type WanDomain: str
        :param Charset: 字符集
        :type Charset: str
        :param CynosVersion: Cynos内核版本
        :type CynosVersion: str
        :param RenewFlag: 续费标志
        :type RenewFlag: int
        :param MinCpu: serverless实例cpu下限
        :type MinCpu: float
        :param MaxCpu: serverless实例cpu上限
        :type MaxCpu: float
        :param ServerlessStatus: serverless实例状态, 可能值：
resume
pause
        :type ServerlessStatus: str
        """
        self.Uin = None
        self.AppId = None
        self.ClusterId = None
        self.ClusterName = None
        self.InstanceId = None
        self.InstanceName = None
        self.ProjectId = None
        self.Region = None
        self.Zone = None
        self.Status = None
        self.StatusDesc = None
        self.DbType = None
        self.DbVersion = None
        self.Cpu = None
        self.Memory = None
        self.Storage = None
        self.InstanceType = None
        self.InstanceRole = None
        self.UpdateTime = None
        self.CreateTime = None
        self.PayMode = None
        self.PeriodEndTime = None
        self.NetType = None
        self.VpcId = None
        self.SubnetId = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.Charset = None
        self.CynosVersion = None
        self.RenewFlag = None
        self.MinCpu = None
        self.MaxCpu = None
        self.ServerlessStatus = None


    def _deserialize(self, params):
        self.Uin = params.get("Uin")
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ProjectId = params.get("ProjectId")
        self.Region = params.get("Region")
        self.Zone = params.get("Zone")
        self.Status = params.get("Status")
        self.StatusDesc = params.get("StatusDesc")
        self.DbType = params.get("DbType")
        self.DbVersion = params.get("DbVersion")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Storage = params.get("Storage")
        self.InstanceType = params.get("InstanceType")
        self.InstanceRole = params.get("InstanceRole")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.PayMode = params.get("PayMode")
        self.PeriodEndTime = params.get("PeriodEndTime")
        self.NetType = params.get("NetType")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.Charset = params.get("Charset")
        self.CynosVersion = params.get("CynosVersion")
        self.RenewFlag = params.get("RenewFlag")
        self.MinCpu = params.get("MinCpu")
        self.MaxCpu = params.get("MaxCpu")
        self.ServerlessStatus = params.get("ServerlessStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CynosdbInstanceGrp(AbstractModel):
    """实例组信息

    """

    def __init__(self):
        r"""
        :param AppId: 用户appId
        :type AppId: int
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param DeletedTime: 删除时间
        :type DeletedTime: str
        :param InstanceGrpId: 实例组ID
        :type InstanceGrpId: str
        :param Status: 状态
        :type Status: str
        :param Type: 实例组类型。ha-ha组；ro-只读组
        :type Type: str
        :param UpdatedTime: 更新时间
        :type UpdatedTime: str
        :param Vip: 内网IP
        :type Vip: str
        :param Vport: 内网端口
        :type Vport: int
        :param WanDomain: 外网域名
        :type WanDomain: str
        :param WanIP: 外网ip
        :type WanIP: str
        :param WanPort: 外网端口
        :type WanPort: int
        :param WanStatus: 外网状态
        :type WanStatus: str
        :param InstanceSet: 实例组包含实例信息
        :type InstanceSet: list of CynosdbInstance
        :param UniqVpcId: VPC的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param UniqSubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param OldAddrInfo: 正在回收IP信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OldAddrInfo: :class:`tencentcloud.cynosdb.v20190107.models.OldAddrInfo`
        :param ProcessingTasks: 正在进行的任务
        :type ProcessingTasks: list of str
        :param Tasks: 任务列表
        :type Tasks: list of ObjectTask
        :param NetServiceId: biz_net_service表id
        :type NetServiceId: int
        """
        self.AppId = None
        self.ClusterId = None
        self.CreatedTime = None
        self.DeletedTime = None
        self.InstanceGrpId = None
        self.Status = None
        self.Type = None
        self.UpdatedTime = None
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanIP = None
        self.WanPort = None
        self.WanStatus = None
        self.InstanceSet = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.OldAddrInfo = None
        self.ProcessingTasks = None
        self.Tasks = None
        self.NetServiceId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.ClusterId = params.get("ClusterId")
        self.CreatedTime = params.get("CreatedTime")
        self.DeletedTime = params.get("DeletedTime")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.Status = params.get("Status")
        self.Type = params.get("Type")
        self.UpdatedTime = params.get("UpdatedTime")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanIP = params.get("WanIP")
        self.WanPort = params.get("WanPort")
        self.WanStatus = params.get("WanStatus")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        if params.get("OldAddrInfo") is not None:
            self.OldAddrInfo = OldAddrInfo()
            self.OldAddrInfo._deserialize(params.get("OldAddrInfo"))
        self.ProcessingTasks = params.get("ProcessingTasks")
        if params.get("Tasks") is not None:
            self.Tasks = []
            for item in params.get("Tasks"):
                obj = ObjectTask()
                obj._deserialize(item)
                self.Tasks.append(obj)
        self.NetServiceId = params.get("NetServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabasePrivileges(AbstractModel):
    """数据库权限列表

    """

    def __init__(self):
        r"""
        :param Db: 数据库
        :type Db: str
        :param Privileges: 权限列表
        :type Privileges: list of str
        """
        self.Db = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DatabaseTables(AbstractModel):
    """数据库表信息

    """

    def __init__(self):
        r"""
        :param Database: 数据库名
注意：此字段可能返回 null，表示取不到有效值。
        :type Database: str
        :param Tables: 表名称列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of str
        """
        self.Database = None
        self.Tables = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        self.Tables = params.get("Tables")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DbTable(AbstractModel):
    """数据库表

    """

    def __init__(self):
        r"""
        :param Db: 数据库名称
        :type Db: str
        :param TableName: 数据库表名称
        :type TableName: str
        """
        self.Db = None
        self.TableName = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.TableName = params.get("TableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditLogFileRequest(AbstractModel):
    """DeleteAuditLogFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param FileName: 审计日志文件名称。
        :type FileName: str
        """
        self.InstanceId = None
        self.FileName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditLogFileResponse(AbstractModel):
    """DeleteAuditLogFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAuditRuleTemplatesRequest(AbstractModel):
    """DeleteAuditRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleTemplateIds: 审计规则模版ID。
        :type RuleTemplateIds: list of str
        """
        self.RuleTemplateIds = None


    def _deserialize(self, params):
        self.RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuditRuleTemplatesResponse(AbstractModel):
    """DeleteAuditRuleTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBackupRequest(AbstractModel):
    """DeleteBackup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SnapshotIdList: 备份文件ID，旧版本使用的字段，不推荐使用
        :type SnapshotIdList: list of int
        :param BackupIds: 备份文件ID，推荐使用
        :type BackupIds: list of int
        """
        self.ClusterId = None
        self.SnapshotIdList = None
        self.BackupIds = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SnapshotIdList = params.get("SnapshotIdList")
        self.BackupIds = params.get("BackupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBackupResponse(AbstractModel):
    """DeleteBackup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountAllGrantPrivilegesRequest(AbstractModel):
    """DescribeAccountAllGrantPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        """
        self.ClusterId = None
        self.Account = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self.Account = InputAccount()
            self.Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountAllGrantPrivilegesResponse(AbstractModel):
    """DescribeAccountAllGrantPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param PrivilegeStatements: 权限语句
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivilegeStatements: list of str
        :param GlobalPrivileges: 全局权限
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalPrivileges: list of str
        :param DatabasePrivileges: 数据库权限
注意：此字段可能返回 null，表示取不到有效值。
        :type DatabasePrivileges: list of DatabasePrivileges
        :param TablePrivileges: 数据库表权限
注意：此字段可能返回 null，表示取不到有效值。
        :type TablePrivileges: list of TablePrivileges
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PrivilegeStatements = None
        self.GlobalPrivileges = None
        self.DatabasePrivileges = None
        self.TablePrivileges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PrivilegeStatements = params.get("PrivilegeStatements")
        self.GlobalPrivileges = params.get("GlobalPrivileges")
        if params.get("DatabasePrivileges") is not None:
            self.DatabasePrivileges = []
            for item in params.get("DatabasePrivileges"):
                obj = DatabasePrivileges()
                obj._deserialize(item)
                self.DatabasePrivileges.append(obj)
        if params.get("TablePrivileges") is not None:
            self.TablePrivileges = []
            for item in params.get("TablePrivileges"):
                obj = TablePrivileges()
                obj._deserialize(item)
                self.TablePrivileges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccountsRequest(AbstractModel):
    """DescribeAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param AccountNames: 需要过滤的账户列表
        :type AccountNames: list of str
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
该参数已废用
        :type DbType: str
        :param Hosts: 需要过滤的账户列表
        :type Hosts: list of str
        :param Limit: 限制量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        """
        self.ClusterId = None
        self.AccountNames = None
        self.DbType = None
        self.Hosts = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.AccountNames = params.get("AccountNames")
        self.DbType = params.get("DbType")
        self.Hosts = params.get("Hosts")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountsResponse(AbstractModel):
    """DescribeAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccountSet: 数据库账号列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountSet: list of Account
        :param TotalCount: 账号总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccountSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountSet") is not None:
            self.AccountSet = []
            for item in params.get("AccountSet"):
                obj = Account()
                obj._deserialize(item)
                self.AccountSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeAuditLogFilesRequest(AbstractModel):
    """DescribeAuditLogFiles请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Limit: 分页大小参数。默认值为 20，最小值为 1，最大值为 100。
        :type Limit: int
        :param Offset: 分页偏移量。
        :type Offset: int
        :param FileName: 审计日志文件名。
        :type FileName: str
        """
        self.InstanceId = None
        self.Limit = None
        self.Offset = None
        self.FileName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogFilesResponse(AbstractModel):
    """DescribeAuditLogFiles返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的审计日志文件个数。
        :type TotalCount: int
        :param Items: 审计日志文件详情。
        :type Items: list of AuditLogFile
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AuditLogFile()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAuditLogsRequest(AbstractModel):
    """DescribeAuditLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param StartTime: 开始时间，格式为："2017-07-12 10:29:20"。
        :type StartTime: str
        :param EndTime: 结束时间，格式为："2017-07-12 10:29:20"。
        :type EndTime: str
        :param Order: 排序方式。支持值包括："ASC" - 升序，"DESC" - 降序。
        :type Order: str
        :param OrderBy: 排序字段。支持值包括：
"timestamp" - 时间戳；
"affectRows" - 影响行数；
"execTime" - 执行时间。
        :type OrderBy: str
        :param Filter: 过滤条件。可按设置的过滤条件过滤日志。
        :type Filter: :class:`tencentcloud.cynosdb.v20190107.models.AuditLogFilter`
        :param Limit: 分页参数，单次返回的数据条数。默认值为100，最大值为100。
        :type Limit: int
        :param Offset: 分页偏移量。
        :type Offset: int
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Order = None
        self.OrderBy = None
        self.Filter = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Order = params.get("Order")
        self.OrderBy = params.get("OrderBy")
        if params.get("Filter") is not None:
            self.Filter = AuditLogFilter()
            self.Filter._deserialize(params.get("Filter"))
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogsResponse(AbstractModel):
    """DescribeAuditLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的审计日志条数。
        :type TotalCount: int
        :param Items: 审计日志详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AuditLog()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAuditRuleTemplatesRequest(AbstractModel):
    """DescribeAuditRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleTemplateIds: 规则模版ID。
        :type RuleTemplateIds: list of str
        :param RuleTemplateNames: 规则模版名称
        :type RuleTemplateNames: list of str
        :param Limit: 单次请求返回的数量。默认值20。
        :type Limit: int
        :param Offset: 偏移量，默认值为 0。
        :type Offset: int
        """
        self.RuleTemplateIds = None
        self.RuleTemplateNames = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.RuleTemplateIds = params.get("RuleTemplateIds")
        self.RuleTemplateNames = params.get("RuleTemplateNames")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRuleTemplatesResponse(AbstractModel):
    """DescribeAuditRuleTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合查询条件的实例总数。
        :type TotalCount: int
        :param Items: 规则模版详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of AuditRuleTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = AuditRuleTemplateInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAuditRuleWithInstanceIdsRequest(AbstractModel):
    """DescribeAuditRuleWithInstanceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例ID。目前仅支持单个实例的查询。
        :type InstanceIds: list of str
        """
        self.InstanceIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditRuleWithInstanceIdsResponse(AbstractModel):
    """DescribeAuditRuleWithInstanceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 无
        :type TotalCount: int
        :param Items: 实例审计规则信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of InstanceAuditRule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = InstanceAuditRule()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBackupConfigRequest(AbstractModel):
    """DescribeBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupConfigResponse(AbstractModel):
    """DescribeBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeBeg: int
        :param BackupTimeEnd: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeEnd: int
        :param ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800
        :type ReserveDuration: int
        :param BackupFreq: 备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupFreq: list of str
        :param BackupType: 备份方式，logic-逻辑备份，snapshot-快照备份
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BackupTimeBeg = None
        self.BackupTimeEnd = None
        self.ReserveDuration = None
        self.BackupFreq = None
        self.BackupType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BackupTimeBeg = params.get("BackupTimeBeg")
        self.BackupTimeEnd = params.get("BackupTimeEnd")
        self.ReserveDuration = params.get("ReserveDuration")
        self.BackupFreq = params.get("BackupFreq")
        self.BackupType = params.get("BackupType")
        self.RequestId = params.get("RequestId")


class DescribeBackupDownloadUrlRequest(AbstractModel):
    """DescribeBackupDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param BackupId: 备份ID
        :type BackupId: int
        """
        self.ClusterId = None
        self.BackupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupId = params.get("BackupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupDownloadUrlResponse(AbstractModel):
    """DescribeBackupDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 备份下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeBackupListRequest(AbstractModel):
    """DescribeBackupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Limit: 备份文件列表大小，取值范围(0,100]
        :type Limit: int
        :param Offset: 备份文件列表偏移，取值范围[0,INF)
        :type Offset: int
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param BackupIds: 备份ID
        :type BackupIds: list of int
        :param BackupType: 备份类型，可选值：snapshot，快照备份； logic，逻辑备份
        :type BackupType: str
        :param BackupMethod: 备份方式，可选值：auto，自动备份；manual，手动备
        :type BackupMethod: str
        :param SnapShotType: 快照类型，可选值：full，全量；increment，增量
        :type SnapShotType: str
        :param StartTime: 备份开始时间
        :type StartTime: str
        :param EndTime: 备份结束时间
        :type EndTime: str
        :param FileNames: 备份文件名，模糊查询
        :type FileNames: list of str
        :param BackupNames: 备份备注名，模糊查询
        :type BackupNames: list of str
        :param SnapshotIdList: 快照备份Id列表
        :type SnapshotIdList: list of int
        """
        self.ClusterId = None
        self.Limit = None
        self.Offset = None
        self.DbType = None
        self.BackupIds = None
        self.BackupType = None
        self.BackupMethod = None
        self.SnapShotType = None
        self.StartTime = None
        self.EndTime = None
        self.FileNames = None
        self.BackupNames = None
        self.SnapshotIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.DbType = params.get("DbType")
        self.BackupIds = params.get("BackupIds")
        self.BackupType = params.get("BackupType")
        self.BackupMethod = params.get("BackupMethod")
        self.SnapShotType = params.get("SnapShotType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.FileNames = params.get("FileNames")
        self.BackupNames = params.get("BackupNames")
        self.SnapshotIdList = params.get("SnapshotIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBackupListResponse(AbstractModel):
    """DescribeBackupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总共备份文件个数
        :type TotalCount: int
        :param BackupList: 备份文件列表
        :type BackupList: list of BackupFileInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BackupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BackupList") is not None:
            self.BackupList = []
            for item in params.get("BackupList"):
                obj = BackupFileInfo()
                obj._deserialize(item)
                self.BackupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBinlogDownloadUrlRequest(AbstractModel):
    """DescribeBinlogDownloadUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param BinlogId: Binlog文件ID
        :type BinlogId: int
        """
        self.ClusterId = None
        self.BinlogId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BinlogId = params.get("BinlogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogDownloadUrlResponse(AbstractModel):
    """DescribeBinlogDownloadUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param DownloadUrl: 下载地址
        :type DownloadUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DownloadUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownloadUrl = params.get("DownloadUrl")
        self.RequestId = params.get("RequestId")


class DescribeBinlogSaveDaysRequest(AbstractModel):
    """DescribeBinlogSaveDays请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogSaveDaysResponse(AbstractModel):
    """DescribeBinlogSaveDays返回参数结构体

    """

    def __init__(self):
        r"""
        :param BinlogSaveDays: Binlog保留天数
        :type BinlogSaveDays: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BinlogSaveDays = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BinlogSaveDays = params.get("BinlogSaveDays")
        self.RequestId = params.get("RequestId")


class DescribeBinlogsRequest(AbstractModel):
    """DescribeBinlogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 限制条数
        :type Limit: int
        """
        self.ClusterId = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBinlogsResponse(AbstractModel):
    """DescribeBinlogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总条数
        :type TotalCount: int
        :param Binlogs: Binlog列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Binlogs: list of BinlogItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Binlogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Binlogs") is not None:
            self.Binlogs = []
            for item in params.get("Binlogs"):
                obj = BinlogItem()
                obj._deserialize(item)
                self.Binlogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterDetailRequest(AbstractModel):
    """DescribeClusterDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterDetailResponse(AbstractModel):
    """DescribeClusterDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Detail: 集群详细信息
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbClusterDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbClusterDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeClusterInstanceGrpsRequest(AbstractModel):
    """DescribeClusterInstanceGrps请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterInstanceGrpsResponse(AbstractModel):
    """DescribeClusterInstanceGrps返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例组个数
        :type TotalCount: int
        :param InstanceGrpInfoList: 实例组列表
        :type InstanceGrpInfoList: list of CynosdbInstanceGrp
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceGrpInfoList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceGrpInfoList") is not None:
            self.InstanceGrpInfoList = []
            for item in params.get("InstanceGrpInfoList"):
                obj = CynosdbInstanceGrp()
                obj._deserialize(item)
                self.InstanceGrpInfoList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterParamLogsRequest(AbstractModel):
    """DescribeClusterParamLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 实例ID列表，用来记录具体操作哪些实例
        :type InstanceIds: list of str
        :param OrderBy: 排序字段，定义在回返结果的基于哪个字段进行排序
        :type OrderBy: str
        :param OrderByType: 定义具体的排序规则，限定为desc,asc,DESC,ASC其中之一
        :type OrderByType: str
        :param Limit: 返回数量，默认为 20，取值范围为(0,100]
        :type Limit: int
        :param Offset: 记录偏移量，默认值为0，取值范围为[0,INF)
        :type Offset: int
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.OrderBy = None
        self.OrderByType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterParamLogsResponse(AbstractModel):
    """DescribeClusterParamLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 记录总数
        :type TotalCount: int
        :param ClusterParamLogs: 参数修改记录
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterParamLogs: list of ClusterParamModifyLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterParamLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterParamLogs") is not None:
            self.ClusterParamLogs = []
            for item in params.get("ClusterParamLogs"):
                obj = ClusterParamModifyLog()
                obj._deserialize(item)
                self.ClusterParamLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClusterParamsRequest(AbstractModel):
    """DescribeClusterParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ParamName: 参数名字
        :type ParamName: str
        """
        self.ClusterId = None
        self.ParamName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ParamName = params.get("ParamName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClusterParamsResponse(AbstractModel):
    """DescribeClusterParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 参数个数
        :type TotalCount: int
        :param Items: 实例参数列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ParamInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParamInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClustersRequest(AbstractModel):
    """DescribeClusters请求参数结构体

    """

    def __init__(self):
        r"""
        :param DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”
        :type DbType: str
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        """
        self.DbType = None
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Filters = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClustersResponse(AbstractModel):
    """DescribeClusters返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 集群数
        :type TotalCount: int
        :param ClusterSet: 集群列表
        :type ClusterSet: list of CynosdbCluster
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClusterSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClusterSet") is not None:
            self.ClusterSet = []
            for item in params.get("ClusterSet"):
                obj = CynosdbCluster()
                obj._deserialize(item)
                self.ClusterSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDBSecurityGroupsRequest(AbstractModel):
    """DescribeDBSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例组ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDBSecurityGroupsResponse(AbstractModel):
    """DescribeDBSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param Groups: 安全组信息
        :type Groups: list of SecurityGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowRequest(AbstractModel):
    """DescribeFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流ID
        :type FlowId: int
        """
        self.FlowId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowResponse(AbstractModel):
    """DescribeFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 任务流状态。0-成功，1-失败，2-处理中
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeInstanceDetailRequest(AbstractModel):
    """DescribeInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceDetailResponse(AbstractModel):
    """DescribeInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Detail: 实例详情
        :type Detail: :class:`tencentcloud.cynosdb.v20190107.models.CynosdbInstanceDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Detail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Detail") is not None:
            self.Detail = CynosdbInstanceDetail()
            self.Detail._deserialize(params.get("Detail"))
        self.RequestId = params.get("RequestId")


class DescribeInstanceSlowQueriesRequest(AbstractModel):
    """DescribeInstanceSlowQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param StartTime: 事务开始最早时间
        :type StartTime: str
        :param EndTime: 事务开始最晚时间
        :type EndTime: str
        :param Limit: 限制条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param Username: 用户名
        :type Username: str
        :param Host: 客户端host
        :type Host: str
        :param Database: 数据库名
        :type Database: str
        :param OrderBy: 排序字段，可选值：QueryTime,LockTime,RowsExamined,RowsSent
        :type OrderBy: str
        :param OrderByType: 排序类型，可选值：asc,desc
        :type OrderByType: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Username = None
        self.Host = None
        self.Database = None
        self.OrderBy = None
        self.OrderByType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Username = params.get("Username")
        self.Host = params.get("Host")
        self.Database = params.get("Database")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSlowQueriesResponse(AbstractModel):
    """DescribeInstanceSlowQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总条数
        :type TotalCount: int
        :param SlowQueries: 慢查询记录
        :type SlowQueries: list of SlowQueriesItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SlowQueries = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SlowQueries") is not None:
            self.SlowQueries = []
            for item in params.get("SlowQueries"):
                obj = SlowQueriesItem()
                obj._deserialize(item)
                self.SlowQueries.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceSpecsRequest(AbstractModel):
    """DescribeInstanceSpecs请求参数结构体

    """

    def __init__(self):
        r"""
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param IncludeZoneStocks: 是否需要返回可用区信息
        :type IncludeZoneStocks: bool
        """
        self.DbType = None
        self.IncludeZoneStocks = None


    def _deserialize(self, params):
        self.DbType = params.get("DbType")
        self.IncludeZoneStocks = params.get("IncludeZoneStocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceSpecsResponse(AbstractModel):
    """DescribeInstanceSpecs返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceSpecSet: 规格信息
        :type InstanceSpecSet: list of InstanceSpec
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceSpecSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSpecSet") is not None:
            self.InstanceSpecSet = []
            for item in params.get("InstanceSpecSet"):
                obj = InstanceSpec()
                obj._deserialize(item)
                self.InstanceSpecSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Offset: 记录偏移量，默认值为0
        :type Offset: int
        :param OrderBy: 排序字段，取值范围：
<li> CREATETIME：创建时间</li>
<li> PERIODENDTIME：过期时间</li>
        :type OrderBy: str
        :param OrderByType: 排序类型，取值范围：
<li> ASC：升序排序 </li>
<li> DESC：降序排序 </li>
        :type OrderByType: str
        :param Filters: 搜索条件，若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Filters: list of QueryFilter
        :param DbType: 引擎类型：目前支持“MYSQL”， “POSTGRESQL”
        :type DbType: str
        :param Status: 实例状态, 可选值:
creating 创建中
running 运行中
isolating 隔离中
isolated 已隔离
activating 恢复中
offlining 下线中
offlined 已下线
        :type Status: str
        :param InstanceIds: 实例id列表
        :type InstanceIds: list of str
        """
        self.Limit = None
        self.Offset = None
        self.OrderBy = None
        self.OrderByType = None
        self.Filters = None
        self.DbType = None
        self.Status = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = QueryFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.DbType = params.get("DbType")
        self.Status = params.get("Status")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 实例个数
        :type TotalCount: int
        :param InstanceSet: 实例列表
        :type InstanceSet: list of CynosdbInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CynosdbInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMaintainPeriodRequest(AbstractModel):
    """DescribeMaintainPeriod请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMaintainPeriodResponse(AbstractModel):
    """DescribeMaintainPeriod返回参数结构体

    """

    def __init__(self):
        r"""
        :param MaintainWeekDays: 维护week days
        :type MaintainWeekDays: list of str
        :param MaintainStartTime: 维护开始时间，单位秒
        :type MaintainStartTime: int
        :param MaintainDuration: 维护时长，单位秒
        :type MaintainDuration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MaintainWeekDays = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.RequestId = params.get("RequestId")


class DescribeParamTemplatesRequest(AbstractModel):
    """DescribeParamTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param EngineVersions: 数据库引擎版本号
        :type EngineVersions: list of str
        :param TemplateNames: 模版名称
        :type TemplateNames: list of str
        :param TemplateIds: 模版ID
        :type TemplateIds: list of int
        :param DbModes: 数据库类型，可选值：NORMAL，SERVERLESS
        :type DbModes: list of str
        :param Offset: 查询偏移量
        :type Offset: int
        :param Limit: 查询限制条数
        :type Limit: int
        :param Products: 查询的模板对应的产品类型
        :type Products: list of str
        :param TemplateTypes: 模版类型
        :type TemplateTypes: list of str
        :param EngineTypes: 版本类型
        :type EngineTypes: list of str
        :param OrderBy: 返回结果的排序字段
        :type OrderBy: str
        :param OrderDirection: 排序方式（asc、desc）
        :type OrderDirection: str
        """
        self.EngineVersions = None
        self.TemplateNames = None
        self.TemplateIds = None
        self.DbModes = None
        self.Offset = None
        self.Limit = None
        self.Products = None
        self.TemplateTypes = None
        self.EngineTypes = None
        self.OrderBy = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.EngineVersions = params.get("EngineVersions")
        self.TemplateNames = params.get("TemplateNames")
        self.TemplateIds = params.get("TemplateIds")
        self.DbModes = params.get("DbModes")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Products = params.get("Products")
        self.TemplateTypes = params.get("TemplateTypes")
        self.EngineTypes = params.get("EngineTypes")
        self.OrderBy = params.get("OrderBy")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeParamTemplatesResponse(AbstractModel):
    """DescribeParamTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 参数模板数量
        :type TotalCount: int
        :param Items: 参数模板信息
        :type Items: list of ParamTemplateListInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Items = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Items") is not None:
            self.Items = []
            for item in params.get("Items"):
                obj = ParamTemplateListInfo()
                obj._deserialize(item)
                self.Items.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProjectSecurityGroupsRequest(AbstractModel):
    """DescribeProjectSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param Limit: 限制量
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param SearchKey: 搜索关键字
        :type SearchKey: str
        """
        self.ProjectId = None
        self.Limit = None
        self.Offset = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectSecurityGroupsResponse(AbstractModel):
    """DescribeProjectSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param Groups: 安全组详情
        :type Groups: list of SecurityGroup
        :param Total: 总数量
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Groups = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Groups") is not None:
            self.Groups = []
            for item in params.get("Groups"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.Groups.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeResourcesByDealNameRequest(AbstractModel):
    """DescribeResourcesByDealName请求参数结构体

    """

    def __init__(self):
        r"""
        :param DealName: 计费订单ID（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）
        :type DealName: str
        :param DealNames: 计费订单ID列表，可以一次查询若干条订单ID对应资源信息（如果计费还没回调业务发货，可能出现错误码InvalidParameterValue.DealNameNotFound，这种情况需要业务重试DescribeResourcesByDealName接口直到成功）
        :type DealNames: list of str
        """
        self.DealName = None
        self.DealNames = None


    def _deserialize(self, params):
        self.DealName = params.get("DealName")
        self.DealNames = params.get("DealNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByDealNameResponse(AbstractModel):
    """DescribeResourcesByDealName返回参数结构体

    """

    def __init__(self):
        r"""
        :param BillingResourceInfos: 计费资源id信息数组
        :type BillingResourceInfos: list of BillingResourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BillingResourceInfos = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BillingResourceInfos") is not None:
            self.BillingResourceInfos = []
            for item in params.get("BillingResourceInfos"):
                obj = BillingResourceInfo()
                obj._deserialize(item)
                self.BillingResourceInfos.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeRangeRequest(AbstractModel):
    """DescribeRollbackTimeRange请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeRangeResponse(AbstractModel):
    """DescribeRollbackTimeRange返回参数结构体

    """

    def __init__(self):
        r"""
        :param TimeRangeStart: 有效回归时间范围开始时间点（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeRangeStart: str
        :param TimeRangeEnd: 有效回归时间范围结束时间点（已废弃）
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeRangeEnd: str
        :param RollbackTimeRanges: 可回档时间范围
        :type RollbackTimeRanges: list of RollbackTimeRange
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None
        self.RollbackTimeRanges = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        if params.get("RollbackTimeRanges") is not None:
            self.RollbackTimeRanges = []
            for item in params.get("RollbackTimeRanges"):
                obj = RollbackTimeRange()
                obj._deserialize(item)
                self.RollbackTimeRanges.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRollbackTimeValidityRequest(AbstractModel):
    """DescribeRollbackTimeValidity请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ExpectTime: 期望回滚的时间点
        :type ExpectTime: str
        :param ExpectTimeThresh: 回滚时间点的允许误差范围
        :type ExpectTimeThresh: int
        """
        self.ClusterId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRollbackTimeValidityResponse(AbstractModel):
    """DescribeRollbackTimeValidity返回参数结构体

    """

    def __init__(self):
        r"""
        :param PoolId: 存储poolID
        :type PoolId: int
        :param QueryId: 回滚任务ID，后续按该时间点回滚时，需要传入
        :type QueryId: int
        :param Status: 时间点是否有效：pass，检测通过；fail，检测失败
        :type Status: str
        :param SuggestTime: 建议时间点，在Status为fail时，该值才有效
        :type SuggestTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PoolId = None
        self.QueryId = None
        self.Status = None
        self.SuggestTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PoolId = params.get("PoolId")
        self.QueryId = params.get("QueryId")
        self.Status = params.get("Status")
        self.SuggestTime = params.get("SuggestTime")
        self.RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    """DescribeZones请求参数结构体

    """

    def __init__(self):
        r"""
        :param IncludeVirtualZones: 是否包含虚拟区
        :type IncludeVirtualZones: bool
        :param ShowPermission: 是否展示地域下所有可用区，并显示用户每个可用区权限
        :type ShowPermission: bool
        """
        self.IncludeVirtualZones = None
        self.ShowPermission = None


    def _deserialize(self, params):
        self.IncludeVirtualZones = params.get("IncludeVirtualZones")
        self.ShowPermission = params.get("ShowPermission")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeZonesResponse(AbstractModel):
    """DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param RegionSet: 地域信息
        :type RegionSet: list of SaleRegion
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RegionSet") is not None:
            self.RegionSet = []
            for item in params.get("RegionSet"):
                obj = SaleRegion()
                obj._deserialize(item)
                self.RegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: 实例组ID数组
        :type InstanceIds: list of str
        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组ID组成的数组。
        :type SecurityGroupIds: list of str
        :param Zone: 可用区
        :type Zone: str
        """
        self.InstanceIds = None
        self.SecurityGroupIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ExportInstanceSlowQueriesRequest(AbstractModel):
    """ExportInstanceSlowQueries请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param StartTime: 事务开始最早时间
        :type StartTime: str
        :param EndTime: 事务开始最晚时间
        :type EndTime: str
        :param Limit: 限制条数
        :type Limit: int
        :param Offset: 偏移量
        :type Offset: int
        :param Username: 用户名
        :type Username: str
        :param Host: 客户端host
        :type Host: str
        :param Database: 数据库名
        :type Database: str
        :param FileType: 文件类型，可选值：csv, original
        :type FileType: str
        """
        self.InstanceId = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Offset = None
        self.Username = None
        self.Host = None
        self.Database = None
        self.FileType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.Username = params.get("Username")
        self.Host = params.get("Host")
        self.Database = params.get("Database")
        self.FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExportInstanceSlowQueriesResponse(AbstractModel):
    """ExportInstanceSlowQueries返回参数结构体

    """

    def __init__(self):
        r"""
        :param FileContent: 慢查询导出内容
        :type FileContent: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FileContent = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FileContent = params.get("FileContent")
        self.RequestId = params.get("RequestId")


class GrantAccountPrivilegesRequest(AbstractModel):
    """GrantAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param DbTablePrivileges: 数据库表权限码数组
        :type DbTablePrivileges: list of str
        :param DbTables: 数据库表信息
        :type DbTables: list of DbTable
        """
        self.ClusterId = None
        self.Account = None
        self.DbTablePrivileges = None
        self.DbTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self.Account = InputAccount()
            self.Account._deserialize(params.get("Account"))
        self.DbTablePrivileges = params.get("DbTablePrivileges")
        if params.get("DbTables") is not None:
            self.DbTables = []
            for item in params.get("DbTables"):
                obj = DbTable()
                obj._deserialize(item)
                self.DbTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GrantAccountPrivilegesResponse(AbstractModel):
    """GrantAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class InputAccount(AbstractModel):
    """账号，包含accountName和host

    """

    def __init__(self):
        r"""
        :param AccountName: 账号
        :type AccountName: str
        :param Host: 主机，默认‘%’
        :type Host: str
        """
        self.AccountName = None
        self.Host = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateRequest(AbstractModel):
    """InquirePriceCreate请求参数结构体

    """

    def __init__(self):
        r"""
        :param Zone: 可用区,每个地域提供最佳实践
        :type Zone: str
        :param GoodsNum: 购买计算节点个数
        :type GoodsNum: int
        :param InstancePayMode: 实例购买类型，可选值为：PREPAID, POSTPAID, SERVERLESS
        :type InstancePayMode: str
        :param StoragePayMode: 存储购买类型，可选值为：PREPAID, POSTPAID
        :type StoragePayMode: str
        :param Cpu: CPU核数，PREPAID与POSTPAID实例类型必传
        :type Cpu: int
        :param Memory: 内存大小，单位G，PREPAID与POSTPAID实例类型必传
        :type Memory: int
        :param Ccu: Ccu大小，serverless类型必传
        :type Ccu: float
        :param StorageLimit: 存储大小，PREPAID存储类型必传
        :type StorageLimit: int
        :param TimeSpan: 购买时长，PREPAID购买类型必传
        :type TimeSpan: int
        :param TimeUnit: 时长单位，可选值为：m,d。PREPAID购买类型必传
        :type TimeUnit: str
        """
        self.Zone = None
        self.GoodsNum = None
        self.InstancePayMode = None
        self.StoragePayMode = None
        self.Cpu = None
        self.Memory = None
        self.Ccu = None
        self.StorageLimit = None
        self.TimeSpan = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.GoodsNum = params.get("GoodsNum")
        self.InstancePayMode = params.get("InstancePayMode")
        self.StoragePayMode = params.get("StoragePayMode")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.Ccu = params.get("Ccu")
        self.StorageLimit = params.get("StorageLimit")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateResponse(AbstractModel):
    """InquirePriceCreate返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstancePrice: 实例价格
        :type InstancePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param StoragePrice: 存储价格
        :type StoragePrice: :class:`tencentcloud.cynosdb.v20190107.models.TradePrice`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstancePrice = None
        self.StoragePrice = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = TradePrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("StoragePrice") is not None:
            self.StoragePrice = TradePrice()
            self.StoragePrice._deserialize(params.get("StoragePrice"))
        self.RequestId = params.get("RequestId")


class InquirePriceRenewRequest(AbstractModel):
    """InquirePriceRenew请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param TimeSpan: 购买时长,与TimeUnit组合才能生效
        :type TimeSpan: int
        :param TimeUnit: 购买时长单位, 与TimeSpan组合生效，可选:日:d,月:m
        :type TimeUnit: str
        """
        self.ClusterId = None
        self.TimeSpan = None
        self.TimeUnit = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.TimeSpan = params.get("TimeSpan")
        self.TimeUnit = params.get("TimeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceRenewResponse(AbstractModel):
    """InquirePriceRenew返回参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIds: 实例ID列表
        :type InstanceIds: list of str
        :param Prices: 对应的询价结果数组
        :type Prices: list of TradePrice
        :param InstanceRealTotalPrice: 续费计算节点的总价格
        :type InstanceRealTotalPrice: int
        :param StorageRealTotalPrice: 续费存储节点的总价格
        :type StorageRealTotalPrice: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ClusterId = None
        self.InstanceIds = None
        self.Prices = None
        self.InstanceRealTotalPrice = None
        self.StorageRealTotalPrice = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIds = params.get("InstanceIds")
        if params.get("Prices") is not None:
            self.Prices = []
            for item in params.get("Prices"):
                obj = TradePrice()
                obj._deserialize(item)
                self.Prices.append(obj)
        self.InstanceRealTotalPrice = params.get("InstanceRealTotalPrice")
        self.StorageRealTotalPrice = params.get("StorageRealTotalPrice")
        self.RequestId = params.get("RequestId")


class InstanceAuditRule(AbstractModel):
    """实例的审计规则详情，DescribeAuditRuleWithInstanceIds接口的出参。

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param AuditRule: 是否是规则审计。true-规则审计，false-全审计。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditRule: bool
        :param AuditRuleFilters: 审计规则详情。仅当AuditRule=true时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditRuleFilters: list of AuditRuleFilters
        """
        self.InstanceId = None
        self.AuditRule = None
        self.AuditRuleFilters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.AuditRule = params.get("AuditRule")
        if params.get("AuditRuleFilters") is not None:
            self.AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self.AuditRuleFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInitInfo(AbstractModel):
    """实例初始化配置信息

    """

    def __init__(self):
        r"""
        :param Cpu: 实例cpu
        :type Cpu: int
        :param Memory: 实例内存
        :type Memory: int
        :param InstanceType: 实例类型 rw/ro
        :type InstanceType: str
        :param InstanceCount: 实例个数,范围[1,15]
        :type InstanceCount: int
        """
        self.Cpu = None
        self.Memory = None
        self.InstanceType = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSpec(AbstractModel):
    """实例可售卖规格详细信息，创建实例时Cpu/Memory确定实例规格，存储可选大小为[MinStorageSize,MaxStorageSize]

    """

    def __init__(self):
        r"""
        :param Cpu: 实例CPU，单位：核
        :type Cpu: int
        :param Memory: 实例内存，单位：GB
        :type Memory: int
        :param MaxStorageSize: 实例最大可用存储，单位：GB
        :type MaxStorageSize: int
        :param MinStorageSize: 实例最小可用存储，单位：GB
        :type MinStorageSize: int
        :param HasStock: 是否有库存
        :type HasStock: bool
        :param MachineType: 机器类型
        :type MachineType: str
        :param MaxIops: 最大IOPS
        :type MaxIops: int
        :param MaxIoBandWidth: 最大IO带宽
        :type MaxIoBandWidth: int
        :param ZoneStockInfos: 地域库存信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneStockInfos: list of ZoneStockInfo
        :param StockCount: 库存数量
注意：此字段可能返回 null，表示取不到有效值。
        :type StockCount: int
        """
        self.Cpu = None
        self.Memory = None
        self.MaxStorageSize = None
        self.MinStorageSize = None
        self.HasStock = None
        self.MachineType = None
        self.MaxIops = None
        self.MaxIoBandWidth = None
        self.ZoneStockInfos = None
        self.StockCount = None


    def _deserialize(self, params):
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.MaxStorageSize = params.get("MaxStorageSize")
        self.MinStorageSize = params.get("MinStorageSize")
        self.HasStock = params.get("HasStock")
        self.MachineType = params.get("MachineType")
        self.MaxIops = params.get("MaxIops")
        self.MaxIoBandWidth = params.get("MaxIoBandWidth")
        if params.get("ZoneStockInfos") is not None:
            self.ZoneStockInfos = []
            for item in params.get("ZoneStockInfos"):
                obj = ZoneStockInfo()
                obj._deserialize(item)
                self.ZoneStockInfos.append(obj)
        self.StockCount = params.get("StockCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterRequest(AbstractModel):
    """IsolateCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param DbType: 该参数已废用
        :type DbType: str
        """
        self.ClusterId = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateClusterResponse(AbstractModel):
    """IsolateCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param DealNames: 退款订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class IsolateInstanceRequest(AbstractModel):
    """IsolateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 实例ID数组
        :type InstanceIdList: list of str
        :param DbType: 该参数已废弃
        :type DbType: str
        """
        self.ClusterId = None
        self.InstanceIdList = None
        self.DbType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.DbType = params.get("DbType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IsolateInstanceResponse(AbstractModel):
    """IsolateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流id
        :type FlowId: int
        :param DealNames: 隔离实例的订单id（预付费实例）
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class ModifiableInfo(AbstractModel):
    """参数是否可修改的详细信息

    """


class ModifyAccountParamsRequest(AbstractModel):
    """ModifyAccountParams请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id，不超过32个字符
        :type ClusterId: str
        :param Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param AccountParams: 数据库表权限数组,当前仅支持参数：max_user_connections，max_user_connections不能大于10240
        :type AccountParams: list of AccountParam
        """
        self.ClusterId = None
        self.Account = None
        self.AccountParams = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self.Account = InputAccount()
            self.Account._deserialize(params.get("Account"))
        if params.get("AccountParams") is not None:
            self.AccountParams = []
            for item in params.get("AccountParams"):
                obj = AccountParam()
                obj._deserialize(item)
                self.AccountParams.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAccountParamsResponse(AbstractModel):
    """ModifyAccountParams返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAuditRuleTemplatesRequest(AbstractModel):
    """ModifyAuditRuleTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleTemplateIds: 审计规则模版ID。
        :type RuleTemplateIds: list of str
        :param RuleFilters: 修改后的审计规则。
        :type RuleFilters: list of RuleFilters
        :param RuleTemplateName: 修改后的规则模版名称。
        :type RuleTemplateName: str
        :param Description: 修改后的规则模版描述。
        :type Description: str
        """
        self.RuleTemplateIds = None
        self.RuleFilters = None
        self.RuleTemplateName = None
        self.Description = None


    def _deserialize(self, params):
        self.RuleTemplateIds = params.get("RuleTemplateIds")
        if params.get("RuleFilters") is not None:
            self.RuleFilters = []
            for item in params.get("RuleFilters"):
                obj = RuleFilters()
                obj._deserialize(item)
                self.RuleFilters.append(obj)
        self.RuleTemplateName = params.get("RuleTemplateName")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditRuleTemplatesResponse(AbstractModel):
    """ModifyAuditRuleTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAuditServiceRequest(AbstractModel):
    """ModifyAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param LogExpireDay: 日志保留时长。
        :type LogExpireDay: int
        :param HighLogExpireDay: 高频日志保留时长。
        :type HighLogExpireDay: int
        :param AuditAll: 修改实例审计规则为全审计。
        :type AuditAll: bool
        :param AuditRuleFilters: 规则审计。
        :type AuditRuleFilters: list of AuditRuleFilters
        :param RuleTemplateIds: 规则模版ID。
        :type RuleTemplateIds: list of str
        """
        self.InstanceId = None
        self.LogExpireDay = None
        self.HighLogExpireDay = None
        self.AuditAll = None
        self.AuditRuleFilters = None
        self.RuleTemplateIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogExpireDay = params.get("LogExpireDay")
        self.HighLogExpireDay = params.get("HighLogExpireDay")
        self.AuditAll = params.get("AuditAll")
        if params.get("AuditRuleFilters") is not None:
            self.AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self.AuditRuleFilters.append(obj)
        self.RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuditServiceResponse(AbstractModel):
    """ModifyAuditService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupConfigRequest(AbstractModel):
    """ModifyBackupConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ReserveDuration: 表示保留备份时长, 单位秒，超过该时间将被清理, 七天表示为3600*24*7=604800，最大为158112000
        :type ReserveDuration: int
        :param BackupTimeBeg: 表示全备开始时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeBeg: int
        :param BackupTimeEnd: 表示全备结束时间，[0-24*3600]， 如0:00, 1:00, 2:00 分别为 0，3600， 7200
        :type BackupTimeEnd: int
        :param BackupFreq: 该参数目前不支持修改，无需填写。备份频率，长度为7的数组，分别对应周一到周日的备份方式，full-全量备份，increment-增量备份
        :type BackupFreq: list of str
        :param BackupType: 该参数目前不支持修改，无需填写。备份方式，logic-逻辑备份，snapshot-快照备份
        :type BackupType: str
        """
        self.ClusterId = None
        self.ReserveDuration = None
        self.BackupTimeBeg = None
        self.BackupTimeEnd = None
        self.BackupFreq = None
        self.BackupType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ReserveDuration = params.get("ReserveDuration")
        self.BackupTimeBeg = params.get("BackupTimeBeg")
        self.BackupTimeEnd = params.get("BackupTimeEnd")
        self.BackupFreq = params.get("BackupFreq")
        self.BackupType = params.get("BackupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupConfigResponse(AbstractModel):
    """ModifyBackupConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBackupNameRequest(AbstractModel):
    """ModifyBackupName请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param BackupId: 备份文件ID
        :type BackupId: int
        :param BackupName: 备注名，长度不能超过60个字符
        :type BackupName: str
        """
        self.ClusterId = None
        self.BackupId = None
        self.BackupName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.BackupId = params.get("BackupId")
        self.BackupName = params.get("BackupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBackupNameResponse(AbstractModel):
    """ModifyBackupName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterNameRequest(AbstractModel):
    """ModifyClusterName请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名
        :type ClusterName: str
        """
        self.ClusterId = None
        self.ClusterName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterNameResponse(AbstractModel):
    """ModifyClusterName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyClusterParamRequest(AbstractModel):
    """ModifyClusterParam请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ParamList: 要修改的参数列表。每一个元素是ParamName、CurrentValue和OldValue的组合。ParamName是参数名称，CurrentValue是当前值，OldValue是之前值且不做校验
        :type ParamList: list of ParamItem
        :param IsInMaintainPeriod: 维护期间执行-yes,立即执行-no
        :type IsInMaintainPeriod: str
        """
        self.ClusterId = None
        self.ParamList = None
        self.IsInMaintainPeriod = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("ParamList") is not None:
            self.ParamList = []
            for item in params.get("ParamList"):
                obj = ParamItem()
                obj._deserialize(item)
                self.ParamList.append(obj)
        self.IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterParamResponse(AbstractModel):
    """ModifyClusterParam返回参数结构体

    """

    def __init__(self):
        r"""
        :param AsyncRequestId: 异步请求Id，用于查询结果
        :type AsyncRequestId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AsyncRequestId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AsyncRequestId = params.get("AsyncRequestId")
        self.RequestId = params.get("RequestId")


class ModifyClusterSlaveZoneRequest(AbstractModel):
    """ModifyClusterSlaveZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param OldSlaveZone: 旧从可用区
        :type OldSlaveZone: str
        :param NewSlaveZone: 新从可用区
        :type NewSlaveZone: str
        """
        self.ClusterId = None
        self.OldSlaveZone = None
        self.NewSlaveZone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldSlaveZone = params.get("OldSlaveZone")
        self.NewSlaveZone = params.get("NewSlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterSlaveZoneResponse(AbstractModel):
    """ModifyClusterSlaveZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步FlowId
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ModifyClusterStorageRequest(AbstractModel):
    """ModifyClusterStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param NewStorageLimit: 集群新存储大小（单位G）
        :type NewStorageLimit: int
        :param OldStorageLimit: 集群原存储大小（单位G）
        :type OldStorageLimit: int
        :param DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        """
        self.ClusterId = None
        self.NewStorageLimit = None
        self.OldStorageLimit = None
        self.DealMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NewStorageLimit = params.get("NewStorageLimit")
        self.OldStorageLimit = params.get("OldStorageLimit")
        self.DealMode = params.get("DealMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyClusterStorageResponse(AbstractModel):
    """ModifyClusterStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param DealNames: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.BigDealIds = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.BigDealIds = params.get("BigDealIds")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class ModifyDBInstanceSecurityGroupsRequest(AbstractModel):
    """ModifyDBInstanceSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例组ID
        :type InstanceId: str
        :param SecurityGroupIds: 要修改的安全组ID列表，一个或者多个安全组ID组成的数组。
        :type SecurityGroupIds: list of str
        :param Zone: 可用区
        :type Zone: str
        """
        self.InstanceId = None
        self.SecurityGroupIds = None
        self.Zone = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDBInstanceSecurityGroupsResponse(AbstractModel):
    """ModifyDBInstanceSecurityGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstanceNameRequest(AbstractModel):
    """ModifyInstanceName请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        """
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceNameResponse(AbstractModel):
    """ModifyInstanceName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMaintainPeriodConfigRequest(AbstractModel):
    """ModifyMaintainPeriodConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param MaintainStartTime: 维护开始时间，单位为秒，如3:00为10800
        :type MaintainStartTime: int
        :param MaintainDuration: 维护持续时间，单位为秒，如1小时为3600
        :type MaintainDuration: int
        :param MaintainWeekDays: 每周维护日期，日期取值范围[Mon, Tue, Wed, Thu, Fri, Sat, Sun]
        :type MaintainWeekDays: list of str
        """
        self.InstanceId = None
        self.MaintainStartTime = None
        self.MaintainDuration = None
        self.MaintainWeekDays = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.MaintainStartTime = params.get("MaintainStartTime")
        self.MaintainDuration = params.get("MaintainDuration")
        self.MaintainWeekDays = params.get("MaintainWeekDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMaintainPeriodConfigResponse(AbstractModel):
    """ModifyMaintainPeriodConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyParamItem(AbstractModel):
    """修改的实例参数信息

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名
        :type ParamName: str
        :param CurrentValue: 参数当前值
        :type CurrentValue: str
        :param OldValue: 参数旧值（只在出参时有用）
注意：此字段可能返回 null，表示取不到有效值。
        :type OldValue: str
        """
        self.ParamName = None
        self.CurrentValue = None
        self.OldValue = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.CurrentValue = params.get("CurrentValue")
        self.OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVipVportRequest(AbstractModel):
    """ModifyVipVport请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param InstanceGrpId: 实例组id
        :type InstanceGrpId: str
        :param Vip: 需要修改的目的ip
        :type Vip: str
        :param Vport: 需要修改的目的端口
        :type Vport: int
        :param DbType: 数据库类型，取值范围: 
<li> MYSQL </li>
        :type DbType: str
        :param OldIpReserveHours: 旧ip回收前的保留时间，单位小时，0表示立即回收
        :type OldIpReserveHours: int
        """
        self.ClusterId = None
        self.InstanceGrpId = None
        self.Vip = None
        self.Vport = None
        self.DbType = None
        self.OldIpReserveHours = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceGrpId = params.get("InstanceGrpId")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.DbType = params.get("DbType")
        self.OldIpReserveHours = params.get("OldIpReserveHours")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVipVportResponse(AbstractModel):
    """ModifyVipVport返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class Module(AbstractModel):
    """系统支持的模块

    """

    def __init__(self):
        r"""
        :param IsDisable: 是否支持，可选值:yes,no
        :type IsDisable: str
        :param ModuleName: 模块名
        :type ModuleName: str
        """
        self.IsDisable = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.IsDisable = params.get("IsDisable")
        self.ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetAddr(AbstractModel):
    """网络信息

    """

    def __init__(self):
        r"""
        :param Vip: 内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param Vport: 内网端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param WanDomain: 外网域名
注意：此字段可能返回 null，表示取不到有效值。
        :type WanDomain: str
        :param WanPort: 外网端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type WanPort: int
        :param NetType: 网络类型（ro-只读,rw/ha-读写）
注意：此字段可能返回 null，表示取不到有效值。
        :type NetType: str
        :param UniqSubnetId: 子网ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqSubnetId: str
        :param UniqVpcId: 私有网络ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param Description: 描述信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param WanIP: 外网IP
注意：此字段可能返回 null，表示取不到有效值。
        :type WanIP: str
        :param WanStatus: 外网状态
注意：此字段可能返回 null，表示取不到有效值。
        :type WanStatus: str
        """
        self.Vip = None
        self.Vport = None
        self.WanDomain = None
        self.WanPort = None
        self.NetType = None
        self.UniqSubnetId = None
        self.UniqVpcId = None
        self.Description = None
        self.WanIP = None
        self.WanStatus = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.WanDomain = params.get("WanDomain")
        self.WanPort = params.get("WanPort")
        self.NetType = params.get("NetType")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Description = params.get("Description")
        self.WanIP = params.get("WanIP")
        self.WanStatus = params.get("WanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewAccount(AbstractModel):
    """x08新创建的账号

    """

    def __init__(self):
        r"""
        :param AccountName: 账户名，包含字母数字_,以字母开头，字母或数字结尾，长度1-16
        :type AccountName: str
        :param AccountPassword: 密码，密码长度范围为8到64个字符
        :type AccountPassword: str
        :param Host: 主机
        :type Host: str
        :param Description: 描述
        :type Description: str
        :param MaxUserConnections: 用户最大连接数，不能大于10240
        :type MaxUserConnections: int
        """
        self.AccountName = None
        self.AccountPassword = None
        self.Host = None
        self.Description = None
        self.MaxUserConnections = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.Host = params.get("Host")
        self.Description = params.get("Description")
        self.MaxUserConnections = params.get("MaxUserConnections")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ObjectTask(AbstractModel):
    """任务信息

    """

    def __init__(self):
        r"""
        :param TaskId: 任务自增ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: int
        :param TaskType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskType: str
        :param TaskStatus: 任务状态
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskStatus: str
        :param ObjectId: 任务ID（集群ID|实例组ID|实例ID）
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectId: str
        :param ObjectType: 任务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ObjectType: str
        """
        self.TaskId = None
        self.TaskType = None
        self.TaskStatus = None
        self.ObjectId = None
        self.ObjectType = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.TaskType = params.get("TaskType")
        self.TaskStatus = params.get("TaskStatus")
        self.ObjectId = params.get("ObjectId")
        self.ObjectType = params.get("ObjectType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterRequest(AbstractModel):
    """OfflineCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineClusterResponse(AbstractModel):
    """OfflineCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OfflineInstanceRequest(AbstractModel):
    """OfflineInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param InstanceIdList: 实例ID数组
        :type InstanceIdList: list of str
        """
        self.ClusterId = None
        self.InstanceIdList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.InstanceIdList = params.get("InstanceIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OfflineInstanceResponse(AbstractModel):
    """OfflineInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class OldAddrInfo(AbstractModel):
    """数据库地址

    """

    def __init__(self):
        r"""
        :param Vip: IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Vip: str
        :param Vport: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Vport: int
        :param ReturnTime: 期望执行回收时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnTime: str
        """
        self.Vip = None
        self.Vport = None
        self.ReturnTime = None


    def _deserialize(self, params):
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.ReturnTime = params.get("ReturnTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceRequest(AbstractModel):
    """OpenAuditService请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID。
        :type InstanceId: str
        :param LogExpireDay: 日志保留时长。
        :type LogExpireDay: int
        :param HighLogExpireDay: 高频日志保留时长。
        :type HighLogExpireDay: int
        :param AuditRuleFilters: 审计规则。同RuleTemplateIds都不填是全审计。
        :type AuditRuleFilters: list of AuditRuleFilters
        :param RuleTemplateIds: 规则模版ID。同AuditRuleFilters都不填是全审计。
        :type RuleTemplateIds: list of str
        """
        self.InstanceId = None
        self.LogExpireDay = None
        self.HighLogExpireDay = None
        self.AuditRuleFilters = None
        self.RuleTemplateIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.LogExpireDay = params.get("LogExpireDay")
        self.HighLogExpireDay = params.get("HighLogExpireDay")
        if params.get("AuditRuleFilters") is not None:
            self.AuditRuleFilters = []
            for item in params.get("AuditRuleFilters"):
                obj = AuditRuleFilters()
                obj._deserialize(item)
                self.AuditRuleFilters.append(obj)
        self.RuleTemplateIds = params.get("RuleTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenAuditServiceResponse(AbstractModel):
    """OpenAuditService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ParamInfo(AbstractModel):
    """参数信息

    """

    def __init__(self):
        r"""
        :param CurrentValue: 当前值
        :type CurrentValue: str
        :param Default: 默认值
        :type Default: str
        :param EnumValue: 参数为enum/string/bool时，可选值列表
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param Max: 参数类型为float/integer时的最大值
        :type Max: str
        :param Min: 参数类型为float/integer时的最小值
        :type Min: str
        :param ParamName: 参数名称
        :type ParamName: str
        :param NeedReboot: 是否需要重启生效
        :type NeedReboot: int
        :param ParamType: 参数类型：integer/float/string/enum/bool
        :type ParamType: str
        :param MatchType: 匹配类型，multiVal, regex在参数类型是string时使用
        :type MatchType: str
        :param MatchValue: 匹配目标值，当multiVal时，各个key用;分割
        :type MatchValue: str
        :param Description: 参数描述
        :type Description: str
        :param IsGlobal: 是否为全局参数
注意：此字段可能返回 null，表示取不到有效值。
        :type IsGlobal: int
        :param ModifiableInfo: 参数是否可修改
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiableInfo: :class:`tencentcloud.cynosdb.v20190107.models.ModifiableInfo`
        :param IsFunc: 是否为函数
注意：此字段可能返回 null，表示取不到有效值。
        :type IsFunc: bool
        :param Func: 函数
注意：此字段可能返回 null，表示取不到有效值。
        :type Func: str
        """
        self.CurrentValue = None
        self.Default = None
        self.EnumValue = None
        self.Max = None
        self.Min = None
        self.ParamName = None
        self.NeedReboot = None
        self.ParamType = None
        self.MatchType = None
        self.MatchValue = None
        self.Description = None
        self.IsGlobal = None
        self.ModifiableInfo = None
        self.IsFunc = None
        self.Func = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.Default = params.get("Default")
        self.EnumValue = params.get("EnumValue")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.ParamName = params.get("ParamName")
        self.NeedReboot = params.get("NeedReboot")
        self.ParamType = params.get("ParamType")
        self.MatchType = params.get("MatchType")
        self.MatchValue = params.get("MatchValue")
        self.Description = params.get("Description")
        self.IsGlobal = params.get("IsGlobal")
        if params.get("ModifiableInfo") is not None:
            self.ModifiableInfo = ModifiableInfo()
            self.ModifiableInfo._deserialize(params.get("ModifiableInfo"))
        self.IsFunc = params.get("IsFunc")
        self.Func = params.get("Func")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamItem(AbstractModel):
    """修改参数时，传入参数描述

    """

    def __init__(self):
        r"""
        :param ParamName: 参数名称
        :type ParamName: str
        :param CurrentValue: 当前值
        :type CurrentValue: str
        :param OldValue: 原有值
        :type OldValue: str
        """
        self.ParamName = None
        self.CurrentValue = None
        self.OldValue = None


    def _deserialize(self, params):
        self.ParamName = params.get("ParamName")
        self.CurrentValue = params.get("CurrentValue")
        self.OldValue = params.get("OldValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamTemplateListInfo(AbstractModel):
    """参数模板信息

    """

    def __init__(self):
        r"""
        :param Id: 参数模板ID
        :type Id: int
        :param TemplateName: 参数模板名称
        :type TemplateName: str
        :param TemplateDescription: 参数模板描述
        :type TemplateDescription: str
        :param EngineVersion: 引擎版本
        :type EngineVersion: str
        :param DbMode: 数据库类型，可选值：NORMAL，SERVERLESS
        :type DbMode: str
        :param ParamInfoSet: 参数模板详情
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamInfoSet: list of TemplateParamInfo
        """
        self.Id = None
        self.TemplateName = None
        self.TemplateDescription = None
        self.EngineVersion = None
        self.DbMode = None
        self.ParamInfoSet = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.TemplateName = params.get("TemplateName")
        self.TemplateDescription = params.get("TemplateDescription")
        self.EngineVersion = params.get("EngineVersion")
        self.DbMode = params.get("DbMode")
        if params.get("ParamInfoSet") is not None:
            self.ParamInfoSet = []
            for item in params.get("ParamInfoSet"):
                obj = TemplateParamInfo()
                obj._deserialize(item)
                self.ParamInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessRequest(AbstractModel):
    """PauseServerless请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ForcePause: 是否强制暂停，忽略当前的用户链接  0:不强制  1:强制， 默认为1
        :type ForcePause: int
        """
        self.ClusterId = None
        self.ForcePause = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ForcePause = params.get("ForcePause")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseServerlessResponse(AbstractModel):
    """PauseServerless返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class PolicyRule(AbstractModel):
    """安全组规则

    """

    def __init__(self):
        r"""
        :param Action: 策略，ACCEPT或者DROP
        :type Action: str
        :param CidrIp: 来源Ip或Ip段，例如192.168.0.0/16
        :type CidrIp: str
        :param PortRange: 端口
        :type PortRange: str
        :param IpProtocol: 网络协议，支持udp、tcp等
        :type IpProtocol: str
        :param ServiceModule: 协议端口ID或者协议端口组ID。
        :type ServiceModule: str
        :param AddressModule: IP地址ID或者ID地址组ID。
        :type AddressModule: str
        :param Id: id
        :type Id: str
        :param Desc: 描述
        :type Desc: str
        """
        self.Action = None
        self.CidrIp = None
        self.PortRange = None
        self.IpProtocol = None
        self.ServiceModule = None
        self.AddressModule = None
        self.Id = None
        self.Desc = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CidrIp = params.get("CidrIp")
        self.PortRange = params.get("PortRange")
        self.IpProtocol = params.get("IpProtocol")
        self.ServiceModule = params.get("ServiceModule")
        self.AddressModule = params.get("AddressModule")
        self.Id = params.get("Id")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryFilter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param Names: 搜索字段，目前支持："InstanceId", "ProjectId", "InstanceName", "Vip"
        :type Names: list of str
        :param Values: 搜索字符串
        :type Values: list of str
        :param ExactMatch: 是否精确匹配
        :type ExactMatch: bool
        :param Name: 搜索字段
        :type Name: str
        :param Operator: 操作符
        :type Operator: str
        """
        self.Names = None
        self.Values = None
        self.ExactMatch = None
        self.Name = None
        self.Operator = None


    def _deserialize(self, params):
        self.Names = params.get("Names")
        self.Values = params.get("Values")
        self.ExactMatch = params.get("ExactMatch")
        self.Name = params.get("Name")
        self.Operator = params.get("Operator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveClusterSlaveZoneRequest(AbstractModel):
    """RemoveClusterSlaveZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param SlaveZone: 从可用区
        :type SlaveZone: str
        """
        self.ClusterId = None
        self.SlaveZone = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.SlaveZone = params.get("SlaveZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveClusterSlaveZoneResponse(AbstractModel):
    """RemoveClusterSlaveZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步FlowId
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ResetAccountPasswordRequest(AbstractModel):
    """ResetAccountPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccountName: 数据库账号名
        :type AccountName: str
        :param AccountPassword: 数据库账号新密码
        :type AccountPassword: str
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param Host: 主机，不填默认为"%"
        :type Host: str
        """
        self.AccountName = None
        self.AccountPassword = None
        self.ClusterId = None
        self.Host = None


    def _deserialize(self, params):
        self.AccountName = params.get("AccountName")
        self.AccountPassword = params.get("AccountPassword")
        self.ClusterId = params.get("ClusterId")
        self.Host = params.get("Host")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAccountPasswordResponse(AbstractModel):
    """ResetAccountPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RestartInstanceRequest(AbstractModel):
    """RestartInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestartInstanceResponse(AbstractModel):
    """RestartInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务id
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class ResumeServerlessRequest(AbstractModel):
    """ResumeServerless请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        """
        self.ClusterId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeServerlessResponse(AbstractModel):
    """ResumeServerless返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步流程ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RevokeAccountPrivilegesRequest(AbstractModel):
    """RevokeAccountPrivileges请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Account: 账号信息
        :type Account: :class:`tencentcloud.cynosdb.v20190107.models.InputAccount`
        :param DbTablePrivileges: 数据库表权限数组
        :type DbTablePrivileges: list of str
        :param DbTables: 数据库表信息
        :type DbTables: list of DbTable
        """
        self.ClusterId = None
        self.Account = None
        self.DbTablePrivileges = None
        self.DbTables = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        if params.get("Account") is not None:
            self.Account = InputAccount()
            self.Account._deserialize(params.get("Account"))
        self.DbTablePrivileges = params.get("DbTablePrivileges")
        if params.get("DbTables") is not None:
            self.DbTables = []
            for item in params.get("DbTables"):
                obj = DbTable()
                obj._deserialize(item)
                self.DbTables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeAccountPrivilegesResponse(AbstractModel):
    """RevokeAccountPrivileges返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RollBackClusterRequest(AbstractModel):
    """RollBackCluster请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param RollbackStrategy: 回档策略 timeRollback-按时间点回档 snapRollback-按备份文件回档
        :type RollbackStrategy: str
        :param RollbackId: 回档ID
        :type RollbackId: int
        :param ExpectTime: 期望回档时间
        :type ExpectTime: str
        :param ExpectTimeThresh: 期望阈值（已废弃）
        :type ExpectTimeThresh: int
        :param RollbackDatabases: 回档数据库列表
        :type RollbackDatabases: list of RollbackDatabase
        :param RollbackTables: 回档数据库表列表
        :type RollbackTables: list of RollbackTable
        :param RollbackMode: 按时间点回档模式，full: 普通; db: 快速; table: 极速  （默认是普通）
        :type RollbackMode: str
        """
        self.ClusterId = None
        self.RollbackStrategy = None
        self.RollbackId = None
        self.ExpectTime = None
        self.ExpectTimeThresh = None
        self.RollbackDatabases = None
        self.RollbackTables = None
        self.RollbackMode = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.RollbackStrategy = params.get("RollbackStrategy")
        self.RollbackId = params.get("RollbackId")
        self.ExpectTime = params.get("ExpectTime")
        self.ExpectTimeThresh = params.get("ExpectTimeThresh")
        if params.get("RollbackDatabases") is not None:
            self.RollbackDatabases = []
            for item in params.get("RollbackDatabases"):
                obj = RollbackDatabase()
                obj._deserialize(item)
                self.RollbackDatabases.append(obj)
        if params.get("RollbackTables") is not None:
            self.RollbackTables = []
            for item in params.get("RollbackTables"):
                obj = RollbackTable()
                obj._deserialize(item)
                self.RollbackTables.append(obj)
        self.RollbackMode = params.get("RollbackMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollBackClusterResponse(AbstractModel):
    """RollBackCluster返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 任务流ID
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class RollbackDatabase(AbstractModel):
    """回滚数据库信息

    """

    def __init__(self):
        r"""
        :param OldDatabase: 旧数据库名称
        :type OldDatabase: str
        :param NewDatabase: 新数据库名称
        :type NewDatabase: str
        """
        self.OldDatabase = None
        self.NewDatabase = None


    def _deserialize(self, params):
        self.OldDatabase = params.get("OldDatabase")
        self.NewDatabase = params.get("NewDatabase")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTable(AbstractModel):
    """回档数据库及表

    """

    def __init__(self):
        r"""
        :param Database: 数据库名称
        :type Database: str
        :param Tables: 数据库表
        :type Tables: list of RollbackTableInfo
        """
        self.Database = None
        self.Tables = None


    def _deserialize(self, params):
        self.Database = params.get("Database")
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = RollbackTableInfo()
                obj._deserialize(item)
                self.Tables.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTableInfo(AbstractModel):
    """回档表信息

    """

    def __init__(self):
        r"""
        :param OldTable: 旧表名称
        :type OldTable: str
        :param NewTable: 新表名称
        :type NewTable: str
        """
        self.OldTable = None
        self.NewTable = None


    def _deserialize(self, params):
        self.OldTable = params.get("OldTable")
        self.NewTable = params.get("NewTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RollbackTimeRange(AbstractModel):
    """可回档的时间范围

    """

    def __init__(self):
        r"""
        :param TimeRangeStart: 开始时间
        :type TimeRangeStart: str
        :param TimeRangeEnd: 结束时间
        :type TimeRangeEnd: str
        """
        self.TimeRangeStart = None
        self.TimeRangeEnd = None


    def _deserialize(self, params):
        self.TimeRangeStart = params.get("TimeRangeStart")
        self.TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleFilters(AbstractModel):
    """审计规则的规则过滤条件

    """

    def __init__(self):
        r"""
        :param Type: 审计规则过滤条件的参数名称。可选值：host – 客户端 IP；user – 数据库账户；dbName – 数据库名称；sqlType-SQL类型；sql-sql语句。
        :type Type: str
        :param Compare: 审计规则过滤条件的匹配类型。可选值：INC – 包含；EXC – 不包含；EQS – 等于；NEQ – 不等于。
        :type Compare: str
        :param Value: 审计规则过滤条件的匹配值。
        :type Value: list of str
        """
        self.Type = None
        self.Compare = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Compare = params.get("Compare")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleRegion(AbstractModel):
    """售卖地域信息

    """

    def __init__(self):
        r"""
        :param Region: 地域英文名
        :type Region: str
        :param RegionId: 地域数字ID
        :type RegionId: int
        :param RegionZh: 地域中文名
        :type RegionZh: str
        :param ZoneSet: 可售卖可用区列表
        :type ZoneSet: list of SaleZone
        :param DbType: 引擎类型
        :type DbType: str
        :param Modules: 地域模块支持情况
        :type Modules: list of Module
        """
        self.Region = None
        self.RegionId = None
        self.RegionZh = None
        self.ZoneSet = None
        self.DbType = None
        self.Modules = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionId = params.get("RegionId")
        self.RegionZh = params.get("RegionZh")
        if params.get("ZoneSet") is not None:
            self.ZoneSet = []
            for item in params.get("ZoneSet"):
                obj = SaleZone()
                obj._deserialize(item)
                self.ZoneSet.append(obj)
        self.DbType = params.get("DbType")
        if params.get("Modules") is not None:
            self.Modules = []
            for item in params.get("Modules"):
                obj = Module()
                obj._deserialize(item)
                self.Modules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SaleZone(AbstractModel):
    """售卖可用区信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区英文名
        :type Zone: str
        :param ZoneId: 可用区数字ID
        :type ZoneId: int
        :param ZoneZh: 可用区中文名
        :type ZoneZh: str
        :param IsSupportServerless: 是否支持serverless集群<br>
0:不支持<br>
1:支持
        :type IsSupportServerless: int
        :param IsSupportNormal: 是否支持普通集群<br>
0:不支持<br>
1:支持
        :type IsSupportNormal: int
        :param PhysicalZone: 物理区
        :type PhysicalZone: str
        :param HasPermission: 用户是否有可用区权限
注意：此字段可能返回 null，表示取不到有效值。
        :type HasPermission: bool
        :param IsWholeRdmaZone: 是否为全链路RDMA可用区
        :type IsWholeRdmaZone: str
        """
        self.Zone = None
        self.ZoneId = None
        self.ZoneZh = None
        self.IsSupportServerless = None
        self.IsSupportNormal = None
        self.PhysicalZone = None
        self.HasPermission = None
        self.IsWholeRdmaZone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.ZoneId = params.get("ZoneId")
        self.ZoneZh = params.get("ZoneZh")
        self.IsSupportServerless = params.get("IsSupportServerless")
        self.IsSupportNormal = params.get("IsSupportNormal")
        self.PhysicalZone = params.get("PhysicalZone")
        self.HasPermission = params.get("HasPermission")
        self.IsWholeRdmaZone = params.get("IsWholeRdmaZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterDatabasesRequest(AbstractModel):
    """SearchClusterDatabases请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Database: 数据库名
        :type Database: str
        :param MatchType: 是否精确搜索。
0: 模糊搜索 1:精确搜索 
默认为0
        :type MatchType: int
        """
        self.ClusterId = None
        self.Database = None
        self.MatchType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Database = params.get("Database")
        self.MatchType = params.get("MatchType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterDatabasesResponse(AbstractModel):
    """SearchClusterDatabases返回参数结构体

    """

    def __init__(self):
        r"""
        :param Databases: 数据库列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Databases: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Databases = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Databases = params.get("Databases")
        self.RequestId = params.get("RequestId")


class SearchClusterTablesRequest(AbstractModel):
    """SearchClusterTables请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群id
        :type ClusterId: str
        :param Database: 数据库名
        :type Database: str
        :param Table: 数据表名
        :type Table: str
        :param TableType: 数据表类型：
view：只返回 view，
base_table： 只返回基本表，
all：返回 view 和表
        :type TableType: str
        """
        self.ClusterId = None
        self.Database = None
        self.Table = None
        self.TableType = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.Database = params.get("Database")
        self.Table = params.get("Table")
        self.TableType = params.get("TableType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClusterTablesResponse(AbstractModel):
    """SearchClusterTables返回参数结构体

    """

    def __init__(self):
        r"""
        :param Tables: 数据表列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tables: list of DatabaseTables
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Tables = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Tables") is not None:
            self.Tables = []
            for item in params.get("Tables"):
                obj = DatabaseTables()
                obj._deserialize(item)
                self.Tables.append(obj)
        self.RequestId = params.get("RequestId")


class SecurityGroup(AbstractModel):
    """安全组详情

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param CreateTime: 创建时间，时间格式：yyyy-mm-dd hh:mm:ss
        :type CreateTime: str
        :param Inbound: 入站规则
        :type Inbound: list of PolicyRule
        :param Outbound: 出站规则
        :type Outbound: list of PolicyRule
        :param SecurityGroupId: 安全组ID
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称
        :type SecurityGroupName: str
        :param SecurityGroupRemark: 安全组备注
        :type SecurityGroupRemark: str
        """
        self.ProjectId = None
        self.CreateTime = None
        self.Inbound = None
        self.Outbound = None
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupRemark = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        if params.get("Inbound") is not None:
            self.Inbound = []
            for item in params.get("Inbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self.Inbound.append(obj)
        if params.get("Outbound") is not None:
            self.Outbound = []
            for item in params.get("Outbound"):
                obj = PolicyRule()
                obj._deserialize(item)
                self.Outbound.append(obj)
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupRemark = params.get("SecurityGroupRemark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagRequest(AbstractModel):
    """SetRenewFlag请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceIds: 需操作的实例ID
        :type ResourceIds: list of str
        :param AutoRenewFlag: 自动续费标志位，续费标记 0:正常续费  1:自动续费 2:到期不续
        :type AutoRenewFlag: int
        """
        self.ResourceIds = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetRenewFlagResponse(AbstractModel):
    """SetRenewFlag返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 操作成功实例数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class SlowQueriesItem(AbstractModel):
    """实例慢查询信息

    """

    def __init__(self):
        r"""
        :param Timestamp: 执行时间戳
        :type Timestamp: int
        :param QueryTime: 执行时长，单位秒
        :type QueryTime: float
        :param SqlText: sql语句
        :type SqlText: str
        :param UserHost: 客户端host
        :type UserHost: str
        :param UserName: 用户名
        :type UserName: str
        :param Database: 数据库名
        :type Database: str
        :param LockTime: 锁时长，单位秒
        :type LockTime: float
        :param RowsExamined: 扫描行数
        :type RowsExamined: int
        :param RowsSent: 返回行数
        :type RowsSent: int
        :param SqlTemplate: sql模版
        :type SqlTemplate: str
        :param SqlMd5: sql语句md5
        :type SqlMd5: str
        """
        self.Timestamp = None
        self.QueryTime = None
        self.SqlText = None
        self.UserHost = None
        self.UserName = None
        self.Database = None
        self.LockTime = None
        self.RowsExamined = None
        self.RowsSent = None
        self.SqlTemplate = None
        self.SqlMd5 = None


    def _deserialize(self, params):
        self.Timestamp = params.get("Timestamp")
        self.QueryTime = params.get("QueryTime")
        self.SqlText = params.get("SqlText")
        self.UserHost = params.get("UserHost")
        self.UserName = params.get("UserName")
        self.Database = params.get("Database")
        self.LockTime = params.get("LockTime")
        self.RowsExamined = params.get("RowsExamined")
        self.RowsSent = params.get("RowsSent")
        self.SqlTemplate = params.get("SqlTemplate")
        self.SqlMd5 = params.get("SqlMd5")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterVpcRequest(AbstractModel):
    """SwitchClusterVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param UniqVpcId: 字符串vpc id
        :type UniqVpcId: str
        :param UniqSubnetId: 字符串子网id
        :type UniqSubnetId: str
        :param OldIpReserveHours: 旧地址回收时间
        :type OldIpReserveHours: int
        """
        self.ClusterId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.OldIpReserveHours = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.OldIpReserveHours = params.get("OldIpReserveHours")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterVpcResponse(AbstractModel):
    """SwitchClusterVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务id。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SwitchClusterZoneRequest(AbstractModel):
    """SwitchClusterZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群Id
        :type ClusterId: str
        :param OldZone: 当前可用区
        :type OldZone: str
        :param NewZone: 要切换到的可用区
        :type NewZone: str
        :param IsInMaintainPeriod: 维护期间执行-yes,立即执行-no
        :type IsInMaintainPeriod: str
        """
        self.ClusterId = None
        self.OldZone = None
        self.NewZone = None
        self.IsInMaintainPeriod = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.OldZone = params.get("OldZone")
        self.NewZone = params.get("NewZone")
        self.IsInMaintainPeriod = params.get("IsInMaintainPeriod")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchClusterZoneResponse(AbstractModel):
    """SwitchClusterZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步FlowId
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class SwitchProxyVpcRequest(AbstractModel):
    """SwitchProxyVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param UniqVpcId: 字符串vpc id
        :type UniqVpcId: str
        :param UniqSubnetId: 字符串子网id
        :type UniqSubnetId: str
        :param OldIpReserveHours: 旧地址回收时间
        :type OldIpReserveHours: int
        :param ProxyGroupId: 数据库代理组Id（该参数为必填项，可以通过DescribeProxies接口获得）
        :type ProxyGroupId: str
        """
        self.ClusterId = None
        self.UniqVpcId = None
        self.UniqSubnetId = None
        self.OldIpReserveHours = None
        self.ProxyGroupId = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        self.OldIpReserveHours = params.get("OldIpReserveHours")
        self.ProxyGroupId = params.get("ProxyGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchProxyVpcResponse(AbstractModel):
    """SwitchProxyVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param FlowId: 异步任务id。
        :type FlowId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FlowId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FlowId = params.get("FlowId")
        self.RequestId = params.get("RequestId")


class TablePrivileges(AbstractModel):
    """mysql表权限

    """

    def __init__(self):
        r"""
        :param Db: 数据库名
        :type Db: str
        :param TableName: 表名
        :type TableName: str
        :param Privileges: 权限列表
        :type Privileges: list of str
        """
        self.Db = None
        self.TableName = None
        self.Privileges = None


    def _deserialize(self, params):
        self.Db = params.get("Db")
        self.TableName = params.get("TableName")
        self.Privileges = params.get("Privileges")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """集群绑定的标签信息，包含标签键TagKey和标签值TagValue

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TemplateParamInfo(AbstractModel):
    """参数模板详情

    """

    def __init__(self):
        r"""
        :param CurrentValue: 当前值
        :type CurrentValue: str
        :param Default: 默认值
        :type Default: str
        :param EnumValue: 参数类型为enum时可选的值类型集合
注意：此字段可能返回 null，表示取不到有效值。
        :type EnumValue: list of str
        :param Max: 参数类型为float/integer时的最大值
注意：此字段可能返回 null，表示取不到有效值。
        :type Max: str
        :param Min: 参数类型为float/integer时的最小值
注意：此字段可能返回 null，表示取不到有效值。
        :type Min: str
        :param ParamName: 参数名称
        :type ParamName: str
        :param NeedReboot: 是否需要重启
        :type NeedReboot: int
        :param Description: 参数描述
        :type Description: str
        :param ParamType: 参数类型，integer/float/string/enum
        :type ParamType: str
        """
        self.CurrentValue = None
        self.Default = None
        self.EnumValue = None
        self.Max = None
        self.Min = None
        self.ParamName = None
        self.NeedReboot = None
        self.Description = None
        self.ParamType = None


    def _deserialize(self, params):
        self.CurrentValue = params.get("CurrentValue")
        self.Default = params.get("Default")
        self.EnumValue = params.get("EnumValue")
        self.Max = params.get("Max")
        self.Min = params.get("Min")
        self.ParamName = params.get("ParamName")
        self.NeedReboot = params.get("NeedReboot")
        self.Description = params.get("Description")
        self.ParamType = params.get("ParamType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TradePrice(AbstractModel):
    """计费询价结果

    """

    def __init__(self):
        r"""
        :param TotalPrice: 预付费模式下资源总价，不包含优惠，单位:分
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPrice: int
        :param Discount: 总的折扣，100表示100%不打折
        :type Discount: float
        :param TotalPriceDiscount: 预付费模式下的优惠后总价, 单位: 分,例如用户享有折扣 =TotalPrice × Discount
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPriceDiscount: int
        :param UnitPrice: 后付费模式下的单位资源价格，不包含优惠，单位:分
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: int
        :param UnitPriceDiscount: 优惠后后付费模式下的单位资源价格, 单位: 分,例如用户享有折扣=UnitPricet × Discount
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: int
        :param ChargeUnit: 计费价格单位
        :type ChargeUnit: str
        """
        self.TotalPrice = None
        self.Discount = None
        self.TotalPriceDiscount = None
        self.UnitPrice = None
        self.UnitPriceDiscount = None
        self.ChargeUnit = None


    def _deserialize(self, params):
        self.TotalPrice = params.get("TotalPrice")
        self.Discount = params.get("Discount")
        self.TotalPriceDiscount = params.get("TotalPriceDiscount")
        self.UnitPrice = params.get("UnitPrice")
        self.UnitPriceDiscount = params.get("UnitPriceDiscount")
        self.ChargeUnit = params.get("ChargeUnit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceRequest(AbstractModel):
    """UpgradeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Cpu: 数据库CPU
        :type Cpu: int
        :param Memory: 数据库内存，单位GB
        :type Memory: int
        :param UpgradeType: 升级类型：upgradeImmediate，upgradeInMaintain
        :type UpgradeType: str
        :param StorageLimit: 该参数已废弃
        :type StorageLimit: int
        :param AutoVoucher: 是否自动选择代金券 1是 0否 默认为0
        :type AutoVoucher: int
        :param DbType: 该参数已废弃
        :type DbType: str
        :param DealMode: 交易模式 0-下单并支付 1-下单
        :type DealMode: int
        :param UpgradeMode: NormalUpgrade：普通变配，FastUpgrade：极速变配，若变配过程判断会造成闪断，变配流程会终止。
        :type UpgradeMode: str
        """
        self.InstanceId = None
        self.Cpu = None
        self.Memory = None
        self.UpgradeType = None
        self.StorageLimit = None
        self.AutoVoucher = None
        self.DbType = None
        self.DealMode = None
        self.UpgradeMode = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        self.UpgradeType = params.get("UpgradeType")
        self.StorageLimit = params.get("StorageLimit")
        self.AutoVoucher = params.get("AutoVoucher")
        self.DbType = params.get("DbType")
        self.DealMode = params.get("DealMode")
        self.UpgradeMode = params.get("UpgradeMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeInstanceResponse(AbstractModel):
    """UpgradeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param TranId: 冻结流水ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TranId: str
        :param BigDealIds: 大订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type BigDealIds: list of str
        :param DealNames: 订单号
        :type DealNames: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TranId = None
        self.BigDealIds = None
        self.DealNames = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TranId = params.get("TranId")
        self.BigDealIds = params.get("BigDealIds")
        self.DealNames = params.get("DealNames")
        self.RequestId = params.get("RequestId")


class ZoneStockInfo(AbstractModel):
    """可用区库存信息

    """

    def __init__(self):
        r"""
        :param Zone: 可用区
        :type Zone: str
        :param HasStock: 是否有库存
        :type HasStock: bool
        :param StockCount: 库存数量
        :type StockCount: int
        """
        self.Zone = None
        self.HasStock = None
        self.StockCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.HasStock = params.get("HasStock")
        self.StockCount = params.get("StockCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        