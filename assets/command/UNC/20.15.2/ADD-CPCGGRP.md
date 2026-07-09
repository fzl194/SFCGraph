---
id: UNC@20.15.2@MMLCommand@ADD CPCGGRP
type: MMLCommand
name: ADD CPCGGRP（增加抄送CG组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: CPCGGRP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- 抄送CG组
status: active
---

# ADD CPCGGRP（增加抄送CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来增加抄送CG组，配置抄送CG组描述信息。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPCGGRPID | 抄送CG组ID | 可选必选说明：必选参数<br>参数含义：抄送CG组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。整数1。<br>默认值：无<br>配置原则：无 |
| DESCRIPTION | 抄送CG组描述 | 可选必选说明：可选参数<br>参数含义：抄送CG组的描述。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [抄送CG组（CPCGGRP）](configobject/UNC/20.15.2/CPCGGRP.md)

## 关联任务

- [0-00024](task/UNC/20.15.2/0-00024.md)

## 使用实例

增加一条抄送CG组配置，其中抄送CG组ID为1，抄送CG组描述为“CpCGGroup1”：

```
ADD CPCGGRP: CPCGGRPID=1, DESCRIPTION="CpCGGroup1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加抄送CG组（ADD-CPCGGRP）_09896864.md`
