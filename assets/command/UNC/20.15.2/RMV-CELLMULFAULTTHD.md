---
id: UNC@20.15.2@MMLCommand@RMV CELLMULFAULTTHD
type: MMLCommand
name: RMV CELLMULFAULTTHD（删除进程频繁故障监控参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CELLMULFAULTTHD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# RMV CELLMULFAULTTHD（删除进程频繁故障监控参数）

## 功能

该命令用于删除进程频繁故障监控参数值。

## 注意事项

- 该命令执行后立即生效。

- 当系统不存在CELL_SSG的故障告警监控配置时，CELL_SSG默认开启监控，故障告警监控时间为1440分钟，故障告警故障次数为5次，恢复告警监控时间为10分钟，恢复告警监控次数为0次。
- 如果通过本命令删除已经添加的CELL_SSG记录，会恢复对CELL_SSG的默认监控行为。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSNAME | 进程名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示微服务的进程类型名称。进程类型名称可以通过<br>[**DSP MSPROCTYPE**](显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [进程频繁故障监控参数（CELLMULFAULTTHD）](configobject/UNC/20.15.2/CELLMULFAULTTHD.md)

## 使用实例

删除进程名称为CELL_SSG的服务进程频繁告警参数配置。

```
RMV CELLMULFAULTTHD: PROCESSNAME="CELL_SSG";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除进程频繁故障监控参数（RMV-CELLMULFAULTTHD）_35065901.md`
