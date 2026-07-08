---
id: UNC@20.15.2@MMLCommand@MOD NGMNO
type: MMLCommand
name: MOD NGMNO（修改5G模式移动网络运营商信息）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGMNO
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- SMF
- NRF
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 5G 移动网络运营商管理
status: active
---

# MOD NGMNO（修改5G模式移动网络运营商信息）

## 功能

![](修改5G模式移动网络运营商信息（MOD NGMNO）_09654365.assets/notice_3.0-zh-cn_2.png)

执行该命令配置的运营商信息配置不合理将导致用户无法驻留网络，影响用户业务。

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于修改移动网络运营商基本信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于在系统内唯一标识移动网络运营商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：无 |
| FULLNAME | 运营商全称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网络运营商的全称。AMF发送给UE的Configuration Update Command消息中携带的“Full name for network”信元值来源于本参数。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |
| SHORTNAME | 运营商简称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网络运营商的简称。AMF下发给UE的Configuration Update Command消息中携带的“Short name for network”信元值来源于本参数。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数表示对移动网络运营商的描述信息，在运维过程中起到助记的作用。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。<br>默认值：无<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGMNO]] · 5G模式移动网络运营商信息（NGMNO）

## 使用实例

修改标识为1的运营商名称，执行如下命令：

```
MOD NGMNO: NOID=0, FULLNAME="Operator B", SHORTNAME="OB";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGMNO.md`
