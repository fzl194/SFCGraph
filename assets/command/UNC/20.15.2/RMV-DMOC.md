---
id: UNC@20.15.2@MMLCommand@RMV DMOC
type: MMLCommand
name: RMV DMOC（删除Diameter流控节点）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMOC
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- Diameterl流控管理
status: active
---

# RMV DMOC（删除Diameter流控节点）

## 功能

**适用网元：SGSN、MME**

该命令用于删除Diameter流控节点，根据Diameter流控节点的索引删除节点。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Diameter流控节点的索引。<br>数据来源：本端规划<br>取值范围：整数范围1~1000<br>默认值： 无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMOC]] · Diameter流控节点（DMOC）

## 使用实例

删除指定索引的Diameter流控节点：

RMV DMOC: INDEX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DMOC.md`
