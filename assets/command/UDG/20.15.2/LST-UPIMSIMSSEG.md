---
id: UDG@20.15.2@MMLCommand@LST UPIMSIMSSEG
type: MMLCommand
name: LST UPIMSIMSSEG（查询IMSI和MSISDN号段）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPIMSIMSSEG
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务匹配公共配置
- 业务公共参数管理
- IMSI MSISDN号段
status: active
---

# LST UPIMSIMSSEG（查询IMSI和MSISDN号段）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询IMSI/MSISDN号码段。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPIMSIMSSEG]] · IMSI和MSISDN号段（UPIMSIMSSEG）

## 使用实例

- 查询IMSI和MSISDN号段：
  ```
  LST UPIMSIMSSEG:;
  ```
  ```

  RETCODE = 0  操作成功。

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称  =  imsi
  IMSI/MSISDN号段类型  =  IMSI
       号段起始字符串  =  1
       号段结束字符串  =  2
           配置域名称  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有IMSI和MSISDN号段：
  ```
  LST UPIMSIMSSEG:;
  ```
  ```

  RETCODE = 0  操作成功。

  IMSI或MSISDN号段信息
  --------------------
  IMSI/MSISDN号段名称    IMSI/MSISDN号段类型    号段起始字符串    号段结束字符串    配置域名称

  huawei                 IMSI                   130               139               NULL      
  huawei1                IMSI                   130               139               NULL      
  imsi                   IMSI                   1                 2                 NULL           
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询IMSI和MSISDN号段（LST-UPIMSIMSSEG）_86561854.md`
