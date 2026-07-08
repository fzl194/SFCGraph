---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3IMPORTROUTE
type: MMLCommand
name: RMV OSPFV3IMPORTROUTE（删除OSPFv3引入路由配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3IMPORTROUTE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3引入路由配置
status: active
---

# RMV OSPFV3IMPORTROUTE（删除OSPFv3引入路由配置）

## 功能

该命令用来删除引入到OSPFv3域中的外部路由。

## 注意事项

- 该命令执行后立即生效。
- 只有配置了OSPFv3进程和引入外部路由后才能使用该命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| PROTOCOL | 协议号 | 可选必选说明：必选参数<br>参数含义：协议号。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- static：静态路由。<br>- bgp：BGP协议。<br>- ospfv3：OSPFv3协议。<br>- wlr：无线路由。<br>默认值：无 |
| PROTOCOLPROCID | 协议进程号 | 可选必选说明：条件可选参数<br>前提条件：该参数在“PROTOCOL”配置为“ospfv3”时为可选参数。<br>参数含义：协议进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3IMPORTROUTE]] · OSPFv3引入路由配置（OSPFV3IMPORTROUTE）

## 使用实例

将OSPFv3进程1下引入的OSPFv3进程2的路由删除：

```
RMV OSPFV3IMPORTROUTE: PROCID=1, TOPOID=0, PROTOCOL=ospfv3, PROTOCOLPROCID=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFV3IMPORTROUTE.md`
