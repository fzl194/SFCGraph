---
id: UDG@20.15.2@MMLCommand@LST HTTPHTRCFG
type: MMLCommand
name: LST HTTPHTRCFG（查询HTR流控全局配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: HTTPHTRCFG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP流控管理
- HTTP HTR流控管理
- HTTP HTR全局配置管理
status: active
---

# LST HTTPHTRCFG（查询HTR流控全局配置）

## 功能

该命令用于查询HTR流控全局配置信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [HTR流控全局配置（HTTPHTRCFG）](configobject/UDG/20.15.2/HTTPHTRCFG.md)

## 使用实例

查询HTR流控全局配置信息，可以用如下命令：

```
%%LST HTTPHTRCFG:;%%
RETCODE = 0  操作成功

结果如下
--------
         HTR流控开关  =  打开
   启控失败率阈值(%)  =  12
   解控失败率阈值(%)  =  1
   目标失败率阈值(%)  =  6
         统计周期(s)  =  5
          启控周期数  =  4
          解控周期数  =  8
     HTR超时时长(ms)  =  2000
 放通阈值减少比例(%)  =  10
放通阈值增加比例1(%)  =  5
放通阈值增加比例2(%)  =  18
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询HTR流控全局配置（LST-HTTPHTRCFG）_35550174.md`
