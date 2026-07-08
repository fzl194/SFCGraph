---
id: UDG@20.15.2@MMLCommand@RMV ETHSUBIF
type: MMLCommand
name: RMV ETHSUBIF（删除子接口配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ETHSUBIF
command_category: 配置类
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

# RMV ETHSUBIF（删除子接口配置）

## 功能

该命令用于删除子接口关联的VLAN。

当网络重新规划，需要重新规划指定子接口的用途，如果指定的子接口已经关联VLAN，此时可执行该命令删除关联的VLAN。

## 注意事项

- 该命令执行后立即生效。
- 删除指定子接口关联的VLAN后，设备将无法通过子接口与此VLAN中的其他设备通信。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 子接口名字 | 可选必选说明：必选参数<br>参数含义：该参数用于指定子接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：该参数必须先由ADD INTERFACE命令定义，才能在此处索引。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ETHSUBIF]] · 子接口配置（ETHSUBIF）

## 使用实例

删除子接口Ethernet64/0/3.1关联的VLAN：

```
RMV ETHSUBIF: IFNAME="Ethernet64/0/3.1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-ETHSUBIF.md`
