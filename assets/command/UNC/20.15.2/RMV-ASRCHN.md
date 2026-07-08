---
id: UNC@20.15.2@MMLCommand@RMV ASRCHN
type: MMLCommand
name: RMV ASRCHN（删除容灾业务通道配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ASRCHN
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
- 网络管理
- 主备容灾管理
- 容灾业务通道
status: active
---

# RMV ASRCHN（删除容灾业务通道配置）

## 功能

**适用网元：SGSN、MME**

该命令已废弃。

此命令用于删除主备网元之间的容灾业务通道。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHNID | 容灾业务通道ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定容灾业务通道ID。<br>数据来源：本端规划<br>取值范围：0<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ASRCHN]] · 容灾业务通道配置（ASRCHN）

## 使用实例

删除 “容灾业务通道ID” 为 “0” 的配置记录。

RMV ASRCHN: CHNID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-ASRCHN.md`
