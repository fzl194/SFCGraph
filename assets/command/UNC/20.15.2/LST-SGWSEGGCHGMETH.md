---
id: UNC@20.15.2@MMLCommand@LST SGWSEGGCHGMETH
type: MMLCommand
name: LST SGWSEGGCHGMETH（查询SGW IMSI/MSISDN Group Charge Method）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGWSEGGCHGMETH
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- SGW计费控制
- SGW IMSI_MSISDN号段组计费方式
status: active
---

# LST SGWSEGGCHGMETH（查询SGW IMSI/MSISDN Group Charge Method）

## 功能

**适用NF：SGW-C**

该命令用于查询SGW基于号段组的计费方式。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWSEGGCHGMETH]] · SGW IMSI/MSISDN Group Charge Method（SGWSEGGCHGMETH）

## 使用实例

根据需求，查询SGW基于号段组的计费方式：

```
LST SGWSEGGCHGMETH:;
```

```

RETCODE = 0  操作成功。

serving-gateway计费方式配置信息
-------------------------------
IMSI/MSISDN号码段组名称    IMSI/MSISDN号码段组优先级    IMSI/MSISDN号段组离线计费开关

huawei                     10                           禁止                         
test                       5                            允许                         
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SGW-IMSI_MSISDN-Group-Charge-Method（LST-SGWSEGGCHGMETH）_09896998.md`
