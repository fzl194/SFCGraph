---
id: UDG@20.15.2@MMLCommand@MOD TWAMPLOGICINF
type: MMLCommand
name: MOD TWAMPLOGICINF（修改本地逻辑接口）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: TWAMPLOGICINF
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- 本端逻辑接口配置
status: active
---

# MOD TWAMPLOGICINF（修改本地逻辑接口）

## 功能

该命令用于修改本地逻辑接口。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 逻辑接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于配置逻辑接口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| AFTYPE | 地址族类型 | 可选必选说明：可选参数<br>参数含义：该参数用于配置地址族类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | 逻辑接口地址 | 可选必选说明：该参数在"AFTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于配置逻辑接口IPv4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>采用点分十进制"X.X.X.X"格式。<br>IP地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。<br>不支持不同VPN下配置相同IP地址。 |
| IPV4MASK | 逻辑接口掩码 | 可选必选说明：该参数在"AFTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于配置逻辑接口掩码。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>采用点分十进制"X.X.X.X"格式。<br>逻辑接口IP地址的掩码为32位。 |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于配置VPN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>VRFNAME必须在<br>[**ADD TWAMPVPNINST**](../VPN实例/增加VPN实例名称（ADD TWAMPVPNINST）_27102474.md)<br>已经配置，可以用<br>[**LST TWAMPVPNINST**](../VPN实例/查询VPN实例名称（LST TWAMPVPNINST）_27262288.md)<br>查询。 |
| SHAREDTYPE | 共享IP地址 | 可选必选说明：可选参数<br>参数含义：该参数用于是否共地址。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TWAMPLOGICINF]] · 本地逻辑接口（TWAMPLOGICINF）

## 使用实例

修改逻辑接口名称为n3if1/1/0的实例：

```
MOD TWAMPLOGICINF: NAME="n3if1/1/0", AFTYPE=IPV4, IPV4ADDRESS="10.0.0.0", IPV4MASK="255.255.255.255", VRFNAME="ck ", SHAREDTYPE=FALSE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-TWAMPLOGICINF.md`
