---
id: UNC@20.15.2@MMLCommand@LST GTPCINTF
type: MMLCommand
name: LST GTPCINTF（查询GTP-C接口信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPCINTF
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C接口信息管理
status: active
---

# LST GTPCINTF（查询GTP-C接口信息）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C接口信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPCINTF]] · GTP-C接口信息（GTPCINTF）

## 使用实例

查询GTP-C接口信息。

```
%%LST GTPCINTF:;%%
RETCODE = 0  操作成功

结果如下
--------
接口类型     组号  

S11接口      0     
N26接口      3     
S5-S接口     1     
S5-P/GN接口  2     
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C接口信息（LST-GTPCINTF）_09652563.md`
