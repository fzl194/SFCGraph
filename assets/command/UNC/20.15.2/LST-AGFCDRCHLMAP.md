---
id: UNC@20.15.2@MMLCommand@LST AGFCDRCHLMAP
type: MMLCommand
name: LST AGFCDRCHLMAP（查询话单通道一级目录映射表配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AGFCDRCHLMAP
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 话单通道映射表
status: active
---

# LST AGFCDRCHLMAP（查询话单通道一级目录映射表配置）

## 功能

**适用NF：NCG**

该命令用于查询OCS NFINSTANCEID与话单通道一级目录映射关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | OCS的NFINSTANCEID值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定OCS的NFINSTANCEID值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~40。NFINSTANCEID必须来源于PNFPROFILE命令中NFINSTANCEID参数。<br>默认值：无<br>配置原则：无 |
| FIELDTYPE | 决定话单通道分拣的字段 | 可选必选说明：可选参数<br>参数含义：该参数用于指定决定话单分拣的字段。<br>数据来源：本端规划<br>取值范围：<br>- SUPI_GPSI（SUPI或GPSI）<br>- APN（APN）<br>默认值：无<br>配置原则：无 |
| CDRFIRSTDIR | 话单通道一级目录名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定话单一级目录名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~30。当FIELDTYPE取值为SUPI_GPSI时，CDRFIRSTDIR只能填00~31通道名。当FIELDTYPE取值为APN时，CDRFIRSTDIR只能填JASPER、IOT、DEFAULT通道。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [话单通道一级目录映射表（AGFCDRCHLMAP）](configobject/UNC/20.15.2/AGFCDRCHLMAP.md)

## 使用实例

查询FIELDTYPE为SUPI_GPSI的话单通道一级目录映射关系：

```
%%LST AGFCDRCHLMAP:;%%
RETCODE = 0  Operation succeeded
The result is as follows
------------------------
                                 OCS NFINSTANCEID  =  00000000-0000-0000-c000-000000000046
Fields that determine CDR channel sorting  =  SUPI or GPSI
                         CDR First Directory  =  01
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单通道一级目录映射表配置（LST-AGFCDRCHLMAP）_79296320.md`
