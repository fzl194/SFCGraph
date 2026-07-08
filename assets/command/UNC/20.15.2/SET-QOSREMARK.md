---
id: UNC@20.15.2@MMLCommand@SET QOSREMARK
type: MMLCommand
name: SET QOSREMARK（设置全局QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: QOSREMARK
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 全局QoS功能配置
- 全局DSCP_ToS映射功能
status: active
---

# SET QOSREMARK（设置全局QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置系统上下行QoS映射功能开关。QoS映射功能表示将会话中QoS信息映射为用户上行或者下行IP数据报文头中的DSCP/ToS值，以满足报文在转发过程中的优先级与会话上下文中QoS定义的优先级保持一致。

该命令支持配置下行和上行两个方向的开关功能。从MS/UE到远程访问主机的数据流方向称为上行数据流，从远程访问主机到MS/UE的数据流方向称为下行数据流。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DOWNLINK | UPLINK |
| --- | --- |
| DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DOWNLINK | 下行标记 | 可选必选说明：可选参数<br>参数含义：该参数用于设置下行标记的开关功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QOSREMARK查询当前参数配置值。<br>配置原则：无 |
| UPLINK | 上行标记 | 可选必选说明：可选参数<br>参数含义：该参数用于设置上行标记的开关功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QOSREMARK查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/QOSREMARK]] · 全局QoS到TOS/DSCP的映射规则（QOSREMARK）

## 使用实例

开启系统上下行QoS映射功能开关：

```
SET QOSREMARK:DOWNLINK=ENABLE,UPLINK=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-QOSREMARK.md`
