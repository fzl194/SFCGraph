---
id: UNC@20.15.2@MMLCommand@LST LIMITMBSWITCH
type: MMLCommand
name: LST LIMITMBSWITCH（查询有界邮箱开关配置状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LIMITMBSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 邮箱配置
status: active
---

# LST LIMITMBSWITCH（查询有界邮箱开关配置状态）

## 功能

该命令用于查询有界邮箱开关配置状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/LIMITMBSWITCH]] · 有界邮箱开关配置状态（LIMITMBSWITCH）

## 使用实例

查询有界邮箱开关配置。

```
%%LST LIMITMBSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
有界邮箱开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LIMITMBSWITCH.md`
