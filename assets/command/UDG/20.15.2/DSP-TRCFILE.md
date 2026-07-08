---
id: UDG@20.15.2@MMLCommand@DSP TRCFILE
type: MMLCommand
name: DSP TRCFILE（显示跟踪文件）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: TRCFILE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 跟踪管理
status: active
---

# DSP TRCFILE（显示跟踪文件）

## 功能

该命令用于显示网元跟踪文件信息。创建上报方式为文件类型的跟踪任务，达到文件生成周期之后，可通过该命令获取跟踪文件信息。上报方式为消息上报类型的跟踪任务，通过该命令获取不到跟踪文件信息。上报类型和文件生成周期均可通过命令DSP TRCTASK获取。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRACETASKID | 跟踪任务号 | 可选必选说明：可选参数<br>参数含义：跟踪任务ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TRCFILE]] · 跟踪文件（TRCFILE）

## 使用实例

显示跟踪任务号为1的跟踪任务生成的跟踪文件信息，可通过如下命令显示：

```
DSP TRCFILE: TRACETASKID=1
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
  跟踪任务号  =  1
跟踪文件名称  =  home:/trace/1_11008_20160103_142029_0.tmf
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示跟踪文件（DSP-TRCFILE）_59103379.md`
