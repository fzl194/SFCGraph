---
id: UDG@20.15.2@MMLCommand@DSP SDRPLCYCHECK
type: MMLCommand
name: DSP SDRPLCYCHECK（显示策略核查任务进度）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRPLCYCHECK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略核查管理
status: active
---

# DSP SDRPLCYCHECK（显示策略核查任务进度）

## 功能

该命令用于显示全部或者某一条策略核查任务的完成进度。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 策略核查任务ID | 可选必选说明：可选参数<br>参数含义：策略核查任务ID，若不输入该参数，则表示查询所有的策略核查任务。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRPLCYCHECK]] · 策略核查任务进度（SDRPLCYCHECK）

## 使用实例

查询系统中存在的所有策略核查任务的完成进度。

```
%%DSP SDRPLCYCHECK:;%%
            RETCODE = 0  操作成功

            结果如下
            --------
            策略核查任务ID  任务进度  任务优先级  策略类型

            e-1             -         1           内部策略
            e-14            -         1           外部通信策略
            e-15            -         1           外部通信策略
            t-6584          -         2           内部策略
            t-6585          -         2           外部通信策略
            t-6586          -         2           内部策略
            t-6587          -         2           外部通信策略
            t-6588          -         2           内部策略
            (结果个数 = 8)

            ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示策略核查任务进度（DSP-SDRPLCYCHECK）_49379570.md`
