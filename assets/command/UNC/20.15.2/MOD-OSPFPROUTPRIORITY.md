---
id: UNC@20.15.2@MMLCommand@MOD OSPFPROUTPRIORITY
type: MMLCommand
name: MOD OSPFPROUTPRIORITY（修改OSPF路由的收敛优先级配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: OSPFPROUTPRIORITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF路由的收敛优先级配置
status: active
---

# MOD OSPFPROUTPRIORITY（修改OSPF路由的收敛优先级配置）

## 功能

该命令用于修改OSPF路由的收敛优先级。

## 注意事项

- 该命令执行后立即生效。
- 只有在配置了OSPF进程后才能使用此命令。
- 缺省情况下，公网OSPF主机路由的收敛优先级为medium，其他OSPF路由的收敛优先级为low，直连路由的收敛优先级为high，静态路由的收敛优先级为medium，其他协议（如BGP等）路由的收敛优先级为low。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| PRIORITY | 收敛优先级 | 可选必选说明：必选参数<br>参数含义：收敛优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- critical：配置OSPF路由的收敛优先级为关键。<br>- high：配置OSPF路由的收敛优先级为高。<br>- medium：配置OSPF路由的收敛优先级为中。<br>默认值：无<br>配置原则：只能修改相同收敛优先级的前缀名。 |
| IPPREFIXNAME | 前缀名 | 可选必选说明：必选参数<br>参数含义：前缀名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：<br>- 不支持空格，区分大小写。<br>- IP-prefix必须已经存在。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPFPROUTPRIORITY]] · OSPF路由的收敛优先级配置（OSPFPROUTPRIORITY）

## 使用实例

修改OSPF进程1下路由优先级为critical的IP前缀名为ip-prefix1：

```
MOD OSPFPROUTPRIORITY:PROCID=1,TOPOID=0,PRIORITY=critical,IPPREFIXNAME="ip-prefix1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-OSPFPROUTPRIORITY.md`
