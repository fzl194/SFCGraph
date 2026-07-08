---
id: UNC@20.15.2@MMLCommand@LST PSDATAOFFFUNC
type: MMLCommand
name: LST PSDATAOFFFUNC（查询3GPP PS data off功能相关的参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PSDATAOFFFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 分组数据离线状态管理
- 3GPP PS data off功能配置
status: active
---

# LST PSDATAOFFFUNC（查询3GPP PS data off功能相关的参数）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询3GPP PS data off功能相关的参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/PSDATAOFFFUNC]] · 3GPP PS data off功能相关的参数（PSDATAOFFFUNC）

## 使用实例

当运营商需要查询是否开启3GPP PS data off功能时，通过该命令查询开关状态：

```
%%LST PSDATAOFFFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
PS data off功能开关  =  使能
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询3GPP-PS-data-off功能相关的参数（LST-PSDATAOFFFUNC）_35439598.md`
