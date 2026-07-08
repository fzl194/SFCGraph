---
id: UNC@20.15.2@MMLCommand@RMV MRGRNC
type: MMLCommand
name: RMV MRGRNC（删除融合RNC）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MRGRNC
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 基于区域SGSN共享管理
- 融合RNC
status: active
---

# RMV MRGRNC（删除融合RNC）

## 功能

**适用网元：SGSN**

该命令用于两网融合中间态，期望HPLMN基于融合区域生效场景下，删除融合区域RNC。

## 注意事项

- 此命令在下一次业务流程时生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RNCX | RNC索引 | 可选必选说明：必选参数<br>参数含义：该参数用于设置融合RNC索引。<br>数据来源：整网规划<br>取值范围：0～511<br>默认值：无<br>配置原则：<br>RNCX来源于ADD RNC表。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MRGRNC]] · 融合RNC（MRGRNC）

## 使用实例

删除一条： “RNC索引” 为 “0” 的记录。

RMV MRGRNC: RNCX=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MRGRNC.md`
