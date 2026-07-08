---
id: UNC@20.15.2@MMLCommand@LST RESCHKSWITCH
type: MMLCommand
name: LST RESCHKSWITCH（查询RCF核查开关状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESCHKSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- RCF管理
status: active
---

# LST RESCHKSWITCH（查询RCF核查开关状态）

## 功能

该命令用于查询RCF核查开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [RCF核查开关状态（RESCHKSWITCH）](configobject/UNC/20.15.2/RESCHKSWITCH.md)

## 使用实例

查询RCF核查开关状态。

```
%%LST RESCHKSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
RCF核查开关  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询RCF核查开关状态（LST-RESCHKSWITCH）_56594041.md`
