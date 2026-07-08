---
id: UNC@20.15.2@MMLCommand@RMV IMEISVSEG
type: MMLCommand
name: RMV IMEISVSEG（删除IMEISV号段）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IMEISVSEG
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMEISV号段
status: active
---

# RMV IMEISVSEG（删除IMEISV号段）

## 功能

**适用NF：PGW-C、SMF**

![](删除IMEISV号段（RMV IMEISVSEG）_09897140.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，如果不输入IMEISV号段名称，表示删除系统内的所有IMEISV号段。删除后引用IMEISV号段的用户可能会因为无法命中UPBindUPG和SUBSCRIBERIDSEGGRP导致业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除IMEISVSEG号段。

支持批量删除。

## 注意事项

- 该命令执行后立即生效。
- 如果引用了该IMEISVSEG的UPBindUPG的记录存在，则不允许删除IMEISVSEG记录。通过LST UPBINDUPG查询绑定关系记录。
- 如果引用了该IMEISVSEG的SUBSCRIBERIDSEGGRP的记录存在，则不允许删除IMEISVSEG记录。通过LST SUBSCRIBERIDSEGGRP查询绑定关系记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMEISV号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMEISV号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：若未指定该参数，则删除所有IMEISVSEG号段。 |

## 操作的配置对象

- [IMEISV号段（IMEISVSEG）](configobject/UNC/20.15.2/IMEISVSEG.md)

## 使用实例

删除IMEISV号段：SEGMENTNAME为TestSegmentName：

```
RMV IMEISVSEG:SEGMENTNAME="TestSegmentName";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IMEISV号段（RMV-IMEISVSEG）_09897140.md`
