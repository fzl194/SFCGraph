---
id: UDG@20.15.2@MMLCommand@LST DCSLIVEPARAS
type: MMLCommand
name: LST DCSLIVEPARAS（查询DCS直播参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DCSLIVEPARAS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- MML命令
- 系统资源配置
status: active
---

# LST DCSLIVEPARAS（查询DCS直播参数）

## 功能

该命令用于查询DCS直播参数。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [DCS直播参数（DCSLIVEPARAS）](configobject/UDG/20.15.2/DCSLIVEPARAS.md)

## 使用实例

查询DCS直播参数。

```
%%LST DCSLIVEPARAS:;%%
RETCODE = 0  操作成功

操作结果如下：
------------------------
       读滞后阈值（MB） =  3
     回源超时阈值（ms） =  200
  回源超时检查周期（s） =  30
订阅关系核查周期（Min） =  30
  直播资源老化周期（s） =  30
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询DCS直播参数（LST-DCSLIVEPARAS）_76289642.md`
