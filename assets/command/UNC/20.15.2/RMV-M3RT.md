---
id: UNC@20.15.2@MMLCommand@RMV M3RT
type: MMLCommand
name: RMV M3RT（删除M3UA信令路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M3RT
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
- M3UA路由
status: active
---

# RMV M3RT（删除M3UA信令路由）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于删除M3UA信令路由。删除对应的M3UA目的实体的最后一条路由时，对应的业务受损。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RTX | 路由索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备删除的路由的索引。<br>取值范围：0~1279<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3RT]] · M3UA信令路由（M3RT）

## 使用实例

删除索引为1的M3UA路由：

RMV M3RT: RTX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除M3UA信令路由(RMV-M3RT)_26146316.md`
