# 命令证据包：RMV CHGIMSICFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/删除IMSI计费配置(RMV CHGIMSICFG)_72225065.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用来删除 “IMSI前缀” 计费配置表中某条 “IMSI前缀” 的配置。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效，影响新激活用户的话单生成策略，但该配置只对之后激活的用户有效。
- 当没有指定“计费属性”、“拜访类型”字段时，如果输入的必选参数“用户范围”、“IMSI前缀”、“APNNI”能够同时匹配到多条记录，则此操作会将所有的匹配记录删除。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 |  | required | 无 | <br>- “ALL_USER（所有用户）” |
| IMSIPRE | IMSI前缀 |  | conditional | 无 | 5～15位十进制字符串 |
| VISITTYPE | 拜访类型 |  | optional | 无 | <br>- “ROAMING（使用归属地GGSN的漫游用户）” |
| APNNI | APNNI |  | required | 无 | 最大长度为62个字符 |
| CC | 计费属性 |  | optional | 无 | <br>- HOT_BILLING(实时计费) |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L25:
    > - [**ADD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/增加IMSI计费配置(ADD CHGIMSICFG)_26145384.md)
    > - [**MOD CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/修改IMSI计费配置(MOD CHGIMSICFG)_26305200.md)
    > - [**RMV CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/删除IMSI计费配置(RMV CHGIMSICFG)_72225065.md)
    > - [**LST CHGIMSICFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/IMSI计费配置/查询IMSI计费配置(LST CHGIMSICFG)_72344987.md)
    > - [**ADD CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)

## ④ 自动比对
- 命令真相参数（5）：['APNNI', 'CC', 'IMSIPRE', 'SUBRANGE', 'VISITTYPE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
