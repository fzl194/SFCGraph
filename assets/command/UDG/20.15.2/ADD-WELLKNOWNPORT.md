---
id: UDG@20.15.2@MMLCommand@ADD WELLKNOWNPORT
type: MMLCommand
name: ADD WELLKNOWNPORT（增加知名端口）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: WELLKNOWNPORT
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 200
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 知名端口
status: active
---

# ADD WELLKNOWNPORT（增加知名端口）

## 功能

**适用NF：PGW-U、UPF**

ADD WELLKNOWNPORT此命令用来添加知名端口。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为200。
- 增加知名端口，支持端口段、支持多个端口一种协议，如果配置的端口有重叠，则根据优先级匹配。 如果通过匹配端口号仍无法识别协议类型，则使用特征字识别。
- 对于协议类型，如FTP，HTTP等类型，可以配置协议类型的知名端口。
- 配置ProtocolName时，SubProtocol表记录必须存在。
- 执行该命令前，需要添加协议识别特征库。
- 该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDENPROTNAME | 知名端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定指知名端口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的子协议，可以通过工程命令smctrldsp protocol-list查询。 |
| PORTOP | 端口范围操作码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定端口范围操作码。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EQUAL：等于指定值。<br>- LT：小于等于指定值。<br>- GT：大于等于指定值。<br>- RANGE：在指定范围内，包括边界值。<br>默认值：无<br>配置原则：<br>- 当运营商需要配置端口号等于指定值时，该参数需配置为EQUAL。<br>- 当运营商需要配置端口号小于等于指定值时，该参数需配置为LT。<br>- 当运营商需要配置端口号大于等于指定值时，该参数需配置为GT。<br>- 当运营商需要配置端口号在指定范围（包括边界值）时，该参数需配置为RANGE。 |
| STARTPORT | 起始端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PORTOP”配置为“EQUAL”、“GT” 或 “RANGE”时为必选参数。<br>参数含义：该参数用于指定起始端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：当PORTOP配置为EQUAL、GT或RANGE时，该参数为必选参数。 |
| ENDPORT | 结束端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PORTOP”配置为“LT” 或 “RANGE”时为必选参数。<br>参数含义：该参数用于指定结束端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无<br>配置原则：当PORTOP配置为LT或RANGE时,该参数为必选参数。 |
| PRIORITY | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。建议配置时按照5、10、15等配置，便于以后再插入新的优先级。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/WELLKNOWNPORT]] · 知名端口（WELLKNOWNPORT）

## 关联任务

- [[UDG@20.15.2@Task@0-00039]]

## 使用实例

添加WellKnownPort知名端口，“IDENPROTNAME”为“10086”,“PROTOCOLNAME”为“http”，“PORTOP”为“RANGE”,“PRIORITY”为“100”，“STARTPORT”为“1000”，“ENDPORT”为“3000”：

```
ADD WELLKNOWNPORT:IDENPROTNAME="10086",PROTOCOLNAME="http",PORTOP=RANGE,STARTPORT=1000,ENDPORT=3000,PRIORITY=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-WELLKNOWNPORT.md`
