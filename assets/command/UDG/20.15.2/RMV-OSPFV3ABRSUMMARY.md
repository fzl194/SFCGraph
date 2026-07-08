---
id: UDG@20.15.2@MMLCommand@RMV OSPFV3ABRSUMMARY
type: MMLCommand
name: RMV OSPFV3ABRSUMMARY（删除OSPFv3区域内路由聚合配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFV3ABRSUMMARY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3区域内路由聚合配置
status: active
---

# RMV OSPFV3ABRSUMMARY（删除OSPFv3区域内路由聚合配置）

## 功能

该命令用于删除OSPFv3区域内路由聚合。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：必选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPFv3进程必须已经存在。 |
| AREAID | OSPFv3区域ID | 可选必选说明：必选参数<br>参数含义：OSPFv3区域ID。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| TOPOID | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为0。<br>默认值：无 |
| IPADDRESS | IPv6地址 | 可选必选说明：必选参数<br>参数含义：IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无 |
| IPV6MASKLEN | IPv6前缀长度 | 可选必选说明：必选参数<br>参数含义：IPv6前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～128。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFV3ABRSUMMARY]] · OSPFv3区域内路由聚合配置（OSPFV3ABRSUMMARY）

## 使用实例

取消OSPFv3进程1区域1下2001:db8::1的区域内路由聚合配置：

```
RMV OSPFV3ABRSUMMARY:PROCID=1,AREAID="0.0.0.1",TOPOID=0,IPADDRESS="2001:db8::1",IPV6MASKLEN=64;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFV3ABRSUMMARY.md`
