---
id: UDG@20.15.2@MMLCommand@SET PPPCFG
type: MMLCommand
name: SET PPPCFG（设置PPP配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PPPCFG
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- PPP配置
status: active
---

# SET PPPCFG（设置PPP配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置系统进行PPP协商时所使用的参数，包括系统侧与用户鉴权时使用的主机名、系统的最大接收单元、PPP协商请求的超时时间。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | HOSTNAME | MRU | TIMEOUT |
| --- | --- | --- | --- |
| 初始值 | UPF | 1500 | 3 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 本端主机名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统侧用户进行鉴权时所使用的主机名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：无<br>配置原则：<br>- 输入单空格将删除该参数已有配置项。<br>- 建议值为UPF。<br>- 该参数只有在APN支持PPP鉴权的前提下才会生效，通过SET APNPPPACCESS命令配置APN是否支持PPP鉴权。<br>- 输入单空格将删除该参数已有配置项，恢复初始值。 |
| MRU | 最大接收单元 | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统侧PPP协商的最大接收单元。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～1500。<br>默认值：无<br>配置原则：建议值为1500。 |
| TIMEOUT | 超时时间（秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定系统侧用户进行PPP协商时的请求超时时间，即系统没有收到用户回应的PPP协商报文而进行重发前所等待的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：无<br>配置原则：建议值为3。 |

## 操作的配置对象

- [PPP配置（PPPCFG）](configobject/UDG/20.15.2/PPPCFG.md)

## 关联任务

- [0-00138](task/UDG/20.15.2/0-00138.md)

## 使用实例

运营商如果需要修改系统侧与用户鉴权时使用的主机名、系统的最大接收单元或PPP协商请求的超时时间参数时，可以使用该命令：

```
SET PPPCFG:HOSTNAME="upf",MRU=1500,TIMEOUT=3;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PPP配置（SET-PPPCFG）_35373544.md`
