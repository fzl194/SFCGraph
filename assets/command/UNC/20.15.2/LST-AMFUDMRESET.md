---
id: UNC@20.15.2@MMLCommand@LST AMFUDMRESET
type: MMLCommand
name: LST AMFUDMRESET（查询AMF的UDM故障处理策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFUDMRESET
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 可靠性管理
- AMF的UDM故障处理策略
status: active
---

# LST AMFUDMRESET（查询AMF的UDM故障处理策略）

## 功能

**适用NF：AMF**

该命令用于查询AMF的UDM故障处理策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFUDMRESET]] · AMF的UDM故障处理策略（AMFUDMRESET）

## 使用实例

查询AMF的UDM故障处理策略。

```
%%LST AMFUDMRESET:;%%
RETCODE = 0  操作成功

结果如下
--------
  recoveryTime变化时重选UDM开关  =  打开
链路故障或者去注册时重选UDM开关  =  关闭
         通过流程触发的扫描速率  =  5
                   立即触发开关  =  关闭
             立即触发的扫描速率  =  1
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF的UDM故障处理策略（LST-AMFUDMRESET）_96242056.md`
