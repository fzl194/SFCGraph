---
id: UNC@20.15.2@MMLCommand@SET UPCSCANRATE
type: MMLCommand
name: SET UPCSCANRATE（设置用户面控制扫描速率）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPCSCANRATE
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- 用户面控制扫描速率管理
status: active
---

# SET UPCSCANRATE（设置用户面控制扫描速率）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于设置用户面控制扫描速率。

## 注意事项

- 该命令执行后立即生效。

- 当SCANTYPE配置为“GTPUPATHFAULT、APNFAULT、PATHFAULTMIGRATE、PATHMIGRATE”时，默认扫描速率初始记录值为1。
- 枚举项BACKMIGRATION默认扫描速率初始记录值为10，默认扫描间隔为5。
- 当SCANTYPE配置为“BACKMIGRATION”时，扫描速率建议保持默认值10，扫描间隔建议保持默认值5。若调大BACKMIGRATION对应的扫描速率或扫描间隔，可能造成CPU使用率升高。若调小BACKMIGRATION对应的扫描速率或扫描间隔，可能会影响故障恢复回迁速度。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCANTYPE | RATE |
| --- | --- |
| DEACTIVE | 1 |
| CHECK | 1 |
| DAILYCHECK | 1 |
| MIGRATE | 1 |
| ADDRDEACTIVE | 1 |
| INERTIALOPERATION | 1 |
| UPPATHFAULT | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCANTYPE | 扫描任务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扫描任务的类型。<br>数据来源：本端规划<br>取值范围：<br>- DEACTIVE（去激活任务）<br>- CHECK（检查任务）<br>- DAILYCHECK（日常检查任务）<br>- MIGRATE（迁移任务）<br>- ADDRDEACTIVE（地址去活任务）<br>- INERTIALOPERATION（惯性运行任务）<br>- UPPATHFAULT（N3/N9链路故障任务）<br>- GTPUPATHFAULT（GTPU链路故障任务）<br>- APNFAULT（APN故障任务）<br>- PATHFAULTMIGRATE（路径故障迁移任务）<br>- PATHMIGRATE（路径迁移任务）<br>- BACKMIGRATION（故障恢复回迁任务）<br>默认值：无。<br>配置原则：无 |
| RATE | 扫描速率(个/秒) | 可选必选说明：必选参数<br>参数含义：该任务用于设置指定扫描任务的扫描速率。取值为0表示不启动对应扫描任务。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~300。<br>默认值：无。<br>配置原则：无 |
| INTERVAL | 扫描间隔（秒） | 可选必选说明：该参数在"SCANTYPE"配置为"BACKMIGRATION"时为条件必选参数。<br>参数含义：该参数用于设置指定扫描任务的定时器间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~60。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPCSCANRATE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPCSCANRATE]] · 用户面控制扫描速率（UPCSCANRATE）

## 使用实例

设置去激活任务的扫描速率为20(个/秒)，使用下列配置：

```
SET UPCSCANRATE: SCANTYPE=DEACTIVE, RATE=20;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置用户面控制扫描速率（SET-UPCSCANRATE）_04284727.md`
