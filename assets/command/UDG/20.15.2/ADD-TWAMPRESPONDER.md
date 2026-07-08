---
id: UDG@20.15.2@MMLCommand@ADD TWAMPRESPONDER
type: MMLCommand
name: ADD TWAMPRESPONDER（增加TWAMP响应端）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: TWAMPRESPONDER
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPAPM功能管理
- TWAMP
- TWAMP响应端配置
status: active
---

# ADD TWAMPRESPONDER（增加TWAMP响应端）

## 功能

该命令用于增加TWAMP响应端。

> **说明**
> - 该命令执行后立即生效。
>
> - 最多可输入32条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESPONDERID | 响应端索引 | 可选必选说明：必选参数<br>参数含义：该参数用于配置响应端索引。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |
| AFTYPE | 地址族类型 | 可选必选说明：必选参数<br>参数含义：该参数用于用户指定地址族类型。<br>数据来源：全网规划<br>取值范围：<br>- IPV4（IPV4）<br>默认值：无<br>配置原则：无 |
| TWAMPARCH | TWAMP架构 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TWAMP架构。<br>数据来源：全网规划<br>取值范围：<br>- FULL（FULL）<br>默认值：无<br>配置原则：无 |
| LOCALIPV4 | 本端IPV4地址 | 可选必选说明：该参数在"AFTYPE"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指示本端IPV4地址。<br>数据来源：全网规划<br>取值范围：IPv4地址类型。0.0.0.0～255.255.255.255。<br>默认值：无<br>配置原则：<br>采用点分十进制"X.X.X.X"格式。<br>IP地址必须是A、B或者C类地址，不能为环回地址（127.x.y.z）、组播地址（240.x.y.z）或（255.0.0.0）。<br>LOCALIPV4必须在<br>[**ADD TWAMPLOGICINF**](../本端逻辑接口配置/增加本地逻辑接口（ADD TWAMPLOGICINF）_27262282.md)<br>已经配置，可以用<br>[**LST TWAMPLOGICINF**](../本端逻辑接口配置/查询本地逻辑接口（LST TWAMPLOGICINF）_73142135.md)<br>查询。<br>LOCALIPV4不能已在<br>[**ADD TWAMPCLIENT**](../TWAMP客户端配置/增加TWAMP客户端（ADD TWAMPCLIENT）_27102472.md)<br>中配置，可以用<br>[**LST TWAMPCLIENT**](../TWAMP客户端配置/查询TWAMP客户端（LST TWAMPCLIENT）_27262286.md)<br>查询。 |
| SERVWAIT | 协商等待时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定协商等待时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~1800，单位是秒。<br>默认值：900<br>配置原则：无 |
| REFWAIT | 测试等待时间 | 可选必选说明：可选参数<br>参数含义：该参数用于指定测试等待时间。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~1800，单位是秒。<br>默认值：900<br>配置原则：无 |

## 操作的配置对象

- [TWAMP响应端（TWAMPRESPONDER）](configobject/UDG/20.15.2/TWAMPRESPONDER.md)

## 关联任务

- [0-00226](task/UDG/20.15.2/0-00226.md)

## 使用实例

增加响应端索引为1的实例：

```
ADD TWAMPRESPONDER: RESPONDERID=1, AFTYPE=IPV4, TWAMPARCH=FULL, LOCALIPV4="10.0.0.0", SERVWAIT=900, REFWAIT=900;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加TWAMP响应端（ADD-TWAMPRESPONDER）_73142131.md`
