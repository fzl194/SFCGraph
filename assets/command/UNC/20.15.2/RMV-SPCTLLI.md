---
id: UNC@20.15.2@MMLCommand@RMV SPCTLLI
type: MMLCommand
name: RMV SPCTLLI（删除特殊随机TLLI配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SPCTLLI
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
- 特殊TLLI配置
status: active
---

# RMV SPCTLLI（删除特殊随机TLLI配置）

## 功能

**适用网元：SGSN**

该命令用于对删除某项RANDOM TLLI的配置记录，删除后对该RANDOM TLLI的附着不做特殊处理。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TLLI | TLLI | 可选必选说明：必选参数<br>参数含义：该参数用于指定RANDOM TLLI。<br>数据来源：网上问题<br>取值范围： 0x00000000～0xffffffff(十六进制)<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SPCTLLI]] · 特殊随机TLLI配置（SPCTLLI）

## 使用实例

删除一条RANDOM TLLI为71234abc的记录：

**RMV SPCTLLI: TLLI="0x71234abc";或者 RMV SPCTLLI: TLLI="71234abc";**

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除特殊随机TLLI配置(RMV-SPCTLLI)_72345093.md`
