---
id: UNC@20.15.2@MMLCommand@RMV CPCGGRP
type: MMLCommand
name: RMV CPCGGRP（删除抄送CG组）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CPCGGRP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
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

# RMV CPCGGRP（删除抄送CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来删除指定的抄送CG组。

## 注意事项

- 该命令执行后立即生效。
- 删除指定抄送CG组，删除时必须要指定抄送CG组的ID。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPCGGRPID | 抄送CG组ID | 可选必选说明：必选参数<br>参数含义：抄送CG组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1。整数1。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CPCGGRP]] · 抄送CG组（CPCGGRP）

## 使用实例

删除抄送CG组ID为1的抄送CG组：

```
RMV CPCGGRP: CPCGGRPID=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-CPCGGRP.md`
