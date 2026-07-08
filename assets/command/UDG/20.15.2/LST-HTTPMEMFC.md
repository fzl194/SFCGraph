---
id: UDG@20.15.2@MMLCommand@LST HTTPMEMFC
type: MMLCommand
name: LST HTTPMEMFC（查询HTTP内存流控）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPMEMFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP内存流控管理
status: active
---

# LST HTTPMEMFC（查询HTTP内存流控）

## 功能

查询HTTP Body内存分区的内存流控配置。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPMEMFC]] · HTTP内存流控（HTTPMEMFC）

## 使用实例

如果想查询HTTP内存流控配置，可以用如下命令：

```
%%LST HTTPCONF:;%%
RETCODE = 0  操作成功

结果如下
--------
                内存流控开关  =  TRUE
            内存流控起控阈值  =  30
            内存流控停控阈值  =  50
            内存流控大包阈值  =  512
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP内存流控（LST-HTTPMEMFC）_01544146.md`
