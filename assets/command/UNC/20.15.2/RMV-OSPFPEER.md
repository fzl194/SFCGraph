---
id: UNC@20.15.2@MMLCommand@RMV OSPFPEER
type: MMLCommand
name: RMV OSPFPEER（删除OSPF的NBMA网络邻居路由器配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OSPFPEER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF的NBMA网络邻居路由器配置
status: active
---

# RMV OSPFPEER（删除OSPF的NBMA网络邻居路由器配置）

## 功能

该命令用于取消在NBMA网络上指定相邻路由器的IP地址。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| IPADDRESS | 邻居路由器IP地址 | 可选必选说明：必选参数<br>参数含义：邻居路由器IP地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFPEER]] · OSPF的NBMA网络邻居路由器配置（OSPFPEER）

## 使用实例

取消在NBMA网络上指定相邻路由器的10.1.1.1的IP地址：

```
RMV OSPFPEER:PROCID=1,IPADDRESS="10.1.1.1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除OSPF的NBMA网络邻居路由器配置（RMV-OSPFPEER）_50280762.md`
