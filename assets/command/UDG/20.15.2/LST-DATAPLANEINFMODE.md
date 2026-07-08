---
id: UDG@20.15.2@MMLCommand@LST DATAPLANEINFMODE
type: MMLCommand
name: LST DATAPLANEINFMODE（查询数据面接口模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DATAPLANEINFMODE
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 数据转发控制
- 入不转板总开关
status: active
---

# LST DATAPLANEINFMODE（查询数据面接口模式）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看用户面IP模式配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/DATAPLANEINFMODE]] · 数据面接口模式（DATAPLANEINFMODE）

## 使用实例

查看当前配置的用户面IP模式配置，可以使用该命令：

```
LST DATAPLANEINFMODE:;
```

```

RETCODE = 0  操作成功。

用户面IP模式配置
------------------
            模式  =  Instance
路由增强功能开关  =  DISABLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询数据面接口模式（LST-DATAPLANEINFMODE）_07148234.md`
