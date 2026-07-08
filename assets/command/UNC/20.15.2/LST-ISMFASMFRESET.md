---
id: UNC@20.15.2@MMLCommand@LST ISMFASMFRESET
type: MMLCommand
name: LST ISMFASMFRESET（查询I-SMF对A-SMF的故障恢复策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ISMFASMFRESET
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- A-SMF故障处理策略管理
status: active
---

# LST ISMFASMFRESET（查询I-SMF对A-SMF的故障恢复策略）

## 功能

**适用NF：SMF**

该命令用于查询I-SMF对A-SMF的故障恢复策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [I-SMF对A-SMF的故障恢复策略（ISMFASMFRESET）](configobject/UNC/20.15.2/ISMFASMFRESET.md)

## 使用实例

查询I-SMF对A-SMF的故障恢复策略。

```
%%LST ISMFAMSFRESET;%%
RETCODE = 0  操作成功

结果如下
--------
   A-SMF故障重选开关  =  打开
            扫描速率  =  5
语音业务快速恢复开关  =  关闭
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询I-SMF对A-SMF的故障恢复策略（LST-ISMFASMFRESET）_23622938.md`
