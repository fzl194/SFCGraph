---
id: UDG@20.15.2@MMLCommand@DSP FOOLPROOFSWITCH
type: MMLCommand
name: DSP FOOLPROOFSWITCH（显示防呆开关状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: FOOLPROOFSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 一键式部署
status: active
---

# DSP FOOLPROOFSWITCH（显示防呆开关状态）

## 功能

该命令用于显示防呆开关状态。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@FOOLPROOFSWITCH]] · 防呆开关状态（FOOLPROOFSWITCH）

## 使用实例

假如操作员想了解防呆开关的当前状态，可以调用以下命令显示所有防呆开关的状态。

```
%%DSP FOOLPROOFSWITCH:;%%
RETCODE = 0  操作成功

结果如下
--------
名称  =  ONECLICKDEPLOY
状态  =  打开
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-FOOLPROOFSWITCH.md`
