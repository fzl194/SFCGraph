---
id: UNC@20.15.2@MMLCommand@SET OVERLOADRC
type: MMLCommand
name: SET OVERLOADRC（设置判断对端过载的返回码）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: OVERLOADRC
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
max_records: 2
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- 过载返回码
status: active
---

# SET OVERLOADRC（设置判断对端过载的返回码）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

![](设置判断对端过载的返回码（SET OVERLOADRC）_09896711.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，该命令会影响Gx，Gy接口智能流控算法，如果配置错误，会导致流控失效，影响用户接入。配置此值需要慎重。

此命令用来配置Gx，Gy接口智能流控时，判断对端过载的返回码列表。

如果对端网元PCRF或者OCS没有按照协议标准实现，过载时的错误返回码不是3004(Diameter too busy)，此时需要使用此命令配置对端过载时的返回码。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- 每次执行该命令，新配置的参数将覆盖掉旧参数。
- 每次执行该命令，如果多个输入参数中间有未输入的参数，将对输入的参数往前补齐。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | INTERFACE | RESULTCODE1 | DIRECTPEER1 | RESULTCODE2 | DIRECTPEER2 | RESULTCODE3 | DIRECTPEER3 | RESULTCODE4 | DIRECTPEER4 | RESULTCODE5 | DIRECTPEER5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | GX | 3004 | NO | 0 | NO | 0 | NO | 0 | NO | 0 | NO |
| 初始值 | GY | 3004 | NO | 0 | NO | 0 | NO | 0 | NO | 0 | NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定配置过载返回码的接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- GX：配置Gx接口。<br>- GY：配置Gy接口。<br>默认值：无<br>配置原则：无 |
| RESULTCODE1 | 返回码1 | 可选必选说明：必选参数<br>参数含义：该参数用于配置第一个过载返回码。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0，1000～9999。不能配置为返回码2001，2002或3006。<br>默认值：无<br>配置原则：该参数配置为0表示清除该接口的过载返回码配置，即不做控制，此时其余参数将被忽略。 |
| DIRECTPEER1 | 直连Peer标记1 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTERFACE”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定第一个过载返回码是否只对直连PCRF生效。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- NO：对所有对端生效。<br>- YES：只对直连PCRF生效。<br>默认值：无<br>配置原则：在ResultCode1配置时生效。 |
| RESULTCODE2 | 返回码2 | 可选必选说明：可选参数<br>参数含义：该参数用于配置第二个过载返回码。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1000～9999。不能配置为返回码2001，2002或3006。<br>默认值：无<br>配置原则：无 |
| DIRECTPEER2 | 直连Peer标记2 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTERFACE”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定第二个过载返回码是否只对直连PCRF生效。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- NO：对所有对端生效。<br>- YES：只对直连PCRF生效。<br>默认值：无<br>配置原则：在ResultCode2配置时生效。 |
| RESULTCODE3 | 返回码3 | 可选必选说明：可选参数<br>参数含义：该参数用于配置第三个过载返回码。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1000～9999。不能配置为返回码2001，2002或3006。<br>默认值：无<br>配置原则：无 |
| DIRECTPEER3 | 直连Peer标记3 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTERFACE”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定第三个过载返回码是否只对直连PCRF生效。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- NO：对所有对端生效。<br>- YES：只对直连PCRF生效。<br>默认值：无<br>配置原则：在ResultCode3配置时生效。 |
| RESULTCODE4 | 返回码4 | 可选必选说明：可选参数<br>参数含义：该参数用于配置第四个过载返回码。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1000～9999。不能配置为返回码2001，2002或3006。<br>默认值：无<br>配置原则：无 |
| DIRECTPEER4 | 直连Peer标记4 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTERFACE”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定第四个过载返回码是否只对直连PCRF生效。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- NO：对所有对端生效。<br>- YES：只对直连PCRF生效。<br>默认值：无<br>配置原则：在ResultCode4配置时生效。 |
| RESULTCODE5 | 返回码5 | 可选必选说明：可选参数<br>参数含义：该参数用于配置第五个过载返回码。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为1000～9999。不能配置为返回码2001，2002或3006。<br>默认值：无<br>配置原则：无 |
| DIRECTPEER5 | 直连Peer标记5 | 可选必选说明：条件可选参数<br>前提条件：该参数在“INTERFACE”配置为“GX”时为可选参数。<br>参数含义：该参数用于指定第五个过载返回码是否只对直连PCRF生效。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- NO：对所有对端生效。<br>- YES：只对直连PCRF生效。<br>默认值：无<br>配置原则：在ResultCode5配置时生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OVERLOADRC]] · 判断对端过载的返回码（OVERLOADRC）

## 使用实例

根据对端PCRF的配置，返回结果码3004和3005表示PCRF过载，则在开启智能流控功能时，配置3004和3005为过载返回码列表：

```
SET OVERLOADRC:INTERFACE=GX,RESULTCODE1=3004,RESULTCODE2=3005;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-OVERLOADRC.md`
