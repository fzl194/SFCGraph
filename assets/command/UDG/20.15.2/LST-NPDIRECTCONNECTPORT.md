---
id: UDG@20.15.2@MMLCommand@LST NPDIRECTCONNECTPORT
type: MMLCommand
name: LST NPDIRECTCONNECTPORT（查询多框级联配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NPDIRECTCONNECTPORT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# LST NPDIRECTCONNECTPORT（查询多框级联配置）

## 功能

查询多框级联配置。

> **说明**
> 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPDIRECTCONNECTPORT]] · 多框级联配置（NPDIRECTCONNECTPORT）

## 使用实例

查询多框级联配置：

```
LST NPDIRECTCONNECTPORT:;
RETCODE = 0  操作成功

结果如下
--------
框号  槽位号  端口号  

0     1       P1      
1     1       P1      
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NPDIRECTCONNECTPORT.md`
