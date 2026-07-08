---
id: UNC@20.15.2@MMLCommand@RMV GTPCAUSE
type: MMLCommand
name: RMV GTPCAUSE（删除GTP原因值）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GTPCAUSE
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
- 网关重选管理
- GTP原因值管理
status: active
---

# RMV GTPCAUSE（删除GTP原因值）

## 功能

**适用网元：SGSN、MME**

此命令用于删除GTP原因值。

## 注意事项

- 此命令执行后立即生效。
- 操作过程或操作后不会引起业务、OM的中断或指标下降。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GTPVERSION | GTP版本 | 可选必选说明：必选参数<br>参数含义：待删除的GTP版本。<br>取值范围：<br>- “GTPV0V1（GTPv0v1）”：表示该指定GTP版本为GTPv0v1。<br>- “GTPV2（GTPv2）”：表示该指定GTP版本为GTPv2。<br>默认值：无 |
| REJCAUSE | 拒绝原因值 | 可选必选说明：必选参数<br>参数含义：待删除的拒绝原因值。<br>取值范围：1~255<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCAUSE]] · GTP原因值（GTPCAUSE）

## 使用实例

删除一条GTP原因值记录，GTP版本为“GTPv0v1”，拒绝原因值为194：

RMV GTPCAUSE: GTPVERSION=GTPV0V1, REJCAUSE=194;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-GTPCAUSE.md`
