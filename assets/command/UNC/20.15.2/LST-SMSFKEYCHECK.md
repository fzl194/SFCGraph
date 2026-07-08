---
id: UNC@20.15.2@MMLCommand@LST SMSFKEYCHECK
type: MMLCommand
name: LST SMSFKEYCHECK（查询SMSF用户关键信息数据核查扫描参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFKEYCHECK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 热备容灾
status: active
---

# LST SMSFKEYCHECK（查询SMSF用户关键信息数据核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF用户关键信息数据核查扫描速率和周期，以及数据有效时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFKEYCHECK]] · SMSF用户关键信息数据核查扫描参数（SMSFKEYCHECK）

## 使用实例

运营商希望查询SMSF用户关键信息数据核查扫描速率和周期，以及数据有效时长，执行如下命令：

```
LST SMSFKEYCHECK:;
%%LST SMSFKEYCHECK:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
       SMSF用户关键信息表核查功能开关       =  打开
       SMSF用户关键信息核查速率(个每秒)        =  70
       SMSF用户关键信息核查周期(分钟)    =  60
       SMSF用户关键信息有效时长开关        =  打开
       SMSF上用户关键信息数据的有效时长(分钟) =  1440
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSFKEYCHECK.md`
