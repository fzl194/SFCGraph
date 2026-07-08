---
id: UNC@20.15.2@MMLCommand@RMV PGWRESEL
type: MMLCommand
name: RMV PGWRESEL（删除本地P-GW重选策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PGWRESEL
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 会话管理
- 本地P-GW重选功能配置
status: active
---

# RMV PGWRESEL（删除本地P-GW重选策略）

## 功能

**适用网元：MME**

该命令用于删除一条本地P-GW重选策略的配置记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APN网络标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN网络标识。当PDN使用了该APN网络标识，系统对其进行本地P-GW重选的识别和处理。<br>数据来源：全网规划<br>取值范围：1~62位字符串<br>默认值：无<br>说明：- APN网络标识由一个或多个LABEL构成，各LABEL间用“.”间隔。<br>- 每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。<br>- APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PGWRESEL]] · 本地P-GW重选策略（PGWRESEL）

## 使用实例

删除 “APN网络标识” 为HUAWEI的本地P-GW重选配置记录：

RMV PGWRESEL: APNNI="HUAWEI";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PGWRESEL.md`
