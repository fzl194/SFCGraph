---
id: UNC@20.15.2@MMLCommand@RMV EPLMNGRP
type: MMLCommand
name: RMV EPLMNGRP（删除等价PLMN组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EPLMNGRP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 等价PLMN组管理
status: active
---

# RMV EPLMNGRP（删除等价PLMN组）

## 功能

**适用NF：AMF**

该命令用于删除等价PLMN组。

## 注意事项

- 该命令执行后立即生效。

- 删除等价PLMN组之前，需要删除该组内的等价PLMN成员。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 等价PLMN组号 | 可选必选说明：必选参数<br>参数含义：该参数用于在UNC系统内唯一标识一个等价PLMN组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@EPLMNGRP]] · 等价PLMN组（EPLMNGRP）

## 使用实例

删除组号为1的等价PLMN组，执行如下命令：

```
RMV EPLMNGRP: GRPIDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-EPLMNGRP.md`
