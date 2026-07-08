---
id: UNC@20.15.2@MMLCommand@LST CREDITPOOLFUNC
type: MMLCommand
name: LST CREDITPOOLFUNC（查询Credit Pooling功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CREDITPOOLFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- 信用池功能控制
status: active
---

# LST CREDITPOOLFUNC（查询Credit Pooling功能）

## 功能

**适用NF：PGW-C、GGSN**

该命令用以查询配置的Credit Pooling功能参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/CREDITPOOLFUNC]] · Credit Pooling功能（CREDITPOOLFUNC）

## 使用实例

查询配置的Credit Pooling特性功能参数，执行如下命令：

```
%%LST CREDITPOOLFUNC:;%%
RETCODE = 0  操作成功
结果如下
------------------------
          Credit Pooling功能开关 = DISABLE  
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Credit-Pooling功能（LST-CREDITPOOLFUNC）_75240938.md`
