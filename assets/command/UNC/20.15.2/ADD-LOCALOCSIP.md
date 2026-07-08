---
id: UNC@20.15.2@MMLCommand@ADD LOCALOCSIP
type: MMLCommand
name: ADD LOCALOCSIP（增加本省OCS的IP号段）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LOCALOCSIP
command_category: 配置类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 本省OCS的IP号段
status: active
---

# ADD LOCALOCSIP（增加本省OCS的IP号段）

## 功能

**适用NF：NCG**

该命令用于增加本省OCS的IP号段。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSID | OCS标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定OCS标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~40。只允许输入字母，数字和中划线。<br>默认值：无<br>配置原则：无 |
| IPADDRESSTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4地址）<br>- IPV6（IPv6地址）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | IPv4地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：该参数在"IPADDRESSTYPE"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALOCSIP]] · 本省OCS的IP号段（LOCALOCSIP）

## 使用实例

增加OCS标识为ocsid001，IP类型为IPV4，IP地址为192.168.100.1的本省OCS的IP号段：

```
ADD LOCALOCSIP:OCSID="ocsid001",IPADDRESSTYPE=IPV4,IPV4ADDRESS="192.168.100.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-LOCALOCSIP.md`
