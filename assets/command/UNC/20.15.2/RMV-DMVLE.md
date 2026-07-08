---
id: UNC@20.15.2@MMLCommand@RMV DMVLE
type: MMLCommand
name: RMV DMVLE（删除Diameter虚拟本地实体）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DMVLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter虚拟本地实体
status: active
---

# RMV DMVLE（删除Diameter虚拟本地实体）

## 功能

**适用网元：MME**

该命令用于删除Diameter虚拟本地实体信息。

## 注意事项

- 该命令执行后立即生效。
- MME链式备份特性（特性编号：WSFD-201201）启用后，若系统内最后一个容灾Diameter本地实体记录删除，会导致S6a接口的设备容灾功能不可用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定虚拟本地实体的索引，唯一标识一个虚拟本地实体。<br>取值范围：32~63<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DMVLE]] · Diameter虚拟本地实体（DMVLE）

## 使用实例

将索引为32的虚拟本地实体删除：

RMV DMVLE: LOINDEX=32;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DMVLE.md`
