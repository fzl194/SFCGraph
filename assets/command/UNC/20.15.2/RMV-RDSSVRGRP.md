---
id: UNC@20.15.2@MMLCommand@RMV RDSSVRGRP
type: MMLCommand
name: RMV RDSSVRGRP（删除Radius服务器组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RDSSVRGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- 连接管理
- Radius服务器组
status: active
---

# RMV RDSSVRGRP（删除Radius服务器组）

## 功能

**适用NF：PGW-C、SMF**

![](删除Radius服务器组（RMV RDSSVRGRP）_09896732.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，删除RADIUS SERVER GROUP时，将同步删除与服务器组相关联的RDSSVR和RADIUSCLIENTIP对象，以及缓存的Accounting-Request Stop消息。

该命令用来删除RADIUS SERVER GROUP配置。

## 注意事项

- 该命令执行后立即生效。
- 删除RADIUS SERVER GROUP时，将同步删除与服务器组相关联的RDSSVR和RADIUSCLIENTIP对象，以及缓存的Accounting-Request Stop消息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RDSSVRGRPNAME | Radius Server Group名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RADIUS服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RDSSVRGRP]] · Radius服务器组（RDSSVRGRP）

## 使用实例

删除Radius服务器组Radius Server Group名称为rsg：

```
RMV RDSSVRGRP:RDSSVRGRPNAME="rsg";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RDSSVRGRP.md`
