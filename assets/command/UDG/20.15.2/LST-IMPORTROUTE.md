---
id: UDG@20.15.2@MMLCommand@LST IMPORTROUTE
type: MMLCommand
name: LST IMPORTROUTE（查询指定协议中的入口路由配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IMPORTROUTE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 入口路由
status: active
---

# LST IMPORTROUTE（查询指定协议中的入口路由配置）

## 功能

该命令用于查询设备上BGP VPN实例下通过Import方式引入其他协议路由的配置信息。

## 注意事项

- 该命令执行后立即生效。
- 如果未指定引入路由协议类型，将查询指定BGP VPN实例下所有通过Import方式引入其他协议路由的配置信息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定BGP VPN实例下的地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4uni：IPv4地址族。<br>- ipv6uni：IPv6地址族。<br>默认值：无 |
| IMPORTPROTOCOL | 路由协议 | 可选必选说明：可选参数<br>参数含义：用户设定引入其他协议路由时的策略名称。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- direct：直连路由。<br>- ospf：开放式最短路径优先协议。<br>- static：静态路由。<br>- ospfv3：OSPFv3协议。<br>- wlr：WLR协议。<br>默认值：无 |
| IMPORTPROCESSID | 路由进程号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IMPORTPROTOCOL”配置为“ospf” 或 “ospfv3”时为必选参数。<br>参数含义：该参数用于指定所引入路由的协议进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IMPORTROUTE]] · 指定协议中的入口路由配置（IMPORTROUTE）

## 使用实例

查询名称为“vrf1”的BGP VPN实例下所引入路由的协议信息：

```
LST IMPORTROUTE:VRFNAME="vrf1",AFTYPE=ipv4uni;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
VPN实例名称    地址族类型       路由协议             路由进程号          引入路由策略        MED       使能MED
vrf1           IPv4uni          开放式最短路径优先   1                   NULL                0         不使能
vrf1           IPv4uni          静态路由             0                   NULL                0         不使能
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IMPORTROUTE.md`
