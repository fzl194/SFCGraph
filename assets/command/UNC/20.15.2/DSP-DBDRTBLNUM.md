---
id: UNC@20.15.2@MMLCommand@DSP DBDRTBLNUM
type: MMLCommand
name: DSP DBDRTBLNUM（查询CSDB容灾主备本记录数）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DBDRTBLNUM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- CSDB功能管理
- CSDB管理
- 容灾管理
status: active
---

# DSP DBDRTBLNUM（查询CSDB容灾主备本记录数）

## 功能

该命令用于查询CSDB容灾主备本记录数。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INSTANCEID | 子实例ID | 可选必选说明：必选参数。<br>参数含义：该参数用于指定唯一一个子实例，可以通过<br>**[DSP DBINSTANCE](../实例管理/查询CSDB子实例信息（DSP DBINSTANCE）_29626987.md)**<br>命令查询获取。<br>数据来源：全网规划<br>取值范围：1~100。<br>默认值：无。 |
| TABLEID | 表ID | 可选必选说明：可选参数。<br>参数含义：该参数用于指定唯一一张数据表。<br>数据来源：全网规划<br>取值范围：0~4294967295。<br>默认值：无。 |
| DRNODETYPE | 数据主备类型 | 可选必选说明：可选参数。<br>参数含义：该参数用于指定查询数据主备类型。<br>数据来源：全网规划<br>取值范围：<br>- “DR_MASTER_NODE”：容灾主本数据<br>- “DR_SLAVE_NODE”容灾备本数据。<br>默认值：容灾主本数据。 |
| DRINSTID | 容灾实例ID | 可选必选说明：条件可选参数。<br>参数含义：表示备份了哪个容灾实例的容灾表数据。可以通过<br>**[LST DRCOMM](查询容灾实例地址(LST DRCOMM)_51012928.md)**<br>命令查询获取。该参数在<br>**“DRNODETYPE”**<br>是<br>“DR_SLAVE_NODE”<br>时生效。<br>数据来源：全网规划<br>取值范围：0～63。<br>默认值：无。 |

## 操作的配置对象

- [CSDB容灾主备本记录数（DBDRTBLNUM）](configobject/UNC/20.15.2/DBDRTBLNUM.md)

## 使用实例

查询CSDB **“子实例ID”** 为 “7” 的容灾主备本记录数：

```
DSP DBDRTBLNUM: INSTANCEID=7;
%%DSP DBDRTBLNUM: INSTANCEID=7;%%
RETCODE = 0  操作成功

操作结果如下：
--------------
子实例ID  表ID  表名称                  容灾记录数

7         201   GeoTable_dr_test            2
7         202   GeoTableCopy_dr_test        1
7         0     ALL                         3
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询CSDB容灾主备本记录数(DSP-DBDRTBLNUM)_49902501.md`
