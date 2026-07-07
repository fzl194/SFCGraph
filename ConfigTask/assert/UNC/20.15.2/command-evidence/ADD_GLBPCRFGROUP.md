# 命令证据包：ADD GLBPCRFGROUP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用来将指定PCRF分组和指定的号段绑定，并且绑定优先级。 同时指定PCRF组名和号段名，则将指定PCRF组和号段绑定。在业务处理过程中，如果APN下PCC使能开关为INHERIT，并且全局PCC使能开关为ENABLE，则优先按照PCRF组和号段的绑定关系进行PCRF组的选择，只有当所有号段都匹配不成功时，才会选用系统缺省的PCRF组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。
- 该命令最大记录数为4096。
- 一个号段最多只能绑定一个指定的PCRF组。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～31。 |
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。 |
| PRIORITY | 优先级 | local_planned | required | 无 | 整数类型，取值范围为1～65535。 |
| DESCRIPTION | 描述 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～63。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L34:
    > - [**ADD PCRFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
    > - [**SET MASTERPCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    > - [**ADD GLBPCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)
    > - [**SET DFTGLBPCRFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)
    > - [**ADD PCRFGRPBNDAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD GLBPCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md) | IMSI/MSISDN号段名称（IMSIMSISDNSEG） | msisdnseg1<br>msisdnseg2 | 已配置数据中获取 | 全局PCRF分组及PCC开关。<br>号段“msisdnseg1”与PCRF分组“pcrf_group_1”绑定，优先级为“1”。<br>号段“msisdnseg2”与PCRF分组“pcrf_group_2”绑定，优先级为“2”。 |
  | [**ADD GLBPCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md) | 优先级（PRIORITY） | 1<br>2 | 本端规划 | 全局PCRF分组及PCC开关。<br>号段“msisdnseg1”与PCRF分组“pcrf_group_1”绑定，优先级为“1”。<br>号段“msisdnseg2”与PCRF分组“pcrf_group_2”绑定，优先级为“2”。 |
  | [**ADD GLBPCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_1<br>pcrf_group_2 | 已配置数据中获取 | 全局PCRF分组及PCC开关。<br>号段“msisdnseg1”与PCRF分组“pcrf_group_1”绑定，优先级为“1”。<br>号段“msisdnseg2”与PCRF分组“pcrf_group_2”绑定，优先级为“2”。 |
- 任务示例脚本（该命令行）：
  `ADD GLBPCRFGROUP:IMSIMSISDNSEG="msisdnseg1",PCRFGRPNAME="pcrf_group_1",PRIORITY=1;`
  `ADD GLBPCRFGROUP:IMSIMSISDNSEG="msisdnseg2",PCRFGRPNAME="pcrf_group_2",PRIORITY=2;`
- 操作步骤上下文（±2 行原文）：
  L109:
    >       [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    >     e. **可选：**基于IMSI号段选择PCRF分组时，需要将指定的PCRF分组绑定到指定的号码段。
    >       [**ADD GLBPCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)
    > 5. **可选：**配置基于整机粒度控制在激活过程中根据PCRF返回的重定向指示重选PCRF。缺省不支持。
    >   [**SET PCCPCRFMSGATTR**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/服务器端信元控制/设置PCRF返回消息属性（SET PCCPCRFMSGATTR）_09897077.md)
  L207:
    > 4. 将指定的PCRF组和号码段绑定，并设置PCRF组“pcrf_group_1”为全局缺省的PCRF组。
    >   ```
    >   ADD GLBPCRFGROUP:IMSIMSISDNSEG="msisdnseg1",PCRFGRPNAME="pcrf_group_1",PRIORITY=1;
    >   ```
    >   ```
  L210:
    >   ```
    >   ```
    >   ADD GLBPCRFGROUP:IMSIMSISDNSEG="msisdnseg2",PCRFGRPNAME="pcrf_group_2",PRIORITY=2;
    >   ```
    >   ```

## ④ 自动比对
- 命令真相参数（4）：['DESCRIPTION', 'IMSIMSISDNSEG', 'PCRFGRPNAME', 'PRIORITY']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 2, '本端规划': 1}（多值→atom 应考虑 decision_driven）
