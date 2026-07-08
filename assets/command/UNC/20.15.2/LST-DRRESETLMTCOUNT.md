---
id: UNC@20.15.2@MMLCommand@LST DRRESETLMTCOUNT
type: MMLCommand
name: LST DRRESETLMTCOUNT（查询复位限制的次数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DRRESETLMTCOUNT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST DRRESETLMTCOUNT（查询复位限制的次数）

## 功能

此命令用于查询配置的在24小时内整系统复位的最大次数：

- 在负荷分担容灾模式下，显示由于关键服务故障或者周边网元故障引发的整系统复位的次数。
- 在冷备容灾模式下，显示运行主由于关键服务故障或周边网元故障叠加通道异常时引发的整系统复位的次数，以及限制运行备由于关键服务故障或周边网元故障引发的整系统复位的次数。
- 在热备容灾模式下，显示运行备由于关键服务故障引发的整系统复位的次数。

## 注意事项

该命令只用于在UEG/UEN/UEG+网元执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [复位限制的次数（DRRESETLMTCOUNT）](configobject/UNC/20.15.2/DRRESETLMTCOUNT.md)

## 使用实例

查询配置的在24小时内由于关键服务故障引发的整系统复位的最大次数。

```
%%LST DRRESETLMTCOUNT:;%%
RETCODE = 0  操作成功

结果如下
--------
  复位限制的次数  =  3
刷新保护期(分钟)  =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询复位限制的次数（LST-DRRESETLMTCOUNT）_42155864.md`
