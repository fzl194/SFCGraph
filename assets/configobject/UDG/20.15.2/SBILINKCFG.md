---
id: UDG@20.15.2@ConfigObject@SBILINKCFG
type: ConfigObject
name: SBILINKCFG（SBI接口链路属性配置）
nf: UDG
version: 20.15.2
object_name: SBILINKCFG
object_kind: entity
status: active
---

# SBILINKCFG（SBI接口链路属性配置）

## 说明

该命令用于增加服务化接口的静态链路及其属性，静态链路可以配置网元级和IP级链路。该命令也可以用于增加动态链路的属性。

> **说明**
> - 该命令执行后立即生效。
>
> - 配置Callback、Location及其他URL消息的链路属性时，参数“NFINSTID”必须配置成对端的IP地址或FQDN（详细参见该参数的描述），参数“NETINFO”配置成“NULL”，参数“NFTYPE”建议配置成“INVALID”（如果需要配置成其他值，请联系华为工程师）。
> - 本端设备NF类型为AMF/SMF，对端设备NF类型为UDM/AUSF/PCF/NRF时，同时未打开链路自动控制功能时，未添加本命令配置时系统默认按整系统控制链路数量。其他场景下，未打开链路自动控制功能且未添加本命令配置时系统默认按单进程控制链路数量；如果打开链路自动控制功能，且未添加本命令配置时系统按链路自动控制规则控制链路数量；如果配置了本命令时，按本命令配置规则控制链路数量。
> - 整系统控制默认链路数4条，单进程控制默认链路数1条，upf单进程控制默认链路数8条。
>
> - 最多可输入512条记录。

## 操作本对象的命令

- [ADD SBILINKCFG](command/UDG/20.15.2/ADD-SBILINKCFG.md)
- [LST SBILINKCFG](command/UDG/20.15.2/LST-SBILINKCFG.md)
- [RMV SBILINKCFG](command/UDG/20.15.2/RMV-SBILINKCFG.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除SBI接口链路属性配置（RMV-SBILINKCFG）_29213291.md`
- 原始手册：`evidence/UDG/20.15.2/增加SBI接口链路属性配置（ADD-SBILINKCFG）_83813628.md`
- 原始手册：`evidence/UDG/20.15.2/查询SBI接口链路属性配置（LST-SBILINKCFG）_29291771.md`
