---
id: UDG@20.15.2@MMLCommand@LST DRSTBYRSTCTRL
type: MMLCommand
name: LST DRSTBYRSTCTRL（查询运行备整系统复位开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DRSTBYRSTCTRL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRSTBYRSTCTRL（查询运行备整系统复位开关）

## 功能

该命令用于查询容灾实例在检测到关键服务异常或者周边网元故障时是否需要复位。

> **说明**
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 主容灾实例和备容灾实例都可以下发该命令，但只有备容灾实例生效。可使用[**DSP DRGROUPSTATUS**](显示容灾组的运行状态信息（DSP DRGROUPSTATUS）_74554621.md)命令中"RUNNINGSTATUS"查询到本容灾实例是运行主还是运行备。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DRSTBYRSTCTRL]] · 运行备整系统复位开关（DRSTBYRSTCTRL）

## 使用实例

查询运行备整系统复位开关:

```
LST DRSTBYRSTCTRL:;
RETCODE = 0  操作成功

结果如下
--------
运行备整系统复位控制  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-DRSTBYRSTCTRL.md`
