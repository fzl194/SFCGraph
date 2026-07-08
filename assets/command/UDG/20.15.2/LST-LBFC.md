---
id: UDG@20.15.2@MMLCommand@LST LBFC
type: MMLCommand
name: LST LBFC（查询流控开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LBFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSLB功能管理
- 操作维护
- 系统调测
- 流控参数
status: active
---

# LST LBFC（查询流控开关）

## 功能

该命令用于查询流控开关状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [流控开关（LBFC）](configobject/UDG/20.15.2/LBFC.md)

## 使用实例

查询流控开关状态。

LST LBFC:;

```
%%LST LBFC:;%%
RETCODE = 0  操作成功 

结果如下:
-------------------------
 流控开关  =  关闭
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询流控开关（LST-LBFC）_29627127.md`
