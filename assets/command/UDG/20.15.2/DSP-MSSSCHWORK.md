---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHWORK
type: MMLCommand
name: DSP MSSSCHWORK（查询调度工作类型信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHWORK
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

# DSP MSSSCHWORK（查询调度工作类型信息）

## 功能

该命令用于查询调度工作类型信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| GROUPID | 调度组ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示调度组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| QOSID | 队列ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示队列ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [调度工作类型信息（MSSSCHWORK）](configobject/UDG/20.15.2/MSSSCHWORK.md)

## 使用实例

查询调度工作类型线程信息：

```
DSP MSSSCHWORK:THREADID = 1,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
任务类型    任务调度次数    任务调度间隔最大/平均值（microsecond）    任务处理时间最大/平均值（microsecond）    任务回调注册次数    添加任务计数   获取任务计数   添加任务失败计数    任务处理占用CPU比率（%）    任务回调函数名

50          73673           1273                                      87                                        1                   --             0              --                  98                          PAE_DP_RunSch
514         32              599810                                    180                                       1                   --             0              --                  1                           ufpTimerWorkCallback
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调度工作类型信息（DSP-MSSSCHWORK）_50121738.md`
