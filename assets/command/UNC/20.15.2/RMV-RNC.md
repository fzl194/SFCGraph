---
id: UNC@20.15.2@MMLCommand@RMV RNC
type: MMLCommand
name: RMV RNC（删除Iu接口RNC信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: RNC
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Iu接口管理
- Iu接口RNC信息
status: active
---

# RMV RNC（删除Iu接口RNC信息）

## 功能

![](删除Iu接口RNC信息(RMV RNC)_72225719.assets/notice_3.0-zh-cn_2.png)

删除RNC将导致该RNC下的业务中断。

**适用网元：SGSN**

该命令用于删除Iu接口RNC信息。删除后，该RNC下的用户业务全部受损，请谨慎使用。

## 注意事项

- 该命令执行后立即生效。
- 删除的记录不能在RNCPFLNK表中使用。
- 删除的记录不能在3G paging表中使用。
- 删除的记录不能在MRGRNC表中使用。
- 删除RNC将导致该RNC下的业务中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RNCX | RNC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置RNC索引。<br>取值范围：0~511（数值型）<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RNC]] · Iu接口RNC信息（RNC）

## 使用实例

删除Iu接口索引为0的RNC：

RMV RNC:RNCX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-RNC.md`
