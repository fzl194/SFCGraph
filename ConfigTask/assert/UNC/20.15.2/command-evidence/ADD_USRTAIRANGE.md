# 命令证据包：ADD USRTAIRANGE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加用户TAI区域配置。该配置为用户区域范围，包含1个或多个用户区域。语音用户建立N7会话时，其用户区域（TAI）会匹配到该配置的某一条记录，从而根据配置PCFSSCOPEBIND匹配该用户区域可用的PCF业务服务区，选择可用PCF。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 系统中保存的TAC包含TACSTART和TACEND。
- 不同用户TAI区域配置的TAC区域范围[TACSTART，TACEND]可以重叠，使用ADD PCFSSCOPEBIND命令将用户TAI区域配置与PCF业务服务区（ADD PCFSSCOPE）绑定时会限制不同PCF业务服务区对应的用户TAI区域不能重叠。

- 最多可输入5000条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| RANGENAME | 区域名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。 |
| MCC | 移动国家码 | global_planned | required | 无 | 字符串类型，输入长度是3。 |
| MNC | 移动网络码 | global_planned | required | 无 | 字符串类型，输入长度范围是2~3。 |
| TACSTART | TAC区域起点值 | global_planned | required | 无 | 字符串类型，输入长度范围是4~6。 |
| TACEND | TAC区域结束值 | global_planned | required | 无 | 字符串类型，输入长度范围是4~6。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**SET AMFPLCYFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > - [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)
    > - [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)
    > - [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)
    > - [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md) | 区域名称（RANGENAME） | tai1 | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md) | 移动国家码（MCC） | 460 | 全网规划 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>增加用户TAI区域配置。 |
  | [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md) | 移动网络码（MNC） | 02 | 全网规划 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>增加用户TAI区域配置。 |
  | [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md) | TAC区域起点值（TACSTART） | 1234 | 全网规划 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>增加用户TAI区域配置。 |
  | [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md) | TAC区域结束值（TACEND） | 1239 | 全网规划 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>增加用户TAI区域配置。 |
- 操作步骤上下文（±2 行原文）：
  L211:
    >       [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)
    >     2. 配置用户TAI区域。
    >       [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)
    >     3. 配置PCF业务服务区和用户TAI区域的绑定关系。
    >       [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)

## ④ 自动比对
- 命令真相参数（5）：['MCC', 'MNC', 'RANGENAME', 'TACEND', 'TACSTART']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 4}（多值→atom 应考虑 decision_driven）
