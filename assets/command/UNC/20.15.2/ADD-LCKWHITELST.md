---
id: UNC@20.15.2@MMLCommand@ADD LCKWHITELST
type: MMLCommand
name: ADD LCKWHITELST（增加锁定白名单记录）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LCKWHITELST
command_category: 配置类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 锁定白名单
status: active
---

# ADD LCKWHITELST（增加锁定白名单记录）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于增加锁定白名单记录。符合该白名单的用户不受LCK APN和LCK SESSIONACT命令的影响，能够创建会话或专载。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| WHITELSTTYPE | 白名单类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定白名单的类型。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（IMSI）<br>- MSISDN（MSISDN）<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"WHITELSTTYPE"配置为"IMSI"时为条件必选参数。<br>参数含义：该参数用于指定国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是14~15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| MSISDN | MSISDN | 可选必选说明：该参数在"WHITELSTTYPE"配置为"MSISDN"时为条件必选参数。<br>参数含义：该参数用于指定移动台国际ISDN号码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~15。每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LCKWHITELST]] · 锁定白名单记录（LCKWHITELST）

## 使用实例

- 在锁定白名单中新增IMSI为123456789012345的用户：
  ```
  ADD LCKWHITELST: WHITELSTTYPE=IMSI, IMSI="123456789012345";
  ```
- 在锁定白名单中新增MSISDN为123456789012345的用户：
  ```
  ADD LCKWHITELST: WHITELSTTYPE=MSISDN, MSISDN="123456789012345";
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LCKWHITELST.md`
