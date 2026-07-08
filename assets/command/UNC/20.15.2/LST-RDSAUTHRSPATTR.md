---
id: UNC@20.15.2@MMLCommand@LST RDSAUTHRSPATTR
type: MMLCommand
name: LST RDSAUTHRSPATTR（查询支持的Radius鉴权响应消息私有属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RDSAUTHRSPATTR
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 鉴权管理
- 应答消息信元控制
status: active
---

# LST RDSAUTHRSPATTR（查询支持的Radius鉴权响应消息私有属性）

## 功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于查询PGW/GGSN是否支持解析RADIUS服务器在鉴权响应消息中返回的运营商私有属性。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | RADIUS服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定RADIUS服务器组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：<br>需要确保RADIUS服务器组名称已经通过ADD RDSSVRGRP配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSAUTHRSPATTR]] · 支持的Radius鉴权响应消息私有属性（RDSAUTHRSPATTR）

## 使用实例

查看RADIUS服务器组“rds”的鉴权应答消息中运营商私有属性是否支持解析：

```
LST RDSAUTHRSPATTR:RDSSVRGRPNAME="rds";
RETCODE = 0 操作成功。

支持的Radius鉴权响应消息私有属性
--------------------------------
Radius Server Group名称 = rds
Operator-Charging-Rule-Base-Name = 禁止
Event-Charging-Function-Name = 禁止
Operator-Vpn-Name = 允许
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RDSAUTHRSPATTR.md`
