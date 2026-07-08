---
id: UDG@20.15.2@MMLCommand@RMV ARPSTATICBLACKLIST
type: MMLCommand
name: RMV ARPSTATICBLACKLIST（删除ARP静态黑名单）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ARPSTATICBLACKLIST
command_category: 配置类
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

# RMV ARPSTATICBLACKLIST（删除ARP静态黑名单）

## 功能

该命令用于删除ARP静态黑名单。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP静态黑名单的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| MACADDR | MAC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP静态黑名单的MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～48。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ARPSTATICBLACKLIST]] · ARP静态黑名单（ARPSTATICBLACKLIST）

## 使用实例

针对已经配置的IP地址为10.1.1.2，MAC地址为00E0-FC12-3456的ARP静态黑名单，现需要删除该黑名单：

```
RMV ARPSTATICBLACKLIST: IPADDR="10.1.1.2", MACADDR="00E0-FC12-3456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ARPSTATICBLACKLIST.md`
