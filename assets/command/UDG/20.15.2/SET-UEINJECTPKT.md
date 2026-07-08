---
id: UDG@20.15.2@MMLCommand@SET UEINJECTPKT
type: MMLCommand
name: SET UEINJECTPKT（设置UE灌包参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UEINJECTPKT
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 10
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- UE侧连通性检测
- UE灌包参数
status: active
---

# SET UEINJECTPKT（设置UE灌包参数）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置UE灌包参数（SET UEINJECTPKT）_82837091.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，请确保SRCPORT参数不要配置保留端口1～1023，否则可能导致通用业务无法正常进行。

该命令用于配置UE下行灌包功能的UE灌包参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10。
- 该命令的Length参数如果不填写，会被默认置为1400。
- 执行该命令配置USERIDINFO参数时，需先执行SET UEINJECTLIST命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERID | 用户标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IMSI：用于指定用户标识为IMSI。<br>- MSISDN：用于指定用户标识为MSISDN。<br>- IMEI：用于指定用户标识为IMEI。<br>默认值：无<br>配置原则：无 |
| IPTYPE | IP 类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示灌包UE的IP类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：表示地址类型为IPv4。<br>- IPv6：表示地址类型为IPv6。<br>默认值：无<br>配置原则：无 |
| LENGTH | 报文净荷长度 | 可选必选说明：可选参数<br>参数含义：该参数用于指定灌包报文UDP上层报文长度，即不包含链路层、IP层、传输层部分。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1280～1600，单位是字节。<br>默认值：无<br>配置原则：无 |
| CONTEXT | 报文内容 | 可选必选说明：可选参数<br>参数含义：该参数用户指定报文内容。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～7。每个字符必须为0~F的十六进制数字。<br>默认值：无<br>配置原则：无 |
| RATE | 灌包速率 | 可选必选说明：必选参数<br>参数含义：该参数用于指定灌包速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～3000000，单位是千比特每秒。<br>默认值：无<br>配置原则：无 |
| SRCPORT | 源端口 | 可选必选说明：必选参数<br>参数含义：该参数用于指定灌包源端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。建议不要配保留端口1～1023。<br>默认值：无<br>配置原则：无 |
| DSTPORT | 目的端口 | 可选必选说明：必选参数<br>参数含义：该参数用于指定灌包目的端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。建议不要配保留端口1～1023。<br>默认值：无<br>配置原则：无 |
| USERIDINFO | 用户ID信息 | 可选必选说明：必选参数<br>参数含义：该参数用于指定用户ID信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～16。1、当用户ID类型为IMSI时，长度范围是1～15，每个字符必须为0~9的数字。 2、当用户ID类型为MSISDN时，长度范围是1～15，每个字符必须为0~9的数字。 3、当用户ID类型为IMEI时，长度范围是1～16，每个字符必须为0~9的数字。<br>默认值：无<br>配置原则：无 |
| CONTROL | 灌包控制 | 可选必选说明：必选参数<br>参数含义：该参数用于指定灌包控制类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NUMBER：控制发包报文数。<br>- TIME：控制发包时长。<br>默认值：无<br>配置原则：无 |
| NUMBER | 灌包数量 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONTROL”配置为“NUMBER”时为必选参数。<br>参数含义：该参数用于指定一次灌包的包数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1125000，单位是包数。<br>默认值：无<br>配置原则：无 |
| TIME | 灌包时长 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONTROL”配置为“TIME”时为必选参数。<br>参数含义：该参数用于指定一次灌包的时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～180，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UEINJECTPKT]] · UE灌包参数（UEINJECTPKT）

## 使用实例

配置指定imsi为12345678901234的UE下行灌包功能的UE灌包参数：

```
SET UEINJECTPKT: USERID=IMSI, IPTYPE=IPv4, LENGTH=1500, CONTEXT="34df", RATE=2000, SRCPORT=2001, DSTPORT=2001, USERIDINFO="12345678901234", CONTROL=TIME, TIME=50;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置UE灌包参数（SET-UEINJECTPKT）_82837091.md`
