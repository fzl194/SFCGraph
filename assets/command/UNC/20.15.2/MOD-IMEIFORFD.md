---
id: UNC@20.15.2@MMLCommand@MOD IMEIFORFD
type: MMLCommand
name: MOD IMEIFORFD（修改强制分离策略）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMEIFORFD
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 强制分离业务IMEI配置
status: active
---

# MOD IMEIFORFD（修改强制分离策略）

## 功能

**适用网元：SGSN**

该命令用来修改强制分离策略的配置数据。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能修改“描述”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEISV | IMEISV | 可选必选说明：必选参数<br>参数含义：该参数用于设置<br>UNC<br>需要保留的IMEISV字段。<br>数据来源：整网规划<br>取值范围：16位十进制数字<br>默认值：无 |
| MASK | 掩码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示IMEISV字段相应的掩码。<br>数据来源：整网规划<br>取值范围：16位二进制数字<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMEISV匹配规则的记录名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IMEIFORFD]] · 强制分离策略（IMEIFORFD）

## 使用实例

将强制分离策略的描述修改为“FOR USERGRP2”：

MOD IMEIFORFD: IMEISV="1234567890123456", MASK="1111110000000000", DESC="FOR USERGRP2";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IMEIFORFD.md`
