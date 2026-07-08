---
id: UDG@20.15.2@MMLCommand@LST CFSRVMODE
type: MMLCommand
name: LST CFSRVMODE（查询URL过滤功能业务模式）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: CFSRVMODE
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 内容过滤
- URL过滤业务模式配置
status: active
---

# LST CFSRVMODE（查询URL过滤功能业务模式）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询URL过滤功能业务模式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [URL过滤功能业务模式（CFSRVMODE）](configobject/UDG/20.15.2/CFSRVMODE.md)

## 使用实例

查询内容过滤本地缓存参数：

```
LST CFSRVMODE:;
```

```

RETCODE = 0 操作成功
 
URL过滤功能业务模式
------------------------------
URL过滤功能业务模式   =  CUSTOMIZATION1
           加密算法  =  SHA256
      加密算法密钥   =  *****
         配置域参数  =  0
(结果个数 = 1)
 
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询URL过滤功能业务模式（LST-CFSRVMODE）_19410194.md`
