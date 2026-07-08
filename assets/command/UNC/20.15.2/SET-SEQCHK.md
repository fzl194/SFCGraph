---
id: UNC@20.15.2@MMLCommand@SET SEQCHK
type: MMLCommand
name: SET SEQCHK（设置序号检查信息表）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SEQCHK
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
- GnGp接口管理
- GTP用户面管理
- 序号检查信息管理
status: active
---

# SET SEQCHK（设置序号检查信息表）

## 功能

**适用网元：SGSN、MME**

该命令用于设置GTP-U序号检查开关，指示是否进行序号检查。GTP协议规定在进行GTP-U用户面数据转发时，可以对GTP的序号进行检查，也可以不进行检查。如果打开序号检查开关，对无效序号的报文将会做丢弃处理。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- “序号检查功能开关”改变后对已经创建的PDP上下文不起作用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCS | 序号检查功能开关 | 可选必选说明：可选参数<br>参数含义：指示数据转发时是否进行GTP-U数据包序号检查。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关)”：表示对用户面数据包不作序号检查。<br>- “ON(开)”：表示对用户面数据包作序号检查，根据3GPP TS 29.060 Annex A，如果序号无效，该GTP-U数据包将被丢弃。<br>系统初始设置值：<br>“OFF(关)”<br>。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SEQCHK]] · 序号检查信息表（SEQCHK）

## 使用实例

当无需对GTP-U的数据报文进行序号检查时，关闭序号检查开关：

SET SEQCHK: SCS=OFF;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SEQCHK.md`
