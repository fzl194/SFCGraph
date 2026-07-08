---
id: UNC@20.15.2@MMLCommand@MOD TALST
type: MMLCommand
name: MOD TALST（修改跟踪区列表）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: TALST
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
- TA List管理
status: active
---

# MOD TALST（修改跟踪区列表）

## 功能

**适用网元：MME**

该命令用来修改跟踪区列表配置数据。

## 注意事项

- 该命令执行后立即生效。
- 该命令只能修改“描述”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TALISTID | TA List 标号 | 可选必选说明：必选参数<br>参数含义：该参数用于在MME内唯一标识一个跟踪区列表。一个跟踪区列表由若干跟踪区TA组合而成。<br>数据来源：本端规划<br>取值范围：0~65534<br>默认值：无 |
| TAI | TAI | 可选必选说明：必选参数<br>参数含义：该参数用于在一个MME内唯一标识一个跟踪区。<br>数据来源：整网规划。<br>取值范围：9~10位字符串<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区列表名称。<br>数据来源：整网规划<br>取值范围：长度不超过32的字符串<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TALST]] · 跟踪区列表（TALST）

## 使用实例

将包含跟踪区1230100010的跟踪列表1的描述改为“AREA3”：

MOD TALST: TALISTID=1, TAI="1230100010", DESC="AREA3";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-TALST.md`
