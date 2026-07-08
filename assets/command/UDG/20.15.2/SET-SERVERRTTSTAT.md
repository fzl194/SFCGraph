---
id: UDG@20.15.2@MMLCommand@SET SERVERRTTSTAT
type: MMLCommand
name: SET SERVERRTTSTAT（设置服务器时延统计功能配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SERVERRTTSTAT
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
- SGW-U
- GGSN
effect_mode: ''
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务运维
- 业务统计管理
- 服务器时延统计
status: active
---

# SET SERVERRTTSTAT（设置服务器时延统计功能配置）

## 功能

**适用NF：UPF、PGW-U、SGW-U、GGSN**

![](设置服务器时延统计功能配置（SET SERVERRTTSTAT）_72428328.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，此命令开启后可能导致性能下降明显。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

该命令用于设置统计服务器时延统计功能。如果现网需要基于特定协议类型的CDN或DNS服务器进行进延统计，则开启开关并选择需要统计的应用类型。

## 注意事项

- 该命令执行后仅对新流生效，老流不生效。
- 该命令最大记录数为1。
- 针对开启时延统计的协议，网元自动学习并保存使用该协议的前1000个IP地址，对访问该服务器的业务流进行流量统计，并按10%的抽样率进行时延统计。
- 如果同一个服务器IP同时部署了多种协议的服务，按首次统计到的协议类型统计流量和时延，不统计到其他类型的协议流量和时延中。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | RTTSTATSW | PROTOCOLLIST | STATDURATION |
| --- | --- | --- | --- |
| 初始值 | DISABLE | NULL | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RTTSTATSW | 服务器时延统计开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置服务器时延统计开关。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| PROTOCOLLIST | 服务器时延统计协议列表 | 可选必选说明：条件必选参数<br>前提条件：该参数在“RTTSTATSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于设置开启时延统计的服务器协议类型。开启时延统计开关时，至少需要选择一种协议。<br>数据来源：本端规划<br>取值范围：时延统计开关至少选择一个协议。<br>- FACEBOOK：Facebook协议CDN服务器。<br>- TIKTOK：Tiktok协议CDN服务器。<br>- YOUTUBE：Youtube协议CDN服务器。<br>- NETFLIX：Netflix协议CDN服务器。<br>- DNS：DNS协议服务器。<br>默认值：无<br>配置原则：无 |
| STATDURATION | 时延统计时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“RTTSTATSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置时延统计的统计时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～7，单位是天。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SERVERRTTSTAT]] · 服务器时延统计功能配置（SERVERRTTSTAT）

## 使用实例

对协议类型是Facebook的服务器 开启时延统计功能，统计周期为2天：

```
SET SERVERRTTSTAT: RTTSTATSW=ENABLE, PROTOCOLLIST=FACEBOOK-1&TIKTOK-0&YOUTUBE-0&NETFLIX-0&DNS-0, STATDURATION=2;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置服务器时延统计功能配置（SET-SERVERRTTSTAT）_72428328.md`
