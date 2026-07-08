---
id: UDG@20.15.2@MMLCommand@MOD PROTFAGETIME
type: MMLCommand
name: MOD PROTFAGETIME（修改协议五元组老化时间）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: PROTFAGETIME
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- 基于协议的五元组节点老化时间
status: active
---

# MOD PROTFAGETIME（修改协议五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

该命令用于修改配置的不同的协议组、协议相关的五元组老化时间。

## 注意事项

- 该命令执行后立即生效。
- 如果五元组老化时间配置过大，会造成整机五元组使用数量太多的情况。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：必选参数<br>参数含义：该参数用于显示配置的协议组、协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于设置协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的默认协议组，可以通过工程命令smctrldsp protocol-list查询。 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于设置协议名称。数据源为系统支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令smctrldsp protocol-list查询。 |
| AGETIME | 老化时间（秒） | 可选必选说明：必选参数<br>参数含义：该参数用于设置五元组节点的老化时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为20～7200，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTFAGETIME]] · 协议五元组老化时间（PROTFAGETIME）

## 使用实例

假如运营商需要修改p2p协议组的五元组老化时间为40秒，配置命令如下：

```
MOD PROTFAGETIME:PROTOCOLLEVEL=PROTOCOLGROUP,PROTGROUPNAME="p2p",AGETIME=40;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改协议五元组老化时间（MOD-PROTFAGETIME）_82837296.md`
