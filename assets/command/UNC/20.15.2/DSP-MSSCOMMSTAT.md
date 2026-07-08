---
id: UNC@20.15.2@MMLCommand@DSP MSSCOMMSTAT
type: MMLCommand
name: DSP MSSCOMMSTAT（查询通信模块规则匹配统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSCOMMSTAT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 通信管理统计查询
status: active
---

# DSP MSSCOMMSTAT（查询通信模块规则匹配统计信息）

## 功能

该命令用于查询COMM规则匹配统计计数信息。

COMM消息、报文的正常流程或者异常流程的规则匹配开关默认关闭，当开关关闭时，查询信息无统计计数。

例如，当发现丢包时，可打开规则匹配开关，并设置匹配规则，然后执行该命令查询COMM规则匹配统计计数，判断是否是COMM丢包。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称，执行DSP RU查看RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSCOMMSTAT]] · 通信模块规则匹配统计信息（MSSCOMMSTAT）

## 使用实例

查询规则匹配统计信息：

```
DSP MSSCOMMSTAT:RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
服务类型    状态     绑定规则ID    源线程ID    目的功能块ID    目的实例ID    记录时间（s）    匹配个数    回调方式通信匹配计数    功能块方式通信匹配计数    实例间队列方式通信匹配计数    工作队列方式通信匹配计数

正常报文    close    NULL          NULL        NULL            NULL          NULL             NULL        NULL                    NULL                      NULL                          NULL
丢弃报文    close    NULL          NULL        NULL            NULL          NULL             NULL        NULL                    NULL                      NULL                          NULL
正常消息    close    NULL          NULL        NULL            NULL          NULL             NULL        NULL                    NULL                      NULL                          NULL
丢弃消息    close    NULL          NULL        NULL            NULL          NULL             NULL        NULL                    NULL                      NULL                          NULL
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MSSCOMMSTAT.md`
