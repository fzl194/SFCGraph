# 命令证据包：SET MASTERPCRF
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

此命令用于设置主用PCRF主机名。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为100。
- 配置的PCRF必须已通过ADD PCRFBINDGRP命令绑定到PCRF组。
- 该命令设定后的数据，需要通过LST PCRFGROUP命令进行查看。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFGRPNAME | PCRF组名称 | local_planned | required | 无 | 字符串类型，输入长度范围为1～128。不支持空格，不区分大小写。 |
| MASTERPCRF | 主用PCRF主机名 | local_planned | required | 无 | 字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L33:
    > - [**ADD PCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    > - [**ADD PCRFBINDGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
    > - [**SET MASTERPCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    > - [**ADD GLBPCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)
    > - [**SET DFTGLBPCRFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)

**md：`WSFD-109101/Gx Failover功能_31422950.md`**
- 操作步骤上下文（±2 行原文）：
  L59:
    >       [**ADD PCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/增加PCRF组（ADD PCRFGROUP）_09897090.md)
    >     c. **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。
    >       [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    > 3. **可选：**配置PCC定时器的消息重传时间间隔。缺省使用默认值。
    >   [**SET PCCTIMER**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/信令控制/定时器/设置PCC定时器（SET PCCTIMER）_09897082.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_2 | 已配置数据中获取 | 修改PCRF分组内的缺省主用PCRF。 |
  | [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md) | 主用PCRF主机名（MASTERPCRF） | pcrf_3 | 本端规划 | 修改PCRF分组内的缺省主用PCRF。 |
- 操作步骤上下文（±2 行原文）：
  L107:
    >       [**ADD PCRFBINDGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF绑定/增加PCRF与PCRF Group的关联关系（ADD PCRFBINDGRP）_09897096.md)
    >     d. **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。
    >       [**SET MASTERPCRF**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    >     e. **可选：**基于IMSI号段选择PCRF分组时，需要将指定的PCRF分组绑定到指定的号码段。
    >       [**ADD GLBPCRFGROUP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)

## ④ 自动比对
- 命令真相参数（2）：['MASTERPCRF', 'PCRFGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1, '本端规划': 1}（多值→atom 应考虑 decision_driven）
