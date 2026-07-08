---
id: UDG@20.15.2@MMLCommand@LST UPFSTARTPARA
type: MMLCommand
name: LST UPFSTARTPARA（查询UPF系统开工流程消息的参数）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPFSTARTPARA
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- PFCP参数管理
- UP系统开工参数
status: active
---

# LST UPFSTARTPARA（查询UPF系统开工流程消息的参数）

## 功能

**适用NF：UPF**

该命令用来查看系统开工流程消息的相关属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPFSTARTPARA]] · UPF系统开工流程消息的参数（UPFSTARTPARA）

## 使用实例

查询系统开工流程消息的相关属性：

```
LST UPFSTARTPARA:;
```

```

RETCODE = 0  Operation Success.

UPF start procedure message configuration is
--------------------------------------------
Start Procedure Interval  =  80
(Number of results = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPFSTARTPARA.md`
