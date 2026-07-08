---
id: UDG@20.15.2@MMLCommand@LST HTTPMSGLOGPARA
type: MMLCommand
name: LST HTTPMSGLOGPARA（查询HTTP消息日志参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPMSGLOGPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP消息日志管理
status: active
---

# LST HTTPMSGLOGPARA（查询HTTP消息日志参数）

## 功能

该命令用于查询HTTP消息日志的参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/HTTPMSGLOGPARA]] · HTTP消息日志参数（HTTPMSGLOGPARA）

## 使用实例

如果想查询HTTP消息日志参数，可以用如下命令：

```
%%LST HTTPMSGLOGPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
  TCP消息日志开关  =  关闭
停止记录的CPU阈值  =  75
恢复记录的CPU阈值  =  65
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTP消息日志参数（LST-HTTPMSGLOGPARA）_06289218.md`
