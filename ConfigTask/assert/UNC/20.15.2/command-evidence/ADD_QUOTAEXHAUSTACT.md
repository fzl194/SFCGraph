# 命令证据包：ADD QUOTAEXHAUSTACT
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/融合计费/配额耗尽处理动作/增加配额耗尽后的动作（ADD QUOTAEXHAUSTACT）_95129686.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：PGW-C、SMF**

该命令用于增加在线RG配额耗尽后的动作。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后只对新激活用户生效。

- 最多可输入101条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| CCTMPLTNAME | 融合计费模板名称 | local_planned | required | 无 | 字符串类型，输入长度范围是1~63。不区分大小写。 |
| ACTION | 在线RG配额耗尽后动作 | local_planned | optional | 无 | 不配置此参数时值默认为0，表示不下发在线RG配额耗尽后动作。 |
| RDVIRTIP | 重定向IPv4地址 | global_planned | conditional | 无 | IPv4地址类型。 |
| RDVIRTIPV6 | 重定向IPv6地址 | global_planned | conditional | 无 | IPv6地址类型。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011206

**md：`WSFD-011206/配置融合计费费率标识_93360308.md`**
- 操作步骤上下文（±2 行原文）：
  L113:
    >             每个DNN实例只能绑定一个UserProfile组。如UserProfile组和DNN实例已配置且已绑定，本步骤只需执行 **ADD UPBINDUPG** 命令，将UserProfile绑定到UserProfile组即可。
    >     5. **可选：** 配置在线RG配额耗尽后的默认动作。
    >       **ADD QUOTAEXHAUSTACT**
    >       > **说明**
    >       > 当计费事件触发SMF发起Charging Data Request[Update]更新消息申请配额，Total Volume到达后仍未收到CHF响应消息，且SMF本地通过 **SET FAILHANDLING** 命令配置的TXTIMER超时时长未到达时，RG配额耗尽后的默认动作根据 “ACTION” 参数配置生效。

## ④ 自动比对
- 命令真相参数（4）：['ACTION', 'CCTMPLTNAME', 'RDVIRTIP', 'RDVIRTIPV6']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
