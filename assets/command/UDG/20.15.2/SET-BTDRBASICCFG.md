---
id: UDG@20.15.2@MMLCommand@SET BTDRBASICCFG
type: MMLCommand
name: SET BTDRBASICCFG（设置BTDR单据上报参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: BTDRBASICCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 智能板管理
- 实时流北向配置管理
- 基本信息配置
status: active
---

# SET BTDRBASICCFG（设置BTDR单据上报参数）

## 功能

**适用NF：PGW-U、UPF**

此命令用于配置BTDR单据上报基础信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWITCH | PERIOD | UDPPKTMAXLEN | SENDBUFTIME | PSEUDONSWITCH | PSEUDONMODE | PSEUDONALGORI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 60 | 1350 | 1 | ENABLE | PRE_DEFINED | HMACSHA256 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 上报开关 | 可选必选说明：必选参数<br>参数含义：该参数用于配置BTDR单据上报开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能BTDR单据上报功能。<br>- ENABLE：使能BTDR单据上报功能。<br>默认值：无<br>配置原则：无 |
| PERIOD | 上报周期（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置BTDR单据上报周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30~3600，单位为秒。<br>默认值：无<br>配置原则：无 |
| UDPPKTMAXLEN | UDP报文净荷最大长度（字节） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置BTDR单据上报UDP报文净荷最大长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为512~1350，单位为字节。<br>默认值：无<br>配置原则：无 |
| SENDBUFTIME | 发送报文缓存时间（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置BTDR单据上报发送报文缓存时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~60，单位为秒。<br>默认值：无<br>配置原则：无 |
| PSEUDONSWITCH | 假名化开关 | 可选必选说明：条件必选参数<br>前提条件：该参数在“SWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于配置BTDR假名化开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能假名化功能。<br>- ENABLE：使能假名化功能。<br>默认值：无<br>配置原则：无 |
| PSEUDONMODE | 加密模式 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PSEUDONSWITCH”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于配置个人敏感数据假名化方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PRE_DEFINED：表示假名化方式使用默认方式，即HMACSHA256假名化方式，通过U2020/MAE统一下发密钥。<br>- USER_DEFINED：表示加密方式使用本命令设置的加密算法和加密密钥。<br>默认值：无<br>配置原则：无 |
| PSEUDONALGORI | 假名化算法 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PSEUDONMODE”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用于配置假名化加密算法。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- HMACSHA256：该参数表示假名化类型为HMACSHA256。<br>默认值：无<br>配置原则：无 |
| KEY | 密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PSEUDONMODE”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用于设置加密算法的密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255位16进制字符串，不支持空格。 如果是HMACSHA256算法，密钥长度为64~255。<br>默认值：无<br>配置原则：如果是HMAC56算法，密钥长度为64~255；。 |
| CONFIRMKEY | 确认密码 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PSEUDONMODE”配置为“USER_DEFINED”时为必选参数。<br>参数含义：该参数用于确认加密算法的密钥。<br>数据来源：本端规划<br>取值范围：密码类型，输入长度范围为1～255位16进制字符串，不支持空格。 如果是HMACSHA256算法，密钥长度为64~255。<br>默认值：无<br>配置原则：如果是HMAC56算法，密钥长度为64~255；。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@BTDRBASICCFG]] · BTDR单据上报参数（BTDRBASICCFG）

## 使用实例

设置BTDR上报基础信息：

```
SET BTDRBASICCFG: SWITCH=ENABLE, PERIOD=50, UDPPKTMAXLEN=520, SENDBUFTIME=30, PSEUDONSWITCH=ENABLE, PSEUDONMODE=PRE_DEFINED;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-BTDRBASICCFG.md`
