---
id: UNC@20.15.2@MMLCommand@LST SMSCHFGRP
type: MMLCommand
name: LST SMSCHFGRP（查询短消息计费CHF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCHFGRP
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHF管理
status: active
---

# LST SMSCHFGRP（查询短消息计费CHF组）

## 功能

**适用NF：SMSF**

在SMSF/VLR计费场景下，通过本命令查询到短消息计费CHF组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSCHFGRP]] · 短消息计费CHF组（SMSCHFGRP）

## 使用实例

查询SMSF/VLR使用的计费CHF组：

```
LST SMSCHFGRP:;
%%LST SMSCHFGRP:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
 主CHF组的名称  =  SMS CHF Group1
 备CHF组的名称  =  SMS CHF Group2
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询短消息计费CHF组（LST-SMSCHFGRP）_13939885.md`
