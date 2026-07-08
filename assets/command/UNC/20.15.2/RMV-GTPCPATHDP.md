---
id: UNC@20.15.2@MMLCommand@RMV GTPCPATHDP
type: MMLCommand
name: RMV GTPCPATHDP（删除GTP-C路径管理自定义策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCPATHDP
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径管理自定义策略
status: active
---

# RMV GTPCPATHDP（删除GTP-C路径管理自定义策略）

## 功能

**适用网元：SGSN**

该命令用于删除GTP-C路径管理自定义策略。

## 注意事项

- 该命令执行后，系统默认的漫游路径的“故障判定钝化系数”的值为1，“漫游路径告警ID控制”的值为“COMMON（公共告警ID）”。
- 该命令执行后，“故障判定钝化系数”对新的故障判定生效，“漫游路径告警ID控制”对新产生的告警生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 路径范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C路径范围。<br>取值范围：<br>- ROAMING（漫游路径）<br>默认值：无 |

## 操作的配置对象

- [GTP-C路径管理自定义策略（GTPCPATHDP）](configobject/UNC/20.15.2/GTPCPATHDP.md)

## 使用实例

删除漫游路径的自定义管理策略:

RMV GTPCPATHDP: RANGE=ROAMING;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除GTP-C路径管理自定义策略(RMV-GTPCPATHDP)_26145914.md`
