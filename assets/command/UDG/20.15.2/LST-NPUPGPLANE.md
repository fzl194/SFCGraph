---
id: UDG@20.15.2@MMLCommand@LST NPUPGPLANE
type: MMLCommand
name: LST NPUPGPLANE（查询NP升级平面）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPUPGPLANE
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP升级管理
- NP平面管理
status: active
---

# LST NPUPGPLANE（查询NP升级平面）

## 功能

该命令用来查询NP升级平面。

## 注意事项

- 该命令执行后立即生效。
- 该命令仅适用于NP卡省交换组网模式。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPUPGPLANE]] · NP升级平面（NPUPGPLANE）

## 使用实例

查询NP升级平面：

```
%%LST NPUPGPLANE:;%%
RETCODE = 0  操作成功

结果如下
--------
RU编号  平面编号  

66      plane_1   
87      plane_2   
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NP升级平面（LST-NPUPGPLANE）_43297437.md`
