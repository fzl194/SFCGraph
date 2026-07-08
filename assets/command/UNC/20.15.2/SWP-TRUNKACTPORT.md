---
id: UNC@20.15.2@MMLCommand@SWP TRUNKACTPORT
type: MMLCommand
name: SWP TRUNKACTPORT（切换Trunk激活口）
nf: UNC
version: 20.15.2
verb: SWP
object_keyword: TRUNKACTPORT
command_category: 动作类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- Trunk成员接口配置
status: active
---

# SWP TRUNKACTPORT（切换Trunk激活口）

## 功能

该命令用于切换Trunk激活口。

该命令仅支持工作模式为主备的Trunk接口。

不指定MEMBERIFNAME参数时，在备份口中随机选择可用的接口作为激活口；指定MEMBERIFNAME参数时，可以切换至指定的成员口。

## 注意事项

- 该操作可能会导致短暂的业务流量中断。
- 该命令执行后可能影响业务，请谨慎使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRUNKIFNAME | Trunk接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Trunk接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| MEMBERIFNAME | 成员接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定成员接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [切换Trunk激活口（TRUNKACTPORT）](configobject/UNC/20.15.2/TRUNKACTPORT.md)

## 使用实例

指定成员口Ethernet64/0/4为Trunk激活口：

```
SWP TRUNKACTPORT: TRUNKIFNAME="Eth-Trunk1",MEMBERIFNAME="Ethernet64/0/4";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/切换Trunk激活口（SWP-TRUNKACTPORT）_00601477.md`
