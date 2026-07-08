---
id: UNC@20.15.2@MMLCommand@RMV TZLST
type: MMLCommand
name: RMV TZLST（删除多时区参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TZLST
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
- 多时区管理
- 多时区参数
status: active
---

# RMV TZLST（删除多时区参数）

## 功能

**适用网元：SGSN、MME**

该命令用于删除位置区对应的时区和夏令时信息。

## 注意事项

- 该命令执行后立即生效。
- 删除前请确保当前时区标识在[**ADD AREATZ**](../区域时区参数配置/增加区域时区参数(ADD AREATZ)_72225267.md)中没有被引用。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TZID | 时区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除时区的索引信息。<br>取值范围：1～24<br>默认值：无 |

## 操作的配置对象

- [多时区参数（TZLST）](configobject/UNC/20.15.2/TZLST.md)

## 使用实例

删除 “时区标识” 为 “1” 的时区和夏令时配置信息:

RMV TZLST: TZID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除多时区参数(RMV-TZLST)_72345187.md`
