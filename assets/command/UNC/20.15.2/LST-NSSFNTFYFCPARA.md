---
id: UNC@20.15.2@MMLCommand@LST NSSFNTFYFCPARA
type: MMLCommand
name: LST NSSFNTFYFCPARA（查询通知流控参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFNTFYFCPARA
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF流控管理
status: active
---

# LST NSSFNTFYFCPARA（查询通知流控参数配置）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF订阅通知流程流控参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFNTFYFCPARA]] · 通知流控参数配置（NSSFNTFYFCPARA）

## 使用实例

当运营商希望查询NSSF通知流控参数配置时，可以通过此命令查询NSSF的通知流控参数配置：

```
LST NSSFNTFYFCPARA:;
%%LST NSSFNTFYFCPARA:;%%
RETCODE = 0 执行成功

结果如下
------------------------
               通知流控开关  =  打开
单个VM发送订阅通知带宽(MB/s)  =  6
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询通知流控参数配置（LST-NSSFNTFYFCPARA）_43978183.md`
