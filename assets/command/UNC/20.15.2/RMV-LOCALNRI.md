---
id: UNC@20.15.2@MMLCommand@RMV LOCALNRI
type: MMLCommand
name: RMV LOCALNRI（删除本局NRI配置信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCALNRI
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- SGSN POOL区管理
- 本局NRI配置
status: active
---

# RMV LOCALNRI（删除本局NRI配置信息）

## 功能

**适用网元：SGSN**

此命令用于删除本局NRI配置信息。

## 注意事项

- 此命令执行立即生效。
- 只有处于BLOCKED状态的记录才允许被删除。在执行该命令之前，需执行**[BLK LOCALNRI](闭塞本局NRI配置信息(BLK LOCALNRI)_26305910.md)**命令，闭塞NRI配置信息，使其处于BLOCKED状态。
- 该命令输入的“NRI起始值”必须为**[ADD LOCALNRI](增加本局NRI配置信息(ADD LOCALNRI)_72345699.md)**命令中输入的“NRI起始值”。从“NRI起始值”开始的N个NRI都将被删除（其中N为**[ADD LOCALNRI](增加本局NRI配置信息(ADD LOCALNRI)_72345699.md)**命令中输入的“NRI个数”）。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POOLID | POOL区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定POOL区标识。<br>取值范围：0～4095<br>默认值：无 |
| NRIVBGN | NRI起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定NRI起始值，NRI（Net Resource Identify），网络资源标识，用于标识一个CN节点。RAN根据NRI将MS的消息路由到对应的SGSN。<br>取值范围：0～1023<br>默认值：无<br>说明：- NRI的取值范围在0～(2n-1)，n为本Pool的NRI长度。<br>- 若POOL表的NRI长度为10，则LOCALNRI表的NRI个数必须大于等于4， NRI起始值小于等于1020。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCALNRI]] · 本局NRI配置信息（LOCALNRI）

## 使用实例

删除一条POOLID为1，NRI起始值为10的本局NRI配置信息：

BLK LOCALNRI: POOLID=1, NRIVBGN=10;

RMV LOCALNRI: POOLID=1, NRIVBGN=10;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除本局NRI配置信息(RMV-LOCALNRI)_26146100.md`
