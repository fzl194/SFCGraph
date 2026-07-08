---
id: UDG@20.15.2@MMLCommand@OPR FEIEXTPORTPKTDEBUG
type: MMLCommand
name: OPR FEIEXTPORTPKTDEBUG（使能外联口报文调测功能）
nf: UDG
version: 20.15.2
verb: OPR
object_keyword: FEIEXTPORTPKTDEBUG
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 外联口报文调测
status: active
---

# OPR FEIEXTPORTPKTDEBUG（使能外联口报文调测功能）

## 功能

![](使能外联口报文调测功能（OPR FEIEXTPORTPKTDEBUG）_49802038.assets/notice_3.0-zh-cn.png)

如果使能调测的时候将消耗内存资源并降低性能，禁用它会释放内存资源并恢复性能，并且会在指定时间内自动禁用，默认时间是60分钟；报文调测产生的文件会在指定时间内自动删除，默认时间是7天。

在报文调测的场景中，该命令用于使能外联口报文调测功能。

## 注意事项

- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。
- 资源单元全部使用EthTrunk子接口场景，无外联子接口，不能自适配VLAN匹配，下发命令时需要添加VLANID。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RULEID | 规则ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示外联口报文调测的规则ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～2。<br>默认值：无 |
| STATUS | 使能状态 | 可选必选说明：必选参数<br>参数含义：该参数用于表示外联口报文调测的使能状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Enable：使能调测。<br>- Disable：去使能调测。<br>默认值：无 |
| VLANID | VLAN ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“STATUS”配置为“Enable”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测要匹配的VLAN ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4095。<br>默认值：无<br>配置原则：如果不设置该参数，则外联口报文调测不指定报文vlan值。 |
| DIRECTION | 报文调测的方向 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATUS”配置为“Enable”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- All：双向。<br>- Rx：接收方向。<br>- Tx：发送方向。<br>默认值：无 |
| TIMEOUT | 有效时间 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATUS”配置为“Enable”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测规则的有效时间，在有效时间范围内重复使能规则会返回失败，单位：分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1440。<br>默认值：无 |
| FILEDELDAY | 结果文件留存天数 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATUS”配置为“Enable”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测结果文件留存天数，单位：天。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1095。<br>默认值：无 |
| DEBUGTYPE | 报文调测的粒度 | 可选必选说明：条件必选参数<br>前提条件：该参数在“STATUS”配置为“Enable”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的粒度。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- All：所有接口。<br>- Vpn：指定VPN。<br>- Interface：指定接口。<br>默认值：无 |
| VPNNAME | VPN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEBUGTYPE”配置为“Vpn”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| IFNAME1 | 接口1 | 可选必选说明：条件必选参数<br>前提条件：该参数在“DEBUGTYPE”配置为“Interface”时为必选参数。<br>参数含义：该参数用于表示外联口报文调测的接口名称1。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| IFNAME2 | 接口2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEBUGTYPE”配置为“Interface”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的接口名称2。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| IFNAME3 | 接口3 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEBUGTYPE”配置为“Interface”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的接口名称3。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| IFNAME4 | 接口4 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEBUGTYPE”配置为“Interface”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的接口名称4。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |
| IFNAME5 | 接口5 | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEBUGTYPE”配置为“Interface”时为可选参数。<br>参数含义：该参数用于表示外联口报文调测的接口名称5。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FEIEXTPORTPKTDEBUG]] · 使能外联口报文调测功能（FEIEXTPORTPKTDEBUG）

## 使用实例

使能外联口报文调测功能：

```
OPR FEIEXTPORTPKTDEBUG: RULEID=1, STATUS=Enable, DIRECTION=All, TIMEOUT=60, FILEDELDAY=1, DEBUGTYPE=All;
RETCODE = 0  操作成功。
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/使能外联口报文调测功能（OPR-FEIEXTPORTPKTDEBUG）_49802038.md`
