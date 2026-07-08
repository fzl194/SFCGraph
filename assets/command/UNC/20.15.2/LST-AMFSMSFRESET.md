---
id: UNC@20.15.2@MMLCommand@LST AMFSMSFRESET
type: MMLCommand
name: LST AMFSMSFRESET（查询AMF的SMSF故障处理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFSMSFRESET
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的SMSF故障处理策略
status: active
---

# LST AMFSMSFRESET（查询AMF的SMSF故障处理策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF的SMSF故障处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFSMSFRESET]] · AMF的SMSF故障处理策略（AMFSMSFRESET）

## 使用实例

查询AMF的SMSF故障处理策略，执行如下命令：

```
%%LST AMFSMSFRESET:;%%
RETCODE = 0  操作成功

结果如下
--------
SMSF故障重选开关  =  打开
 扫描速率(个/秒)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFSMSFRESET.md`
