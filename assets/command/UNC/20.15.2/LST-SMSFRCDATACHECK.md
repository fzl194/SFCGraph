---
id: UNC@20.15.2@MMLCommand@LST SMSFRCDATACHECK
type: MMLCommand
name: LST SMSFRCDATACHECK（查询SMSF核查注册中心状态功能配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSFRCDATACHECK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 数据核查
status: active
---

# LST SMSFRCDATACHECK（查询SMSF核查注册中心状态功能配置）

## 功能

**适用NF：SMSF**

该命令用于查询SMSF核查注册中心状态功能配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSFRCDATACHECK]] · SMSF核查注册中心状态功能配置（SMSFRCDATACHECK）

## 使用实例

运营商希望查询SMSF核查注册中心状态功能配置，执行如下命令：

```
LST SMSFRCDATACHECK:;
%%LST SMSFRCDATACHECK:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
SMSF核查注册中心状态功能开关 =  打开
每秒钟SMSF核查注册中心状态的条数(个每秒) = 5
SMSF核查注册中心状态周期(分钟) = 5
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSFRCDATACHECK.md`
