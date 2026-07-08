---
id: UNC@20.15.2@MMLCommand@SET TCPSACKSWITCH
type: MMLCommand
name: SET TCPSACKSWITCH（设置TCP SACK开关配置）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: TCPSACKSWITCH
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- 公共参数
- TCP SACK开关
status: active
---

# SET TCPSACKSWITCH（设置TCP SACK开关配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

SET TcpSackSwitch命令用来修改Gx，Gy接口TCP协议是否支持SACK选项。

## 注意事项

- 该命令需要重新建链后才能生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | GX | GY |
| --- | --- | --- |
| 初始值 | DISABLE | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GX | Gx接口TCP协议支持SACK选项开关 | 可选必选说明：可选参数<br>参数含义：Gx接口TCP是否支持SACK选项。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：Gx接口支持TCP SACK选项。<br>- DISABLE：Gx接口不支持TCP SACK选项。 |
| GY | Gy接口TCP协议支持SACK选项开关 | 可选必选说明：可选参数<br>参数含义：Gy接口TCP是否支持SACK选项。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：否。<br>- ENABLE：是。<br>默认值：无<br>配置原则：<br>- ENABLE：Gy接口支持TCP SACK选项。<br>- DISABLE：Gy接口不支持TCP SACK选项。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/TCPSACKSWITCH]] · TCP SACK开关配置（TCPSACKSWITCH）

## 使用实例

GX接口使能TCP的SACK选项，GY接口使能TCP的SACK选项：

```
SET TCPSACKSWITCH:GX=ENABLE,GY=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-TCPSACKSWITCH.md`
