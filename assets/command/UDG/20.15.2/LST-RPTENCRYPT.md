---
id: UDG@20.15.2@MMLCommand@LST RPTENCRYPT
type: MMLCommand
name: LST RPTENCRYPT（查询业务报表加密算法配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTENCRYPT
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表功能管理
- 报表加密控制
status: active
---

# LST RPTENCRYPT（查询业务报表加密算法配置）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询业务报表加密算法配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTENCRYPT]] · 业务报表加密算法配置（RPTENCRYPT）

## 使用实例

假如运营商需要查询业务报表加密算法配置：

```
LST RPTENCRYPT:;
```

```

RETCODE = 0 操作成功

业务报表加密算法配置信息
---------------------------
加密模式 = DEFAULT
加密算法 = SHA256
     
(结果个数 = 1)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询业务报表加密算法配置（LST-RPTENCRYPT）_06561550.md`
