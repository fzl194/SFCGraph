---
id: UDG@20.15.2@MMLCommand@DSP NPNODE
type: MMLCommand
name: DSP NPNODE（NP状态查询）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPNODE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- FEMF
status: active
---

# DSP NPNODE（NP状态查询）

## 功能

该命令用于查询NP所在槽位号、框号和状态等信息。

> **说明**
> 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NPNODE]] · NP状态查询（NPNODE）

## 使用实例

查询NP槽号、框号和状态等信息：

```
DSP NPNODE:;
RETCODE = 0  操作成功

结果如下
--------
槽号  框号  NP号  状态  NP卡名称  Mesh类型  

7     0     0     正常  NP100     MESH6603  
8     0     0     正常  NP100     MESH6603  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NPNODE.md`
