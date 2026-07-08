---
id: UDG@20.15.2@MMLCommand@DSP MSSADAPTDETAILSERVICE
type: MMLCommand
name: DSP MSSADAPTDETAILSERVICE（查询适配层业务表详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSADAPTDETAILSERVICE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 适配层统计查询
status: active
---

# DSP MSSADAPTDETAILSERVICE（查询适配层业务表详细信息）

## 功能

该命令用于查询适配层业务表详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| TABLENAME | 表名 | 可选必选说明：必选参数<br>参数含义：该参数用于表示表名。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RUNINSTANCEID | 运行实例号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示运行实例号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [适配层业务表详细信息（MSSADAPTDETAILSERVICE）](configobject/UDG/20.15.2/MSSADAPTDETAILSERVICE.md)

## 使用实例

查询适配层业务表详细信息：

```
DSP MSSADAPTDETAILSERVICE:TABLENAME = 1,RUNINSTANCEID=1,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                适配层物理表号  =  65535
              业务定义表有效性  =  FALSE
                业务定义表属性  =  CTL_PROC
        业务定义控制层备份标识  =  FALSE
  业务定义业务运行实例共享标识  =  FALSE
            业务定义物理表类型  =  DEFAULT
          业务定义表的表项规格  =  0
业务定义表项关键字长度（byte）  =  0
  业务定义表项数据长度（byte）  =  0
              业务定义业务类型  =  SERVICE_ALL
            业务创建表创建标识  =  FALSE
              业务创建共享标识  =  FALSE
            业务创建表创建计数  =  0
              业务创建业务表号  =  65535
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询适配层业务表详细信息（DSP-MSSADAPTDETAILSERVICE）_00441421.md`
