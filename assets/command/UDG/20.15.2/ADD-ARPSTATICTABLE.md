---
id: UDG@20.15.2@MMLCommand@ADD ARPSTATICTABLE
type: MMLCommand
name: ADD ARPSTATICTABLE（配置静态ARP表项）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: ARPSTATICTABLE
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 16384
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP系统配置
status: active
---

# ADD ARPSTATICTABLE（配置静态ARP表项）

## 功能

该命令用于配置ARP静态表项，出于安全或管理方面的考虑，用户有时需要指定IP地址和MAC地址的映射关系。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为16384。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPADDR | IP地址 | 可选必选说明：必选参数<br>参数含义：该参数用于显示指定（目的）IPv4地址的ARP表项。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| VLANID | VLAN ID值 | 可选必选说明：可选参数<br>参数含义：接口所属的VLAN ID值。如果不输入该参数，则静态ARP表项中不携带VLAN ID信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4094。<br>默认值：无 |
| MACADDR | MAC地址 | 可选必选说明：必选参数<br>参数含义：MAC地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～48。<br>默认值：无 |
| VRFNAME | VPN实例名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP表项的VPN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，取值范围是1～31。<br>默认值：无<br>配置原则：该参数必须先由ADD L3VPNINST命令定义，才能在此处索引。 |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于显示指定要重置ARP表项的接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：<br>- 该参数必须先由ADD INTERFACE命令定义，才能在此处索引。<br>- 接口下需要有和IPv4地址同网段的配置地址，接口地址不支持DHCP动态分配的地址。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPSTATICTABLE]] · 静态ARP表项（ARPSTATICTABLE）

## 使用实例

配置接口Ethernet64/0/5的静态ARP表项，IP地址为10.1.1.2，MAC地址为00E0-FC12-3456，VPN实例名称为_public_：

```
ADD ARPSTATICTABLE:IPADDR="10.1.1.2",MACADDR="00E0-FC12-3456",VRFNAME="_public_",IFNAME="Ethernet64/0/5";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-ARPSTATICTABLE.md`
