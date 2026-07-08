---
id: UNC@20.15.2@MMLCommand@LST SMAMEVTEXPPLY
type: MMLCommand
name: LST SMAMEVTEXPPLY（查询SMF向AMF下发事件订阅时的老化策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMAMEVTEXPPLY
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 位置上报管理
- 老化时间管理
status: active
---

# LST SMAMEVTEXPPLY（查询SMF向AMF下发事件订阅时的老化策略）

## 功能

**适用NF：SMF**

该命令用于查询SMF向AMF下发事件订阅时的老化策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [SMF向AMF下发事件订阅时的老化策略（SMAMEVTEXPPLY）](configobject/UNC/20.15.2/SMAMEVTEXPPLY.md)

## 使用实例

查询SMF向AMF下发事件订阅时的老化策略：

```
%%LST SMAMEVTEXPPLY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
 下发老化时间开关 =  使能
老化时间时长(min) =  1440
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SMF向AMF下发事件订阅时的老化策略（LST-SMAMEVTEXPPLY）_77579560.md`
