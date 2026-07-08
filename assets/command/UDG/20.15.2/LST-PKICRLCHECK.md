---
id: UDG@20.15.2@MMLCommand@LST PKICRLCHECK
type: MMLCommand
name: LST PKICRLCHECK（查询CRL检查）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PKICRLCHECK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 公钥基础设施
- 使能CRL检查
status: active
---

# LST PKICRLCHECK（查询CRL检查）

## 功能

该命令用于查询是否进行CRL检查。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [CRL检查（PKICRLCHECK）](configobject/UDG/20.15.2/PKICRLCHECK.md)

## 使用实例

查询CRL检查：

```
LST PKICRLCHECK:;
        RETCODE = 0  操作成功

        结果如下
        -------------------------
          CRL检查  = FALSE
        (结果个数 = 1)
        ---   END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询CRL检查（LST-PKICRLCHECK）_41422663.md`
