---
id: UNC@20.15.2@MMLCommand@LST ACCESSLISTFUNC
type: MMLCommand
name: LST ACCESSLISTFUNC（查询接入控制名单功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ACCESSLISTFUNC
command_category: 查询类
applicable_nf:
- GGSN
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 黑白名单控制
status: active
---

# LST ACCESSLISTFUNC（查询接入控制名单功能）

## 功能

**适用NF：GGSN、SGW-C、PGW-C**

该命令用来查询接入控制名单功能。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ACCESSLISTFUNC]] · 接入控制名单功能（ACCESSLISTFUNC）

## 使用实例

显示接入控制名单功能：

```
LST ACCESSLISTFUNC
RETCODE = 0  操作成功。

结果如下
--------
设置系统是否支持接入控制名单的功能  =  使能
                      黑白名单类型  =  白名单
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ACCESSLISTFUNC.md`
