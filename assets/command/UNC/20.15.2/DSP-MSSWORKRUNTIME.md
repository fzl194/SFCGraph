---
id: UNC@20.15.2@MMLCommand@DSP MSSWORKRUNTIME
type: MMLCommand
name: DSP MSSWORKRUNTIME（查询Work运行时间信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSWORKRUNTIME
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

# DSP MSSWORKRUNTIME（查询Work运行时间信息）

## 功能

该命令用于查询Work的运行时间信息。

通过统计特定规则的Work的运行信息，进行故障诊断。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示线程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MSSWORKRUNTIME]] · Work运行时间信息（MSSWORKRUNTIME）

## 使用实例

查询目前为止统计的Work运行时间信息：

```
DSP MSSWORKRUNTIME:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
Work序列号 Work类型     组ID       权重   调度类型         第一个参数         第二个参数    线程ID       起始时间（ms）     完成时间（ms）

1          50           1          0      静态调度类型     0                  0             1            40553173           40553173
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSWORKRUNTIME.md`
