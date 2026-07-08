---
id: UNC@20.15.2@MMLCommand@CLR SCTPAS
type: MMLCommand
name: CLR SCTPAS（清除SCTP统计信息）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: SCTPAS
command_category: 动作类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- SCTP统计信息
status: active
---

# CLR SCTPAS（清除SCTP统计信息）

## 功能

**适用网元：SGSN、MME**

此命令用于清除SCTP统计信息

## 注意事项

无。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLRAST | 统计类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SCTP偶联统计类型。<br>取值范围：<br>- “PROINT(协议内部实体)”<br>- “GLBTR(全局实体)”<br>- “ERROR(错误实体)”<br>- “ASSOC(偶联实体)”<br>- “ALL(全部)”<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划。<br>取值范围：1~63 位字符串<br>默认值：无 |
| PN | 进程号 | 可选必选说明：必选参数<br>参数含义：该参数用于设置需要查询的SGP进程的进程号。<br>取值范围：0～11<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPAS]] · SCTP统计信息（SCTPAS）

## 使用实例

清除RU名称为USN_VSU1、进程号为0的SCTP偶联统计信息：

CLR SCTPAS: CLRAST=GLBTR, RUNAME="USN_VSU1", PN=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除SCTP统计信息(CLR-SCTPAS)_26305666.md`
