---
id: UNC@20.15.2@MMLCommand@LST GLBDFTCHFGROUP
type: MMLCommand
name: LST GLBDFTCHFGROUP（查询全局默认CHF组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBDFTCHFGROUP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- CHF选择
status: active
---

# LST GLBDFTCHFGROUP（查询全局默认CHF组）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询全局默认CHF组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [全局默认CHF组（GLBDFTCHFGROUP）](configobject/UNC/20.15.2/GLBDFTCHFGROUP.md)

## 使用实例

查询全局CHF组配置：

```
%%LST GLBDFTCHFGROUP:;%%
RETCODE = 0  操作成功

结果如下
--------
主CHF组  =  NULL
备CHF组  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局默认CHF组（LST-GLBDFTCHFGROUP）_09651740.md`
