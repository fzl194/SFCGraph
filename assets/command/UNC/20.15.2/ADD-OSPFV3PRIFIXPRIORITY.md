---
id: UNC@20.15.2@MMLCommand@ADD OSPFV3PRIFIXPRIORITY
type: MMLCommand
name: ADD OSPFV3PRIFIXPRIORITY（创建OSPFv3路由收敛优先级配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OSPFV3PRIFIXPRIORITY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 8000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3路由收敛优先级配置
status: active
---

# ADD OSPFV3PRIFIXPRIORITY（创建OSPFv3路由收敛优先级配置）

## 功能

该命令用于配置OSPFv3路由的收敛优先级。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8000。
- 只有执行ADD OSPFV3配置了OSPFV3进程后才能使用此命令。
- 缺省情况下，公网OSPFv3主机路由的收敛优先级为medium，直连路由的收敛优先级为high，静态路由的收敛优先级为medium，其他协议（如BGP等）路由的收敛优先级为low。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。请使用LST OSPFV3命令查看可用的OSPFv3进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：0<br>配置原则：目前只支持默认拓扑0。 |
| PRIORITY | 路由优先级 | 可选必选说明：必选参数<br>参数含义：路由优先级。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- critical：配置OSPFv3路由的收敛优先级为关键。<br>- high：配置OSPFv3路由的收敛优先级为高。<br>- medium：配置OSPFv3路由的收敛优先级为中。<br>默认值：无 |
| IPPREFIXNAME | IPv6前缀列表名称 | 可选必选说明：必选参数<br>参数含义：IPv6前缀列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～169。<br>默认值：无<br>配置原则：不支持空格，区分大小写。 |

## 操作的配置对象

- [OSPFv3路由收敛优先级配置（OSPFV3PRIFIXPRIORITY）](configobject/UNC/20.15.2/OSPFV3PRIFIXPRIORITY.md)

## 使用实例

配置路由收敛优先级为critical的ipv6-prefix名为prefix-name：

```
ADD OSPFV3PRIFIXPRIORITY:PROCID=1,TOPOID=0,PRIORITY=critical,IPPREFIXNAME="prefix-name";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/创建OSPFv3路由收敛优先级配置（ADD-OSPFV3PRIFIXPRIORITY）_50280562.md`
