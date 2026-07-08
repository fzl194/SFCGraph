---
id: UDG@20.15.2@MMLCommand@DSP MSSSCHSUMHEAD
type: MMLCommand
name: DSP MSSSCHSUMHEAD（查询调度部署概要信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: MSSSCHSUMHEAD
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

# DSP MSSSCHSUMHEAD（查询调度部署概要信息）

## 功能

该命令用于查询调度部署概要信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/MSSSCHSUMHEAD]] · 调度部署概要信息（MSSSCHSUMHEAD）

## 使用实例

查询调度模块概要统计信息：

```
DSP MSSSCHSUMHEAD:RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。
结果如下
--------
            线程个数  =  2
        调度组最大值  =  32
      调度组使用个数  =  1
        优先级最大值  =  8
  调度任务队列最大值  =  512
调度任务队列已用个数  =  1
      调度组位图偏移  =  4
          调度组掩码  =  31
  优先级队列位图偏移  =  4
      优先级队列掩码  =  15
      CPU频率（MHz）  =  2899
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询调度部署概要信息（DSP-MSSSCHSUMHEAD）_50120590.md`
