---
id: UNC@20.15.2@MMLCommand@LST DEFAULTASN
type: MMLCommand
name: LST DEFAULTASN（查询缺省ASN值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DEFAULTASN
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- 缺省ASN管理
status: active
---

# LST DEFAULTASN（查询缺省ASN值）

## 功能

**适用NF：PGW-C、GGSN、SGW-C**

该命令用于查看SGSN/SGW-C对应的缺省ASN值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [缺省ASN值（DEFAULTASN）](configobject/UNC/20.15.2/DEFAULTASN.md)

## 使用实例

查询缺省ASN值：

```
LST DEFAULTASN:;
RETCODE = 0  操作成功。

缺省ASN值
---------
缺省ASN  =  1000
  ASN值  =  指定ASN值
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询缺省ASN值（LST-DEFAULTASN）_90657140.md`
