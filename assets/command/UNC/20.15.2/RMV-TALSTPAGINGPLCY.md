---
id: UNC@20.15.2@MMLCommand@RMV TALSTPAGINGPLCY
type: MMLCommand
name: RMV TALSTPAGINGPLCY（删除TA List寻呼策略配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: TALSTPAGINGPLCY
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- 基于TA List寻呼策略管理
status: active
---

# RMV TALSTPAGINGPLCY（删除TA List寻呼策略配置）

## 功能

**适用网元：MME**

该命令用于删除基于TAI List的寻呼策略配置数据。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List标号 | 可选必选说明：可选参数<br>参数含义：该参数用于在MME内唯一标识一个跟踪区列表。一个跟踪区列表由若干跟踪区TA组合而成。<br>数据来源：本端规划<br>取值范围：0~65534。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TALSTPAGINGPLCY]] · TA List寻呼策略配置（TALSTPAGINGPLCY）

## 使用实例

1. 删除所有TA List寻呼策略配置：
  RMV TALSTPAGINGPLCY:;
2. 删除一条TA List寻呼策略配置：
  RMV TALSTPAGINGPLCY: TALISTID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-TALSTPAGINGPLCY.md`
