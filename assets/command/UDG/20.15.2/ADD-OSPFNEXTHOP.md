---
id: UDG@20.15.2@MMLCommand@ADD OSPFNEXTHOP
type: MMLCommand
name: ADD OSPFNEXTHOP（创建OSPF等价路由优先级配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: OSPFNEXTHOP
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
- OSPF等价路由优先级配置
status: active
---

# ADD OSPFNEXTHOP（创建OSPF等价路由优先级配置）

## 功能

该命令用于设置等价路由的优先级。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| TOPOID | 拓扑标识 | 可选必选说明：可选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：0 |
| NBRIPADDRESS | 下一跳IP地址 | 可选必选说明：必选参数<br>参数含义：下一跳IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| WEIGHT | 下一跳权重 | 可选必选说明：必选参数<br>参数含义：下一跳权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～254。<br>默认值：无<br>配置原则：该值越小，路由优先级越高。 |

## 操作的配置对象

- [OSPF等价路由优先级配置（OSPFNEXTHOP）](configobject/UDG/20.15.2/OSPFNEXTHOP.md)

## 使用实例

设置OSPF进程1中等价路由的权重值为10：

```
ADD OSPFNEXTHOP:PROCID=1,TOPOID=0,NBRIPADDRESS="10.1.1.1",WEIGHT=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/创建OSPF等价路由优先级配置（ADD-OSPFNEXTHOP）_50121470.md`
