# WSFD-106303 基于ARP的差异化服务参考信息（适用于GGSN、SGW-C、PGW-C）

- [命令](#ZH-CN_TOPIC_0000001440400505__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0000001440400505__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0000001440400505__1.3.3.1)
- [测量指标](#ZH-CN_TOPIC_0000001440400505__1.3.4.1)

#### [命令](#ZH-CN_TOPIC_0000001440400505)

本特性相关的MML命令如下：

- **[SET LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)**
- **[LST LICENSESWITCH](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)**
- **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)**
- **[LST USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/查询用户ARP优先级配置（LST USERPRIORARP）_28093181.md)**
- **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)**
- **[RMV BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/删除基于带宽的ARP控制配置（RMV BANDWIDTHARP）_09653157.md)**
- **[MOD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/修改基于带宽的ARP控制配置（MOD BANDWIDTHARP）_09652360.md)**
- **[LST BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/查询基于带宽的ARP控制配置（LST BANDWIDTHARP）_09651453.md)**
- **[ADD QOSPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)**
- **[MOD QOSPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/修改QoS描述配置（MOD QOSPROFILE）_09652553.md)**
- **[RMV QOSPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/删除QoS描述配置（RMV QOSPROFILE）_09653062.md)**
- **[LST QOSPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/查询QoS描述配置（LST QOSPROFILE）_09652691.md)**
- **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)**
- **[RMV BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/删除基于带宽的ARP控制配置（RMV BANDWIDTHARP）_09653157.md)**
- **[MOD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/修改基于带宽的ARP控制配置（MOD BANDWIDTHARP）_09652360.md)**
- **[LST BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/查询基于带宽的ARP控制配置（LST BANDWIDTHARP）_09651453.md)**
- **[ADD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/增加基于PDP数的ARP控制（ADD PDPNUMBERARP）_09653030.md)**
- **[RMV PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/删除基于PDP数的ARP控制（RMV PDPNUMBERARP）_09653198.md)**
- **[MOD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/修改基于PDP数的ARP控制（MOD PDPNUMBERARP）_09651802.md)**
- **[LST PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/查询基于PDP数的ARP控制（LST PDPNUMBERARP）_09653024.md)**
- **[SET APNQOSATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)**
- **[LST APNQOSATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/查询指定APN的QoS属性配置信息（LST APNQOSATTR）_09651477.md)**
- **[SET APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)**
- **[LST APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/查询APN访问控制参数（LST APNACCESSCTRL）_09652260.md)**
- **[DSP PDUSESSION](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/接入管理运维/查询PDP上下文信息/显示PDU会话（DSP PDUSESSION）_09653215.md)**

#### [告警](#ZH-CN_TOPIC_0000001440400505)

本特性相关的告警如下：

- [ALM- 100515 差异化服务APN粒度流控](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-100515 ARP APN门限控制_42668809.md)
- [ALM-100520 整机ARP门限控制](../../../../../../网络运维/故障处理/UNC告警处理/业务告警/SMF&GW-C&GGSN/ALM-100520 整机ARP门限控制_42508633.md)

#### [软参](#ZH-CN_TOPIC_0000001440400505)

本特性无相关软参。

#### [测量指标](#ZH-CN_TOPIC_0000001440400505)

本特性无相关测量指标。
