---
id: UDG@20.15.2@MMLCommand@RMV OSPFDOMAINID
type: MMLCommand
name: RMV OSPFDOMAINID（删除OSPF域标识配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFDOMAINID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF域标识配置
status: active
---

# RMV OSPFDOMAINID（删除OSPF域标识配置）

## 功能

该命令用于恢复OSPF域标识符默认值。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| DOMAINID | 域标识 | 可选必选说明：必选参数<br>参数含义：域标识。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| DOMAINTYPEVALUE | 域标识符类型的值 | 可选必选说明：可选参数<br>参数含义：指定OSPF域标识符类型的值。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFF。<br>默认值：无 |
| DOMAINIDTYPE | 域标识符的类型 | 可选必选说明：可选参数<br>参数含义：指定OSPF域标识符的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Type0005：Type0005。<br>- Type0105：Type0105。<br>- Type0205：Type0205。<br>- Type8005：Type8005。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFDOMAINID]] · 创建OSPF域标识配置（OSPFDOMAINID）

## 使用实例

恢复OSPF进程1 VPN扩展中的默认VPN域标识符：

```
RMV OSPFDOMAINID:PROCID=1,DOMAINID="10.1.1.1",DOMAINTYPEVALUE="150",DOMAINIDTYPE=Type0005;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFDOMAINID.md`
