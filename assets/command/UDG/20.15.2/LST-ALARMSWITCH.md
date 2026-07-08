---
id: UDG@20.15.2@MMLCommand@LST ALARMSWITCH
type: MMLCommand
name: LST ALARMSWITCH（查询安全事件告警开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ALARMSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 安全管理
- 安全事件告警管理
status: active
---

# LST ALARMSWITCH（查询安全事件告警开关）

## 功能

此命令用于查询安全事件告警开关状态。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/ALARMSWITCH]] · 安全事件告警开关（ALARMSWITCH）

## 使用实例

查询安全事件告警开关状态：

```
%%LST ALARMSWITCH:;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------
安全事件告警开关  =  关闭 
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询安全事件告警开关（LST-ALARMSWITCH）_42999599.md`
