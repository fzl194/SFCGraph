---
id: UDG@20.15.2@MMLCommand@SET MSSPBUFTRACELT
type: MMLCommand
name: SET MSSPBUFTRACELT（设置PBUF轨迹开关和持续时间）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: MSSPBUFTRACELT
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 轨迹开关
status: active
---

# SET MSSPBUFTRACELT（设置PBUF轨迹开关和持续时间）

## 功能

![](设置PBUF轨迹开关和持续时间（SET MSSPBUFTRACELT）_45801325.assets/notice_3.0-zh-cn.png)

本命令用于使能PBUF轨迹开关，开启后会降低性能且在用户指定的时间后会自动去使能，关闭后会恢复性能。默认时间是24小时。

该命令用于设置MSS的PBUF轨迹开关和持续时间。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | TRACESWITCH | TIME |
> | --- | --- |
> | ON | 1440 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRACESWITCH | PBUF轨迹开关 | 可选必选说明：必选参数<br>参数含义：该参数用于表示轨迹开关标记。<br>数据来源：本端规划<br>取值范围：<br>- ON（开）<br>- OFF（关）<br>默认值：无。<br>配置原则：无 |
| TIME | 轨迹开关持续时间（分钟） | 可选必选说明：该参数在"TRACESWITCH"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于表示本次规则设置的持续时间，单位:分钟。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~43200。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MSSPBUFTRACELT查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSPBUFTRACELT]] · PBUF轨迹开关状态和持续时间（MSSPBUFTRACELT）

## 使用实例

打开PBUF轨迹开关，设置持续时间为66分钟:

```
%%SET MSSPBUFTRACELT: TRACESWITCH=ON, TIME=66;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PBUF轨迹开关和持续时间（SET-MSSPBUFTRACELT）_45801325.md`
