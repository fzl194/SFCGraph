---
id: UDG@20.15.2@MMLCommand@RMV FLOWFILTERGRP
type: MMLCommand
name: RMV FLOWFILTERGRP（删除流过滤器组）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: FLOWFILTERGRP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 流过滤器组
status: active
---

# RMV FLOWFILTERGRP（删除流过滤器组）

## 功能

**适用NF：PGW-U、UPF**

![](删除流过滤器组（RMV FLOWFILTERGRP）_82837385.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会删除流过滤器组下所有绑定关系。

该命令删除所有的流过滤器组，删除指定名称的流过滤器组，或者删除指定流过滤器组和指定流过滤器的绑定关系。删除流过滤器组的同时，该流过滤器组与流过滤器的绑定关系都会同步删除。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 如果流过滤器组被Rule绑定，删除时，需要将绑定关系解除。
- 删除操作要求：
    - 不允许只输入流过滤器名称参数。
    - 如果不输入任何参数，表示要删除所有的流过滤器组。当配置量较大时单次执行可能无法删除全部记录，需要执行多次。
    - 如果只输入流过滤器组名称，表示要删除该流过滤器组，删除该流过滤器组与流过滤器的绑定关系。
    - 如果同时输入流过滤器组名称和流过滤器名称，表示要删除指定流过滤器组与指定的流过滤器的绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLWFLTRGRPNAME | 流过滤器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流过滤器组名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流过滤器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [流过滤器组（FLOWFILTERGRP）](configobject/UDG/20.15.2/FLOWFILTERGRP.md)

## 使用实例

删除流过滤器组，流过滤器组名称为testflowfiltergrp：

```
RMV FLOWFILTERGRP: FLWFLTRGRPNAME="testflowfiltergrp";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流过滤器组（RMV-FLOWFILTERGRP）_82837385.md`
