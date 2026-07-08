---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHTHRDLOAD
type: MMLCommand
name: DSP MSSSCHTHRDLOAD（查询调度线程负载信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHTHRDLOAD
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

# DSP MSSSCHTHRDLOAD（查询调度线程负载信息）

## 功能

该命令用于查询调度线程负载信息。

调度线程负载信息统计默认是关闭的，当统计关闭时，查询信息无回显。

例如，当发现某个线程的负载不符合预期时，可打开统计开关，然后执行该命令查询线程的负载统计，查看具体是哪一种业务的负载统计不符合预期。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称，执行DSP RU查看RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |

## 操作的配置对象

- [调度线程负载信息（MSSSCHTHRDLOAD）](configobject/UDG/20.15.2/MSSSCHTHRDLOAD.md)

## 使用实例

查询调度线程的负载信息：

```
DSP MSSSCHTHRDLOAD:THREADID=1,RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
索引   负载次数    空载次数    负载占比（%）    函数名称

1      3412        2310        30               PAE_DP_RunSch
2      2141        1012        20               PAE_DP_RunProc
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调度线程负载信息（DSP-MSSSCHTHRDLOAD）_49962094.md`
