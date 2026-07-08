---
id: UDG@20.15.2@MMLCommand@LST DOMAINSEPARATOR
type: MMLCommand
name: LST DOMAINSEPARATOR（查询前后缀分隔符）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DOMAINSEPARATOR
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- L2TP隧道管理
- 域名分隔符
status: active
---

# LST DOMAINSEPARATOR（查询前后缀分隔符）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看已设置的前缀分割符和后缀分割符。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [前后缀分隔符（DOMAINSEPARATOR）](configobject/UDG/20.15.2/DOMAINSEPARATOR.md)

## 使用实例

查询已设置的前缀分隔符和后缀分隔符的配置信息：

```
LST DOMAINSEPARATOR:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
前缀域名分隔符  =  @%
后缀域名分隔符  =  #/
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询前后缀分隔符（LST-DOMAINSEPARATOR）_35373551.md`
