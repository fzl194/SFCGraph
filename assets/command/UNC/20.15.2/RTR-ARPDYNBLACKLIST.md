---
id: UNC@20.15.2@MMLCommand@RTR ARPDYNBLACKLIST
type: MMLCommand
name: RTR ARPDYNBLACKLIST（清除ARP动态黑名单）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: ARPDYNBLACKLIST
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP防欺骗配置
status: active
---

# RTR ARPDYNBLACKLIST（清除ARP动态黑名单）

## 功能

该命令用于清除ARP动态黑名单。

当ARP动态黑名单已经不需要且未到老化时间，可使用该命令清除。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP动态黑名单的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| MACADDR | MAC地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP动态黑名单的MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～48。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP动态黑名单的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [ARP动态黑名单（ARPDYNBLACKLIST）](configobject/UNC/20.15.2/ARPDYNBLACKLIST.md)

## 使用实例

不指定参数时，清除VNFC上所有ARP动态黑名单：

```
RTR ARPDYNBLACKLIST:;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除ARP动态黑名单（RTR-ARPDYNBLACKLIST）_00840989.md`
