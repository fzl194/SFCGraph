# 设置跟踪流控参数配置（SET TWAMPFLOWCTLCFG）

- [命令功能](#ZH-CN_MMLREF_0000002142846237__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000002142846237__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000002142846237__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000002142846237__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000002142846237)

该命令用于设置TWAMP功能的跟踪流控配置参数。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | FCSWITCH | RECOVERLIMIT | TRIGGERLIMIT | TRACETHD |
> | --- | --- | --- | --- |
> | OPEN | 60 | 70 | 60 |

#### [操作用户权限](#ZH-CN_MMLREF_0000002142846237)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000002142846237)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FCSWITCH | 跟踪流控开关 | 可选必选说明：必选参数<br>参数含义：该参数用于控制流控功能开关。<br>数据来源：本端规划<br>取值范围：<br>- OPEN（打开）<br>- CLOSE（关闭）<br>默认值：OPEN。<br>配置原则：无 |
| RECOVERLIMIT | 流控恢复阈值 | 可选必选说明：该参数在"FCSWITCH"配置为"OPEN"时为条件可选参数。<br>参数含义：该参数用于设置流控恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~70。<br>默认值：60。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TWAMPFLOWCTLCFG查询当前参数配置值。<br>配置原则：<br>本参数取值需要小于等于参数“TRACETHD” 的取值。 |
| TRIGGERLIMIT | 流控触发阈值 | 可选必选说明：该参数在"FCSWITCH"配置为"OPEN"时为条件可选参数。<br>参数含义：该参数用于设置流控触发阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是70~80。<br>默认值：70。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TWAMPFLOWCTLCFG查询当前参数配置值。<br>配置原则：<br>本参数取值需要大于参数“TRACETHD”的取值。 |
| TRACETHD | 允许跟踪创建阈值 | 可选必选说明：该参数在"FCSWITCH"配置为"OPEN"时为条件可选参数。<br>参数含义：该参数用于设置允许跟踪创建阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~70。<br>默认值：60。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST TWAMPFLOWCTLCFG查询当前参数配置值。<br>配置原则：<br>本参数取值需要小于参数“TRIGGERLIMIT”的取值，并且需要大于等于参数“RECOVERLIMIT”的取值。 |

## [使用实例](#ZH-CN_MMLREF_0000002142846237)

- 关闭TWAMP功能的流控跟踪功能。
  ```
  SET TWAMPFLOWCTLCFG: FCSWITCH=CLOSE;
  ```
- 开启并设置TWAMP功能的流控跟踪配置参数。
  ```
  SET TWAMPFLOWCTLCFG: FCSWITCH=OPEN, RECOVERLIMIT=60, TRIGGERLIMIT=70, TRACETHD=60;
  ```
