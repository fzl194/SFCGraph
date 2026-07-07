# 命令证据包：ADD PCRFBINDGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用于添加指定的PCRF到PCRF分组中。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为3200。
- 单个PCRF分组内最多可以有32个PCRF。
- 如果一个PCRF Group的工作模式为主备模式，且PCRF Group中绑定多个备PCRF，在不执行绑定关系删除的操作时，先绑定的备PCRF优先级高。
- 使用EXP MML命令导出的配置文件中，备PCRF绑定的配置顺序会按PCRF名称的字典序排序，再进行配置导入时，备PCRF的选

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 |
| PCRFHOSTNAME | PCRF主机名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 |
| WEIGHT | PCRF权重 | local_planned | optional | 无 | 整数类型，取值范围为1～100。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L32:
    > - [**ADD IMSIMSISDNSEG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务公共/IMSI MSISDN号段/增加IMSI和MSISDN号段（ADD IMSIMSISDNSEG）_09897128.md)
    > - [**ADD PCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    > - [**ADD PCRFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
    > - [**SET MASTERPCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    > - [**ADD GLBPCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md) | PCRF组名称（PCRFGRPNAME） | pcrf.group.1 | 已配置数据中获取 | 添加PCRF到PCRF分组中。 |
  | [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md) | PCRF主机名称（PCRFHOSTNAME） | pcrf1<br>pcrf2 | 已配置数据中获取 | 添加PCRF到PCRF分组中。 |
- 任务示例脚本（该命令行）：
  `ADD PCRFBINDGRP:PCRFGRPNAME="pcrf.group.1",PCRFHOSTNAME="pcrf1";`
  `ADD PCRFBINDGRP:PCRFGRPNAME="pcrf.group.1",PCRFHOSTNAME="pcrf2";`
- 操作步骤上下文（±2 行原文）：
  L99:
    >   ```
    >   ```
    >   ADD PCRFBINDGRP:PCRFGRPNAME="pcrf.group.1",PCRFHOSTNAME="pcrf1";
    >   ```
    >   ```
  L102:
    >   ```
    >   ```
    >   ADD PCRFBINDGRP:PCRFGRPNAME="pcrf.group.1",PCRFHOSTNAME="pcrf2";
    >   ```
    > 3. 配置Tx定时器的时长。

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_1<br>pcrf_group_2 | 已配置数据中获取 | “pcrf_1”和“pcrf_2”属于“pcrf_group_1”，“pcrf_group_1”内的PCRF按配置的百分比进行负荷分担。“pcrf_3”和“pcrf_4”属于“pcrf_group_2”，“pcrf_group_2”内的PCRF为主备模式，且“pcrf_3”为主用PCRF。 |
  | [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md) | PCRF主机名称（PCRFHOSTNAME） | pcrf_1<br>pcrf_2<br>pcrf_3<br>pcrf_4 | 已配置数据中获取 | “pcrf_1”和“pcrf_2”属于“pcrf_group_1”，“pcrf_group_1”内的PCRF按配置的百分比进行负荷分担。“pcrf_3”和“pcrf_4”属于“pcrf_group_2”，“pcrf_group_2”内的PCRF为主备模式，且“pcrf_3”为主用PCRF。 |
- 任务示例脚本（该命令行）：
  `ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",PCRFHOSTNAME="pcrf_1",WEIGHT=40;`
  `ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",PCRFHOSTNAME="pcrf_2",WEIGHT=60;`
  `ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_2",PCRFHOSTNAME="pcrf_3";`
  `ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_2",PCRFHOSTNAME="pcrf_4";`
- 操作步骤上下文（±2 行原文）：
  L105:
    >       [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    >     c. 添加指定的PCRF到指定的PCRF分组中。
    >       [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
    >     d. **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。
    >       [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
  L191:
    >   ```
    >   ```
    >   ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",PCRFHOSTNAME="pcrf_1",WEIGHT=40;
    >   ```
    >   ```
  L194:
    >   ```
    >   ```
    >   ADD PCRFBINDGRP:PCRFGRPNAME="pcrf_group_1",PCRFHOSTNAME="pcrf_2",WEIGHT=60;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（3）：['PCRFGRPNAME', 'PCRFHOSTNAME', 'WEIGHT']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 4}（多值→atom 应考虑 decision_driven）
