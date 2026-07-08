---
id: UDG@20.15.2@MMLCommand@LST COLOCATEDLBO
type: MMLCommand
name: LST COLOCATEDLBO（显示本地分流共部署参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: COLOCATEDLBO
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 共部署的本地分流开关
status: active
---

# LST COLOCATEDLBO（显示本地分流共部署参数）

## 功能

**适用NF：UPF**

该命令用于查询共部署的本地分流参数。

## 注意事项

该命令执行后只对之后发生承载更新的用户或者新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/COLOCATEDLBO]] · 本地分流共部署参数（COLOCATEDLBO）

## 使用实例

查询共部署的本地分流参数：

```
LST COLOCATEDLBO:;
```

```

RETCODE = 0  操作成功。

共部署LBO开关
------------------------
ULCL功能开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-COLOCATEDLBO.md`
