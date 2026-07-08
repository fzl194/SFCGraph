---
id: UDG@20.15.2@MMLCommand@MOD ARPPROBESTANDBYSRCIP
type: MMLCommand
name: MOD ARPPROBESTANDBYSRCIP（修改备用成员口ARP探测源地址）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: ARPPROBESTANDBYSRCIP
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP探测配置
status: active
---

# MOD ARPPROBESTANDBYSRCIP（修改备用成员口ARP探测源地址）

## 功能

该命令用于修改备用成员口ARP探测的源地址。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP探测会话的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：该参数必须先由ADD INTERFACE命令定义，才能在此处索引。并且只能为捆绑口或其子接口，子接口必须是vlan-type dot1q类型。 |
| SOURCEIPV4 | ARP探测源IPv4地址 | 可选必选说明：必选参数<br>参数含义：该参数用于指定备用成员口ARP探测的源IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |

## 操作的配置对象

- [备用成员口ARP探测源地址（ARPPROBESTANDBYSRCIP）](configobject/UDG/20.15.2/ARPPROBESTANDBYSRCIP.md)

## 使用实例

修改备用成员口ARP探测的源地址：

```
MOD ARPPROBESTANDBYSRCIP:IFNAME="Eth-Trunk1.1",SOURCEIPV4="10.10.10.10";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改备用成员口ARP探测源地址（MOD-ARPPROBESTANDBYSRCIP）_49961706.md`
