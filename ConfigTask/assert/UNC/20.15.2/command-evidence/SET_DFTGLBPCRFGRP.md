# 命令证据包：SET DFTGLBPCRFGRP
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、GGSN**

此命令用来修改缺省全局PCRF分组。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。
- 该命令最大记录数为1。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| PCRFGRPNAME | PCRF组名称 | local_planned | optional | 无 | 字符串类型，输入长度范围为1～128。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（2G_3G_4G）参考信息_29056160.md`**
- 操作步骤上下文（±2 行原文）：
  L35:
    > - [**SET MASTERPCRF**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组/设置主用PCRF（SET MASTERPCRF）_09897094.md)
    > - [**ADD GLBPCRFGROUP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/全局PCRF组/增加全局PCRF组绑定关系（ADD GLBPCRFGROUP）_09897116.md)
    > - [**SET DFTGLBPCRFGRP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)
    > - [**ADD PCRFGRPBNDAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/PCRF组绑定APN/增加APN和Pcrf组关联关系（ADD PCRFGRPBNDAPN）_09897106.md)
    > - [**SET PCCFAILACTION**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC故障处理（SET PCCFAILACTION）_09897058.md)

**md：`WSFD-109101/配置动态PCC功能_30805098.md`**
- 数据规划表（该命令的参数行）：
  | [**SET DFTGLBPCRFGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md) | PCRF组名称（PCRFGRPNAME） | pcrf_group_1 | 已配置数据中获取 | 指定全局缺省的PCRF分组。 |
- 任务示例脚本（该命令行）：
  `SET DFTGLBPCRFGRP:PCRFGRPNAME="pcrf_group_1";`
- 操作步骤上下文（±2 行原文）：
  L114:
    > 6. 开启全局缺省PCC开关。
    >     a. 设置全局缺省的PCRF分组的名称。
    >       [**SET DFTGLBPCRFGRP**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCRF Diameter连接/缺省全局PCRF组/设置全局缺省PCRF组（SET DFTGLBPCRFGRP）_09897113.md)
    >     b. 针对全局配置PCC使能开关。
    >       [**SET PCCFUNC**](../../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/基本功能/PCC公共参数/设置PCC功能（SET PCCFUNC）_09897057.md)
  L213:
    >   ```
    >   ```
    >   SET DFTGLBPCRFGRP:PCRFGRPNAME="pcrf_group_1";
    >   ```
    > 5. 配置全局缺省的PCC开关。

## ④ 自动比对
- 命令真相参数（1）：['PCRFGRPNAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'已配置数据中获取': 1}（多值→atom 应考虑 decision_driven）
