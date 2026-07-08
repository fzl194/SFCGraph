---
id: UDG@20.15.2@MMLCommand@LST ECOPOLICY
type: MMLCommand
name: LST ECOPOLICY（查询全局的CPU调频和休眠策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ECOPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- CPU节能策略
status: active
---

# LST ECOPOLICY（查询全局的CPU调频和休眠策略）

## 功能

使用CPU节能功能时，通过此命令可以查询全局的调频和休眠策略。

> **说明**
> 此命令仅在虚机场景下支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/ECOPOLICY]] · 全局的CPU调频和休眠策略（ECOPOLICY）

## 使用实例

查询全局CPU节能策略：

```
%%LST ECOPOLICY:;%%
RETCODE = 0  操作成功

结果如下
------------------------
CPU休眠策略 = 深休眠
CPU调频策略 = 开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询全局的CPU调频和休眠策略（LST-ECOPOLICY）_45912120.md`
