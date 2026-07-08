---
id: UNC@20.15.2@MMLCommand@RMV IMEIGP
type: MMLCommand
name: RMV IMEIGP（删除IMEI群组）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV IMEIGP（删除IMEI群组）

## 功能

**适用网元：SGSN、MME**

此命令用于删除IMEI群组记录。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMEIGPID | IMEI群组标识 | 可选必选说明：必选参数<br>参数含义：待删除的IMEI群组标识。<br>取值范围：1~50<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IMEIGP]] · IMEI群组（IMEIGP）

## 使用实例

删除群组标识为1的IMEI群组：

RMV IMEIGP: IMEIGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMEI群组(RMV-IMEIGP)_72345357.md`
