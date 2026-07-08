---
id: UNC@20.15.2@MMLCommand@LST NSSFCFGSUBSW
type: MMLCommand
name: LST NSSFCFGSUBSW（查询按签约NSSAI分配Configed NSSAI的PLMN级别开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFCFGSUBSW
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能开关配置
status: active
---

# LST NSSFCFGSUBSW（查询按签约NSSAI分配Configed NSSAI的PLMN级别开关）

## 功能

**适用NF：NSSF**

该命令用于查询按签约NSSAI生成configuredNssai信元的PLMN级别开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [按签约NSSAI分配Configed NSSAI的PLMN级别开关（NSSFCFGSUBSW）](configobject/UNC/20.15.2/NSSFCFGSUBSW.md)

## 使用实例

若运营商希望查询所有的数据，执行下列命令。

```
LST NSSFCFGSUBSW:;
%%LST NSSFCFGSUBSW:;%%
RETCODE = 0 执行成功

结果如下
------------------------
                       移动国家码  =  245
                         移动网号  =  38
按签约NSSAI分配configuredNssai开关  =  打开
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询按签约NSSAI分配Configed-NSSAI的PLMN级别开关（LST-NSSFCFGSUBSW）_98101324.md`
