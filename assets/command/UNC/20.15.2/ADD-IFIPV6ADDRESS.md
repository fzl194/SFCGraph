---
id: UNC@20.15.2@MMLCommand@ADD IFIPV6ADDRESS
type: MMLCommand
name: ADD IFIPV6ADDRESS（增加接口IPv6地址）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: IFIPV6ADDRESS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- IPv6地址
status: active
---

# ADD IFIPV6ADDRESS（增加接口IPv6地址）

## 功能

该命令用于手工配置接口的IPv6地址。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 该命令可以在VNRS_VNFC的Ethernet接口，Ethernet子接口，Eth-Trunk接口，Eth-Trunk子接口以及Loopback口，Tunnel口上配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPV6ADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：该参数用于配置接口IPv6地址。如果想要修改接口的IPv6地址，需要使用RMV IFIPV6ADDRESS将该地址删除后，使用ADD IFIPV6ADDRESS添加新地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备是否在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| PREFIXLEN | IPv6地址前缀 | 可选必选说明：必选参数<br>参数含义：该参数用于配置接口IPv6地址前缀。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无<br>配置原则：本参数参与自动化配置，请在下发本MML命令前使用DSP OPSASSISTSTATE命令查询自动化配置维护助手autoscaling_autoconfig.py，确保当前设备是否在自动化配置过程中。如果当前正在自动化配置过程中，不要做本业务的增删改操作，否则最终生效的配置将不可预期。 |
| ADDRTYPE | IPv6地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置接口IPv6地址类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- global：全球单播地址。<br>- linkLocal：链路本地地址。<br>- anycast：任播地址。<br>默认值：global |
| IDGENTYPE | IPv6地址计算类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置接口IPv6地址计算类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- none：None。<br>- cga：CGA。<br>- eui64：Eui64。<br>默认值：none |

## 操作的配置对象

- [[configobject/UNC/20.15.2/IFIPV6ADDRESS]] · 接口IPv6地址（IFIPV6ADDRESS）

## 使用实例

配置IPv6地址为2001:db8::11/64：

```
ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/3",IPV6ADDRESS="2001:db8::11",PREFIXLEN=64;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加接口IPv6地址（ADD-IFIPV6ADDRESS）_49961222.md`
