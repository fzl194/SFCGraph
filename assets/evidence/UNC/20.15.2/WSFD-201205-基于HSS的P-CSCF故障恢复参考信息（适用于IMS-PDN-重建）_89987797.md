# WSFD-201205 基于HSS的P-CSCF故障恢复 参考信息（适用于IMS PDN 重建）

- [命令](#ZH-CN_TOPIC_0000001189987797__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0000001189987797__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0000001189987797__1.3.3.1)
- [测量指标](#ZH-CN_TOPIC_0000001189987797__1.3.4.1)

#### [命令](#ZH-CN_TOPIC_0000001189987797)

本特性相关的MML命令如下：

- [**ADD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/增加IMSI对应的Diameter兼容性(ADD DMCMPTBYIMSI)_72225977.md)
- [**RMV DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/删除IMSI对应的Diameter兼容性(RMV DMCMPTBYIMSI)_72345899.md)
- [**MOD DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/修改IMSI对应的Diameter兼容性(MOD DMCMPTBYIMSI)_26306110.md)
- [**LST DMCMPTBYIMSI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性IMSI号段配置/查询IMSI对应的Diameter兼容性(LST DMCMPTBYIMSI)_26146300.md)
- [**SET DMCMPT**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/信令传输管理/Diameter管理/Diameter协议接口兼容性配置/设置Diameter兼容性(SET DMCMPT)_26306080.md)

#### [告警](#ZH-CN_TOPIC_0000001189987797)

本特性无相关告警。

#### [软参](#ZH-CN_TOPIC_0000001189987797)

本特性相关的软参如下：

DWORD_EX12 BIT30 控制UNC在向UE发送Deactivate EPS bearer context request消息删除承载，如果删除的不是最后一个PDN的场景下，携带的原因值是否为Reactivation requested

#### [测量指标](#ZH-CN_TOPIC_0000001189987797)

本特性相关的测量指标如下：

- [117491049 HSS发起的P-CSCF Restoration请求次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/SGSN_MME业务性能指标/USN性能指标/S6a/S6a接口统计/117491049 HSS发起的P-CSCF Restoration请求次数_06830821.md)
- [117496021 S1模式P-CSCF Restoration触发PDN断连次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/SGSN_MME业务性能指标/USN性能指标/S1模式会话管理/S1模式PDN断连/117496021 S1模式P-CSCF Restoration触发PDN断连次数_06833251.md)
- [117491225 S1模式P-CSCF Restoration触发分离次数](../../../../../../OM参考/性能指标/UNC业务性能指标/业务性能指标/SGSN_MME业务性能指标/USN性能指标/S1模式移动管理/S1模式分离/117491225 S1模式P-CSCF Restoration触发分离次数_06831018.md)
