---
id: UNC@20.15.2@MMLCommand@LCK APN
type: MMLCommand
name: LCK APN（锁定APN配置）
nf: UNC
version: 20.15.2
verb: LCK
object_keyword: APN
command_category: 动作类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN管理
- APN
status: active
---

# LCK APN（锁定APN配置）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用来配置对指定APN进行锁定操作。当APN锁定后，后续使用该APN激活的用户激活失败，已经在线的用户无影响。缺省情况下APN未锁定。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 锁定APN的条件是SGW为激活携带的APN，PGW、SMF和GGSN为实际业务APN。如PGW、SMF或GGSN激活携带为虚拟APN，需锁定虚拟APN映射的APN，锁定功能才生效。
- 正在改变APN的锁定状态，如果配置为锁定，会导致用户接入失败。
- 在基于APN进行业务割接、迁移的场景下，需要将某些业务进行迁移，使用该命令对APN进行锁定，防止新用户基于该APN接入，再通过DEA SMCTX命令去活该APN下的用户。
- 当执行命令LCK APN，LOCKED为ENABLE，且选了锁定的RAT类型，表示基于该接入类型的APN被锁定；
- 当执行命令LCK APN，LOCKED为DISABLE，且选了锁定的RAT类型，表示解锁该接入类型的APN，此后允许新用户按此接入类型和该APN接入。
- 当执行命令LCK APN，LOCKED为ENABLE，在未明确指定RAT类型的情况下（例如：LCK APN: APN="test", LOCKED=ENABLE;），表示对test这个APN下所有RAT类型锁定，不允许此APN下所有RAT类型新用户接入；
- 当执行命令LCK APN，LOCKED为DISABLE，在未明确指定RAT类型的情况下（例如：LCK APN: APN="test", LOCKED=DISABLE;），表示对test这个APN下所有RAT类型解锁，此后允许此APN下所有RAT类型新用户接入。
- LCK APN和LCK APNFORBYPASS两个命令任一个对APN进行了锁定，则APN被锁定。
- 针对I-SMF或者S-GW的APN锁定功能是否生效取决于软参BIT1182，若生效，则锁定条件为激活携带的APN。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |
| LOCKED | 锁定 | 可选必选说明：必选参数<br>参数含义：该参数用于配置APN进行锁定操作。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（使能）<br>- DISABLE（不使能）<br>默认值：无<br>配置原则：<br>- 该参数由ENABLE变成DISABLE时，需要判断“锁定的RAT类型”是否都解锁，如果没有都解锁，该字段保持ENABLE。<br>- 该参数为ENABLE时，指定为锁定该APN。<br>- 该参数为DISABLE时，指定为解锁该APN。 |
| LCKRATTYPE | 锁定的RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该APN下锁定的接入类型。<br>数据来源：本端规划<br>取值范围：<br>- UTRAN（通用陆地无线接入网）<br>- GERAN（GSM/EDGE无线接入网）<br>- WLAN（无线局域网）<br>- GAN（通用访问网络）<br>- HSPA（高速分组接入）<br>- EUTRAN（演进型通用陆地无线接入网）<br>- VIRTUAL（非可信接入网）<br>- EUTRAN_NB_IoT（窄带物联网）<br>- LTE_M（演进的高速包数据网络）<br>- NR（5G新空口接入网）<br>- REDCAP（轻量化5G接入）<br>默认值：UTRAN-1&GERAN-1&WLAN-1&GAN-1&HSPA-1&EUTRAN-1&VIRTUAL-1&EUTRAN_NB_IoT-1&LTE_M-1&NR-1&REDCAP-1<br>配置原则：无 |

## 操作的配置对象

- [APN配置（APN）](configobject/UNC/20.15.2/APN.md)

## 使用实例

- 将APN “test”下的所有类型都锁定:
  ```
  LCK APN: APN="test", LOCKED=ENABLE;
  ```
- 将APN “test” 下 RAT类型 “WLAN” 锁定:
  ```
  LCK APN: APN="test", LOCKED=ENABLE, LCKRATTYPE=UTRAN-0&GERAN-0&WLAN-1&GAN-0&HSPA-0&EUTRAN-0&VIRTUAL-0&EUTRAN_NB_IoT-0&LTE_M-0&NR-0&REDCAP-0;
  ```
- 当 APN “test” 下 RAT类型 “WLAN” 被锁定时，解锁此类型：
  ```
  LCK APN: APN="test", LOCKED=DISABLE, LCKRATTYPE=UTRAN-0&GERAN-0&WLAN-1&GAN-0&HSPA-0&EUTRAN-0&VIRTUAL-0&EUTRAN_NB_IoT-0&LTE_M-0&NR-0&REDCAP-0;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/锁定APN配置（LCK-APN）_09652640.md`
