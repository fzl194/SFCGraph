# 激活基于ARP的差异化服务（适用于GGSN、SGW-C、PGW-C）

- [操作场景](#ZH-CN_OPI_0000001388712956__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001388712956__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001388712956__1.3.3)
- [任务示例](#ZH-CN_OPI_0000001388712956__1.3.4)

## [操作场景](#ZH-CN_OPI_0000001388712956)

通过配置差异化服务功能，可实现以下需求：

- 在资源紧缺时，运营商为高优先级用户优先分配资源。
- 在资源相对富余时，更充分地发挥网络资源的效益，提高客户满意度。

> **说明**
> 适用于 GGSN、 SGW-C、PGW-C。

## [必备事项](#ZH-CN_OPI_0000001388712956)

前提条件

- 请仔细阅读[WSFD-106303 基于ARP的差异化服务特性概述（适用于GGSN、SGW-C、PGW-C）](特性概述_40520681.md)。
- 完成加载License。

数据

| 类别 | 参数名 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | License项（LICITEM） | LKV2DIFFSEC01 | 本端规划 | 打开本特性的License配置开关。 |
| [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md) | 开关（SWITCH） | ENABLE | 本端规划 | 打开本特性的License配置开关。 |
| **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)** | 漫游用户ARP级别限制（ROAMHIGHESTARP） | LOW | 本端规划 | 配置漫游以及拜访用户的级别限制。 |
| **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)** | 拜访用户ARP级别限制（VISITHIGHESTARP） | HIGH | 本端规划 | 配置漫游以及拜访用户的级别限制。 |
| **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)** | 漫游用户级别限制开关（ROAMARPSWITCH） | ENABLE | 本端规划 | 配置漫游以及拜访用户的级别限制。 |
| **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)** | 拜访用户级别限制开关（VISITARPSWITCH） | ENABLE | 本端规划 | 配置漫游以及拜访用户的级别限制。 |
| **[ADD QOSPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)** | QoS Profile名（QOSPROFILENAME） | profilename | 本端规划 | 基于带宽的接入优先级。 |
| **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)** | 用户级别（USERPRIORITY） | NORMAL | 本端规划 | 基于带宽的接入优先级。 |
| **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)** | 业务级别（SERVICELEVEL） | GENERAL | 本端规划 | 基于带宽的接入优先级。 |
| **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)** | 拒绝告警门限（REJECTLIMIT） | 20 | 本端规划 | 基于带宽的接入优先级。 |
| **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)** | 恢复告警门限（RESTORELIMIT） | 30 | 本端规划 | 基于带宽的接入优先级。 |
| **[ADD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/增加基于PDP数的ARP控制（ADD PDPNUMBERARP）_09653030.md)** | 用户级别（USERPRIORITY） | NORMAL | 本端规划 | 基于PDP数的接入优先级。 |
| **[ADD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/增加基于PDP数的ARP控制（ADD PDPNUMBERARP）_09653030.md)** | 业务级别（SERVICELEVEL） | GENERAL | 本端规划 | 基于PDP数的接入优先级。 |
| **[ADD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/增加基于PDP数的ARP控制（ADD PDPNUMBERARP）_09653030.md)** | 拒绝告警门限（REJECTLIMIT） | 40 | 本端规划 | 基于PDP数的接入优先级。 |
| **[ADD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/增加基于PDP数的ARP控制（ADD PDPNUMBERARP）_09653030.md)** | 恢复告警门限（RESTORELIMIT） | 30 | 本端规划 | 基于PDP数的接入优先级。 |
| **[SET APNQOSATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)** | APN名称（APN） | huawei.com | 本端规划 | 为APN实例绑定qos-profile。 |
| **[SET APNQOSATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)** | 有QoS Profile（HASQOSPROFILE） | ENABLE | 本端规划 | 为APN实例绑定qos-profile。 |
| **[SET APNQOSATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)** | QoS Profile名（QOSPROFILENAME） | profilename | 本端规划 | 为APN实例绑定qos-profile。 |
| **[SET APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)** | APN名称（APN） | huawei.com | 本端规划 | 设置APN访问控制策略相关参数信息。 |
| **[SET APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)** | 最大PDP数目（MAXPDBNUMBER） | 10 | 本端规划 | 设置APN访问控制策略相关参数信息。 |
| **[SET APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)** | 最大带宽（MAXBANDWIDTH） | 200 | 本端规划 | 设置APN访问控制策略相关参数信息。 |

## [操作步骤](#ZH-CN_OPI_0000001388712956)

1. 打开本特性的License配置开关。
  [**SET LICENSESWITCH**](../../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)
2. **可选：**配置拜访或漫游用户的级别限制功能，以及限制级别。
  **[SET USERPRIORARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/全局QoS功能配置/全局QoS参数/设置用户ARP优先级配置（SET USERPRIORARP）_27933281.md)**
3. 为指定APN配置带宽和PDP数的接入优先级。
    a. 配置QoS Profile名称。
      **[ADD QOSPROFILE](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/QoS模板/增加QoS描述配置（ADD QOSPROFILE）_09654430.md)**
    b. 为指定APN配置带宽的接入优先级，即为不同的用户、业务级别配置不同的拒绝、恢复告警门限。
      **[ADD BANDWIDTHARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于带宽的ARP控制/增加基于带宽的ARP控制配置（ADD BANDWIDTHARP）_09653114.md)**
    c. 为指定APN配置PDP数的接入优先级，即为不同的用户、业务级别配置不同的拒绝、恢复告警门限。
      **[ADD PDPNUMBERARP](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/Qos管理/基于PDP数的ARP控制/增加基于PDP数的ARP控制（ADD PDPNUMBERARP）_09653030.md)**
    d. 为APN实例绑定qos-profile。
      **[SET APNQOSATTR](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/QoS/APN的QoS属性/设置指定APN的QoS属性配置信息（SET APNQOSATTR）_09651825.md)**
    e. 设置APN访问控制策略相关参数信息。
      **[SET APNACCESSCTRL](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的接入属性控制/设置APN访问控制参数（SET APNACCESSCTRL）_09654434.md)**

## [任务示例](#ZH-CN_OPI_0000001388712956)

任务描述

为名称为 “huawei.com” 的APN配置接入的用户级别和业务级别，及PDP/带宽拒绝接入门限和恢复接入门限，实现差异化服务。

- PDP拒绝接入拒绝门限为40%，PDP恢复接入门限为30%。
- 带宽拒绝告警门限为30%，带宽恢复接入告警门限为20%。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2DIFFSEC01", SWITCH=ENABLE;
```

//配置拜访及漫游用户的级别限制功能，以及限制级别。

```
SET USERPRIORARP:ROAMARPSWITCH=ENABLE,ROAMHIGHESTARP=LOW,VISITARPSWITCH=ENABLE,VISITHIGHESTARP=HIGH;
```

//为名称为 “huawei.com” 的APN配置接入的用户级别和业务级别，及PDP/带宽拒绝接入门限和恢复接入门限。

```
ADD QOSPROFILE: QOSPROFILENAME="profilename";
ADD BANDWIDTHARP:QOSPROFILENAME="profilename",USERPRIORITY=NORMAL,SERVICELEVEL=GENERAL,REJECTLIMIT=30,RESTORELIMIT=20;
ADD PDPNUMBERARP: QOSPROFILENAME="profilename", USERPRIORITY=HIGH, SERVICELEVEL=GENERAL, REJECTLIMIT=40, RESTORELIMIT=30;
SET APNQOSATTR: APN="huawei.com",HASQOSPROFILE=ENABLE,QOSPROFILENAME="profilename";
```

//设置APN访问控制策略相关参数信息。

```
SET APNACCESSCTRL: APN="huawei.com",MAXPDBNUMBER=10,MAXBANDWIDTH=200;
```
