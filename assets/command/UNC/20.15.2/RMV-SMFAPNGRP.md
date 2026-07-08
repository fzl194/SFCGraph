---
id: UNC@20.15.2@MMLCommand@RMV SMFAPNGRP
type: MMLCommand
name: RMV SMFAPNGRP（删除DNS关联的APN组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFAPNGRP
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
- APN管理
- APN组管理
status: active
---

# RMV SMFAPNGRP（删除DNS关联的APN组）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于删除DNS关联的APN组。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPNAME | APN组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [DNS关联的APN组的描述信息（SMFAPNGRP）](configobject/UNC/20.15.2/SMFAPNGRP.md)

## 使用实例

删除DNS关联的APN组，组名为grp1：

```
RMV SMFAPNGRP:GRPNAME="grp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DNS关联的APN组（RMV-SMFAPNGRP）_88537106.md`
