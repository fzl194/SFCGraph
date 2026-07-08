---
id: UDG@20.15.2@MMLCommand@LST SFETRACEQUEFC
type: MMLCommand
name: LST SFETRACEQUEFC（查询VNRS IP消息跟踪的队列流控配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SFETRACEQUEFC
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 跟踪管理
status: active
---

# LST SFETRACEQUEFC（查询VNRS IP消息跟踪的队列流控配置）

## 功能

该命令用来查询VNRS IP消息跟踪的队列流控配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFETRACEQUEFC]] · VNRS IP消息跟踪的队列流控配置（SFETRACEQUEFC）

## 使用实例

查询VNRS IP消息跟踪的队列流控配置：

```
LST SFETRACEQUEFC:;
```

```
RETCODE = 0  操作成功

结果如下
------------------------
       队列流控使能开关  =  是
          起控阈值（%）  =  70
   队列流控自动恢复开关  =  是
          恢复阈值（%）  =  30
自动恢复检测时间（min）  =  5
(结果个数 = 1) 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SFETRACEQUEFC.md`
