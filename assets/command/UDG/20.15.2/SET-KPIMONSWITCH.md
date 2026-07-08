---
id: UDG@20.15.2@MMLCommand@SET KPIMONSWITCH
type: MMLCommand
name: SET KPIMONSWITCH（设置KPI异常检测功能开关）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: KPIMONSWITCH
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 指标监控
status: active
---

# SET KPIMONSWITCH（设置KPI异常检测功能开关）

## 功能

![](设置KPI异常检测功能开关（SET KPIMONSWITCH）_35322753.assets/notice_3.0-zh-cn.png)

关闭开关会清理掉持久化数据，重新打开检测开关后，需要重新累积7天KPI数据才做检测。

该命令用于设置KPI异常检测功能开关。

> **说明**
> - 该命令执行后立即生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | SWITCH |
> | --- |
> | ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | KPI异常检测开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定KPI异常检测开关。<br>数据来源：本端规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [KPI异常检测功能开关（KPIMONSWITCH）](configobject/UDG/20.15.2/KPIMONSWITCH.md)

## 使用实例

- 开启KPI异常检测。
  ```
  SET KPIMONSWITCH: SWITCH=ON;
  ```
- 关闭KPI异常检测。
  ```
  SET KPIMONSWITCH: SWITCH=OFF;
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置KPI异常检测功能开关（SET-KPIMONSWITCH）_35322753.md`
