---
id: UNC@20.15.2@MMLCommand@LST LCKWHITELST
type: MMLCommand
name: LST LCKWHITELST（查询锁定白名单记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LCKWHITELST
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 锁定白名单
status: active
---

# LST LCKWHITELST（查询锁定白名单记录）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询锁定白名单记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LCKWHITELST]] · 锁定白名单记录（LCKWHITELST）

## 使用实例

查询锁定白名单记录：

```
%%LST LCKWHITELST:;%%
RETCODE = 0  操作成功

结果如下
--------
白名单类型  IMSI             MSISDN           

IMSI        123456789012345  000000000000000  
MSISDN      000000000000000  123456789012345  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LCKWHITELST.md`
