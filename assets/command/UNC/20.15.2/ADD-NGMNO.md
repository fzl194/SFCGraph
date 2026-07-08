---
id: UNC@20.15.2@MMLCommand@ADD NGMNO
type: MMLCommand
name: ADD NGMNO（增加5G模式移动网络运营商信息）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD NGMNO（增加5G模式移动网络运营商信息）

## 功能

**适用NF：SGW-C、PGW-C、AMF、SMF、NRF、NSSF**

该命令用于配置移动网络运营商的基本信息，如运营商名称等。

## 注意事项

- 该命令执行后立即生效。

- 系统初始化后，生成一条“NOID”为0的默认记录。
- 整系统仅支持配置一个运营商。
- 本命令配置的运营商名称可通过Configuration Update Command消息由AMF下发给UE。该功能是否启用，受SET NGMMFUNC命令的“发送网络信息”参数控制。
- 在配置或者修改运营商名称后，不支持立即触发UE Configuration Update流程。
- 因终端实现不同，可能部分终端优先使用SIM/USIM卡自带的网络名称，此时网络侧下发的网络名称会不生效。
- 网络名称仅支持中文（包括简体、繁体）和英文。

- 最多可输入1条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NOID |
| --- |
| 0 |

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

- [[configobject/UNC/20.15.2/NGMNO]] · 5G模式移动网络运营商信息（NGMNO）

## 使用实例

本NF被其它运营商共享，增加运营商信息，执行如下命令：

```
ADD NGMNO: NOID=0, FULLNAME="Operator A", SHORTNAME="OA";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加5G模式移动网络运营商信息（ADD-NGMNO）_09652141.md`
