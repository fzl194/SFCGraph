# 命令证据包：ADD PCFSSCOPE
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SMF、PGW-C、GGSN**

该命令用于增加PCF的业务服务区配置。语音用户通过N7口向PCF请求策略时，可通过服务区名称选择可用PCF。具体过程如下：PCF向NRF注册时携带其服务区名称。会话建立阶段，SMF通过语音用户TAI区域查询配置PCFSSCOPEBIND得到对应的服务区标识，再通过本配置匹配到对应的服务区名称，并携带该服务区名称向NRF查询可用PCF，从而发起会话建
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 若PCFSSCOPE配置有记录（通过LST PCFSSCOPE查询），且激活请求未携带用户TAI、或根据用户TAI无法从PCFSSCOPEBIND中匹配到合适的SSCOPEID，则从PCFSSCOPE的记录内随机选择一个SSCOPENAME用于PCF服务发现。
- 若PCFSSCOPE配置无记录（通过LST PCFSSCOPE查询），会根据PNFSLCTSSCOP

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SSCOPEID | 服务区标识 | local_planned | required | 无 | 字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。 |
| SSCOPENAME | 服务区名称 | global_planned | required | 无 | 字符串类型，输入长度范围是1~50。 区分大小写。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-109101

**md：`WSFD-109101/WSFD-109101 PCC基本功能（5G）参考信息_72466541.md`**
- 操作步骤上下文（±2 行原文）：
  L24:
    > - [**MOD AMUEPLCYCTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AM策略和UE策略控制参数/修改AM策略和UE策略控制参数（MOD AMUEPLCYCTRL）_09654427.md)
    > - [**SET AMFPLCYFUNC**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/5G接入业务管理/移动性管理/AM策略和UE策略管理/AMF策略功能管理/设置AMF策略功能（SET AMFPLCYFUNC）_96792665.md)
    > - [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)
    > - [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)
    > - [**ADD PCFSSCOPEBIND**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区绑定/增加PCF业务服务区的绑定关系（ADD PCFSSCOPEBIND）_88537090.md)

**md：`WSFD-109101/激活PCC基本功能_72467890.md`**
- 数据规划表（该命令的参数行）：
  | [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md) | 服务区标识（SSCOPEID） | citya | 本端规划 | 存在多条记录时，该参数不能重复。 |
  | [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md) | 服务区名称（SSCOPENAME） | City_A | 全网规划 | SMF需要根据SERVINGSCOPE选择PCF时需要规划。<br>与PCF向NRF注册时携带的服务区名称相同。 |
- 操作步骤上下文（±2 行原文）：
  L209:
    > - SMF需要根据SERVINGSCOPE选择PCF时，配置PCF业务服务区和用户TAI区域的绑定关系。
    >     1. 增加PCF的业务服务区。
    >       [**ADD PCFSSCOPE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/PCF业务服务区/增加PCF的业务服务区（ADD PCFSSCOPE）_35636447.md)
    >     2. 配置用户TAI区域。
    >       [**ADD USRTAIRANGE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/PCC管理/PCF发现和选择管理/用户TAI区域/增加用户TAI区域（ADD USRTAIRANGE）_88537092.md)

## ④ 自动比对
- 命令真相参数（2）：['SSCOPEID', 'SSCOPENAME']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'本端规划': 1, '全网规划': 1}（多值→atom 应考虑 decision_driven）
