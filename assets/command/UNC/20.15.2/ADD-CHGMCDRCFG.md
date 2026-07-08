---
id: UNC@20.15.2@MMLCommand@ADD CHGMCDRCFG
type: MMLCommand
name: ADD CHGMCDRCFG（增加M-CDR计费配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CHGMCDRCFG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- 基于PLMN的M-CDR计费配置
status: active
---

# ADD CHGMCDRCFG（增加M-CDR计费配置）

## 功能

**适用网元：SGSN**

本命令用于添加对特定PLMN用户生成M-CDR的配置。

## 注意事项

- 该命令配置数据仅在软参**[BYTE_EX_B76 BIT3](../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/移动性管理/BYTE_EX_B76 BIT3 控制用户detach或inter流程老侧生成M-CDR是否基于PLMN进行控制_98826731.md)**置为1时生效。
- 该命令控制效果与命令**[SET CHGCHAR](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)**的优先级相同。即：**ADD CHGMCDRCFG**配置了对应PLMN或者**[SET CHGCHAR](../计费属性参数配置/设置计费属性参数(SET CHGCHAR)_26145368.md)**开启时，均会生成M-CDR。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定所包含的用户范围。<br>数据来源：整网规划<br>取值范围：<br>- “PLMNID（指定PLMNID）”<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>前提条件：该参数在“用户范围”参数设置为“PLMNID（指定PLMNID）”时生效。<br>数据来源：整网规划<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：条件必选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>前提条件：该参数在“用户范围”参数设置为“PLMNID（指定PLMNID）”时生效。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGMCDRCFG]] · M-CDR计费配置（CHGMCDRCFG）

## 使用实例

增加对MCC=460、MNC=03的用户生成M-CDR的配置。

```
ADD CHGMCDRCFG: SUBRANGE=PLMNID, MCC="460", MNC="03";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-CHGMCDRCFG.md`
