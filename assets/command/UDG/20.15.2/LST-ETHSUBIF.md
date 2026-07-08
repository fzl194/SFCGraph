---
id: UDG@20.15.2@MMLCommand@LST ETHSUBIF
type: MMLCommand
name: LST ETHSUBIF（查询子接口配置信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ETHSUBIF
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VLAN管理
- VLAN子接口
status: active
---

# LST ETHSUBIF（查询子接口配置信息）

## 功能

该命令用于查询子接口上已配置的VLAN信息。

为了实现VLAN间通信，可在接入用户终端的接口上通过创建子接口并关联VLAN实现二层网络接入三层网络，从而实现不同网段、不同VLAN间的通信。

当设备上存在多个子接口关联了不同VLAN，可使用该命令查询子接口已配置的VLAN信息。

## 注意事项

- 该命令执行后立即生效。
- 为了保证查询到有效的信息，执行该命令前必须已经成功创建子接口，并通过命令增加VLAN（ADD ETHSUBIF）将子接口关联了VLAN。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 子接口名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定子接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：该参数必须先由ADD INTERFACE命令定义，才能在此处索引。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ETHSUBIF]] · 子接口配置（ETHSUBIF）

## 使用实例

查询子接口Ethernet64/0/3.1上配置的VLAN信息：

```
LST ETHSUBIF: IFNAME="Ethernet64/0/3.1";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
      子接口名字  =  Ethernet64/0/3.1
子接口流封装类型  =  VLAN类型
         VLAN ID  =  100
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ETHSUBIF.md`
