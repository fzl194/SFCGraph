---
id: UDG@20.15.2@MMLCommand@RMV PROTFAGETIME
type: MMLCommand
name: RMV PROTFAGETIME（删除协议五元组老化时间）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PROTFAGETIME
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务五元组管理
- 基于协议的五元组节点老化时间
status: active
---

# RMV PROTFAGETIME（删除协议五元组老化时间）

## 功能

**适用NF：PGW-U、UPF**

![](删除协议五元组老化时间（RMV PROTFAGETIME）_82837297.assets/notice_3.0-zh-cn.png)

本命令属于高危命令,执行本命令后将删除指定或所有协议或协议组的五元组老化时间，影响资源利用或影响业务识别解析成功率，请谨慎使用。

该命令用于删除配置的协议组、协议相关的五元组老化时间。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：可选参数<br>参数含义：该参数用于显示配置的协议组、协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于设置协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的默认协议组，可以通过工程命令smctrldsp protocol-list查询。 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于设置协议名称。数据源为系统支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令display protocol-list查询。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PROTFAGETIME]] · 协议五元组老化时间（PROTFAGETIME）

## 使用实例

假如运营商需要删除配置的p2p协议组的五元组老化时间，则执行如下命令：

```
RMV PROTFAGETIME:PROTOCOLLEVEL=PROTOCOLGROUP,PROTGROUPNAME="p2p";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除协议五元组老化时间（RMV-PROTFAGETIME）_82837297.md`
