---
id: UNC@20.15.2@MMLCommand@ADD DNAIUPFINFO
type: MMLCommand
name: ADD DNAIUPFINFO（增加指定DNAI的UPF节点信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DNAIUPFINFO
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- DNAI UPF信息管理
status: active
---

# ADD DNAIUPFINFO（增加指定DNAI的UPF节点信息）

## 功能

**适用NF：SMF、PGW-C**

该命令用于增加指定DNAI的UPF节点信息。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入16000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| UPFINSTANCEID | UPF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。该参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。<br>默认值：无<br>配置原则：无 |
| SHAREDUPFSW | UPF共享开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示该DNAI下UPF是否支持作为共享UPF使用。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：该DNAI下的能力继承整机的共享UPF能力<br>- “DISABLE（不使能）”：不支持共享UPF<br>- “ENABLE（使能）”：支持共享UPF<br>默认值：INHERIT<br>配置原则：<br>如果要设置UPF在DNAI下支持共享UPF能力并正常使用，还需要配置虚拟UPF以及配置虚拟UPF绑定该DNAI。相关配置：VIRTUALUPFID、VUPFIDBINDDNAI。 |

## 操作的配置对象

- [指定DNAI的UPF节点信息（DNAIUPFINFO）](configobject/UNC/20.15.2/DNAIUPFINFO.md)

## 使用实例

设置UPF在DNAI下支持作为共享UPF，DNAI名称为huawei.com，UPF实例标识为upf1。

```
ADD DNAIUPFINFO:DNAI="huawei.com",UPFINSTANCEID="upf1",SHAREDUPFSW=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加指定DNAI的UPF节点信息（ADD-DNAIUPFINFO）_69277824.md`
