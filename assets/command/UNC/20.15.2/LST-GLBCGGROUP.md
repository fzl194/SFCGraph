---
id: UNC@20.15.2@MMLCommand@LST GLBCGGROUP
type: MMLCommand
name: LST GLBCGGROUP（查询全局CG组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBCGGROUP
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- GTPP信令
- CG组管理
- 全局CG组
status: active
---

# LST GLBCGGROUP（查询全局CG组）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

本条命令用于查询全局CG组。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [全局CG组（GLBCGGROUP）](configobject/UNC/20.15.2/GLBCGGROUP.md)

## 使用实例

查询全局CG组：

```
LST GLBCGGROUP:;
```

```

RETCODE = 0  操作成功

全局CG组
--------
CG组ID  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局CG组（LST-GLBCGGROUP）_09896862.md`
