---
id: UNC@20.15.2@MMLCommand@LST NRFFUNCTION
type: MMLCommand
name: LST NRFFUNCTION（查询NRF功能实体配置信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFFUNCTION
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- NRF性能对象管理
status: active
---

# LST NRFFUNCTION（查询NRF功能实体配置信息）

## 功能

**适用NF：NRF**

该命令用于查询特定NRF功能实例的配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFFUNCTION]] · NRF功能实例信息（NRFFUNCTION）

## 使用实例

查询所有NRF功能实例的配置信息:

```
LST NRFFUNCTION:;
%%LST NRFFUNCTION:;%%
RETCODE = 0 执行成功

结果如下
-------------------------
NRF功能实体号  NRF功能实体描述  管理状态    运行状态      FQDN      最大服务请求次数

Instanceid01   nfdescription01  锁定        运行          fqdn01          1000                                
Instanceid02   nfdescription02  锁定        运行          fqdn02          1000                                

(结果个数 = 2)
        
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF功能实体配置信息（LST-NRFFUNCTION）_09652771.md`
