---
id: UNC@20.15.2@MMLCommand@ADD IMEIGP
type: MMLCommand
name: ADD IMEIGP（增加IMEI群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IMEIGP
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 50
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户终端管理
- IMEI群组管理
status: active
---

# ADD IMEIGP（增加IMEI群组）

## 功能

**适用网元：SGSN、MME**

此命令用于增加IMEI群组记录，为IMEI群组成员提供群组标识等信息，以群粒度进行业务策略控制。需要结合 [**ADD IMEIGPMEM**](../IMEI群组成员管理/增加IMEI群组成员(ADD IMEIGPMEM)_26305568.md) 命令配置成员信息。

## 注意事项

- 此命令最大记录数为50。
- 此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IMEI群组标识。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |
| IMEIGPN | IMEI群组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMEI群组名称。<br>数据来源：本端规划<br>取值范围：0~255位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIGP]] · IMEI群组（IMEIGP）

## 使用实例

增加一个IMEI群组，其群组名称为“iphone”，群组成员设备型号核准号码为35437906：

ADD IMEIGP: IMEIGPID=1, IMEIGPN="iphone";

ADD IMEIGPMEM: IMEIGPID=1, IMEITAC="35437906";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-IMEIGP.md`
