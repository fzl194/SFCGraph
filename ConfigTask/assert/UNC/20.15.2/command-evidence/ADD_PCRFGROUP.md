# 命令证据包：ADD PCRFGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md`
> 用该命令的特性数：3

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

该命令用于添加PCRF Group，设置是否Gx的failover功能以及设置工作模式。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 主备工作模式时，第一个添加到某PCRF组的PCRF将被设置为该组的缺省Master PCRF，后续添加的PCRF将被缺省设置为组内的Slave PCRF，这种状态将一直持续下去，直到通过SET MASTERPCRF改变Master PCRF或者Master PCRF被删除。Master PCRF为该组的主用PCRF，当有PCC用户激活

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 |
| LOADBALANCEMODE | 负荷分担模式 | global_planned | optional | MASTER_SLAVE | 枚举类型。 |
| FAILOVERSW | 宕机备份开关 | local_planned | optional | DISABLE | 枚举类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L31:
    > - [**ADD APNUSRPROFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/APN用户模板组绑定/增加APN用户模板组绑定关系（ADD APNUSRPROFG）_09897224.md)
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD PCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    > - [**ADD PCRFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
    > - [**SET MASTERPCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | PCRF组名称（PCRFGRPNAME） | pcrf.group.1 | 本端规划 | PCRF group信息。 |
  | [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | 负荷分担模式（LOADBALANCEMODE） | MASTER_SLAV | 全网规划 | PCRF group信息。 |
  | [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | 宕机备份开关（FAILOVERSW） | ENABLE | 本端规划 | PCRF group信息。 |
- 任务示例脚本（该命令行）：
  `ADD PCRFGROUP:PCRFGRPNAME="pcrf.group.1",LOADBALANCEMODE=MASTER_SLAVE,FAILOVERSW=ENABLE;`
- 操作步骤上下文（±2 行原文）：
  L10:
    > ## [操作场景](#ZH-CN_OPI_0231422950)
    > 
    > 当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果 [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) 命令中 “FAILOVERSW” 参数值为 “ENABLE” ，则进行failover处理；否则按照 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令设置的动作进行处理。
    > 
    > GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据 [**SET PCCFAILACTION**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md) 和 [**ADD PCCTEMPLATE**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC模板/增加PCC模板（ADD PCCTEMPLATE）_09897064.md) 命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。
  L57:
    >       [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    >     b. 配置PCRF组。
    >       [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    >     c. **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。
    >       [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
  L96:
    > 2. 配置PCRF组。
    >   ```
    >   ADD PCRFGROUP:PCRFGRPNAME="pcrf.group.1",LOADBALANCEMODE=MASTER_SLAVE,FAILOVERSW=ENABLE;
    >   ```
    >   ```

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_1<br>pcrf_group_2 | 本端规划 | “pcrf_1”和“pcrf_2”属于“pcrf_group_1”，“pcrf_group_1”内的PCRF按配置的百分比进行负荷分担。“pcrf_3”和“pcrf_4”属于“pcrf_group_2”，“pcrf_group_2”内的PCRF为主备模式，且“pcrf_3”为主用PCRF。 |
  | [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | 负荷分担模式（LOADBALANCEMODE） | LOAD_BALANCE<br>MASTER_SLAVE | 全网规划 | “pcrf_1”和“pcrf_2”属于“pcrf_group_1”，“pcrf_group_1”内的PCRF按配置的百分比进行负荷分担。“pcrf_3”和“pcrf_4”属于“pcrf_group_2”，“pcrf_group_2”内的PCRF为主备模式，且“pcrf_3”为主用PCRF。 |
- 任务示例脚本（该命令行）：
  `ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_1",LOADBALANCEMODE=LOAD_BALANCE;`
  `ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_2",LOADBALANCEMODE=MASTER_SLAVE;`
- 操作步骤上下文（±2 行原文）：
  L103:
    >       [**ADD PCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF/增加PCRF（ADD PCRF）_09897101.md)
    >     b. 配置PCRF分组。
    >       [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    >     c. 添加指定的PCRF到指定的PCRF分组中。
    >       [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
  L188:
    >   ```
    >   ```
    >   ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_1",LOADBALANCEMODE=LOAD_BALANCE;
    >   ```
    >   ```
  L197:
    >   ```
    >   ```
    >   ADD PCRFGROUP:PCRFGRPNAME="pcrf_group_2",LOADBALANCEMODE=MASTER_SLAVE;
    >   ```
    >   ```

**md：`WSFD-109101/调测PCRF负荷分担功能_31422955.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_1 | 已配置数据中获取 | PCRF组 |

### WSFD-102001

**md：`WSFD-102001/激活VoLTE基础语音业务（适用于SGW-C_PGW-C）_67930995.md`**
- 操作步骤上下文（±2 行原文）：
  L84:
    > ```
    > 
    > //将指定的PCRF分组及号段信息绑定到指定APN。 参数 PCRFGRPNAME使用 **[ADD PCRFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)** 命令配置生成。执行该命令前请先通过 **[LST PCRFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/查询PCRF组（LST PCRFGROUP）_09897093.md)** 查询当前是否已添加该PCRF Group。 根据查询结果，选择是否配置该参数。
    > 
    > ```

### WSFD-201207

**md：`WSFD-201207/WSFD-201207 语音PCF_PCRF故障Bypass参考信息_85304300.md`**
- 操作步骤上下文（±2 行原文）：
  L152:
    > **[DSP IMSBYPASSUSER](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/语音PCF_PCRF Bypass管理/显示进入语音PCF_PCRF故障Bypass状态的用户的IMSI列表（DSP IMSBYPASSUSER）_54762937.md)**
    > 
    > **[ADD PCRFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)**
    > 
    > **[MOD PCRFGROUP](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/修改PCRF组（MOD PCRFGROUP）_09897091.md)**

## ④ 自动比对
- 命令真相参数（3）：['FAILOVERSW', 'LOADBALANCEMODE', 'PCRFGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 3, '全网规划': 2, '已配置数据中获取': 1}（多值→atom 应考虑 decision_driven）
