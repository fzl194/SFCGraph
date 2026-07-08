---
id: UNC@20.15.2@MMLCommand@RMV QCICONV
type: MMLCommand
name: RMV QCICONV（删除扩展QCI转换关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QCICONV
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- EPS QoS
- 扩展QCI转换关系
status: active
---

# RMV QCICONV（删除扩展QCI转换关系）

## 功能

**适用网元：MME**

该命令用于删除系统中扩展QCI(QoS Class Identifier)向标准QCI的转换关系配置表。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QCIEXT | 扩展QCI基准值 | 可选必选说明：必选参数<br>参数含义：待删除的扩展QCI基准值。<br>取值范围：10～254<br>默认值：无 |
| QCISTEP | 扩展QCI范围 | 可选必选说明：可选参数<br>参数含义：待删除的扩展QCI取值范围值。扩展QCI范围是指<br>“扩展QCI基准值”<br>加上<br>“扩展QCI范围”<br>，在这一范围内的扩展QCI向标准QCI的转换关系配置表将统一被删除。<br>取值范围：0～244<br>默认值：无<br>说明：- “扩展QCI范围”与“扩展QCI基准值”之和必须大于9并小于255。<br>- 如果不输入，则表示删除系统内扩展QCI值为扩展QCI基准值向QCI标准值的转换关系。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QCICONV]] · 扩展QCI转换关系（QCICONV）

## 使用实例

删除扩展QCI值从10到30内向标准QCI的转换关系配置表：

RMV QCICONV: QCIEXT=10, QCISTEP=20;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除扩展QCI转换关系(RMV-QCICONV)_26146214.md`
