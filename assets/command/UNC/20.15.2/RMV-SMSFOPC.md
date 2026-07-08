---
id: UNC@20.15.2@MMLCommand@RMV SMSFOPC
type: MMLCommand
name: RMV SMSFOPC（删除SMSF本局信令点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMSFOPC
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SMSFOPC本局信令点
status: active
---

# RMV SMSFOPC（删除SMSF本局信令点）

## 功能

**适用NF：SMSF**

该命令用于删除SMSFOPC本局信令点指定配置。

## 注意事项

- 该命令执行后立即生效。
- 删除该记录会导致SMSF业务失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPX | SMSF信令点索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMSF本局信令点索引。<br>数据来源：本端规划<br>取值范围：1～10<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFOPC]] · SMSF本局信令点（SMSFOPC）

## 使用实例

删除SMSF信令点索引为1的SMSFOPC信令点。

```
RMV SMSFOPC: OPX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SMSFOPC.md`
