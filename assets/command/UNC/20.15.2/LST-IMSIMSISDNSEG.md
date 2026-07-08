---
id: UNC@20.15.2@MMLCommand@LST IMSIMSISDNSEG
type: MMLCommand
name: LST IMSIMSISDNSEG（查询IMSI和MSISDN号段）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IMSIMSISDNSEG
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
- IMSI MSISDN号段
status: active
---

# LST IMSIMSISDNSEG（查询IMSI和MSISDN号段）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询IMSI/MSISDN号码段。

## 注意事项

LST IMSIMSISDNSEG时如果显示有%3f表示的是通配符“？”。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：如果参数不提供则查询所有IMSI/MSISDN号码段。 |

## 操作的配置对象

- [IMSI和MSISDN号段（IMSIMSISDNSEG）](configobject/UNC/20.15.2/IMSIMSISDNSEG.md)

## 使用实例

- 查询IMSI和MSISDN号段：
  ```
  LST IMSIMSISDNSEG: SEGMENTNAME="huawei";
  ```
  ```

  RETCODE = 0  操作成功

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称  =  huawei
  IMSI/MSISDN号段类型  =  IMSI
       号段起始字符串  =  130
       号段结束字符串  =  139
       通配号段字符串  =  NULL
   锁定IMSIMSISDN号段  =  不使能
  (结果个数 = 1)

  ---    END
  ```
- 查询所有IMSI和MSISDN号段：
  ```
  LST IMSIMSISDNSEG:;
  ```
  ```

  RETCODE = 0  操作成功

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称  =  huawei
  IMSI/MSISDN号段类型  =  IMSI
       号段起始字符串  =  130
       号段结束字符串  =  139
       通配号段字符串  =  NULL
   锁定IMSIMSISDN号段  =  不使能
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询IMSI和MSISDN号段（LST-IMSIMSISDNSEG）_09897131.md`
