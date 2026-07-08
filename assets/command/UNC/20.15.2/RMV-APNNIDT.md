---
id: UNC@20.15.2@MMLCommand@RMV APNNIDT
type: MMLCommand
name: RMV APNNIDT（删除APNNI Direct Tunnel配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNNIDT
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- Direct Tunnel管理
status: active
---

# RMV APNNIDT（删除APNNI Direct Tunnel配置）

## 功能

![](删除APNNI Direct Tunnel配置(RMV APNNIDT)_26146046.assets/notice_3.0-zh-cn_2.png)

如果删除APNNI="*", DT=NO;配置，将会使默认情况下所有APNNI都支持DT，可能导致业务异常。

**适用网元：SGSN**

此命令用于删除APNNI DT属性信息表中的某个APNNI的DT属性记录。

## 注意事项

- 此命令执行后立即生效。
- 用户要使用DT功能还需满足RNC和GGSN支持DT功能。
- 如果删除APNNI="*", DT=NO;配置，将会使默认情况下所有APNNI都支持DT，可能导致业务异常。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNNI | APNNI | 可选必选说明：必选参数<br>参数含义：该参数用于指定启用基于APNNI的DT功能的APNNI。<br>取值范围：1～62位字符串<br>默认值：无<br>说明：“APNNI”<br>（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。“*”表示通配符，如果用户使用的APNNI在配置表中无法匹配到对应的记录，则查询“*”通配符对应的配置记录。如果查询成功则使用“*”对应的配置；如果查询失败，则默认支持DT。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNNIDT]] · APNNI Direct Tunnel配置（APNNIDT）

## 使用实例

删除一条APNNI DT权限属性记录：

RMV APNNIDT: APNNI="huawei.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNNIDT.md`
