---
id: UDG@20.15.2@MMLCommand@ADD UDGNRMINTF
type: MMLCommand
name: ADD UDGNRMINTF（增加逻辑口）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UDGNRMINTF
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 200
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口配置
- 备份逻辑接口
status: active
---

# ADD UDGNRMINTF（增加逻辑口）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于添加逻辑口记录。

## 注意事项

- 该命令最大记录数为200。
- 执行此命令时，要保证当前记录不存在相同neType和Interface Type的数据，否则请先删除已存在的数据。
- 执行此命令添加Interface Type为MGT的数据时，不需要添加ip地址。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTNAME | 保留逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置保留的逻辑接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| NETYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：网元的类型。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SGWU<br>- PGWU<br>- UPF<br>- ProxySGWU<br>- ProxyUPF<br>默认值：无<br>配置原则：无 |
| EXINTTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPFN4<br>- UPFN3<br>- UPFN19<br>- UPFN9<br>- SGWUSx<br>- SGWUS5U<br>- SGWUS8U<br>- SGWUS11U<br>- SGWUS1U<br>- PGWUSx<br>- PGWUS5U<br>- PGWUS8U<br>- PROXYSGWUSx<br>- PROXYSGWUS5U<br>- PROXYSGWUS8U<br>- PROXYUPFN4<br>- PROXYUPFN9<br>- Mgt<br>默认值：无<br>配置原则：无 |
| IPV4ADDR1 | 逻辑接口的IPv4地址1 | 可选必选说明：可选参数<br>参数含义：逻辑接口的ipv4地址1。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR2 | 逻辑接口的IPv4地址2 | 可选必选说明：可选参数<br>参数含义：预留逻辑接口的ipv4地址2。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR3 | 逻辑接口的IPv4地址3 | 可选必选说明：可选参数<br>参数含义：预留逻辑接口的ipv4地址3。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR4 | 逻辑接口的IPv4地址4 | 可选必选说明：可选参数<br>参数含义：预留逻辑接口的ipv4地址4。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV4ADDR5 | 逻辑接口的IPv4地址5 | 可选必选说明：可选参数<br>参数含义：预留逻辑接口的ipv4地址5。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR1 | 逻辑接口的IPv6地址1 | 可选必选说明：可选参数<br>参数含义：该参数用于指示逻辑接口配置主IPV6地址1。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR2 | 逻辑接口的IPv6地址2 | 可选必选说明：可选参数<br>参数含义：该参数用于指示逻辑接口配置主IPV6地址2。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR3 | 逻辑接口的IPv6地址3 | 可选必选说明：可选参数<br>参数含义：该参数用于指示逻辑接口配置主IPV6地址3。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR4 | 逻辑接口的IPv6地址4 | 可选必选说明：可选参数<br>参数含义：该参数用于指示逻辑接口配置主IPV6地址4。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |
| IPV6ADDR5 | 逻辑接口的IPv6地址5 | 可选必选说明：可选参数<br>参数含义：该参数用于指示逻辑接口配置主IPV6地址5。<br>数据来源：全网规划<br>取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [逻辑口（UDGNRMINTF）](configobject/UDG/20.15.2/UDGNRMINTF.md)

## 使用实例

假设需要添加名称为pgwusxif，netye为PGWU，Interface Type为Sx的逻辑口记录，配置如下：

```
ADD UDGNRMINTF: INTNAME="pgwusxif", NETYPE=PGWU, EXINTTYPE=PGWUSx, IPV4ADDR1="127.127.127.127";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加逻辑口（ADD-UDGNRMINTF）_96709875.md`
