---
id: UNC@20.15.2@MMLCommand@RMV SCCPOPC
type: MMLCommand
name: RMV SCCPOPC（删除SCCP本局信令点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SCCPOPC
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP本局信令点
status: active
---

# RMV SCCPOPC（删除SCCP本局信令点）

## 功能

![](删除SCCP本局信令点(RMV SCCPOPC)_26306142.assets/notice_3.0-zh-cn_2.png)

删除带SGSN Number的SCCPOPC，会导致各业务功能失效。

**适用网元：SGSN、MME、SMSF**

此命令用于删除SCCP本局信令点表中指定的记录。

## 注意事项

- 本局信令点对应的记录在本局信令点表中已经存在。
- SCCP目的信令点、子系统、GT表中不能存在与该本局信令点相关的记录。
- 删除携带SGSN Number的SCCPOPC，会导致2、3G业务功能失效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | 本局信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本局信令点索引。<br>取值范围：1～64<br>默认值：无<br>说明：- 删除时要先检查本局信令点索引不能被[**ADD HNOINFO**](../../../网络管理/归属网络运营商管理/归属网络信息管理/增加归属网络信息(ADD HNOINFO)_26305862.md)、[**ADD IMSICHAR**](../../../网络管理/归属网络运营商管理/IMSI号段属性配置表/增加IMSI号段属性配置(ADD IMSICHAR)_72225729.md)命令引用。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCCPOPC]] · SCCP本局信令点（SCCPOPC）

## 使用实例

以下命令删除索引值为1的SCCP本局信令点表中记录：

RMV SCCPOPC: OPX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SCCP本局信令点(RMV-SCCPOPC)_26306142.md`
