---
id: UNC@20.15.2@MMLCommand@LST SCTPBUFFERMODE
type: MMLCommand
name: LST SCTPBUFFERMODE（查询SCTP缓冲区模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCTPBUFFERMODE
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

# LST SCTPBUFFERMODE（查询SCTP缓冲区模式）

## 功能

**适用NF：SGSN、MME、AMF**

该命令用于查询系统中SCTP缓冲区的模式。

## 注意事项

无。

## 权限

manage-ug;system-ug;monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPBUFFERMODE]] · SCTP缓冲区模式（SCTPBUFFERMODE）

## 使用实例

查询当前系统中SCTP缓冲区模式：

```
LST SCTPBUFFERMODE:;
```

```
查询结果如下
-------------------------
 接收端缓冲区模式  =  私有模式
 发送端缓冲区模式  =  私有模式
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SCTP缓冲区模式(LST-SCTPBUFFERMODE)_50612759.md`
