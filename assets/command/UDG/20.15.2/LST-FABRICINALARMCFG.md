---
id: UDG@20.15.2@MMLCommand@LST FABRICINALARMCFG
type: MMLCommand
name: LST FABRICINALARMCFG（查询PAE告警配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FABRICINALARMCFG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# LST FABRICINALARMCFG（查询PAE告警配置）

## 功能

该命令用于查询多框级联的情况下PAE的Fabric平面不可达告警的屏蔽配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [PAE告警配置（FABRICINALARMCFG）](configobject/UDG/20.15.2/FABRICINALARMCFG.md)

## 使用实例

查询PAE的Fabric平面不可达告警配置：

```
%%LST FABRICINALARMCFG:;%%
RETCODE = 0  操作成功

结果如下:
---------
屏蔽告警标记  =  否
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询PAE告警配置（LST-FABRICINALARMCFG）_38263899.md`
