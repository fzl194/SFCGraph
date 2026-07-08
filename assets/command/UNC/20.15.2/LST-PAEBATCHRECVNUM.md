---
id: UNC@20.15.2@MMLCommand@LST PAEBATCHRECVNUM
type: MMLCommand
name: LST PAEBATCHRECVNUM（查询PAE批量收包的数量）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PAEBATCHRECVNUM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 时延统计
status: active
---

# LST PAEBATCHRECVNUM（查询PAE批量收包的数量）

## 功能

该命令用于查询PAE批量收包的数量。

## 注意事项

- 该命令查询结果为记录在OM DB中的值，即[**SET PAEBATCHRECVNUM**](设置PAE批量收包的数量（SET PAEBATCHRECVNUM）_35145969.md)命令所配置的原始值。
- 查询实际生效值请使用[**DSP PAEBATCHRECVNUM**](显示PAE批量接收报文数（DSP PAEBATCHRECVNUM）_35145961.md)命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [PAE批量接收报文数（PAEBATCHRECVNUM）](configobject/UNC/20.15.2/PAEBATCHRECVNUM.md)

## 使用实例

查询PAE批量收包数量：

```
+++    UNC/*MEID:0 MENAME:project-v6*/        2024-01-24 14:39:30
O&M    #172
%%LST PAEBATCHRECVNUM:;%%
RETCODE = 0  操作成功

结果如下
--------
PAE批收数量  =  批收数224
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询PAE批量收包的数量（LST-PAEBATCHRECVNUM）_35145965.md`
