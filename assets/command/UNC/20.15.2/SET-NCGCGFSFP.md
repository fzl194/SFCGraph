---
id: UNC@20.15.2@MMLCommand@SET NCGCGFSFP
type: MMLCommand
name: SET NCGCGFSFP（设置软参）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NCGCGFSFP
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
max_records: 5000
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- NCG大颗粒软参
status: active
---

# SET NCGCGFSFP（设置软参）

## 功能

**适用NF：NCG**

该命令用于设置NCG大颗粒软参。

## 注意事项

- 该命令生效方式参考具体的软参说明。
- 该命令最大记录数为5000。
- 该命令存在系统初始设置记录，所有默认记录的软参值都为0。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFPID | 软参ID | 可选必选说明：必选参数<br>参数含义：用于表示NCG大颗粒软参ID，可以使用<br>**LST NCGCGFSFP**<br>命令查询获得。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4999。<br>默认值：无<br>配置原则：无 |
| SFPVALUE | 软参值 | 可选必选说明：必选参数<br>参数含义：用于表示NCG大颗粒软参值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [软参（NCGCGFSFP）](configobject/UNC/20.15.2/NCGCGFSFP.md)

## 使用实例

设置NCG大颗粒软参，将“软参ID”为“1”的“软参值”设置为“10”：

```
SET NCGCGFSFP: SFPID=1, SFPVALUE=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置软参（SET-NCGCGFSFP）_85862272.md`
