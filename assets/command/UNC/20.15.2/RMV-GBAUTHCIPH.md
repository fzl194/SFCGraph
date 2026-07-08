---
id: UNC@20.15.2@MMLCommand@RMV GBAUTHCIPH
type: MMLCommand
name: RMV GBAUTHCIPH（删除Gb模式用户安全参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GBAUTHCIPH
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- Gb模式用户安全参数
status: active
---

# RMV GBAUTHCIPH（删除Gb模式用户安全参数）

## 功能

**适用网元：SGSN**

该命令用于删除2G鉴权加密的配置信息。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于系统根据指定用户的IMSI进行匹配，从而区分不同的用户群。<br>取值范围：5～15位十进制数字<br>默认值：无<br>说明：- 按照IMSI最长匹配进行查询，相同IMSI前缀只能配置一条记录。<br>- IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBAUTHCIPH]] · Gb模式用户安全参数（GBAUTHCIPH）

## 使用实例

删除2G鉴权加密配置，IMSI前缀为"123456＂：

RMV GBAUTHCIPH: IMSIPRE="123456";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GBAUTHCIPH.md`
