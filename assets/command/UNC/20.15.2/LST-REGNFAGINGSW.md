---
id: UNC@20.15.2@MMLCommand@LST REGNFAGINGSW
type: MMLCommand
name: LST REGNFAGINGSW（查询NF实例老化开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: REGNFAGINGSW
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- NF信息老化管理
status: active
---

# LST REGNFAGINGSW（查询NF实例老化开关）

## 功能

**适用NF：NRF**

该命令用于查询NRF老化功能相关配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/REGNFAGINGSW]] · NF实例老化开关（REGNFAGINGSW）

## 使用实例

当运营商希望查询NF实例的老化开关状态，老化时长及NRF老化通知开关时，执行此命令。

```
LST REGNFAGINGSW:;
%%LST REGNFAGINGSW:;%%
RETCODE = 0  操作成功
结果如下
-------------------------
     开关状态  =  开启
 老化时长(分)  =  60
 NRF老化通知开关  =  开启
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NF实例老化开关（LST-REGNFAGINGSW）_09654407.md`
