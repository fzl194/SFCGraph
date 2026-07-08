---
id: UNC@20.15.2@MMLCommand@RMV DNNGRP
type: MMLCommand
name: RMV DNNGRP（删除DNN群组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNNGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- DNN群组标识管理
status: active
---

# RMV DNNGRP（删除DNN群组）

## 功能

**适用NF：AMF**

该命令用于删除指定的DNN群组。

## 注意事项

- 该命令执行后立即生效。

- 在执行本命令前请先执行LST DNNGRPMEM确保该群组下的DNN成员已经删除，再执行LST NGPARKPLCY确保该群组下的园区策略已经删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNGRPID | DNN群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个DNN群组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNN群组（DNNGRP）](configobject/UNC/20.15.2/DNNGRP.md)

## 使用实例

删除群组名称为“ABC”的DNN群组，执行如下命令：

```
RMV DNNGRP: DNNGRPID="ABC";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNN群组（RMV-DNNGRP）_64343905.md`
