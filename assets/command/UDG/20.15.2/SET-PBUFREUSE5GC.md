---
id: UDG@20.15.2@MMLCommand@SET PBUFREUSE5GC
type: MMLCommand
name: SET PBUFREUSE5GC（设置pbuf重用检测开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PBUFREUSE5GC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- MSS 调测命令
- PBUF
status: active
---

# SET PBUFREUSE5GC（设置pbuf重用检测开关）

## 功能

![](设置pbuf重用检测开关（SET PBUFREUSE5GC）_99859361.assets/notice_3.0-zh-cn.png)

本命令用于使能PBUF重用检测，开启后会降低性能，关闭后性能恢复。请谨慎使用并联系华为技术支持协助操作。

此命令用于设置MSS的PBUF重用检测开关，重用检测功能用来检测多个进程是否同时在使用同一片PBUF。用户打开开关后，系统收集运行信息，导致转发面性能下降，开关关闭后性能恢复。

> **说明**
> - 该命令执行后立即生效。
>
> - 本命令用于使能PBUF重用检测，开启后会降低性能，关闭后会恢复性能。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODTYPE | pod类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定pod类型。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无。<br>配置原则：无 |
| POOLNAME | 内存池名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定内存池名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~31。<br>默认值：无。<br>配置原则：无 |
| REUSESWITCH | 开关标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定pbuf重用检测开关的状态。<br>如果开关取值是Enable，则表示检测开关打开；<br>如果开关取值是Disable，则表示检测开关关闭。<br>数据来源：本端规划<br>取值范围：<br>- Enable（开关打开）<br>- Disable（开关关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PBUFREUSE5GC]] · pbuf重用检测开关设置（PBUFREUSE5GC）

## 使用实例

通过如下命令打开podtype为aa的pod内PAE内存池pbuf重用检测开关：

```
SET PBUFREUSE5GC:PODTYPE="aa",POOLNAME="PAE",REUSESWITCH=Enable;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置pbuf重用检测开关（SET-PBUFREUSE5GC）_99859361.md`
