---
id: UDG@20.15.2@MMLCommand@LST HIGHRISKPERIOD
type: MMLCommand
name: LST HIGHRISKPERIOD（查询高危时间段提示状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HIGHRISKPERIOD
command_category: 查询类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 高危时间段状态管理
status: active
---

# LST HIGHRISKPERIOD（查询高危时间段提示状态）

## 功能

该命令用于查询高危时间段提示状态、高危时间段和高危命令提示信息。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@HIGHRISKPERIOD]] · 高危时间段提示状态（HIGHRISKPERIOD）

## 使用实例

查询高危时间段提示状态：

```
%%LST HIGHRISKPERIOD:;%% 
RETCODE = 0  操作成功

操作结果如下 
------------ 
高危时间段提示状态  =  开启           
          起始时间  =  09:36           
          结束时间  =  23:36           
          提示信息  =  SFWEFGSDF 
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-HIGHRISKPERIOD.md`
