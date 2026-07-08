---
id: UDG@20.15.2@MMLCommand@RMV ARPSTATICTABLE
type: MMLCommand
name: RMV ARPSTATICTABLE（删除静态ARP表项）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ARPSTATICTABLE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# RMV ARPSTATICTABLE（删除静态ARP表项）

## 功能

该命令用于删除ARP静态表项。当网络重新规划，之前创建的ARP静态表项失效。此时可执行该命令删除已创建的ARP静态表项。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定（目的）IPv4地址的ARP表项。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP表项的VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，取值范围是1～31。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPSTATICTABLE]] · 静态ARP表项（ARPSTATICTABLE）

## 使用实例

针对已经配置的VPN实例名称为_public_的静态ARP表项，现需要删除该表项：

```
RMV ARPSTATICTABLE:VRFNAME="_public_";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ARPSTATICTABLE.md`
