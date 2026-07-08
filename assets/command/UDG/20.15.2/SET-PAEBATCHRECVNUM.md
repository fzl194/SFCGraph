---
id: UDG@20.15.2@MMLCommand@SET PAEBATCHRECVNUM
type: MMLCommand
name: SET PAEBATCHRECVNUM（设置PAE批量收包的数量）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: PAEBATCHRECVNUM
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 时延统计
status: active
---

# SET PAEBATCHRECVNUM（设置PAE批量收包的数量）

## 功能

![](设置PAE批量收包的数量（SET PAEBATCHRECVNUM）_35145969.assets/notice_3.0-zh-cn.png)

PAE的批收数与转发性能有关，设置不当会降低转发性能。

该命令用于设置PAE批量收包的数量。

> **说明**
> - 该命令执行后立即生效。
>
> - 设置批收数的对象包括：普通channel、svc channel、外联口channel、外联口、fabric口。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NUMBER | PAE批收数量 | 可选必选说明：必选参数<br>参数含义：该参数表示PAE批量收包的数量。<br>数据来源：本端规划<br>取值范围：<br>- “PAE_BATCHNUM_64（批收数64）”：批收数64<br>- “PAE_BATCHNUM_96（批收数96）”：批收数96<br>- “PAE_BATCHNUM_128（批收数128）”：批收数128<br>- “PAE_BATCHNUM_160（批收数160）”：批收数160<br>- “PAE_BATCHNUM_192（批收数192）”：批收数192<br>- “PAE_BATCHNUM_224（批收数224）”：批收数224<br>默认值：无。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/PAEBATCHRECVNUM]] · PAE批量接收报文数（PAEBATCHRECVNUM）

## 使用实例

设置PAE批量收包数量：

```
+++    UNC/*MEID:0 MENAME:project-v6*/        2024-01-24 14:40:06
O&M    #173
%%SET PAEBATCHRECVNUM: NUMBER=PAE_BATCHNUM_224;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置PAE批量收包的数量（SET-PAEBATCHRECVNUM）_35145969.md`
