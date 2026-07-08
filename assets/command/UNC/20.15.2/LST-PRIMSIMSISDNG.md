---
id: UNC@20.15.2@MMLCommand@LST PRIMSIMSISDNG
type: MMLCommand
name: LST PRIMSIMSISDNG（查询代理IMSI/MSISDN号段组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PRIMSIMSISDNG
command_category: 查询类
applicable_nf:
- PGW-C
- GGSN
- SGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- GGSN和P-GW Proxy
- 代理选择的IMSI_MSISDN号段组
status: active
---

# LST PRIMSIMSISDNG（查询代理IMSI/MSISDN号段组）

## 功能

**适用NF：PGW-C、GGSN、SGW-C、SMF**

该命令用于查询代理IMSI/MSISDN号段组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN号段组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRIMSIMSISDNG]] · 代理IMSI/MSISDN号段组（PRIMSIMSISDNG）

## 使用实例

查询“IMSI/MSISDN号段组名称”为“grp1”的代理IMSI/MSISDN号段组配置：

```
%%LST PRIMSIMSISDNG: SEGGROUPNAME="grp1";%%
RETCODE = 0  操作成功

结果如下
------------------------
IMSI/MSISDN号段组名称  IMSI/MSISDN号段名称  

grp1                   imsi1                     
grp1                   imsi2                     
grp1                   imsi3                     
grp1                   imsi4                     
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PRIMSIMSISDNG.md`
