---
id: UNC@20.15.2@MMLCommand@LST LOGCLEANPOLICY
type: MMLCommand
name: LST LOGCLEANPOLICY（查询日志老化策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOGCLEANPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST LOGCLEANPOLICY（查询日志老化策略）

## 功能

本命令用于查询审计日志老化策略。

日志老化策略包括日志存留期和日志占用空间，用于设置系统对日志的最大存留时长和最大占用空间大小。当日志超过最大存留时长或者最大占用空间大小时，系统按照日志产生时间，删除最老的日志。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOGCLEANPOLICY]] · 日志老化策略（LOGCLEANPOLICY）

## 使用实例

查询系统当前的日志老化策略信息：

```
%%LST LOGCLEANPOLICY:;%%
RETCODE = 0  操作成功
 
操作结果如下
------------
    日志存留期（天）  =  365
  日志占用空间（MB）  =  400
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询日志老化策略（LST-LOGCLEANPOLICY）_36328275.md`
