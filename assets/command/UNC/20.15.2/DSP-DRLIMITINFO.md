---
id: UNC@20.15.2@MMLCommand@DSP DRLIMITINFO
type: MMLCommand
name: DSP DRLIMITINFO（显示已发生的倒换和复位次数和距离限制结束的时间）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DRLIMITINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP DRLIMITINFO（显示已发生的倒换和复位次数和距离限制结束的时间）

## 功能

此命令用于查询由于关键服务故障而引发的复位次数和距离限制结束的时间以及备升主已发生的次数和距离限制结束的时间。

## 注意事项

- 该命令只用于在UEG/UEN/UEG+网元执行。
- 不能简单依据此命令的查询结果判定是否受到限制，需要结合其他配置，如查询521软参的配置、[**LST DRSTBYRSTCTRL**](查询运行备整系统复位开关（LST DRSTBYRSTCTRL）_51001445.md)中配置综合判断 ：

- 以521软参的优先级最高，当521软参设置为1时，忽略是否超过复位限制的次数。当设置为0时，则再以DRSTBYRSTCTRL命令设置为准。
- 以DRSTBYRSTCTRL命令的优先级更高，当设置为“否”时，忽略是否超过复位限制的次数。当设置为“是”时，则再以DRRESETLMTCOUNT命令设置为准。
- 达到复位限制次数后才会显示距离限制复位结束的时间。
- 在负荷分担容灾模式下，倒换次数和距离限制倒换结束的时间显示为NULL。
- 在冷备模式下，倒换限制依照当前时间过去24小时计算，在热备模式下，倒换限制依照每日24小时计算。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DRLIMITINFO]] · 已发生的倒换和复位次数和距离限制结束的时间（DRLIMITINFO）

## 使用实例

显示由于关键服务故障而引发的复位次数和距离限制结束的时间以及备升主已发生的次数和距离限制结束的时间。

```
%%DSP DRLIMITINFO:;%%
RETCODE = 0  操作成功

结果如下
--------
              复位次数  =  0
距离限制复位结束的时间  =  NULL
              倒换次数  =  0
距离限制倒换结束的时间  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示已发生的倒换和复位次数和距离限制结束的时间（DSP-DRLIMITINFO）_42635008.md`
