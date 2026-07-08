---
id: UNC@20.15.2@MMLCommand@SET DRSTBYRSTCTRL
type: MMLCommand
name: SET DRSTBYRSTCTRL（设置运行备整系统复位开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DRSTBYRSTCTRL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# SET DRSTBYRSTCTRL（设置运行备整系统复位开关）

## 功能

该命令用于设置容灾实例在检测到关键服务异常或者周边网元故障时是否需要复位。

## 注意事项

- 该命令执行后立即生效。

- 该命令只用于在UEN/UEG-S/UEG-L/UEG-M网元采用主备容灾模式下执行。
- 主容灾实例和备容灾实例都可以下发该命令，但只有备容灾实例生效。可使用[**DSP DRGROUPSTATUS**](显示容灾组的运行状态信息（DSP DRGROUPSTATUS）_74554621.md)命令中"RUNNINGSTATUS"查询到本容灾实例是运行主还是运行备。
- 当此命令与521软参冲突时，以521软参的优先级为最高，当521软参设置为1时，忽略此命令的设置。当设置为0时，则再以此命令设置为准。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| STANDBYRESETSW |
| --- |
| TRUE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STANDBYRESETSW | 运行备整系统复位控制 | 可选必选说明：可选参数<br>参数含义：该参数用于设置容灾实例在检测到关键服务异常或者周边网元故障时是否需要复位处理。<br>数据来源：本端规划<br>取值范围：<br>- TRUE（是）<br>- FALSE（否）<br>默认值：TRUE。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DRSTBYRSTCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRSTBYRSTCTRL]] · 运行备整系统复位开关（DRSTBYRSTCTRL）

## 使用实例

开启运行备整系统复位开关：

```
SET DRSTBYRSTCTRL: STANDBYRESETSW=TRUE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DRSTBYRSTCTRL.md`
