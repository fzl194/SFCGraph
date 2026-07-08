---
id: UDG@20.15.2@MMLCommand@RMV SADEDICBEARER
type: MMLCommand
name: RMV SADEDICBEARER（删除业务感知专有承载配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: SADEDICBEARER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- 用户QOS控制
- 业务QOS控制
- 业务感知专有承载
status: active
---

# RMV SADEDICBEARER（删除业务感知专有承载配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除业务感知专有承载配置（RMV SADEDICBEARER）_82837656.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该命令会影响业务触发的QoS保障特性，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除某一个协议或协议组触发专有承载创建的模式。

## 注意事项

- 该命令执行后立即生效。
- 不支持批量删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议、子协议类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于指定协议名称。数据源为系统支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于指定协议组名称。数据源为系统支持识别的所有类型的协议分类。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SADEDICBEARER]] · 业务感知专有承载配置（SADEDICBEARER）

## 使用实例

删除业务感知专有承载配置：PROTOCOLEVEL为PROTOCOLGROUP，PROTGROUPNAME为p2p：

```
RMV SADEDICBEARER:PROTOCOLLEVEL=PROTOCOLGROUP,PROTGROUPNAME="p2p";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除业务感知专有承载配置（RMV-SADEDICBEARER）_82837656.md`
