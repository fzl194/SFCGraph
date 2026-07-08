---
id: UNC@20.15.2@MMLCommand@LST SUBSCRIBERIDSEGGRP
type: MMLCommand
name: LST SUBSCRIBERIDSEGGRP（查询IMSI/MSISDN/IMEISV号段组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SUBSCRIBERIDSEGGRP
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务公共
- IMSI MSISDN IMEISV号段组
status: active
---

# LST SUBSCRIBERIDSEGGRP（查询IMSI/MSISDN/IMEISV号段组）

## 功能

**适用NF：PGW-C、SMF**

该命令用来显示本地所有已配置的IMSI/MSISDN/IMEISV号码段组信息，或者根据号码段组的名称来显示指定IMSI/MSISDN/IMEISV号码段组的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGGROUPNAME | IMSI/MSISDN/IMEISV号段组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUBSCRIBERIDSEGGRP]] · IMSI/MSISDN/IMEISV号段组（SUBSCRIBERIDSEGGRP）

## 使用实例

- 查询IMSI/MSISDN/IMEISV号码段组信息，其中IMSI/MSISDN/IMEISV号段组名称为group1：
  ```
  LST SUBSCRIBERIDSEGGRP: SEGGROUPNAME="group1";
  ```
  ```

  RETCODE = 0 Operation succeeded

  IMSI/MSISDN/IMEISV号段组信息
  --------------------------------------------
  IMSI/MSISDN/IMEISV号段组名称 = group1
  IMSI/MSISDN/IMEISV号段名称 = huawei
  号段类型 = IMEISV
  (结果个数 = 1)

  --- END
  ```
- 查询所有IMSI/MSISDN/IMEISV号码段组信息：
  ```
  LST SUBSCRIBERIDSEGGRP:;
  ```
  ```

  RETCODE = 0 Operation succeeded

  IMSI/MSISDN/IMEISV号段组信息
  --------------------------------------------
  IMSI/MSISDN/IMEISV号段组名称 = group1
  IMSI/MSISDN/IMEISV号段名称 = huawei
  号段类型 = IMEISV
  (结果个数 = 1)

  --- END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SUBSCRIBERIDSEGGRP.md`
