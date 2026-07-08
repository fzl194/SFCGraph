---
id: UDG@20.15.2@MMLCommand@LST MBSQOSGLOBAL
type: MMLCommand
name: LST MBSQOSGLOBAL（查询MBS QosGlobal配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MBSQOSGLOBAL
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- MBS管理
- MBS整机QoS配置
status: active
---

# LST MBSQOSGLOBAL（查询MBS QosGlobal配置）

## 功能

**适用NF：UPF**

该命令用于查询MBS会话的QOS功能配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MBSQOSGLOBAL]] · MBS QosGlobal配置（MBSQOSGLOBAL）

## 使用实例

查询MBS会话的QOS功能开关配置：

```
LST MBSQOSGLOBAL:;
```

```

RETCODE = 0  操作成功

MBS整机QoS配置
----------------------------
 MBS QoS 功能开关  =  ENABLE
   MBS QosCar 功能 =  DISABLE
MBS QosShape 功能  =  ENABLE
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MBSQOSGLOBAL.md`
