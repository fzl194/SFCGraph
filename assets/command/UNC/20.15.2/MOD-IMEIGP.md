---
id: UNC@20.15.2@MMLCommand@MOD IMEIGP
type: MMLCommand
name: MOD IMEIGP（修改IMEI群组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: IMEIGP
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
- 业务安全管理
- 用户终端管理
- IMEI群组管理
status: active
---

# MOD IMEIGP（修改IMEI群组）

## 功能

**适用网元：SGSN、MME**

此命令用于修改IMEI群组名称，无法修改群组标识。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：待修改的IMEI群组标识。<br>数据来源：本端规划<br>取值范围：1~50<br>默认值：无 |
| IMEIGPN | IMEI群组名称 | 可选必选说明：可选参数<br>参数含义：待修改的IMEI群组名称。<br>数据来源：本端规划<br>取值范围：0~255位字符串<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIGP]] · IMEI群组（IMEIGP）

## 使用实例

将IMEI群组标识为1的群组名称修改为“iphone”：

MOD IMEIGP: IMEIGPID=1, IMEIGPN="iphone";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-IMEIGP.md`
