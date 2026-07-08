---
id: UNC@20.15.2@MMLCommand@LST OLNCHGPARA
type: MMLCommand
name: LST OLNCHGPARA（显示在线计费全局参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OLNCHGPARA
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 在线计费参数管理
- 在线计费参数
status: active
---

# LST OLNCHGPARA（显示在线计费全局参数配置）

## 功能

**适用NF：PGW-C、SMF**

该命令用于显示在线计费参数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/OLNCHGPARA]] · 在线计费全局参数配置（OLNCHGPARA）

## 使用实例

查看当前配置：

```
LST OLNCHGPARA:;
```

```

RETCODE = 0  操作成功

在线计费全局参数配置
--------------------
Reporting Level为SID时的配额申请方式  =  按RG申请配额
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OLNCHGPARA.md`
