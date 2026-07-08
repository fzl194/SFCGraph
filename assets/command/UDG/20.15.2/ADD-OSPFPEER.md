---
id: UDG@20.15.2@MMLCommand@ADD OSPFPEER
type: MMLCommand
name: ADD OSPFPEER（创建OSPF的NBMA网络邻居路由器配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: OSPFPEER
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
- OSPF的NBMA网络邻居路由器配置
status: active
---

# ADD OSPFPEER（创建OSPF的NBMA网络邻居路由器配置）

## 功能

该命令用于在NBMA网络上指定相邻路由器的IP地址，并配置DR选举权。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为8000。
- 只有执行ADD OSPF配置了OSPF进程后才能使用该命令。
- 通过此命令设置对端设备的DR选举的优先级，必须与本端设备的DR的优先级一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：必选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。 |
| IPADDRESS | 邻居路由器IP地址 | 可选必选说明：必选参数<br>参数含义：邻居路由器IP地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |
| DRPRIORITY | 邻居路由器优先级 | 可选必选说明：可选参数<br>参数含义：邻居路由器优先级。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～255。<br>默认值：1 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFPEER]] · OSPF的NBMA网络邻居路由器配置（OSPFPEER）

## 使用实例

在NBMA网络中指定相邻邻居设备的IP地址为10.1.1.1：

```
ADD OSPFPEER:PROCID=1,IPADDRESS="10.1.1.1",DRPRIORITY=10;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-OSPFPEER.md`
