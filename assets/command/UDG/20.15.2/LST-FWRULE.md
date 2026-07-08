---
id: UDG@20.15.2@MMLCommand@LST FWRULE
type: MMLCommand
name: LST FWRULE（查询转发规则）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FWRULE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# LST FWRULE（查询转发规则）

## 功能

此命令用于查询已配置的转发规则。

> **说明**
> 无。

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/FWRULE]] · 转发规则（FWRULE）

## 使用实例

查询转发规则：

```
%%LST FWRULE:;%%
RETCODE = 0  操作成功

操作结果如下
------------
目的IP         端口   目的端口

192.168.1.1    22       2222
192.168.1.2    22       2222
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询转发规则（LST-FWRULE）_02004268.md`
