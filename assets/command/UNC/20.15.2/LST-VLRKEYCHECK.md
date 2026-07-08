---
id: UNC@20.15.2@MMLCommand@LST VLRKEYCHECK
type: MMLCommand
name: LST VLRKEYCHECK（查询VLR用户关键信息数据核查扫描参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRKEYCHECK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 热备容灾
status: active
---

# LST VLRKEYCHECK（查询VLR用户关键信息数据核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于查询VLR用户关键信息数据核查扫描速率和周期，以及数据有效时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/VLRKEYCHECK]] · VLR用户关键信息数据核查扫描参数（VLRKEYCHECK）

## 使用实例

运营商希望查询VLR用户关键信息数据核查扫描速率和周期，以及数据有效时长，执行如下命令：

```
LST VLRKEYCHECK:;
%%LST VLRKEYCHECK:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
       VLR用户关键信息核查功能开关        =  打开
       VLR用户关键信息核查速率(个每秒)    =  70
       VLR上用户关键信息核查周期(分钟)    =  60
       VLR用户关键信息有效时长开关        =  打开
       VLR上用户关键信息的有效时长(分钟) =  10080
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR用户关键信息数据核查扫描参数（LST-VLRKEYCHECK）_80800289.md`
