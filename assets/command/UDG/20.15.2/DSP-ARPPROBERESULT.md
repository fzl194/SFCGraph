---
id: UDG@20.15.2@MMLCommand@DSP ARPPROBERESULT
type: MMLCommand
name: DSP ARPPROBERESULT（查询ARP探测结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ARPPROBERESULT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP探测结果查询
status: active
---

# DSP ARPPROBERESULT（查询ARP探测结果）

## 功能

该命令用于显示ARP探测的结果。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP探测会话的接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EthTrunk：Eth-Trunk接口。<br>默认值：无 |
| IFNAME | 探测会话接口名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IFTYPE”配置为“EthTrunk”时为可选参数。<br>参数含义：该参数用于指定ARP探测会话的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| MEMBERIFNAME | 成员口名称 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IFTYPE”配置为“EthTrunk”时为可选参数。<br>参数含义：该参数用于显示成员口的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| SESSIONIP | ARP探测会话IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“IFTYPE”配置为“EthTrunk”时为可选参数。<br>参数含义：该参数用于显示ARP探测会话的目的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [ARP探测结果（ARPPROBERESULT）](configobject/UDG/20.15.2/ARPPROBERESULT.md)

## 使用实例

显示ARP探测的结果：

```
DSP ARPPROBERESULT:IFTYPE=EthTrunk,IFNAME="Eth-Trunk1.1";
```

```

RETCODE = 0  操作成功

结果如下
--------
   探测会话接口名称 = Eth-Trunk1.1
         成员口名称 = Ethernet64/0/3
ARP探测会话IPv4地址 = 10.10.10.10
        ARP探测结果 = 探测成功
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ARP探测结果（DSP-ARPPROBERESULT）_49801870.md`
