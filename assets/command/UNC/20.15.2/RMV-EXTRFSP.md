---
id: UNC@20.15.2@MMLCommand@RMV EXTRFSP
type: MMLCommand
name: RMV EXTRFSP（删除扩展RFSP策略组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EXTRFSP
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
- 移动性管理
- RFSP管理
- 扩展RFSP策略管理
status: active
---

# RMV EXTRFSP（删除扩展RFSP策略组成员）

## 功能

**适用网元：SGSN、MME**

该命令用于从RFSP策略组删除策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TYPE | 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该扩展RFSP策略的类型。<br>数据来源：整网规划<br>取值范围：<br>- “SPEC_MOVE_SUB(指定的移动用户)”<br>默认值：无 |
| ARETYPE | 区域类型 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定扩展RFSP策略控制区域范围类型。<br>前提条件：该参数在“TYPE（类型）”参数配置为“SPEC_MOVE_SUB(指定的移动用户)”后生效。<br>数据来源：整网规划<br>取值范围：<br>- “TAGP(跟踪区群组)”<br>- “ENBGP(eNodeB群组)”<br>默认值：无 |
| TAGPID | 跟踪区群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定跟踪区群组标识。<br>前提条件: 该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“TAGP(跟踪区群组)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无 |
| ENBGPID | eNodeB群组标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定eNodeB群组标识。<br>前提条件: 该参数在<br>“ARETYPE（区域类型）”<br>参数配置为<br>“ENBGP(eNodeB群组)”<br>后生效。<br>数据来源：整网规划<br>取值范围：1~2048<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EXTRFSP]] · 扩展RFSP策略组成员（EXTRFSP）

## 使用实例

运营商需要删除针对指定的移动用户，区域类型为TAGP，跟踪区群组为1的扩展RFSP策略组的策略：

RMV EXTRFSP:TYPE=SPEC_MOVE_SUB, ARETYPE=TAGP, TAGPID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EXTRFSP.md`
