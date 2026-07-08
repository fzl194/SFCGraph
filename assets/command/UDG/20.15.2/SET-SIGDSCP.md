---
id: UDG@20.15.2@MMLCommand@SET SIGDSCP
type: MMLCommand
name: SET SIGDSCP（设置信令报文DSCP值）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SIGDSCP
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 5
category_path:
- 用户面服务管理
- 业务控制策略
- 信令QOS控制
- 信令DSCP
status: active
---

# SET SIGDSCP（设置信令报文DSCP值）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于设置信令报文的DSCP值。在IP承载网络中，通常使用DSCP标记来进行业务优先级的区分和QoS保证。为区分不同信令在IP承载网络中不同的转发优先级，系统支持设置具体信令流报文的DSCP值，使不同的信令按照DSCP值进行优先级转发。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为5。
- TM信令和GTP信令在未配置时不显示且导出命令时没有对应记录。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | PROTOCOL | DSCPV |
| --- | --- | --- |
| 初始值 | PFCP | 46 |
| 初始值 | L2TP_SIGNALING | 46 |
| 初始值 | PPP_SIGNALING | 46 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOL | 信令协议 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信令协议的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PFCP：N4接口的PFCP协议信令。<br>- L2TP_SIGNALING：Gi接口的L2TP信令。<br>- PPP_SIGNALING：L2TP承载的PPP信令。<br>- TM：Tm3接口的TM协议信令。<br>- GTP_SIGNALING：GTP信令。<br>默认值：无<br>配置原则：无 |
| DSCPV | DSCP值 | 可选必选说明：必选参数<br>参数含义：该参数用于设置指定信令协议的DSCP值，DSCP值越大，优先级越高。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SIGDSCP]] · 信令报文DSCP值（SIGDSCP）

## 使用实例

如果需要将PFCP信令流报文的DSCP值设置为25，可以执行该命令：

```
SET SIGDSCP:PROTOCOL=PFCP,DSCPV=25;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SIGDSCP.md`
