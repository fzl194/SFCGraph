---
id: UDG@20.15.2@MMLCommand@LST CSLOGLEVEL
type: MMLCommand
name: LST CSLOGLEVEL（查询日志输出级别）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CSLOGLEVEL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 日志管理
status: active
---

# LST CSLOGLEVEL（查询日志输出级别）

## 功能

此命令用于查询日志输出级别。

> **说明**
> 该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@CSLOGLEVEL]] · 更新日志输出级别（CSLOGLEVEL）

## 使用实例

查询日志输出级别：

```
%%LST CSLOGLEVEL:;%%
RETCODE = 0  操作成功

结果如下
--------
日志级别  =  调试级别
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-CSLOGLEVEL.md`
