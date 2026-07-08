---
id: UDG@20.15.2@MMLCommand@RMV OSPFASBRSUMMARY
type: MMLCommand
name: RMV OSPFASBRSUMMARY（删除引入路由聚合配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFASBRSUMMARY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF引入路由聚合配置
status: active
---

# RMV OSPFASBRSUMMARY（删除引入路由聚合配置）

## 功能

该命令用于取消ASBR对OSPF引入的路由进行路由聚合。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无<br>配置原则：目前只支持默认拓扑0。 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| ADDRESSMASK | 地址掩码 | 可选必选说明：必选参数<br>参数含义：地址掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFASBRSUMMARY]] · 引入路由聚合配置（OSPFASBRSUMMARY）

## 使用实例

取消OSPF进程1下引入10.1.0.0的路由聚合：

```
RMV OSPFASBRSUMMARY:PROCID=1,TOPOID=0,IPADDRESS="10.1.0.0",ADDRESSMASK="255.255.0.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFASBRSUMMARY.md`
