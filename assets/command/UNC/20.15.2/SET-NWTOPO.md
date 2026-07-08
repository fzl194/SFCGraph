---
id: UNC@20.15.2@MMLCommand@SET NWTOPO
type: MMLCommand
name: SET NWTOPO（设置组网拓扑采集功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NWTOPO
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 系统维护
- 组网拓扑功能
status: active
---

# SET NWTOPO（设置组网拓扑采集功能开关）

## 功能

**适用网元：SGSN、MME**

该命令用于设置是否打开组网拓扑信息采集功能。如果设置为关闭，则组网拓扑采集服务器通过下发组网拓扑采集任务无法获取到对应的组网拓扑信息；如果设置为打开，则组网拓扑采集服务器可通过下发组网拓扑采集任务获取系统的组网拓扑信息。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行以后只对新下发的组网拓扑采集任务生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TOPOFUNC | 拓扑采集功能 | 可选必选说明：可选参数<br>参数含义：该参数用于设置拓扑采集功能开关。<br>数据来源：全网规划<br>取值范围：<br>- “ENABLE(使能)”<br>- “DISABLE(去使能)”<br>系统初始设置值：<br>“DISABLE(去使能)” |

## 操作的配置对象

- [组网拓扑采集功能开关（NWTOPO）](configobject/UNC/20.15.2/NWTOPO.md)

## 使用实例

设置组网拓扑采集功能开关为打开：

SET NWTOPO: TOPOFUNC=ENABLE;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置组网拓扑采集功能开关（SET-NWTOPO）_26146358.md`
