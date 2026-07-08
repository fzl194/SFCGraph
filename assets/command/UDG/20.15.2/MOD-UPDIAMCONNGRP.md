---
id: UDG@20.15.2@MMLCommand@MOD UPDIAMCONNGRP
type: MMLCommand
name: MOD UPDIAMCONNGRP（修改Diameter链路组）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: UPDIAMCONNGRP
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter管理
- Diameter连接
- Diameter链路组
status: active
---

# MOD UPDIAMCONNGRP（修改Diameter链路组）

## 功能

**适用NF：UPF**

该命令用于修改Diameter链路组的链路选择模式。当Diameter链路组建立后，需要修改链路选择模式时执行该命令。

## 注意事项

- 该命令执行后立即生效。
- 配置SELECTMODE为SESSION_ID时，根据session-id选择Diameter链路状态异常时，会选择其他可用Diameter链路进行消息交互。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter链路组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SELECTMODE | 链路选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter链路组的链路选择模式。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SESSION_ID：基于会话（Session-id）轮询方式进行链路选择。<br>- MASTER_SLAVE：基于主备方式进行链路选择。<br>- ROUND_ROBIN：基于消息轮询方式进行链路选择。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMCONNGRP]] · Diameter链路组（UPDIAMCONNGRP）

## 使用实例

如果希望diameter链路组swmconngrp的链路选择模式修改为session-id轮选方式，可以使用该命令修改链路组：

```
MOD UPDIAMCONNGRP: CONNGROUPNAME="swmconngrp", SELECTMODE=SESSION_ID;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/MOD-UPDIAMCONNGRP.md`
