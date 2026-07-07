# 命令证据包：ADD PCFSSCOPEBIND
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加PCF业务服务区与用户基本信息（如用户TAI区域）的绑定关系。其中，PCF业务服务区通过ADD PCFSSCOPE增加配置。当语音用户通过N7口发起会话建立请求时，可根据该绑定关系映射PCF业务服务区，从而选择可用PCF。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 需要预先配置ADD PCFSSCOPE。若BINDTYPE取值为USRTAIRANGE，需要预先配置ADD USRTAIRANGE。
- 若BINDTYPE取值为USRTAIRANGE，系统中不同PCF业务服务区对应的用户TAI区域不能重叠，配置命令时会有相应检测，若用户TAI区域有重叠则配置下发失败。
- 若PCFSSCOPE配置有记录，且激活请求未携带用户TA

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| BINDNAME | 绑定名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。 |
| SSCOPEID | 服务区标识 | local_planned | required | 无 | 字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。 |
| BINDTYPE | 绑定类型 | local_planned | required | 无 | <br>- “USRTAIRANGE（用户TAI范围）”：指定用户TAI范围与PCF服务区标识绑定。 |
| USRTAIRANGENAME | 用户TAI区域名称 | local_planned | conditional | 无 | 字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L26:
    > - [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)
    > - [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)
    > - [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)
    > - [**ADD NGMMSUBDATA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/签约数据管理/增加用户移动性管理参数（ADD NGMMSUBDATA）_09651362.md)
    > - [**ADD RULEBINDDNAI**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费和策略的业务管理/业务模板/预定义规则DNAI绑定/增加预定义规则关联的DNAI（ADD RULEBINDDNAI）_27170471.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md) | 绑定名称（BINDNAME） | towna | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md) | 服务区标识（SSCOPEID） | citya | 已配置数据中获取 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>配置PCF业务服务区与用户TAI区域的绑定关系。 |
  | [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md) | 绑定类型（BINDTYPE） | USRTAIRANGE | 固定取值 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>配置PCF业务服务区与用户TAI区域的绑定关系。 |
  | [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md) | 用户TAI区域名称（USRTAIRANGENAME） | tai1 | 已配置数据中获取 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>配置PCF业务服务区与用户TAI区域的绑定关系。 |
- 操作步骤上下文（±2 行原文）：
  L213:
    >       [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)
    >     3. 配置PCF业务服务区和用户TAI区域的绑定关系。
    >       [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)
    > 
    > ## [任务示例](#ZH-CN_OPI_0172467890)

## ④ 自动比对
- 命令真相参数（4）：['BINDNAME', 'BINDTYPE', 'SSCOPEID', 'USRTAIRANGENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '已配置数据中获取': 2, '固定取值': 1}（多值→atom 应考虑 decision_driven）
