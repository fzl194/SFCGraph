---
id: UDG@20.15.2@MMLCommand@DSP MSSCNTINFOBRI
type: MMLCommand
name: DSP MSSCNTINFOBRI（查询简要计数器信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSCNTINFOBRI
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- 计数器统计查询
status: active
---

# DSP MSSCNTINFOBRI（查询简要计数器信息）

## 功能

该命令用于查询简要计数器信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [简要计数器信息（MSSCNTINFOBRI）](configobject/UDG/20.15.2/MSSCNTINFOBRI.md)

## 使用实例

查询简要计数器信息：

```
DSP MSSCNTINFOBRI:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
--------
计数器组ID    计数器ID    计数器类型           计数器值0    计数器值1

0             0           ATOMIC_COUNTER_64    0            NULL
0             1           ATOMIC_COUNTER_64    0            NULL
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询简要计数器信息（DSP-MSSCNTINFOBRI）_50280914.md`
