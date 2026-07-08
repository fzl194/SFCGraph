---
id: UNC@20.15.2@MMLCommand@LST SELECTCHFGBYCC
type: MMLCommand
name: LST SELECTCHFGBYCC（查询基于CC选择CHF处理）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SELECTCHFGBYCC
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

# LST SELECTCHFGBYCC（查询基于CC选择CHF处理）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询基于CC选择CHF处理。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SELECTCHFGBYCC]] · 基于CC选择CHF处理（SELECTCHFGBYCC）

## 使用实例

查询基于CC选择CHF处理：

```
%%LST SELECTCHFGBYCC:;%%
RETCODE = 0  操作成功

结果如下
--------
      Charge Characteristic类型  =  未指定Charge Characteristic的值
        Charge Characteristic值  =  0x0000
Charge Characteristic特定值掩码  =  0xFFFF
    Charge Characteristic优先级  =  0
                        主CHF组  =  chf-grp01
                        备CHF组  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SELECTCHFGBYCC.md`
