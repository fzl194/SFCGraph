---
id: UNC@20.15.2@MMLCommand@LST PRIMSIMSISDNSEG
type: MMLCommand
name: LST PRIMSIMSISDNSEG（查询代理IMSI/MSISDN号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PRIMSIMSISDNSEG
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
- 代理选择的IMSI_MSISDN号段
status: active
---

# LST PRIMSIMSISDNSEG（查询代理IMSI/MSISDN号段）

## 功能

**适用NF：PGW-C、GGSN、SGW-C、SMF**

该命令用于查询代理IMSI/MSISDN号段。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定信令代理特性所使用的IMSI/MSISDN号码段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRIMSIMSISDNSEG]] · 代理IMSI/MSISDN号段（PRIMSIMSISDNSEG）

## 使用实例

- 查询“IMSI/MSISDN号段名称”为“imsi1”的代理IMSI/MSISDN号段配置：
  ```
  %%LST PRIMSIMSISDNSEG: SEGMENTNAME="imsi1";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  IMSI/MSISDN号段名称  =  imsi1
  IMSI/MSISDN号段类型  =  IMSI Type
       号段起始字符串  =  460000000000000
       号段结束字符串  =  469999999999999
       通配号段字符串  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有代理IMSI/MSISDN号段配置：
  ```
  %%LST PRIMSIMSISDNSEG:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  IMSI/MSISDN号段名称  IMSI/MSISDN号段类型  号段起始字符串  号段结束字符串  通配号段字符串  

  imsi1                IMSI类型             460000000000000 469999999999999 NULL                     
  imsi2                IMSI类型             460000000000000 469999999999999 NULL                     
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PRIMSIMSISDNSEG.md`
