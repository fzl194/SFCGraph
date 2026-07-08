---
id: UNC@20.15.2@MMLCommand@RMV SGWDNS
type: MMLCommand
name: RMV SGWDNS（删除S-GW DNS域名策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWDNS
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- S11接口管理
- S-GW域名策略
status: active
---

# RMV SGWDNS（删除S-GW DNS域名策略）

## 功能

**适用网元：SGSN、MME**

该命令用于删除S-GW的域名中PLMNID的组装策略。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNTYPE | 域名类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS域名类型。<br>取值范围：<br>- “RAI(RAI)”<br>- “TAI(TAI)”<br>默认值：无 |
| LAC | 位置区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定位置区域码。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>取值范围：0x0000～0xFFFF<br>默认值：无 |
| RAC | 路由区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定路由区域码。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“RAI(RAI)”<br>时生效。<br>取值范围：0x00～0xFF<br>默认值：无 |
| TAC | 跟踪区域码 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区域码。<br>前提条件：该参数在<br>“DNTYPE(域名类型)”<br>设置为<br>“TAI(TAI)”<br>时生效。<br>取值范围：0x0000～0xFFFF<br>默认值 ：无 |

## 操作的配置对象

- [S-GW DNS域名策略（SGWDNS）](configobject/UNC/20.15.2/SGWDNS.md)

## 使用实例

删除一条域名类型为“TAI”，跟踪区域码为“1”的DNS域名策略记录：

RMV SGWDNS: DNTYPE=TAI, TAC="1";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S-GW-DNS域名策略（RMV-SGWDNS）_26145972.md`
