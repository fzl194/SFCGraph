---
id: UNC@20.15.2@MMLCommand@RMV SCEF
type: MMLCommand
name: RMV SCEF（删除SCEF配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCEF
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Diameter应用协议
- SCEF管理
status: active
---

# RMV SCEF（删除SCEF配置）

## 功能

**适用网元：MME**

该命令用于删除SCEF配置。

## 注意事项

- 此命令执行后立即生效。
- 删除后，将导致系统无法找到指定的SCEF。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCEFHTN | SCEF主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCEF主机名。<br>数据来源：对端协商<br>取值范围：1~127位字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCEF]] · SCEF配置（SCEF）

## 使用实例

删除SCEF配置：

RMV SCEF: SCEFHTN="scef0701.huawei01.com";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SCEF.md`
