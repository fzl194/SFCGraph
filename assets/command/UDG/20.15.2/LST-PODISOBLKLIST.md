---
id: UDG@20.15.2@MMLCommand@LST PODISOBLKLIST
type: MMLCommand
name: LST PODISOBLKLIST（查询Pod隔离黑名单）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PODISOBLKLIST
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# LST PODISOBLKLIST（查询Pod隔离黑名单）

## 功能

该命令用于查询Pod隔离黑名单。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@PODISOBLKLIST]] · Pod隔离黑名单（PODISOBLKLIST）

## 使用实例

查询Pod隔离黑名单。

```
%%LST PODISOBLKLIST:;%%
RETCODE = 0  操作成功

结果如下
--------
Pod类型   =  sbim-pod
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PODISOBLKLIST.md`
