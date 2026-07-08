---
id: UNC@20.15.2@MMLCommand@LST NONIPFUNC
type: MMLCommand
name: LST NONIPFUNC（查询Non-IP功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NONIPFUNC
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- M2M
- 全局Non-IP配置
status: active
---

# LST NONIPFUNC（查询Non-IP功能配置）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用于查询Non-IP功能相关的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NONIPFUNC]] · Non-IP功能配置（NONIPFUNC）

## 使用实例

显示全局Non-IP功能配置：

```
%%LST NONIPFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
Non-IP功能开关  =  不使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Non-IP功能配置（LST-NONIPFUNC）_28567650.md`
