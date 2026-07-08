---
id: UNC@20.15.2@MMLCommand@RMV SUBGPMEM
type: MMLCommand
name: RMV SUBGPMEM（删除用户群成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SUBGPMEM
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
- 移动性管理
- 区域漫游限制管理
- 用户群成员管理
status: active
---

# RMV SUBGPMEM（删除用户群成员）

## 功能

**适用网元：SGSN、MME**

此命令用于删除用户群成员。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：待删除的IMSI前缀。<br>取值范围：5～15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBGPMEM]] · 用户群成员（SUBGPMEM）

## 使用实例

删除一条IMSI前缀为12345的用户群成员记录：

RMV SUBGPMEM: IMSIPRE="12345";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SUBGPMEM.md`
