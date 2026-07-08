---
id: UNC@20.15.2@MMLCommand@LST DSCPPRI
type: MMLCommand
name: LST DSCPPRI（查询DSCP映射优先级配置表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DSCPPRI
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- QoS管理
- DSCP
- DSCP优先级映射管理
status: active
---

# LST DSCPPRI（查询DSCP映射优先级配置表）

## 功能

**适用网元：SGSN、MME**

本命令用于查询DSCP映射优先级表，以及数据报文入发送队列的策略。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DSCPPRI]] · DSCP映射优先级配置表（DSCPPRI）

## 使用实例

查询映射关系表：

```
%%LST DSCPPRI:;%%
RETCODE = 0  操作成功。

数据包映射策略结果如下
------------------------------
数据报文的映射队列策略  =  基于业务类别
仍有后续报告输出

---    END

%%LST DSCPPRI:;%%
RETCODE = 0  操作成功。

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

- 原始手册：`evidence/UNC/20.15.2/LST-DSCPPRI.md`
