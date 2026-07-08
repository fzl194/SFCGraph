---
id: UNC@20.15.2@MMLCommand@LST PCCALMTHD
type: MMLCommand
name: LST PCCALMTHD（查询PCC告警阈值）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCCALMTHD
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 告警管理
- PCC告警门限
status: active
---

# LST PCCALMTHD（查询PCC告警阈值）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询PCC告警阈值。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCCALMTHD]] · PCC告警阈值（PCCALMTHD）

## 使用实例

查询PCC告警阈值配置：

```
LST PCCALMTHD:;
```

```

RETCODE = 0  操作成功

PCC告警阈值信息
---------------
应用层PCRF无响应告警恢复阈值  =  1
    应用层PCRF无响应告警阈值  =  0
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCCALMTHD.md`
