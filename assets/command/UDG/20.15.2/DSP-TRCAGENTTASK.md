---
id: UDG@20.15.2@MMLCommand@DSP TRCAGENTTASK
type: MMLCommand
name: DSP TRCAGENTTASK（显示跟踪代理侧跟踪任务信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TRCAGENTTASK
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 跟踪管理调测
status: active
---

# DSP TRCAGENTTASK（显示跟踪代理侧跟踪任务信息）

## 功能

该命令用于显示跟踪代理侧跟踪任务信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程ID | 可选必选说明：必选参数<br>参数含义：进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| TRACETASKID | 跟踪任务号 | 可选必选说明：可选参数<br>参数含义：跟踪任务号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [跟踪代理侧跟踪任务信息（TRCAGENTTASK）](configobject/UDG/20.15.2/TRCAGENTTASK.md)

## 使用实例

显示跟踪代理侧跟踪任务信息：

```
DSP TRCAGENTTASK:PROCESSID=1003
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
--------
跟踪任务号    跟踪业务类型    组合条件

1             512             1       
2             512             1       
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示跟踪代理侧跟踪任务信息（DSP-TRCAGENTTASK）_59104041.md`
