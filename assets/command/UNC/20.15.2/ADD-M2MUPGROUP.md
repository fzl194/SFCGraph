---
id: UNC@20.15.2@MMLCommand@ADD M2MUPGROUP
type: MMLCommand
name: ADD M2MUPGROUP（增加M2M关联的UPF组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: M2MUPGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- M2M关联的UPF组管理
status: active
---

# ADD M2MUPGROUP（增加M2M关联的UPF组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于增加M2M关联的UPF组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGRPNAME | UPF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UPF组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M2MUPGROUP]] · M2M关联的UPF组（M2MUPGROUP）

## 使用实例

增加M2M关联的UPF组，组名为upfgrp1：

```
ADD M2MUPGROUP: UPFGRPNAME="upfgrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加M2M关联的UPF组（ADD-M2MUPGROUP）_96241690.md`
