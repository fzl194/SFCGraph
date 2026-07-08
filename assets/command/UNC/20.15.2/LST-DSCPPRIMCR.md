---
id: UNC@20.15.2@MMLCommand@LST DSCPPRIMCR
type: MMLCommand
name: LST DSCPPRIMCR（查询DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DSCPPRIMCR
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- 接口DSCP管理
- DSCP优先级映射管理
status: active
---

# LST DSCPPRIMCR（查询DSCP映射优先级配置表）

## 功能

**适用网元：MME**

本命令用于查询DSCP映射优先级表，以及数据报文入发送队列的策略。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [DSCP映射优先级配置表（DSCPPRIMCR）](configobject/UNC/20.15.2/DSCPPRIMCR.md)

## 使用实例

查询映射关系表：

```
%%LST DSCPPRIMCR:;%%
RETCODE = 0  操作成功

数据包映射策略结果如下
------------------------------
数据报文的映射队列策略  =  基于DSCP
To be continued...

---    END

%%LST DSCPPRIMCR:;%%
RETCODE = 0  操作成功

DSCP映射结果如下
-------------------------------
 DSCP值      映射优先级

 0           优先级4      
 10          优先级3      
 12          优先级3      
 14          优先级3      
 18          优先级3      
 20          优先级3      
 22          优先级3      
 26          优先级2      
 28          优先级2      
 30          优先级2      
 34          优先级2      
 36          优先级2      
 38          优先级2      
 46          优先级2      
 48          优先级1      
 56          优先级1      
(结果个数 = 17)
共2条报告

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DSCP映射优先级配置表(LST-DSCPPRIMCR)_25291202.md`
