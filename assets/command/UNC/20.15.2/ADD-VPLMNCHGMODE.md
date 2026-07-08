---
id: UNC@20.15.2@MMLCommand@ADD VPLMNCHGMODE
type: MMLCommand
name: ADD VPLMNCHGMODE（增加基于VPLMN配置的漫游用户归属地计费模式）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VPLMNCHGMODE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- QBC计费控制
status: active
---

# ADD VPLMNCHGMODE（增加基于VPLMN配置的漫游用户归属地计费模式）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于增加基于VPLMN配置的漫游用户归属地计费模式。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入200条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VPLMN | VPLMN信息 | 可选必选说明：必选参数<br>参数含义：该参数用表示漫游场景拜访地的PLMN信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~6。PLMN字符串的格式为MCCMNC，MCC长度为3个字符，MNC长度为2或者3个字符。<br>默认值：无<br>配置原则：无 |
| CHGMODE | 计费模式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置漫游用户在归属地的计费模式。<br>数据来源：全网规划<br>取值范围：<br>- “FBC（FBC计费）”：漫游用户在归属地使用FBC计费。<br>- “QBC（QBC计费）”：漫游用户在归属地使用QBC计费。<br>- “NOCHG（不计费）”：漫游用户在归属地不做计费功能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/VPLMNCHGMODE]] · 基于VPLMN配置的漫游用户归属地计费模式（VPLMNCHGMODE）

## 使用实例

增加VPLMN为“08600”的漫游用户归属地计费模式为FBC计费：

```
ADD VPLMNCHGMODE: VPLMN="08600", CHGMODE=FBC;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-VPLMNCHGMODE.md`
