---
id: UDG@20.15.2@MMLCommand@LST AFDNSCHECKTYPE
type: MMLCommand
name: LST AFDNSCHECKTYPE（查询需要进行防欺诈检查的DNS报文类型）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AFDNSCHECKTYPE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- 根据报文类型进行的DNS防欺诈检测
status: active
---

# LST AFDNSCHECKTYPE（查询需要进行防欺诈检查的DNS报文类型）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询所有的进行防欺诈检查的DNS报文类型。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [需要进行防欺诈检查的DNS报文类型（AFDNSCHECKTYPE）](configobject/UDG/20.15.2/AFDNSCHECKTYPE.md)

## 使用实例

如果运营商要查询所有的进行防欺诈检查的DNS报文类型，则命令如下：

```
LST AFDNSCHECKTYPE:;
```

```

RETCODE = 0  操作成功。

DNS防欺诈检查类型信息
---------------------
Dns防欺诈检查类型值  =  5
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询需要进行防欺诈检查的DNS报文类型（LST-AFDNSCHECKTYPE）_82837805.md`
