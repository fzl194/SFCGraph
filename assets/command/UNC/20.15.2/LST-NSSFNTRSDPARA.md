---
id: UNC@20.15.2@MMLCommand@LST NSSFNTRSDPARA
type: MMLCommand
name: LST NSSFNTRSDPARA（查询NSSF通知重传参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NSSFNTRSDPARA
command_category: 查询类
applicable_nf:
- NSSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF通知重传参数配置
status: active
---

# LST NSSFNTRSDPARA（查询NSSF通知重传参数）

## 功能

**适用NF：NSSF**

该命令用于查询NSSF通知重传参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [NSSF通知重传参数（NSSFNTRSDPARA）](configobject/UNC/20.15.2/NSSFNTRSDPARA.md)

## 使用实例

运营商希望查询NSSF通知重传参数信息，执行如下命令。

```
LST NSSFNTRSDPARA:;
%%LST NSSFNTRSDPARA:;%%
RETCODE = 0  操作成功

结果如下
------------------------

      最大通知重传次数 = 1000
通知重传执行周期(分钟) = 50
        重传响应码列表 = 429.500.503.504

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NSSF通知重传参数（LST-NSSFNTRSDPARA）_96242341.md`
