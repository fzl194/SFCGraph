---
id: UDG@20.15.2@MMLCommand@MOD OSPFNEXTHOP
type: MMLCommand
name: MOD OSPFNEXTHOP（修改OSPF等价路由优先级配置）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: OSPFNEXTHOP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF等价路由优先级配置
status: active
---

# MOD OSPFNEXTHOP（修改OSPF等价路由优先级配置）

## 功能

该命令用于修改等价路由的优先级。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| NBRIPADDRESS | 下一跳IP地址 | 可选必选说明：必选参数<br>参数含义：下一跳IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| WEIGHT | 下一跳权重 | 可选必选说明：必选参数<br>参数含义：下一跳权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～254。<br>默认值：无<br>配置原则：该值越小，路由优先级越高。 |

## 操作的配置对象

- [OSPF等价路由优先级配置（OSPFNEXTHOP）](configobject/UDG/20.15.2/OSPFNEXTHOP.md)

## 使用实例

修改OSPF进程1中等价路由的权重值为100：

```
MOD OSPFNEXTHOP:PROCID=1,TOPOID=0,NBRIPADDRESS="10.1.1.1",WEIGHT=100;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改OSPF等价路由优先级配置（MOD-OSPFNEXTHOP）_00601297.md`
