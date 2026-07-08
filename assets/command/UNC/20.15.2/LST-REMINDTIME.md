---
id: UNC@20.15.2@MMLCommand@LST REMINDTIME
type: MMLCommand
name: LST REMINDTIME（查询证书到期提醒时间）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: REMINDTIME
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 证书维护
status: active
---

# LST REMINDTIME（查询证书到期提醒时间）

## 功能

本命令用于查询系统内所有证书到期提醒时间。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/REMINDTIME]] · 证书到期提醒时间（REMINDTIME）

## 使用实例

查询证书到期提醒时间。

```
%%LST REMINDTIME:;%% 
RETCODE = 0  操作成功

操作结果如下
------------ 
证书到期提醒时间（天） =  44 
(结果个数 = 1)

  ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询证书到期提醒时间（LST-REMINDTIME）_92173706.md`
