---
id: UNC@20.15.2@MMLCommand@ADD SELCHFGBYIMSI
type: MMLCommand
name: ADD SELCHFGBYIMSI（增加IMSI与CHF组的绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SELCHFGBYIMSI
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# ADD SELCHFGBYIMSI（增加IMSI与CHF组的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于增加IMSI与CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于拨测CHF，拨测完成后建议立即删除该配置。
- SMF选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。

- 最多可输入30条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | 用户的IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于设置绑定的IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。<br>默认值：无<br>配置原则：<br>该参数表示用户完整的IMSI信息，不支持前缀匹配。 |
| PRIMARYCHFGRP | 主CHF组 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主CHF组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |
| SECONDARYCHFGRP | 备CHF组 | 可选必选说明：可选参数<br>参数含义：该参数用于设置备CHF组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD TNFGRP命令配置生成。 |

## 操作的配置对象

- [IMSI与CHF组的绑定关系（SELCHFGBYIMSI）](configobject/UNC/20.15.2/SELCHFGBYIMSI.md)

## 使用实例

增加基于IMSI值123456789012345选择主CHF组CHF1和备CHF组CHF2的处理:

```
ADD SELCHFGBYIMSI: IMSI="123456789012345", PRIMARYCHFGRP="CHF1", SECONDARYCHFGRP="CHF2";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加IMSI与CHF组的绑定关系（ADD-SELCHFGBYIMSI）_88303804.md`
