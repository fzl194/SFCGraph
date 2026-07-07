# 命令证据包：ADD PCRFGRPBNDAPN
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md`
> 用该命令的特性数：2

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用来设置APN和Pcrf组关联关系。PCC即策略和计费控制，运营商可以通过PCC功能，做到对计费策略和计费粒度的灵活控制，从而优化运营商的计费手段，提高收益。从业务功能角度看，在MS用户激活或者更新过程中，可以选择由网元PCRF下发计费策略，做到业务级的QoS控制和计费，并可以动态调整策略。在UNC系统中，可以通过ADD PCRF等一系列命令实现该功
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为3000。
- 在添加记录前，确认APN是否配置；指定如果DefaultFlag字段的值为DEFAULT，可设置APN的缺省PCRF Group；指定DefaultFlag字段为IMSI_MSISDN_SEG，则为APN基于IMSI/MSISDN号段设置PCRF组，则添加成功。
- APN下只允许配置一个不带号段的PCRF组名称，每个APN最多绑定

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| APN | APN名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～63。不支持空格。 |
| DEFAULTFLAG | 缺省标记 | local_planned | required | 无 | 枚举类型。 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 |
| PRIORITY | 优先级 | local_planned | conditional | 无 | 整数类型，取值范围为1～65535。优先级唯一。 |
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 |
| DESCRIPTION | 描述 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L36:
    > - [**ADD GLBPCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)
    > - [**SET DFTGLBPCRFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)
    > - [**ADD PCRFGRPBNDAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    > - [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)
    > - [**ADD RESULTCODECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/返回码控制/增加返回码控制（ADD RESULTCODECTRL）_09897084.md)

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 任务示例脚本（该命令行）：
  `ADD PCRFGRPBNDAPN:APN="apn1",DEFAULTFLAG=DEFAULT,PCRFGRPNAME="pcrf.group.1";`
- 操作步骤上下文（±2 行原文）：
  L63:
    >   [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)
    > 4. 将指定的PCRF分组绑定到指定APN。
    >   [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    > 5. **可选：**如果PCRF不支持热备份功能，GGSN/PGW-C上需要开启failover增强功能。
    >     a. GGSN/PGW-C上开启failover增强功能。
  L110:
    > 4. 将PCRF分组绑定到指定APN。
    >   ```
    >   ADD PCRFGRPBNDAPN:APN="apn1",DEFAULTFLAG=DEFAULT,PCRFGRPNAME="pcrf.group.1";
    >   ```
    > 5. PCRF不支持热备时，开启failover增强功能并配置上报[步骤 5.b](#ZH-CN_OPI_0231422950__substep826311974175816)和[步骤 5.c](#ZH-CN_OPI_0231422950__substep1922626752175816)描述的需携带的参数。

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md) | APN名称（APN） | apn-test1<br>apn-test2 | 已配置数据中获取 | APN绑定的PCRF分组。 |
  | [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_2 | 已配置数据中获取 | APN绑定的PCRF分组。 |
  | [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md) | 缺省标记（DEFAULTFLAG） | IMSI_MSISDN_SEG | 本端规划 | APN绑定的PCRF分组。 |
  | [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md) | IMSI/MSISDN号段名称（IMSIMSISDNSEG） | msisdnseg1<br>msisdnseg2 | 本端规划 | APN绑定的PCRF分组。 |
- 任务示例脚本（该命令行）：
  `ADD PCRFGRPBNDAPN:APN="apn-test1",DEFAULTFLAG=DEFAULT,PCRFGRPNAME="pcrf_group_2";`
- 操作步骤上下文（±2 行原文）：
  L121:
    > 7. 开启APN下的PCC开关，并将指定的PCRF分组绑定到该APN下。
    >     a. 将指定的PCRF分组 及号段信息 绑定到指定APN。
    >       [**ADD PCRFGRPBNDAPN**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    >       > **说明**
    >       > 号段信息为可选配置。APN下只允许配置一个不带号段信息的PcrfGroup。
  L221:
    > 6. 配置2个APN下的PCC开关，其中APN apn-test1的PCC开关为 “ENABLE” ，并绑定PCRF组 “pcrf_group_2” ，APN apn-test2的PCC开关为 “INHERIT” ，当通过该APN接入的用户的特定号段未与PCRF组绑定时，使用全局缺省的PCRF组“pcrf_group_1”。
    >   ```
    >   ADD PCRFGRPBNDAPN:APN="apn-test1",DEFAULTFLAG=DEFAULT,PCRFGRPNAME="pcrf_group_2";
    >   ```
    >   ```

### WSFD-102001

**md：`WSFD-102001/激活VoLTE基础语音业务（适用于SGW-C_PGW-C）_67930995.md`**
- 任务示例脚本（该命令行）：
  `ADD PCRFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, PCRFGRPNAME="aaa";`
- 操作步骤上下文（±2 行原文）：
  L43:
    >   [**SET APNPCCFUNC**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/APN控制/设置APN PCC功能（SET APNPCCFUNC）_09897034.md)
    > 5. 将指定的PCRF分组及号段信息绑定到指定APN。
    >   [**ADD PCRFGRPBNDAPN**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    > 
    > 配置基于APN的IMS业务
  L87:
    > 
    > ```
    > ADD PCRFGRPBNDAPN: APN="ims", DEFAULTFLAG=DEFAULT, PCRFGRPNAME="aaa";
    > ```
    > 

## ④ 自动比对
- 命令真相参数（6）：['APN', 'DEFAULTFLAG', 'DESCRIPTION', 'IMSIMSISDNSEG', 'PCRFGRPNAME', 'PRIORITY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 2, '本端规划': 2}（多值→atom 应考虑 decision_driven）
