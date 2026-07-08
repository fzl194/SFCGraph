---
id: UNC@20.15.2@MMLCommand@DSP CDRQUERYSTATUS
type: MMLCommand
name: DSP CDRQUERYSTATUS（查询话单查询任务状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CDRQUERYSTATUS
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务系统管理
- 话单查询
status: active
---

# DSP CDRQUERYSTATUS（查询话单查询任务状态）

## 功能

**适用NF：NCG**

该命令用于查询指定话单查询任务的状态。

## 注意事项

- 在网管上执行该命令时，只支持相同版本（包括补丁号）的NCG并行查询，不支持多版本并行查询。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 查询任务标识 | 可选必选说明：可选参数<br>参数含义：该参数用来表示查询任务标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：<br>- 输入为空时，查询当前所有话单查询任务的状态。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRQUERYSTATUS]] · 话单查询任务状态（CDRQUERYSTATUS）

## 使用实例

查询“查询任务标识”为“task”的话单查询任务的状态。示例如下：

```
DSP CDRQUERYSTATUS: TASKID="task";
```

```
RETCODE = 0  操作成功
结果如下:
---------
    查询任务标识  =  task
    任务启动时间  =  2022-08-04 16:00:00
    任务结束时间  =  2022-08-04 17:00:00
       进度（%）  =  100
        补充信息  =  查询成功
存在查询结果文件  =  是
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CDRQUERYSTATUS.md`
