---
id: UNC@20.15.2@MMLCommand@RTR ARPBYIF
type: MMLCommand
name: RTR ARPBYIF（根据接口清除ARP动态表项）
nf: UNC
version: 20.15.2
verb: RTR
object_keyword: ARPBYIF
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP表项统计查询
status: active
---

# RTR ARPBYIF（根据接口清除ARP动态表项）

## 功能

![](根据接口清除ARP动态表项（RTR ARPBYIF）_00840969.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于基于接口清除ARP动态表项。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要重置ARP表项的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| IPADDRVALUE | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要重置的具体表项。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ARPBYIF]] · 根据接口清除ARP动态表项（ARPBYIF）

## 使用实例

重置Ethernet64/0/5的动态表项：

```
RTR ARPBYIF:IFNAME="Ethernet64/0/5";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RTR-ARPBYIF.md`
