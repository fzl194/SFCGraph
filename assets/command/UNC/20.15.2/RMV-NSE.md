---
id: UNC@20.15.2@MMLCommand@RMV NSE
type: MMLCommand
name: RMV NSE（删除信令实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSE
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- 信令实体管理
status: active
---

# RMV NSE（删除信令实体）

## 功能

![](删除信令实体(RMV NSE)_72225707.assets/notice_3.0-zh-cn_2.png)

删除NSE将导致该NSE相关业务无法继续。

**适用网元：SGSN**

该命令用于删除NSE网络服务实体参数。信令实体分别位于BSS侧和SGSN侧，用于提供Gb接口操作所需的网络管理功能。请参考 3GPP TS 48.016。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令后被删除的NSE下所属小区的业务无法进行，在实际应用中除非网络调整，否则不建议使用。
- 如果不输入任何参数，则提示：请输入"NSE connection direction"参数或者"NSE ID"参数。
- 若输入“OTHERNODE（NSE连接方向）”，表示删除所有属于该OTHERNODE的记录。
- 通过“OTHERNODE（NSE连接方向）”删除记录时不可同时输入“NSEI”参数。
- 若输入“NSEI”，表示删除所有属于该NSEI的记录。
- 若小区信息表中存在属于该NSE的小区记录，则不允许删除该NSE。小区信息表中的信息，请参考[**LST CELL**](../小区管理/查询小区(LST CELL)_26145990.md)命令。
- 如果删除NSE时提示NSE下存在远端端点，无法删除NSE，可以执行[**RMV GBIPRMTENDPT**](../Gb over IP管理/对端IP端点配置/删除对端端点配置(RMV GBIPRMTENDPT)_72345613.md)强制删除远端端点后，删除NSE。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OTHERNODE | NSE连接方向 | 可选必选说明：可选参数<br>参数含义：该参数用于指定该NSE所连接的对端局点的名字。<br>取值范围：1～29位字符串<br>默认值：无 |
| SGSNINDEX | SGSN索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SGSN索引。<br>取值范围：0<br>默认值：0 |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSE]] · 信令实体（NSE）

## 使用实例

1. 删除连接方向为“ShangHai”的所有NSE：
  RMV NSE: OTHERNODE="ShangHai";
2. 删除NSEI为10的NSE：
  RMV NSE: NSEI=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NSE.md`
