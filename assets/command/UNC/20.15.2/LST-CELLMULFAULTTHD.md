---
id: UNC@20.15.2@MMLCommand@LST CELLMULFAULTTHD
type: MMLCommand
name: LST CELLMULFAULTTHD（查询进程频繁故障监控参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CELLMULFAULTTHD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST CELLMULFAULTTHD（查询进程频繁故障监控参数）

## 功能

该命令用于查询进程频繁故障监控参数值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSNAME | 进程名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示微服务的进程类型名称。进程类型名称可以通过<br>[**DSP MSPROCTYPE**](显示微服务进程类型（DSP MSPROCTYPE）_09587905.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CELLMULFAULTTHD]] · 进程频繁故障监控参数（CELLMULFAULTTHD）

## 使用实例

查询服务进程频繁告警参数配置。

```
%%LST CELLMULFAULTTHD:;%%
RETCODE = 20111  无数据。

没有查到相应结果
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CELLMULFAULTTHD.md`
