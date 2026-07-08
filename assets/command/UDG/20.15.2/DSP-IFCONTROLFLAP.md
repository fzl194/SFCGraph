---
id: UDG@20.15.2@MMLCommand@DSP IFCONTROLFLAP
type: MMLCommand
name: DSP IFCONTROLFLAP（显示接口震荡抑制动态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: IFCONTROLFLAP
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口震荡抑制
status: active
---

# DSP IFCONTROLFLAP（显示接口震荡抑制动态信息）

## 功能

该命令用于显示接口震荡抑制动态信息。

若不指定IFNAME参数时，则查询所有接口的震荡抑制动态信息；若指定IFNAME参数时，则可以查询指定接口的震荡抑制动态信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定震荡抑制的接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IFCONTROLFLAP]] · 接口震荡抑制（IFCONTROLFLAP）

## 使用实例

显示接口震荡抑制动态信息：

```
DSP IFCONTROLFLAP:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
接口名            当前震荡次数    当前惩罚值    当前抑制状态
Ethernet64/0/3    0               0.000         未抑制
Ethernet64/0/4    1000            0.100         抑制
(结果个数 = 2)
---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-IFCONTROLFLAP.md`
