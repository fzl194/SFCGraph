---
id: UDG@20.15.2@MMLCommand@SET LDPBFD
type: MMLCommand
name: SET LDPBFD（设置LDP BFD配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: LDPBFD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP BFD管理
status: active
---

# SET LDPBFD（设置LDP BFD配置）

## 功能

该命令用于设置LDP BFD配置。使能LDP BFD功能后，可以对LDP Tunnel进行快速的故障检测，提高整网可靠性。

## 注意事项

- 该命令执行后立即生效。
- 可选参数至少选一项。
- 配置该命令前，需要通过SET MPLSSITE全局使能MPLS能力。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| LDPBFDENABLE | LDPBFDTRIGGERTUNNEL | DETCTMULTFORTNL |
| --- | --- | --- |
| FALSE | NONE | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LDPBFDENABLE | LDP BFD能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定LDP BFD能力。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无<br>配置原则：配置该参数前，需要通过SET BFD全局使能BFD能力。 |
| LDPBFDTRIGGERTUNNEL | BFD For LDP Tunnel触发策略 | 可选必选说明：可选参数<br>参数含义：该参数用于指定检测LDP Tunnel的BFD触发策略。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NONE：无触发策略。<br>- HOST：触发方式为主机地址。<br>- FEC_LIST：触发方式为FEC列表。<br>- IP_PREFIX：触发方式为IP前缀列表。<br>默认值：无<br>配置原则：配置该参数前，需要通过SET BFD全局使能BFD能力。 |
| TUNNELIPPREFIXNAME | BFD For LDP Tunnel的IP前缀名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LDPBFDTRIGGERTUNNEL”配置为“IP_PREFIX”时为必选参数。<br>参数含义：该参数用于指定IP前缀名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：所用的IP前缀名需提前配好。通过LST PREFIXFILTERNODE查看当前已存在的IP前缀列表。 |
| TNLFECLISTNAME | BFD For LDP Tunnel FEC列表名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“LDPBFDTRIGGERTUNNEL”配置为“FEC_LIST”时为必选参数。<br>参数含义：该参数用于指定FEC列表的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：所用的FEC列表名称需提前配好。通过LST LDPFECLIST查看当前已存在的FEC列表。 |
| MINTXINTVFORTNL | BFD For LDP Tunnel的BFD最小发送时间间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定BFD会话最小发送时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000。<br>默认值：无<br>配置原则：如果不配置此参数，则实际生效值为200。可以通过DSP BFDSESSION查看。 |
| MINRXINTVFORTNL | BFD For LDP Tunnel的BFD最小接收时间间隔（ms） | 可选必选说明：可选参数<br>参数含义：该参数用于指定BFD会话最小接收时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000。<br>默认值：无<br>配置原则：如果不配置此参数，则实际生效值为200。可以通过DSP BFDSESSION查看。 |
| DETCTMULTFORTNL | BFD For LDP Tunnel的BFD可容忍丢失次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BFD会话可容忍丢失次数。如果BFD会话在设置的检测周期内没有收到对端发来的BFD报文，则认为链路发生了故障，BFD会话的状态将会置为Down。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无<br>配置原则：如果不配置此参数，则实际生效值为3。可以通过DSP BFDSESSION查看。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPBFD]] · LDP BFD配置（LDPBFD）

## 使用实例

设置LDP BFD配置：

```
SET LDPBFD:LDPBFDENABLE=TRUE,LDPBFDTRIGGERTUNNEL=HOST,MINTXINTVFORTNL=45,MINRXINTVFORTNL=45,DETCTMULTFORTNL=40;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-LDPBFD.md`
