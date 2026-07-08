---
id: UNC@20.15.2@MMLCommand@LST SELECTCCTBYCC
type: MMLCommand
name: LST SELECTCCTBYCC（查询基于CC配置融合计费模板处理）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SELECTCCTBYCC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费模板绑定
status: active
---

# LST SELECTCCTBYCC（查询基于CC配置融合计费模板处理）

## 功能

**适用NF：PGW-C、SMF、SGW-C**

该命令用于查询基于CC配置融合计费模板处理。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SELECTCCTBYCC]] · 基于CC配置融合计费模板处理（SELECTCCTBYCC）

## 使用实例

查询基于CC配置的融合计费模板：

```
%%LST SELECTCCTBYCC:;%%
RETCODE = 0  操作成功

结果如下
--------
                         CC类型  =  未指定Charge Characteristic的值
        Charge Characteristic值  =  0x0000
Charge Characteristic特定值掩码  =  0xFFFF
    Charge Characteristic优先级  =  0
               融合计费模板名称  =  global
I-SMF/SGW使用的融合计费模板名称  =  servingcct
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SELECTCCTBYCC.md`
