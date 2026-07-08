---
id: UNC@20.15.2@MMLCommand@RMV HSSBPFAULTCODE
type: MMLCommand
name: RMV HSSBPFAULTCODE（删除HSS BYPASS故障状态码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HSSBPFAULTCODE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS HSS BYPASS故障状态码
status: active
---

# RMV HSSBPFAULTCODE（删除HSS BYPASS故障状态码）

## 功能

**适用网元：MME**

该命令用于删除HSS BYPASS故障状态码。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RANGE | 生效范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定特定故障码的生效范围。<br>数据来源：全网规划<br>取值范围：<br>- ALL（整系统）：整系统<br>- OFFICE（局向）：特定HSS局向<br>- KEYWORD（对端主机名关键字）：包含关键字的特定HSS局向<br>默认值：无<br>配置原则：无 |
| HOSTNAME | 对端主机名 | 可选必选说明：分支必选参数<br>参数含义：该参数用于指定进入故障状态的HSS主机名。<br>前提条件：该参数在“生效范围”配置为“OFFICE（局向）”时生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1~127<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置字符串“NULL”。<br>- 该参数不区分大小写。 |
| KEYWORD | 对端主机名关键字 | 可选必选说明：分支必选参数<br>参数含义：该参数用于指定进入故障状态的HSS主机名关键字。<br>前提条件：该参数在“生效范围”参数配置为“KEYWORD（对端主机名关键字）”时生效。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1~31<br>默认值：无<br>配置原则：<br>- 不能为非法字符，只允许输入字母，数字，“.”和“-”。例如:hss.epc.mnc123.mcc123.3gppnetwork.org<br>- 不允许配置字符串“NULL”。<br>- 该参数不区分大小写。 |
| FAULTCODE | 故障码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进入HSS BYPASS状态的原因值。<br>数据来源：全网规划<br>取值范围：0-4294967295<br>- “3002(DIAMETER_UNABLE_TO_DELIVER)”：对端不能把消息发送到目的地<br>- “3004(DIAMETER_TOO_BUSY)”：对端不能提供请求的服务<br>- “3005(DIAMETER_LOOP_DETECTED)”：系统向对端发消息时检测到有环路<br>- “1001、2002、3001、3003、3007～3010、4001～4003、5001～5017”：当配置此区间的错误码后，UNC也可触发重选路由功能，但同时可能会影响UNC下发给用户的Attach Reject等消息的拒绝原因值<br>- “10001”：HSS响应超时/未响应原因值<br>- “其他值”：当前不支持重选路由功能<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HSS BYPASS故障状态码（HSSBPFAULTCODE）](configobject/UNC/20.15.2/HSSBPFAULTCODE.md)

## 使用实例

删除HSS BYPASS故障状态码配置，生效范围为OFFICE（局向），对端主机名为hostname，故障码为3002。

```
RMV HSSBPFAULTCODE: RANGE=OFFICE, HOSTNAME="hostname", FAULTCODE=3002;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除HSS-BYPASS故障状态码(RMV-HSSBPFAULTCODE)_10494885.md`
