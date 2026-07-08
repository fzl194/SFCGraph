---
id: UNC@20.15.2@MMLCommand@LST PERFNGPEIGRP
type: MMLCommand
name: LST PERFNGPEIGRP（查询NG PEI组性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFNGPEIGRP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# LST PERFNGPEIGRP（查询NG PEI组性能统计对象）

## 功能

**适用NF：AMF**

该命令用于查询NG PEI组性能统计对象信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NG PEI组性能统计对象（PERFNGPEIGRP）](configobject/UNC/20.15.2/PERFNGPEIGRP.md)

## 使用实例

查询系统配置的所有NG PEI组信息：

```
%%LST PERFNGPEIGRP:;%%
RETCODE = 0  操作成功

结果如下
--------
NG PEI群组名称

123/13
464564454
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NG-PEI组性能统计对象（LST-PERFNGPEIGRP）_89159153.md`
