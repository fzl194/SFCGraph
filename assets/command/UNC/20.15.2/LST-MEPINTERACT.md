---
id: UNC@20.15.2@MMLCommand@LST MEPINTERACT
type: MMLCommand
name: LST MEPINTERACT（查询MEP_SMF联动功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MEPINTERACT
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- SMF公共配置
- MEP_SMF联动功能开关
status: active
---

# LST MEPINTERACT（查询MEP_SMF联动功能开关）

## 功能

**适用NF：SMF**

该参数用于查看MEP_SMF联动功能开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [MEP_SMF联动功能开关（MEPINTERACT）](configobject/UNC/20.15.2/MEPINTERACT.md)

## 使用实例

该命令用来查看当前MEP_SMF联动控制开关。 LST MEPINTERACT:;

```
%%LST MEPINTERACT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
功能开关  =  使能
(结果个数 = 1)

----    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MEP_SMF联动功能开关（LST-MEPINTERACT）_09652273.md`
