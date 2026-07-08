---
id: UDG@20.15.2@MMLCommand@RMV OSPFABRSUMMARY
type: MMLCommand
name: RMV OSPFABRSUMMARY（删除区域内路由聚合配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: OSPFABRSUMMARY
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF区域内路由聚合配置
status: active
---

# RMV OSPFABRSUMMARY（删除区域内路由聚合配置）

## 功能

该命令用于取消区域边界路由器ABR对区域内路由进行路由聚合。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域ID | 可选必选说明：必选参数<br>参数含义：区域ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| TOPONAME | 拓扑标识 | 可选必选说明：必选参数<br>参数含义：拓扑标识。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- base：基础类型。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：必选参数<br>参数含义：IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| ADDRESSMASK | IP地址的掩码 | 可选必选说明：必选参数<br>参数含义：IP地址的掩码。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFABRSUMMARY]] · 区域内路由聚合配置（OSPFABRSUMMARY）

## 使用实例

取消OSPF进程1下10.2.0.0的区域内路由聚合配置：

```
RMV OSPFABRSUMMARY:PROCID=1,AREAID="0.0.0.1",TOPONAME=base,IPADDRESS="10.2.0.0",ADDRESSMASK="255.255.0.0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-OSPFABRSUMMARY.md`
