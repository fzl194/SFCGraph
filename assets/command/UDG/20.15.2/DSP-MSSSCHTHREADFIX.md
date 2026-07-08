---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHTHREADFIX
type: MMLCommand
name: DSP MSSSCHTHREADFIX（查询调度工作线程信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHTHREADFIX
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

# DSP MSSSCHTHREADFIX（查询调度工作线程信息）

## 功能

该命令用于查询调度工作线程信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSSCHTHREADFIX]] · 调度工作线程信息（MSSSCHTHREADFIX）

## 使用实例

查询调度工作线程信息：

```
DSP MSSSCHTHREADFIX:THREADID = 1,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
端口任务索引    任务类型    调度组ID    优先级队列ID    用户自定义字段0    用户自定义字段1    调度权重    调用剩余权重    任务回调函数

0               50          0           0               0                  0                  50          27              PAE_DP_RunSch
1               50          0           0               1                  0                  50          27              PAE_DP_RunSch
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-MSSSCHTHREADFIX.md`
