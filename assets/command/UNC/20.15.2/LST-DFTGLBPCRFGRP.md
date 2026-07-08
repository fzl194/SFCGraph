---
id: UNC@20.15.2@MMLCommand@LST DFTGLBPCRFGRP
type: MMLCommand
name: LST DFTGLBPCRFGRP（查询全局缺省PCRF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DFTGLBPCRFGRP
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCRF Diameter连接
- 缺省全局PCRF组
status: active
---

# LST DFTGLBPCRFGRP（查询全局缺省PCRF组）

## 功能

**适用NF：PGW-C、GGSN**

此命令用来查询缺省全局PCRF分组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [全局缺省PCRF组（DFTGLBPCRFGRP）](configobject/UNC/20.15.2/DFTGLBPCRFGRP.md)

## 使用实例

显示DFTGLBPCRFGRP：

```
LST DFTGLBPCRFGRP:;
```

```

RETCODE = 0  操作成功。

全局缺省PCRF组
--------------
PCRF组名称  =  pcr
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局缺省PCRF组（LST-DFTGLBPCRFGRP）_09897114.md`
