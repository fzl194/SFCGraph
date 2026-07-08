---
id: UNC@20.15.2@MMLCommand@LST NRFSMSFWHITELST
type: MMLCommand
name: LST NRFSMSFWHITELST（查询SMSF白名单）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSMSFWHITELST
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- SMSF割接场景NRF处理策略
status: active
---

# LST NRFSMSFWHITELST（查询SMSF白名单）

## 功能

**适用NF：NRF**

该命令用于查询SMSF白名单列表的SMSF实例。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSMSFWHITELST]] · SMSF白名单（NRFSMSFWHITELST）

## 使用实例

查询SMSF白名单的NF实例列表，执行如下命令：

```
LST NRFSMSFWHITELST:;
%%LST NRFSMSFWHITELST:;%%
RETCODE = 0  操作成功

结果如下
-----------
NF实例标识  =  88888888-4444-1234-5678-123456789abc
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSMSFWHITELST.md`
