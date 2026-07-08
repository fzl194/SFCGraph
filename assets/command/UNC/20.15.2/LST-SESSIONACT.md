---
id: UNC@20.15.2@MMLCommand@LST SESSIONACT
type: MMLCommand
name: LST SESSIONACT（查询新创建会话或专载的锁定状态）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SESSIONACT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- 会话锁定管理
status: active
---

# LST SESSIONACT（查询新创建会话或专载的锁定状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询新创建会话或专载的锁定状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SESSIONACT]] · 新创建会话或专载的锁定状态（SESSIONACT）

## 使用实例

查询新创建会话或专载的锁定状态。

```
%%LST SESSIONACT:;%%
RETCODE = 0  操作成功

结果如下
--------
    锁定范围  = 所有会话
锁定会话操作  = 解锁
锁定专载操作  = 解锁
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SESSIONACT.md`
