---
id: UNC@20.15.2@MMLCommand@LST STRINGMK
type: MMLCommand
name: LST STRINGMK（查询字符串Monitoring-Key）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STRINGMK
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 字符串Monitoring-Key
status: active
---

# LST STRINGMK（查询字符串Monitoring-Key）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于查询字符串类型的Monitoring-Key。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [字符串类型Monitoring-Key（STRINGMK）](configobject/UNC/20.15.2/STRINGMK.md)

## 使用实例

查询当前配置的stringmk：

```
LST STRINGMK:;
RETCODE = 0  操作成功。

结果如下
--------
字符串Monitoring-Key    监控属性值

test                     100       
test1                    200       
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询字符串Monitoring-Key（LST-STRINGMK）_70382341.md`
