---
id: UNC@20.15.2@MMLCommand@ADD DIAMAAAGRP
type: MMLCommand
name: ADD DIAMAAAGRP（增加Diameter AAA服务器组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DIAMAAAGRP
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA组
status: active
---

# ADD DIAMAAAGRP（增加Diameter AAA服务器组）

## 功能

**适用NF：PGW-C**

此命令用于新建一个Diameter AAA组，并设置PGW向Diameter AAA服务器组中Diameter AAA请求授权时的消息属性。

## 注意事项

- 该命令执行后对新接入的non-3GPP会话生效。

- 此命令为建立non-3GPP会话的核心配置，需绑定到APN后才能生效。

- 最多可输入10条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PGWIDENTITY | PDN GW Identity携带方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDN GW Identity携带方式。<br>数据来源：全网规划<br>取值范围：<br>- “HOST_NAME（P-GW主机名）”：表示向Diameter AAA请求授权时携带P-GW的主机名称。<br>- “IP（P-GW IP地址）”：表示向Diameter AAA请求授权时携带P-GW的IP地址。<br>默认值：HOST_NAME<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMAAAGRP]] · Diameter AAA服务器组（DIAMAAAGRP）

## 使用实例

根据网络规划，需要新增一个名称为“diametergroup”的Diameter AAA组，向Diameter AAA请求授权时携带PGW IP地址：

```
ADD DIAMAAAGRP:GROUPNAME="diametergroup",PGWIDENTITY=IP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加Diameter-AAA服务器组（ADD-DIAMAAAGRP）_64343820.md`
