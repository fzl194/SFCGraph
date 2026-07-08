---
id: UNC@20.15.2@MMLCommand@LCK IMSIMSISDNSEG
type: MMLCommand
name: LCK IMSIMSISDNSEG（锁定IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
verb: LCK
object_keyword: IMSIMSISDNSEG
command_category: 动作类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMSI MSISDN号段
status: active
---

# LCK IMSIMSISDNSEG（锁定IMSI和MSISDN号段）

## 功能

**适用NF：PGW-C、SMF**

该命令用来配置对指定IMSI/MSISDN号码段进行锁定操作。当IMSI/MSISDN号码段锁定后，后续该IMSI/MSISDN号码段内的用户会激活失败，已经在线的用户无影响。缺省情况下IMSI/MSISDN号码段未锁定。

## 注意事项

- 该命令执行后立即生效。
- 修改IMSI/MSISDN号码段的锁定状态时，对后续激活的用户生效。
- 一般情况下不要锁定IMSI/MSISDN号码段。只有在特殊情况下，例如需要手动去活UNC上该IMSI/MSISDN号码段内的所有用户时，可以将LOCKED参数置为ENABLE来限制用户激活。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| LOCKED | 锁定IMSIMSISDN号段 | 可选必选说明：必选参数<br>参数含义：该参数用于锁定或解锁标识。当IMSI/MSISDN号码段锁定后，后续该IMSI/MSISDN号码段内的用户会激活失败，已经在线的用户无影响。通过LCK IMSIMSISDNSEG配置。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMSIMSISDNSEG]] · IMSI和MSISDN号段（IMSIMSISDNSEG）

## 使用实例

锁定IMSI/MSISDN号码段，IMSI/MSISDN号码段名称为huawei：

```
LCK IMSIMSISDNSEG:SEGMENTNAME="huawei",LOCKED=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LCK-IMSIMSISDNSEG.md`
