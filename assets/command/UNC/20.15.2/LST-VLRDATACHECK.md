---
id: UNC@20.15.2@MMLCommand@LST VLRDATACHECK
type: MMLCommand
name: LST VLRDATACHECK（查询VLR用户数据核查扫描参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRDATACHECK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- 数据核查
status: active
---

# LST VLRDATACHECK（查询VLR用户数据核查扫描参数）

## 功能

**适用NF：SMSF**

该命令用于查询VLR数据核查时的扫描速率和周期，以及VLR数据有效时长。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [VLR用户数据核查扫描参数（VLRDATACHECK）](configobject/UNC/20.15.2/VLRDATACHECK.md)

## 使用实例

运营商希望查询VLR用户数据核查扫描参数，执行如下命令：

```
LST VLRDATACHECK:;
%%LST VLRDATACHECK:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
       VLR用户数据核查开关       =  打开
       VLR用户数据核查速率(个每秒)        =  3
       VLR上用户数据核查周期(分钟)    =  90
       VLR数据有效时长开关        =  打开
       VLR上用户数据的有效时长(小时) =  48
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR用户数据核查扫描参数（LST-VLRDATACHECK）_04281137.md`
