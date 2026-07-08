---
id: UNC@20.15.2@MMLCommand@RMV QOSIFTRUST
type: MMLCommand
name: RMV QOSIFTRUST（删除QoS接口信任）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: QOSIFTRUST
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 接口信任信息
status: active
---

# RMV QOSIFTRUST（删除QoS接口信任）

## 功能

该命令用来删除绑定在以太主接口上的DS域。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@QOSIFTRUST]] · QoS接口信任（QOSIFTRUST）

## 使用实例

删除配置在以太主接口Ethernet66/0/3上的DS域：

```
RMV QOSIFTRUST:IFNAME="Ethernet66/0/3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-QOSIFTRUST.md`
