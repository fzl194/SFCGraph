---
id: UNC@20.15.2@MMLCommand@LST SMSREGTIMER
type: MMLCommand
name: LST SMSREGTIMER（查询VLR/SMSF向注册中心注册的时间参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMSREGTIMER
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- SMSF业务管理
- 定时器管理
status: active
---

# LST SMSREGTIMER（查询VLR/SMSF向注册中心注册的时间参数）

## 功能

**适用NF：SMSF**

该命令用于查询向注册中心注册的时间参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMSREGTIMER]] · VLR/SMSF向注册中心注册的时间参数（SMSREGTIMER）

## 使用实例

运营商希望查询VLR/SMSF向注册中心注册的时间参数，执行如下命令：

```
LST SMSREGTIMER:;
%%LST SMSREGTIMER:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        SMSF向注册中心注册更新的时间间隔(分钟) =  24
VLR向注册中心注册更新的时间间隔(分钟) =  24
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMSREGTIMER.md`
