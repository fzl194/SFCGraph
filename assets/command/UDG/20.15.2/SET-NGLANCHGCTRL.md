---
id: UDG@20.15.2@MMLCommand@SET NGLANCHGCTRL
type: MMLCommand
name: SET NGLANCHGCTRL（设置5G LAN计费控制相关参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: NGLANCHGCTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 5G LAN管理
- 5G LAN计费控制信息
status: active
---

# SET NGLANCHGCTRL（设置5G LAN计费控制相关参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置5G LAN计费控制相关参数。

## 注意事项

- 该命令执行后只对之后发生承载更新的用户或者新激活用户生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | OFFLOCCHGPLYSW |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFFLOCCHGPLYSW | 5G LAN本地离线计费策略开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制5GLAN用户本地离线计费策略功能是否使能。当开关开启时，如果N4接口下发的PDR未绑定离线业务级URR，则可以使用本地用户模板绑定的缺省URR组进行计费；开关关闭时，仅使用PDR下绑定的URR进行计费。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：当开启5G LAN本地离线计费策略功能时，需提前使用 SET URRGRPBINDING对本地用户模板绑定缺省URR组，若缺省URR组配置的上行发起URR名称和下行发起URR名称不相同，优先选择上行发起URR名称对应的URR进行计费。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NGLANCHGCTRL]] · 5G LAN计费控制相关参数（NGLANCHGCTRL）

## 使用实例

开启5G LAN本地离线计费策略功能：

```
SET NGLANCHGCTRL: OFFLOCCHGPLYSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-NGLANCHGCTRL.md`
