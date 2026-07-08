---
id: UNC@20.15.2@MMLCommand@DSP MSSSCHGRPHEAD
type: MMLCommand
name: DSP MSSSCHGRPHEAD（查询调度组统计概要信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSSCHGRPHEAD
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

# DSP MSSSCHGRPHEAD（查询调度组统计概要信息）

## 功能

该命令用于查询调度组统计概要信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| INGROUPID | 调度组ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示调度组ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |

## 操作的配置对象

- [调度组统计概要信息（MSSSCHGRPHEAD）](configobject/UNC/20.15.2/MSSSCHGRPHEAD.md)

## 使用实例

查询调度组概要信息：

```
DSP MSSSCHGRPHEAD:INGROUPID = 0,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
        调度组状态  =  used
        调度组类型  =  io type
          队列个数  =  1
调度组绑定线程个数  =  2
  调度组绑定线程号  =  1 2
  端口调度任务个数  =  2
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询调度组统计概要信息（DSP-MSSSCHGRPHEAD）_00441525.md`
