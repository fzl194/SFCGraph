---
id: UDG@20.15.2@MMLCommand@DSP MSSCOMMADAPTSERV
type: MMLCommand
name: DSP MSSCOMMADAPTSERV（查询通信服务信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSCOMMADAPTSERV
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

# DSP MSSCOMMADAPTSERV（查询通信服务信息）

## 功能

该命令用于查询通信服务信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| SERVICETYPE | 服务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示服务类型。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～65535。<br>默认值：无 |

## 操作的配置对象

- [通信服务信息（MSSCOMMADAPTSERV）](configobject/UDG/20.15.2/MSSCOMMADAPTSERV.md)

## 使用实例

查询通信服务信息：

```
DSP MSSCOMMADAPTSERV:RUNAME = "VNODE_VNRS_VNFC_IPU_0064",SERVICETYPE = 9;
```

```

RETCODE = 0  操作成功。

结果如下
--------
服务类型使能状态  =  FALSE
        功能块号  =  1065
      初始化函数  =  NULL
    去初始化函数  =  NULL
  定时器处理函数  =  NULL
    报文处理函数  =  NULL
    报文路选函数  =  NULL
    消息处理函数  =  NULL
    消息路选函数  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询通信服务信息（DSP-MSSCOMMADAPTSERV）_00440293.md`
