---
id: UNC@20.15.2@MMLCommand@RMV M3LE
type: MMLCommand
name: RMV M3LE（删除M3UA本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M3LE
command_category: 配置类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA本地实体
status: active
---

# RMV M3LE（删除M3UA本地实体）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于删除M3UA本地实体。

## 注意事项

- 该命令执行后立即生效。
- 执行该命令将中断该本地实体上的所有业务。
- 如果M3UA目的实体表中有该本地实体的相关记录，或者该本地实体的相关记录在SCCP本局信令点存在，则不能删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LEX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备删除的本地实体的索引。<br>取值范围：0~63<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3LE]] · M3UA本地实体（M3LE）

## 使用实例

删除索引为1的本地实体：

```
RMV M3LE: LEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除M3UA本地实体(RMV-M3LE)_72345913.md`
