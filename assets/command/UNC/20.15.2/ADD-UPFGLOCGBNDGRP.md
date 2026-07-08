---
id: UNC@20.15.2@MMLCommand@ADD UPFGLOCGBNDGRP
type: MMLCommand
name: ADD UPFGLOCGBNDGRP（增加UPF组与Diameter本端主机组的绑定关系组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: UPFGLOCGBNDGRP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 3000
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- UPF组与Diam本端主机组的绑定关系组
status: active
---

# ADD UPFGLOCGBNDGRP（增加UPF组与Diameter本端主机组的绑定关系组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于添加UPF组与Diameter本端主机组的绑定关系组。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为3000。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称 | 可选必选说明：必选参数<br>参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPFGLOCGBNDGRP]] · UPF组与Diameter本端主机组的绑定关系组（UPFGLOCGBNDGRP）

## 使用实例

添加UPF组与Diameter本端主机组的绑定关系组，“UPFGLOCGBNDGNAME”为“huawei”：

```
ADD UPFGLOCGBNDGRP: UPFGLOCGBNDGNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF组与Diameter本端主机组的绑定关系组（ADD-UPFGLOCGBNDGRP）_29420948.md`
