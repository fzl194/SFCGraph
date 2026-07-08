---
id: UNC@20.15.2@MMLCommand@RMV UEDNSUPGROUP
type: MMLCommand
name: RMV UEDNSUPGROUP（删除DNS关联的UPF组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: UEDNSUPGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- DN网络DNS_NBNS选择管理
- DNS选择管理
- DNS关联的UPF组管理
status: active
---

# RMV UEDNSUPGROUP（删除DNS关联的UPF组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除DNS关联的UPF组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@UEDNSUPGROUP]] · DNS关联的UPF组（UEDNSUPGROUP）

## 使用实例

删除DNS关联的UPF组，组名为upfgrp1：

```
RMV UEDNSUPGROUP: UPFGRPNAME="upfgrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-UEDNSUPGROUP.md`
