---
id: UNC@20.15.2@MMLCommand@SET MSFAULTALARM
type: MMLCommand
name: SET MSFAULTALARM（设置告警开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: MSFAULTALARM
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET MSFAULTALARM（设置告警开关）

## 功能

该命令功能不可用，"ALM-100001进程故障告警"是否抑制及抑制时长，请使用OM Portal上“告警配置”进行相关抑制配置操作。

## 注意事项

- 该命令执行后立即生效。

- 当前版本配置此命令不生效。
- 默认进程故障持续超过告警抑制时间上报ALM-100001 进程故障告警，如果关闭告警抑制开关，则此告警立即上报。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SUPPRESSENABLE | SUPPRESSTIME |
| --- | --- |
| TRUE | 300 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUPPRESSENABLE | 告警抑制使能开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示告警抑制使能开关。<br>数据来源：本端规划<br>取值范围：<br>- “TRUE（开启）”：打开告警抑制<br>- “FALSE（关闭）”：关闭告警抑制<br>默认值：无。<br>配置原则：无 |
| SUPPRESSTIME | 告警抑制时间(秒) | 可选必选说明：该参数在"SUPPRESSENABLE"配置为"TRUE"时为条件可选参数。<br>参数含义：该参数用于表示告警抑制时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~42949672，单位是秒。<br>默认值：300。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MSFAULTALARM查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSFAULTALARM]] · 告警开关配置数据（MSFAULTALARM）

## 使用实例

- 打开抑制告警上报的开关，设置告警抑制时间为300秒，故障在告警抑制时间内没有恢复，上报告警。
  ```
  SET MSFAULTALARM: SUPPRESSENABLE=TRUE, SUPPRESSTIME=300;
  ```
- 关闭抑制告警上报的开关，故障产生立即上报告警。
  ```
  SET MSFAULTALARM: SUPPRESSENABLE=FALSE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-MSFAULTALARM.md`
