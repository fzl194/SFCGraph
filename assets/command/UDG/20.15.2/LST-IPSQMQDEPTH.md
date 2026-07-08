---
id: UDG@20.15.2@MMLCommand@LST IPSQMQDEPTH
type: MMLCommand
name: LST IPSQMQDEPTH（查询IPSQM缓存队列深度）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: IPSQMQDEPTH
command_category: 查询类
applicable_nf:
- SGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- IPSQM控制
- IPSQM整形队列深度
status: active
---

# LST IPSQMQDEPTH（查询IPSQM缓存队列深度）

## 功能

**适用NF：SGW-U、UPF**

该命令用于查询整形队列深度。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPSQMQDEPTH]] · IPSQM缓存队列深度（IPSQMQDEPTH）

## 使用实例

查询整形队列深度：

```
LST IPSQMQDEPTH:;
```

```

RETCODE = 0  操作成功

IPSQM缓存队列深度
-----------------
队列深度（报文个数）  =  256
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-IPSQMQDEPTH.md`
