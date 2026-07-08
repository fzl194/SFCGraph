---
id: UNC@20.15.2@MMLCommand@LST SCTPBUFFCFG
type: MMLCommand
name: LST SCTPBUFFCFG（查询SCTP缓冲区参数源）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPBUFFCFG
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# LST SCTPBUFFCFG（查询SCTP缓冲区参数源）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于查询系统在为SCTP分配缓冲区时使用的参数来源。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [SCTP缓冲区参数源（SCTPBUFFCFG）](configobject/UNC/20.15.2/SCTPBUFFCFG.md)

## 使用实例

查询SCTP缓冲区参数源类型：

```
LST SCTPBUFFCFG:;
```

```
查询结果如下
-------------------------
 SCTP缓冲区参数源类型  =  自定义
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP缓冲区参数源(LST-SCTPBUFFCFG)_50812805.md`
