---
id: UNC@20.15.2@MMLCommand@ADD TRUNKMEMBER
type: MMLCommand
name: ADD TRUNKMEMBER（增加Trunk成员接口）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TRUNKMEMBER
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 65535
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- Trunk成员接口配置
status: active
---

# ADD TRUNKMEMBER（增加Trunk成员接口）

## 功能

Trunk是一种捆绑技术。将多个物理接口捆绑成一个逻辑接口，这个逻辑接口就称为Trunk接口。捆绑在一起的每个物理接口称为成员接口。Trunk技术可以实现增加带宽、提高可靠性和负载分担的功能。当用户设备使用的是以太网接口，需要实现这些功能时，可以通过该命令创建Eth-Trunk接口，并通过该命令将以太网接口加入创建的Eth-Trunk接口中。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 在SRIOV bonding组网时，非硬件加速场景下，需保证只有MAC地址一样的VNIC加到同一个TRUNK里，硬件加速场景下，加到同一个TRUNK里的VNIC可以有不一样的MAC地址。具体接口MAC地址可通过LST INTERFACE命令查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKIFNAME | Trunk接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置Trunk接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无 |
| MEMBERIFNAME | 成员接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要配置成员接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TRUNKMEMBER]] · Trunk成员接口（TRUNKMEMBER）

## 使用实例

添加Eth-Trunk1的成员接口Ethernet64/0/3：

```
ADD TRUNKMEMBER: TRUNKIFNAME="Eth-Trunk1", MEMBERIFNAME="Ethernet64/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TRUNKMEMBER.md`
