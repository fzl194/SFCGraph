---
id: UNC@20.15.2@MMLCommand@DSP MSSSCHGRPFIX
type: MMLCommand
name: DSP MSSSCHGRPFIX（查询调度组详细统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSSCHGRPFIX
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 调度统计查询
status: active
---

# DSP MSSSCHGRPFIX（查询调度组详细统计信息）

## 功能

该命令用于查询调度组统计工作组信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| INGROUPID | 输入调度组ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示输入调度组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSSCHGRPFIX]] · 调度组详细统计信息（MSSSCHGRPFIX）

## 使用实例

查询调度组的统计工作组信息：

```
DSP MSSSCHGRPFIX:INGROUPID = 0,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                     端口任务索引   =  0
                         任务类型   =  516
                         调度组ID   =  0
                     优先级队列ID   =  0
                  用户自定义字段0   =  0
                  用户自定义字段1   =  0
                         调度权重   =  50
                     调用剩余权重   =  50
                       调度次数值   =  0
调度间隔最大/平均值（microsecond）  =  0/0
                    任务回调函数    =  ufpTimerClockHighPrecision
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询调度组详细统计信息（DSP-MSSSCHGRPFIX）_50280610.md`
