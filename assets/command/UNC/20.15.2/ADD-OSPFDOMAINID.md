---
id: UNC@20.15.2@MMLCommand@ADD OSPFDOMAINID
type: MMLCommand
name: ADD OSPFDOMAINID（创建OSPF域标识配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OSPFDOMAINID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF域标识配置
status: active
---

# ADD OSPFDOMAINID（创建OSPF域标识配置）

## 功能

该命令用于配置OSPF域标识符。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8000。
- 只有在执行ADD OSPF配置了OSPF进程后才能使用此命令。
- 每一个OSPF域都有一个或多个域标识符，其中有一个是主标识符，其它为从标识符。
- 如果OSPF实例没有明确域标识符，则认为它的标识符为NULL。
- 域标识符的值为0时不能配置secondary参数。
- 每个OSPF进程上domain-id secondary的最大条目数是1000条。
- 此命令不允许在公网中配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| DOMAINID | 域标识 | 可选必选说明：必选参数<br>参数含义：域标识。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| DOMAINTYPEVALUE | 域标识符类型的值 | 可选必选说明：可选参数<br>参数含义：指定OSPF域标识符类型的值。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFF。<br>默认值：0 |
| DOMAINIDTYPE | 域标识符的类型 | 可选必选说明：可选参数<br>参数含义：指定OSPF域标识符的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Type0005：Type0005。<br>- Type0105：Type0105。<br>- Type0205：Type0205。<br>- Type8005：Type8005。<br>默认值：Type0005 |
| DOMAINIDSECFLG | 次级域标识符 | 可选必选说明：可选参数<br>参数含义：指定次级域标识符。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：FALSE |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFDOMAINID]] · 创建OSPF域标识配置（OSPFDOMAINID）

## 使用实例

配置OSPF进程1 VPN扩展中的VPN域标识符：

```
ADD OSPFDOMAINID:PROCID=1,DOMAINIDSECFLG=FALSE,DOMAINID="10.1.1.1",DOMAINTYPEVALUE="100",DOMAINIDTYPE=Type0005;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/创建OSPF域标识配置（ADD-OSPFDOMAINID）_00440729.md`
