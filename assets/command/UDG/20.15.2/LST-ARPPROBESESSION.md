---
id: UDG@20.15.2@MMLCommand@LST ARPPROBESESSION
type: MMLCommand
name: LST ARPPROBESESSION（查询ARP探测会话）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ARPPROBESESSION
command_category: 查询类
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

# LST ARPPROBESESSION（查询ARP探测会话）

## 功能

该命令用于查询ARP探测会话信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定ARP探测会话的接口类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- EthTrunk：Eth-Trunk接口。<br>默认值：无 |
| SESSIONIP | ARP探测会话IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP探测会话的目的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定ARP探测会话的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数必须先由ADD INTERFACE命令定义，才能在此处索引。并且只能为捆绑口或其子接口，子接口必须是vlan-type dot1q类型。<br>- 接口下需要有和ARP探测会话IPv4地址同网段的配置地址，接口地址不支持DHCP动态分配的地址。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPPROBESESSION]] · ARP探测会话（ARPPROBESESSION）

## 使用实例

查询ARP探测会话信息：

```
LST ARPPROBESESSION:IFTYPE=EthTrunk,IFNAME="Eth-Trunk1.1",SESSIONIP="10.10.10.10";
```

```

RETCODE = 0  操作成功

结果如下
 -------------------------
ARP探测会话IPv4地址  =  10.10.10.10
           接口名称  =  Eth-Trunk1.1
      探测间隔（s）  =  3
       探测失败门限  =  4
   探测失败恢复门限  =  6
 是否使能激活口切换  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ARPPROBESESSION.md`
