---
id: UDG@20.15.2@MMLCommand@SET HBUSRCTRL
type: MMLCommand
name: SET HBUSRCTRL（设置高带宽用户功能控制参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: HBUSRCTRL
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 业务匹配策略
- 体验分级
- 体验分级全局参数
- 高带宽用户功能控制参数
status: active
---

# SET HBUSRCTRL（设置高带宽用户功能控制参数）

## 功能

**适用NF：PGW-U、UPF**

该命令用于设置高带宽用户功能相关控制参数。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | FASTFWDSW | LOADBALANCESW | LOCALCFGAGETM | SUBSCFGAGETM | AUTOLEARNAGETM |
| --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | DISABLE | 60 | 300 | 7200 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FASTFWDSW | 高带宽用户快转加速开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置高带宽用户快转加速功能是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能高带宽用户加速功能。<br>- ENABLE：使能高带宽用户快转加速功能。<br>默认值：无<br>配置原则：无 |
| LOADBALANCESW | 高带宽用户资源均衡开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置高带宽用户资源均衡加速功能是否使能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能高带宽用户资源均衡功能。<br>- ENABLE：使能高带宽用户资源均衡加速功能。<br>默认值：无<br>配置原则：该参数仅在FASTFWDSW参数配置为ENABLE时生效。 |
| GLBPROTGROUP | 全局协议组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置高带宽用户支持的协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD PROTOCOLGROUP命令配置生成。<br>- 该命令配置为NULL时表示所有协议均不支持高带宽用户快转加速功能。<br>- 该参数只能配置仅包含Speedtest业务相关协议的协议组。 |
| LOCALCFGAGETM | 本地配置高带宽用户老化时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置本地配置的高带宽用户记录老化时间。<br>数据来源：本端规划<br>取值范围：整数类型 ，取值范围是0~3600，单位是秒。<br>默认值：无<br>配置原则：该参数配置为0时代表不老化。 |
| SUBSCFGAGETM | 订阅接口下发高带宽用户老化时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置订阅接口下发高带宽用户老化时间。<br>数据来源：本端规划<br>取值范围：整数类型 ，取值范围是0~3600，单位是秒。<br>默认值：无<br>配置原则：该参数配置为0时代表不老化。 |
| AUTOLEARNAGETM | 自学习高带宽用户老化时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于设置自学习高带宽用户老化时间。<br>数据来源：本端规划<br>取值范围：整数类型 ，取值范围是0~999999999，单位是秒。<br>默认值：无<br>配置原则：该参数配置为0时代表不老化。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/HBUSRCTRL]] · 高带宽用户功能控制参数（HBUSRCTRL）

## 使用实例

设置高带宽用户快转加速功能使能：

```
SET HBUSRCTRL: FASTFWDSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-HBUSRCTRL.md`
