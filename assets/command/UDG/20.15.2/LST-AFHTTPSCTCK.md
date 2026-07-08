---
id: UDG@20.15.2@MMLCommand@LST AFHTTPSCTCK
type: MMLCommand
name: LST AFHTTPSCTCK（查询HTTPS证书检查功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: AFHTTPSCTCK
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- HTTPS证书检查功能配置
status: active
---

# LST AFHTTPSCTCK（查询HTTPS证书检查功能配置）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询配置的HTTPS证书检查功能。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [HTTPS证书检查功能配置（AFHTTPSCTCK）](configobject/UDG/20.15.2/AFHTTPSCTCK.md)

## 使用实例

查询所有HTTPS证书检查功能配置：

```
LST AFHTTPSCTCK:;
```

```

RETCODE = 0  操作成功

HTTPS证书检查配置信息
---------------------
协议名称      证书检查开关  配置域名称  

facebook      使能（开启）  NULL        
youtube       使能（开启）  NULL        
all-protocol  使能（开启）  NULL        
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTTPS证书检查功能配置（LST-AFHTTPSCTCK）_01168648.md`
