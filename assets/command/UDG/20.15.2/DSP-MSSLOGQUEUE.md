---
id: UDG@20.15.2@MMLCommand@DSP MSSLOGQUEUE
type: MMLCommand
name: DSP MSSLOGQUEUE（查询日志队列详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSLOGQUEUE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 日志信息查询
status: active
---

# DSP MSSLOGQUEUE（查询日志队列详细信息）

## 功能

该命令用于查询日志队列详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| QUEUEID | 队列号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示队列号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSLOGQUEUE]] · 日志队列详细信息（MSSLOGQUEUE）

## 使用实例

查询日志队列详细信息：

```
DSP MSSLOGQUEUE:QUEUEID=1,RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                           队列号  =  1
                         使用标识  =  TRUE
                       队列总深度  =  1024
                 队列已使用单元数  =  100
                   队列空闲单元数  =  924
                         内存池号  =  1
              内存单元大小（byte） =  8
                 内存单元使用个数  =  10
                 内存单元空闲个数  =  118
               每周期存储日志条数  =  1024
      每周期日志任务休眠时间（ms） =  20
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询日志队列详细信息（DSP-MSSLOGQUEUE）_00440917.md`
