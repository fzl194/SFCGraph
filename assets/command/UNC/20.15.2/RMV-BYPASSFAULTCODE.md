---
id: UNC@20.15.2@MMLCommand@RMV BYPASSFAULTCODE
type: MMLCommand
name: RMV BYPASSFAULTCODE（删除BYPASS故障状态码）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: BYPASSFAULTCODE
command_category: 配置类
applicable_nf:
- AMF
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- Bypass故障状态码管理
status: active
---

# RMV BYPASSFAULTCODE（删除BYPASS故障状态码）

## 功能

**适用NF：AMF、SMF**

该命令用于删除BYPASS故障状态码。若全部删除后，主备对端网元返回500以上的状态码，用户或会话均进入Bypass状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端网元类型。<br>数据来源：全网规划<br>取值范围：<br>- “UDM（UDM）”：UDM<br>- “AUSF（AUSF）”：AUSF<br>默认值：无<br>配置原则：无 |
| NFINSTANCEID | 网元实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定网元实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。<br>默认值：无<br>配置原则：<br>该参数只能由字母（A-Z或者a-z）、数字（0-9）、中划线（-）、下划线（_）组成或者配置为通配符（*）。该参数不区分大小写。配置为“*”时，表示针对所有的网元实例生效，如果用户所在的网元实例标识在配置表中无法匹配到对应的记录，则使用“*”对应的记录。 |
| CUSFAULTCODE | 自定义故障码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定自定义的对端网元故障状态码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。该参数格式定义如下：1、状态码1\|状态码2\|...\|状态码s。状态码必须为300以上（含300），且同一个网元实例定义的状态码不能重复。例如"501\|504\|602"表示当对端网元返回状态码为501、504或602时，该网元为故障状态。2、配置为“*”，表示记录对于所有的故障码生效。如果未配置“错误信息”参数，表示对应的网元处于故障状态，无需再基于故障码识别网元状态。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [BYPASS故障状态码（BYPASSFAULTCODE）](configobject/UNC/20.15.2/BYPASSFAULTCODE.md)

## 使用实例

若删除网元类型为UDM、网元实例标识为instanceid01、状态码为504的BYPASS故障状态码配置，执行如下命令：

```
RMV BYPASSFAULTCODE: PEERNFTYPE=UDM, NFINSTANCEID="instanceid01", CUSFAULTCODE="504";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除BYPASS故障状态码（RMV-BYPASSFAULTCODE）_59000293.md`
