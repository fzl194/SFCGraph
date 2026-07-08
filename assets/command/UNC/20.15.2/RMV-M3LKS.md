---
id: UNC@20.15.2@MMLCommand@RMV M3LKS
type: MMLCommand
name: RMV M3LKS（删除M3UA信令链路集）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: M3LKS
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
- M3UA链路集
status: active
---

# RMV M3LKS（删除M3UA信令链路集）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于删除M3UA信令链路集。

## 注意事项

- 该命令执行后立即生效。
- 当M3UA链路表或M3UA路由表中存在此链路集相关的记录时，不允许删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LSX | 链路集索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备删除的链路集的索引。<br>取值范围：0～1279<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/M3LKS]] · M3UA信令链路集（M3LKS）

## 使用实例

删除索引为1的M3UA链路集：

RMV M3LKS: LSX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-M3LKS.md`
