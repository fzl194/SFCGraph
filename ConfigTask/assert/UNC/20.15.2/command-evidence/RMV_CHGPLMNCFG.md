# 命令证据包：RMV CHGPLMNCFG
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/删除PLMN计费配置(RMV CHGPLMNCFG)_26305206.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用网元：SGSN**

该命令用来删除话单生成策略配置信息。
**notes（规格/上限→应投影 atom rule）**：
- 该命令执行后立即生效。执行后会影响新激活用户的话单生成策略。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| SUBRANGE | 用户范围 |  | required | 无 | <br>- “ALL_USER（所有用户）” |
| MCC | 移动国家码 |  | conditional | 无 | 位数为3的十进制数字 |
| MNC | 移动网号 |  | conditional | 无 | 位数为2或3的十进制数字 |
| APNNI | APNNI |  | required | 无 | 1～62位字符串 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/WSFD-011201 支持离线计费参考信息（适用于SGSN）_29423865.md`**
- 操作步骤上下文（±2 行原文）：
  L29:
    > - [**ADD CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/增加PLMN计费配置(ADD CHGPLMNCFG)_72225071.md)
    > - [**MOD CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/修改PLMN计费配置(MOD CHGPLMNCFG)_72344993.md)
    > - [**RMV CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/删除PLMN计费配置(RMV CHGPLMNCFG)_26305206.md)
    > - [**LST CHGPLMNCFG**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/PLMN计费配置/查询PLMN计费配置(LST CHGPLMNCFG)_26145392.md)
    > - [**ADD CHGAPN**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/计费管理/APN计费属性/增加APN计费属性(ADD CHGAPN)_72344965.md)

## ④ 自动比对
- 命令真相参数（4）：['APNNI', 'MCC', 'MNC', 'SUBRANGE']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
