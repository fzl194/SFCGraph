---
id: UNC@20.15.2@MMLCommand@RMV M3DE
type: MMLCommand
name: RMV M3DE（删除M3UA目的实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M3DE
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
- M3UA目的实体
status: active
---

# RMV M3DE（删除M3UA目的实体）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于删除M3UA目的实体。

## 注意事项

- 该命令执行后立即生效。
- 当M3UA路由表或M3UA链路集表中存在此目的信令点相关的记录时，不允许删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DEX | 目的实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除的目的实体的索引。<br>取值范围：0~1279<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3DE]] · M3UA目的实体（M3DE）

## 使用实例

删除索引为1的M3UA目的实体：

```
RMV M3DE: DEX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除M3UA目的实体(RMV-M3DE)_26146302.md`
