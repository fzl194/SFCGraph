---
id: UNC@20.15.2@MMLCommand@LST SMSCHRCFG
type: MMLCommand
name: LST SMSCHRCFG（查询SMS CHR单据上报策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSCHRCFG
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- CHR管理
status: active
---

# LST SMSCHRCFG（查询SMS CHR单据上报策略）

## 功能

**适用NF：SMSF**

该命令用于查询SMS CHR单据上报策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSCHRCFG]] · SMS CHR单据上报策略（SMSCHRCFG）

## 使用实例

运营商希望查询系统上报SMS CHR单据时，SMS CHR单据采集及订阅流程的配置，执行如下命令：

```
LST SMSCHRCFG:;
%%LST SMSCHRCFG:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
高性能服务器上报流程控制模板索引 =  1
低性能服务器上报流程控制模板索引  =  2
       
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSCHRCFG.md`
