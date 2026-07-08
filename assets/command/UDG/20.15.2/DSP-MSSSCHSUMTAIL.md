---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHSUMTAIL
type: MMLCommand
name: DSP MSSSCHSUMTAIL（查询调度部署详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHSUMTAIL
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

# DSP MSSSCHSUMTAIL（查询调度部署详细信息）

## 功能

该命令用于查询调度部署详细信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSSCHSUMTAIL]] · 调度部署详细信息（MSSSCHSUMTAIL）

## 使用实例

查询调度模块统计信息：

```
DSP MSSSCHSUMTAIL:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
线程逻辑ID    线程绑定核号    可调度的组数量    输入输出调度任务数    当前调度的调度组号    当前正在调度功能块    任务处理占用CPU比率（%）    维测开关

1             2               1                 2                     0                     NULL                  3                           OFF
2             3               1                 2                     0                     NULL                  4                           OFF
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调度部署详细信息（DSP-MSSSCHSUMTAIL）_00866425.md`
