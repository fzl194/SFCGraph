---
id: UDG@20.15.2@MMLCommand@SET DDNCTRL
type: MMLCommand
name: SET DDNCTRL（设置DDN报文策略）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: DDNCTRL
command_category: 配置类
applicable_nf:
- SGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 2
category_path:
- 用户面服务管理
- 会话管理
- GTP隧道管理
- 报文DDN 触发策略
status: active
---

# SET DDNCTRL（设置DDN报文策略）

## 功能

**适用NF：SGW-U、UPF**

该命令用来控制报文DDN触发策略。可以通过设置TCP信令报文或流的动作为阻塞的报文不触发DDN消息，来降低呼叫负载。其中TCP信令报文包含FIN，FIN ACK，RST，RST ACK报文。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为2。
- SGW-U不支持设置流的动作为阻塞的报文。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PKTTYPE | SWITCH | ACTION |
| --- | --- | --- | --- |
| 初始值 | TCPSIG | DISABLE | BUFFER |
| 初始值 | FLOWDISCARD | DISABLE | BUFFER |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PKTTYPE | 报文类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定设置DDN触发策略的报文类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TCPSIG：FIN，FIN ACK，RST，RST ACK的TCP信令报文。<br>- FLOWDISCARD：流的动作为阻塞的报文。<br>默认值：无<br>配置原则：无 |
| SWITCH | 使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制DDN触发策略是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| ACTION | 报文策略 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于指定报文的处理动作。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- BUFFER：缓存报文。<br>- DROP：丢弃报文。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DDN控制策略（DDNCTRL）](configobject/UDG/20.15.2/DDNCTRL.md)

## 使用实例

配置TCP信令报文不触发DDN，且丢弃：

```
SET DDNCTRL: PKTTYPE=TCPSIG, SWITCH=ENABLE, ACTION=DROP;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置DDN报文策略（SET-DDNCTRL）_82837183.md`
