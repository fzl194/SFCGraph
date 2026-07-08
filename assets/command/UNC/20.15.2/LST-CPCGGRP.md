---
id: UNC@20.15.2@MMLCommand@LST CPCGGRP
type: MMLCommand
name: LST CPCGGRP（显示抄送CG组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CPCGGRP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- 抄送CG组
status: active
---

# LST CPCGGRP（显示抄送CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来查询指定的抄送CG组。

## 注意事项

当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/CPCGGRP]] · 抄送CG组（CPCGGRP）

## 使用实例

查询所有的抄送CG组：

```
LST CPCGGRP:;
```

```

RETCODE = 0  操作成功

抄送CG组
--------
  抄送CG组ID  =  1
抄送CG组描述  =  test
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-CPCGGRP.md`
