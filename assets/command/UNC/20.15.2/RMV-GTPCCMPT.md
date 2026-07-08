---
id: UNC@20.15.2@MMLCommand@RMV GTPCCMPT
type: MMLCommand
name: RMV GTPCCMPT（删除GTP-C V0/V1协议兼容性配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCCMPT
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
- GTP-C协议管理
- GTP-C V0 V1协议兼容性
status: active
---

# RMV GTPCCMPT（删除GTP-C V0/V1协议兼容性配置）

## 功能

**适用网元：SGSN、MME**

- 此命令用于删除GTP-C V0/V1协议兼容性配置。

## 注意事项

- 此命令执行后立即生效。
- SGSN发送GTP消息SGSN Context Response、Forward Relocation Request时，可以控制在GTP消息中是否允许携带R4协议版本新增加的可选信元RAB Context、Charging Characteristics等。当没有指定在GTP消息中，是否允许携带特定的可选信元时，系统默认情况下将在GTP消息中携带这些可选信元。
- 一次只允许删除一条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定唯一标识特定的可选信元的索引。<br>取值范围：0～511<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCCMPT]] · GTP-C V0/V1协议兼容性配置（GTPCCMPT）

## 使用实例

删除一条GTP-C V0/V1协议兼容性配置，索引为0的记录：

RMV GTPCCMPT: IDX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-C-V0_V1协议兼容性配置(RMV-GTPCCMPT)_26305732.md`
