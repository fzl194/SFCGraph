---
id: UNC@20.15.2@MMLCommand@LST PCSCFGRPSELECT
type: MMLCommand
name: LST PCSCFGRPSELECT（查询P-CSCF组选择模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCSCFGRPSELECT
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF组选择模式
status: active
---

# LST PCSCFGRPSELECT（查询P-CSCF组选择模式）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询配置的P-CSCF-GROUP的选择模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PCSCFGRPSELECT]] · P-CSCF组选择模式（PCSCFGRPSELECT）

## 使用实例

查询P-CSCF-GROUP的选择模式：

```
%%LST PCSCFGRPSELECT:;%%
RETCODE = 0  操作成功

结果如下
----------------
选择模式  =  主备
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCSCFGRPSELECT.md`
