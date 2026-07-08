---
id: UNC@20.15.2@MMLCommand@SET ARPEPS2PRER8
type: MMLCommand
name: SET ARPEPS2PRER8（设置EPS ARP到Pre-R8 ARP的映射规则）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: ARPEPS2PRER8
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- EPS ARP到PreR8 ARP映射
status: active
---

# SET ARPEPS2PRER8（设置EPS ARP到Pre-R8 ARP的映射规则）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于配置Gn接口和Gx接口之间ARP的映射值。

在Gn接口，ARP对应QoSProfile信元中的Allocation/Retention priority字段（3GPP R99 及之后）或Precedence class字段（3GPP R97/R98），取值范围为1~3。在Gx接口，ARP定义有专门的AVP（属性值对），取值范围为1~15。Gn接口和Gx接口的取值范围不一致，需要进行映射。

假设本命令配置的ARP高优先级上限（HIGH）为H，ARP中优先级上限（MEDIUM）为M，则ARP映射规则如下：

在Gn接口到Gx接口方向上，ARP为1时映射为1，ARP为2时映射为H+1，ARP为3时映射为M+1。在Gx接口到Gn接口方向上，ARP在<1，H>、<H+1，M>、<M+1，15>范围之内分别映射到1，2和3。

## 注意事项

- 该命令执行后只对新激活用户生效。

- ARP高优先级上限必须小于ARP中优先级上限。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HIGH | MEDIUM |
| --- | --- |
| 5 | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HIGH | ARP高优先级上限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP优先级正常时（ARP值为2）的映射值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~13。<br>默认值：无。<br>配置原则：无 |
| MEDIUM | ARP中优先级上限 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP优先级低时（ARP值为3）的映射值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是2~14。<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ARPEPS2PRER8]] · EPS ARP到Pre-R8 ARP的映射规则（ARPEPS2PRER8）

## 使用实例

配置“ARP高优先级上限”为“6”，“ARP中优先级上限”为“7”：

```
SET ARPEPS2PRER8:HIGH=6,MEDIUM=7;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-ARPEPS2PRER8.md`
