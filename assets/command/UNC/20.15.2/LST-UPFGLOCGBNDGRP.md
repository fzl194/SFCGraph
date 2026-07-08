---
id: UNC@20.15.2@MMLCommand@LST UPFGLOCGBNDGRP
type: MMLCommand
name: LST UPFGLOCGBNDGRP（查询UPF组与Diameter本端主机组的绑定关系组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPFGLOCGBNDGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 计费和策略接口管理
- Diameter管理
- Diameter连接
- UPF组与Diam本端主机组的绑定关系组
status: active
---

# LST UPFGLOCGBNDGRP（查询UPF组与Diameter本端主机组的绑定关系组）

## 功能

**适用NF：PGW-C、SMF**

此命令用于查询UPF组与Diameter本端主机组的绑定关系组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

无。

## 操作的配置对象

- [UPF组与Diameter本端主机组的绑定关系组（UPFGLOCGBNDGRP）](configobject/UNC/20.15.2/UPFGLOCGBNDGRP.md)

## 使用实例

查询UPF组与Diameter本端主机组的绑定关系组记录：

```
LST UPFGLOCGBNDGRP:;
```

```

RETCODE = 0 操作成功。

UPF组与Diameter本端主机组的绑定关系组
-----------------------------
UPF组与Diameter本端主机组的绑定关系组名称  =  huawei
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF组与Diameter本端主机组的绑定关系组（LST-UPFGLOCGBNDGRP）_29660170.md`
