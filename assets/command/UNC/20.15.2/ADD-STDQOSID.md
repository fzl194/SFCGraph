---
id: UNC@20.15.2@MMLCommand@ADD STDQOSID
type: MMLCommand
name: ADD STDQOSID（增加标准QoS ID配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: STDQOSID
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 扩展QCI功能
- 标准QoS ID配置
status: active
---

# ADD STDQOSID（增加标准QoS ID配置）

## 功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于增加标准QoS ID配置。根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。关于最初的标准QCI/5QI的资源类型参见协议3GPP TS 23.203和3GPP TS 23.501。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。QOSIDSV-QOSIDEV的取值范围要与EXTENDQCIMAP中配置的EXTENDQCI互斥，同时，同一QOSIDTYPE下，QOSIDSV-QOSIDEV的取值范围不能重叠。

- 最多可输入492条记录。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QOSIDTYPE | QOSIDSV | QOSIDEV | RESOURCETYPE |
| --- | --- | --- | --- |
| FIVEQI | 65 | 67 | GBR |
| FIVEQI | 69 | 70 | NONGBR |
| FIVEQI | 71 | 76 | GBR |
| FIVEQI | 79 | 80 | NONGBR |
| FIVEQI | 82 | 86 | GBR |
| QCI | 65 | 67 | GBR |
| QCI | 69 | 70 | NONGBR |
| QCI | 71 | 76 | GBR |
| QCI | 79 | 80 | NONGBR |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSIDTYPE | QoS ID类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS ID类型。<br>数据来源：本端规划<br>取值范围：<br>- “QCI（QCI）”：QCI<br>- “FIVEQI（5QI）”：5QI<br>默认值：无<br>配置原则：无 |
| QOSIDSV | QoS ID起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS ID起始值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~255。<br>默认值：无<br>配置原则：<br>该参数的值必须小于等于QoS ID的结束值。 |
| QOSIDEV | QoS ID结束值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS ID结束值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~255。<br>默认值：无<br>配置原则：<br>该参数的值必须大于等于QoS ID的起始值。 |
| RESOURCETYPE | 标准QoS ID的资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定标准QoS ID的资源类型。<br>数据来源：全网规划<br>取值范围：<br>- NONGBR（指定QoS ID的资源类型为Non-GBR）<br>- GBR（指定QoS ID的资源类型为GBR）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/STDQOSID]] · 标准QoS ID配置（STDQOSID）

## 使用实例

增加“QCI=90”为“标准QCI”，资源类型为"GBR"：

```
ADD STDQOSID:QOSIDTYPE=QCI,QOSIDSV=90,RESOURCETYPE=GBR;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加标准QoS-ID配置（ADD-STDQOSID）_06399909.md`
