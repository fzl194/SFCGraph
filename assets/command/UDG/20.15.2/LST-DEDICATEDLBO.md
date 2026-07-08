---
id: UDG@20.15.2@MMLCommand@LST DEDICATEDLBO
type: MMLCommand
name: LST DEDICATEDLBO（查询系统是否开启专网UPF动态分流功能）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DEDICATEDLBO
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 动态分流业务控制
- 动态分流功能接入控制
status: active
---

# LST DEDICATEDLBO（查询系统是否开启专网UPF动态分流功能）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查看专网UPF动态分流功能开关状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DEDICATEDLBO]] · 系统是否开启专网UPF动态分流功能（DEDICATEDLBO）

## 使用实例

查看专网UPF动态分流功能开关状态，可以使用该命令：

```
LST DEDICATEDLBO:;
```

```

RETCODE = 0  操作成功。

开关状态
------------------
专网UPF动态分流功能开关  =  使能
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询系统是否开启专网UPF动态分流功能（LST-DEDICATEDLBO）_43025982.md`
