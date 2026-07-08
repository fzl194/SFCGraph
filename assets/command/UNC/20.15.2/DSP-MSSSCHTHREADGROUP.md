---
id: UNC@20.15.2@MMLCommand@DSP MSSSCHTHREADGROUP
type: MMLCommand
name: DSP MSSSCHTHREADGROUP（查询MSS线程级调度组的维测信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSSCHTHREADGROUP
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

# DSP MSSSCHTHREADGROUP（查询MSS线程级调度组的维测信息）

## 功能

该命令用于查询线程级调度组维测信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示的RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| THREADID | 线程ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示线程的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～255。<br>默认值：无 |
| GROUPID | 调度组ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示调度组的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [MSS线程级调度组的维测信息（MSSSCHTHREADGROUP）](configobject/UNC/20.15.2/MSSSCHTHREADGROUP.md)

## 使用实例

查询线程调度组统计信息：

```
DSP MSSSCHTHREADGROUP:THREADID=1,GROUPID=1,RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
         间隔时间最大/平均值（microsecond）  =  10000/9302
         处理时间最大/平均值（microsecond）  =  100/93
                              空调度率（%）  =  10
                                调度率（%）  =  20
 常驻队列调度间隔最大/平均值（microsecond）  =  10/5
                               常驻队列长度  =  64
                               常驻队列深度  =  10

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MSS线程级调度组的维测信息（DSP-MSSSCHTHREADGROUP）_00840837.md`
