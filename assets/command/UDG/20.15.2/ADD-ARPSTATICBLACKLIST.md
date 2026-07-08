---
id: UDG@20.15.2@MMLCommand@ADD ARPSTATICBLACKLIST
type: MMLCommand
name: ADD ARPSTATICBLACKLIST（配置ARP静态黑名单）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ARPSTATICBLACKLIST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1000
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP防欺骗配置
status: active
---

# ADD ARPSTATICBLACKLIST（配置ARP静态黑名单）

## 功能

该命令用于配置ARP静态黑名单。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 执行该命令前，需要先执行SET ARPANTISPOOFING命令使能ARP防欺骗功能。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP静态黑名单的IP地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| MACADDR | MAC地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP静态黑名单的MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～48。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPSTATICBLACKLIST]] · ARP静态黑名单（ARPSTATICBLACKLIST）

## 使用实例

配置IP地址为10.1.1.2，MAC地址为00E0-FC12-3456的ARP静态黑名单：

```
ADD ARPSTATICBLACKLIST: IPADDR="10.1.1.2", MACADDR="00E0-FC12-3456";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/配置ARP静态黑名单（ADD-ARPSTATICBLACKLIST）_49961726.md`
