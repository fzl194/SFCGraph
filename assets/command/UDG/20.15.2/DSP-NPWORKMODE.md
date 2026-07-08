---
id: UDG@20.15.2@MMLCommand@DSP NPWORKMODE
type: MMLCommand
name: DSP NPWORKMODE（显示NP工作模式）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPWORKMODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# DSP NPWORKMODE（显示NP工作模式）

## 功能

该命令用于显示NP所在槽号、框号和工作模式。

> **说明**
> 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPWORKMODE]] · NP工作模式（NPWORKMODE）

## 使用实例

显示NP槽号、框号和工作模式：

```
%%DSP NPWORKMODE:;%%
RETCODE = 0  操作成功

结果如下
--------
槽号  框号  NP号  工作模式  

1     0     0     1  
2     0     0     1  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示NP工作模式（DSP-NPWORKMODE）_71503457.md`
