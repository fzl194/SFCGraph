---
id: UNC@20.15.2@MMLCommand@LST CHFSELECTMODE
type: MMLCommand
name: LST CHFSELECTMODE（查询用户激活和在线恢复场景CHF的选择模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CHFSELECTMODE
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

# LST CHFSELECTMODE（查询用户激活和在线恢复场景CHF的选择模式）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询用户激活和在线恢复场景CHF的选择模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [用户激活和在线恢复场景CHF的选择模式（CHFSELECTMODE）](configobject/UNC/20.15.2/CHFSELECTMODE.md)

## 使用实例

查询当前CHF选择模式：

```
%%LST CHFSELECTMODE:;%%
RETCODE = 0  操作成功
结果如下
--------
首选模式  =  NRF
备选模式  =  Local
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询用户激活和在线恢复场景CHF的选择模式（LST-CHFSELECTMODE）_34667401.md`
