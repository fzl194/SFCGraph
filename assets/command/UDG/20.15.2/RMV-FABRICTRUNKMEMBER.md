---
id: UDG@20.15.2@MMLCommand@RMV FABRICTRUNKMEMBER
type: MMLCommand
name: RMV FABRICTRUNKMEMBER（删除Fabric-Trunk成员接口）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: FABRICTRUNKMEMBER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP Fabric链路管理
- Fabric-Trunk成员接口管理
status: active
---

# RMV FABRICTRUNKMEMBER（删除Fabric-Trunk成员接口）

## 功能

该命令用于删除NP卡Fabric-Trunk成员接口。

## 注意事项

该命令仅适用于非NP卡基础上扩容NP卡的异构场景，在纯NP场景该命令不生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRACK | 框号 | 可选必选说明：必选参数。<br>参数含义：该参数标识Fabric-Trunk接口内成员口所属框的编号。<br>数据来源：本端规划。<br>取值范围：<br>- “Subrack_0”：框号0。<br>- “Subrack_1”：框号1。<br>- “Subrack_2”：框号2。<br>- “Subrack_3”：框号3。<br>配置原则：无。<br>默认值：无。 |
| SLOTID | 槽位号 | 可选必选说明：必选参数。<br>参数含义：该参数标识Fabric-Trunk接口内成员口所属插槽的编号。<br>数据来源：本端规划。<br>取值范围：<br>- “Slot_1”：槽位号1。<br>- “Slot_2”：槽位号2。<br>- “Slot_3”：槽位号3。<br>- “Slot_4”：槽位号4。<br>- “Slot_5”：槽位号5。<br>- “Slot_6”：槽位号6。<br>- “Slot_7”：槽位号7。<br>- “Slot_8”：槽位号8。<br>配置原则：无。<br>默认值：无。 |
| PORTID | 端口号 | 可选必选说明：必选参数。<br>参数含义：该参数标识Fabric-Trunk接口内成员口所对应的端口编号。<br>数据来源：本端规划。<br>取值范围：<br>- “P1”：端口号1。<br>- “P2”：端口号2。<br>- “P3”：端口号3。<br>- “P4”：端口号4。<br>配置原则：无。<br>默认值：无。 |

## 操作的配置对象

- [Fabric-Trunk成员接口（FABRICTRUNKMEMBER）](configobject/UDG/20.15.2/FABRICTRUNKMEMBER.md)

## 使用实例

删除一个Fabric-Trunk成员接口，该接口是1号框，8号槽位中的3号端口：

```
%%RMV FABRICTRUNKMEMBER: SUBRACK=Subrack_1, SLOTID=Slot_8, PORTID=P3;%%
RETCODE = 0  操作成功
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除Fabric-Trunk成员接口（RMV-FABRICTRUNKMEMBER）_19886585.md`
