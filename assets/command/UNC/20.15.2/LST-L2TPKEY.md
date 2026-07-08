---
id: UNC@20.15.2@MMLCommand@LST L2TPKEY
type: MMLCommand
name: LST L2TPKEY（查询L2TP加密配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: L2TPKEY
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
- L2TP
- L2TP加密配置
status: active
---

# LST L2TPKEY（查询L2TP加密配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询L2TP加密配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/L2TPKEY]] · L2TP加密配置（L2TPKEY）

## 使用实例

查询L2TP加密配置

```
%%LST L2TPKEY:;%%
RETCODE = 0  操作成功

结果如下
--------
  加密开关  =  不使能
  密钥口令  =  *****
  密钥变更  =  不变更
时长(分钟)  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-L2TPKEY.md`
