---
id: UDG@20.15.2@MMLCommand@LST PDFUNC
type: MMLCommand
name: LST PDFUNC（查询报文检测功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PDFUNC
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 数据转发控制
- 报文检测功能
status: active
---

# LST PDFUNC（查询报文检测功能配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询Tx-U接口的下行报文检测功能开关状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDFUNC]] · 报文检测功能配置（PDFUNC）

## 使用实例

查询Tx-U接口的下行报文检测功能开关状态：

```
LST PDFUNC:;
```

```

RETCODE = 0  操作成功

报文检测功能配置
----------------
Tx-U接口下行报文  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PDFUNC.md`
