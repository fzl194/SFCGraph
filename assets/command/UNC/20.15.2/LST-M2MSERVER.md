---
id: UNC@20.15.2@MMLCommand@LST M2MSERVER
type: MMLCommand
name: LST M2MSERVER（查询M2M服务器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: M2MSERVER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M服务器
status: active
---

# LST M2MSERVER（查询M2M服务器）

## 功能

**适用NF：PGW-C、SMF**

该命令用来查询M2M服务器组下的M2M服务器的相关信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | M2M服务器组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器所属M2M服务器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：<br>GROUPNAME参数依赖M2MSERVERGRP命令的GROUPNAME参数。 |
| SERVERINDEX | M2M服务器索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定M2M服务器索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MSERVER]] · M2M服务器（M2MSERVER）

## 使用实例

查询“m2msrvgroup01”M2M服务器组下的M2M服务器的相关信息：

```
%%LST M2MSERVER: GROUPNAME="m2msrvgroup01";%%
RETCODE = 0  操作成功

结果如下
--------
    M2M服务器组名称  =  m2msrvgroup01
      M2M服务器索引  =  1
M2M服务器IP地址类型  =  IPv4
  M2M服务器IPv4地址  =  10.107.242.17
  M2M服务器IPv6地址  =  ::
       服务器端口号  =  5683
       域名配置开关  =  不使能
      M2M服务器域名  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询M2M服务器（LST-M2MSERVER）_73321233.md`
