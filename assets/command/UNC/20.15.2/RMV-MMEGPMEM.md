---
id: UNC@20.15.2@MMLCommand@RMV MMEGPMEM
type: MMLCommand
name: RMV MMEGPMEM（删除MME群组成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMEGPMEM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组成员配置
status: active
---

# RMV MMEGPMEM（删除MME群组成员）

## 功能

**适用网元：MME**

该命令用于删除MME群组成员。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无 |
| MMEC | MME编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME编码。<br>数据来源：全网规划<br>取值范围：2位16进制编码<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEGPMEM]] · MME群组成员（MMEGPMEM）

## 使用实例

1. 删除MME群组索引 = 1，MME编码 = 11的记录。
  RMV MMEGPMEM: MMEGPIDX=1, MMEC="11";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MMEGPMEM.md`
