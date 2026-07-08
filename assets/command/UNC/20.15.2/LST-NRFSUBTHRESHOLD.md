---
id: UNC@20.15.2@MMLCommand@LST NRFSUBTHRESHOLD
type: MMLCommand
name: LST NRFSUBTHRESHOLD（查询NF的订阅门限）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFSUBTHRESHOLD
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF订阅参数
status: active
---

# LST NRFSUBTHRESHOLD（查询NF的订阅门限）

## 功能

**适用NF：NRF**

该命令用于查询NF的订阅个数的上限。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFSUBTHRESHOLD]] · NF的订阅门限（NRFSUBTHRESHOLD）

## 使用实例

查询NF的订阅门限：

```
LST NRFSUBTHRESHOLD:;
%%LST NRFSUBTHRESHOLD:;%%
RETCODE = 0  操作成功

结果如下
------------------------
   订阅门限  =  90
内部订阅门限 = 100
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFSUBTHRESHOLD.md`
