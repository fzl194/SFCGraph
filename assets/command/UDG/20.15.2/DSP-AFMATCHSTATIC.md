---
id: UDG@20.15.2@MMLCommand@DSP AFMATCHSTATIC
type: MMLCommand
name: DSP AFMATCHSTATIC（查询HTTP欺诈场景的统计结果）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: AFMATCHSTATIC
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- HTTP欺诈场景的匹配情况统计
status: active
---

# DSP AFMATCHSTATIC（查询HTTP欺诈场景的统计结果）

## 功能

**适用NF：PGW-U、UPF**

该命令用来查询所有HTTP欺诈场景的匹配情况统计结果，或者根据指定的防欺诈数据库场景ID查询统计结果。

## 注意事项

如果长时间统计，可能导致统计计数翻转后不准确。建议在执行本命令之前通过CLR AFMATCHSTATIC命令对计数进行重置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFMATCHTYPE | 欺诈场景类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定欺诈场景类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AF_DATABASE：防欺诈库定义的欺诈场景。<br>- AF_SOFTWARE：软参定义的欺诈场景。<br>默认值：AF_DATABASE<br>配置原则：无 |
| SCENARIOID | 防欺诈数据库场景ID | 可选必选说明：条件可选参数<br>前提条件：该参数在“AFMATCHTYPE”配置为“AF_DATABASE”时为可选参数。<br>参数含义：该参数用于指定防欺诈数据库场景ID。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@AFMATCHSTATIC]] · HTTP欺诈场景的统计结果（AFMATCHSTATIC）

## 使用实例

- 查询防欺诈数据库场景ID为2的匹配情况统计结果：
  ```
  DSP AFMATCHSTATIC: AFMATCHTYPE=AF_DATABASE,SCENARIOID=2;
  ```
  ```

  RETCODE = 0  操作成功。

  基于欺诈库场景的统计
  -----------------------------------------------
  防欺诈数据库场景ID = 2
  匹配上此场景的次数 = 1
          上行报文数 = 6
          上行字节数 = 3252
          下行报文数 = 34
          下行字节数 = 16341
  (结果个数 = 1)
  ---    END
  ```
- 查询软参欺诈场景的匹配情况统计结果：
  ```
  DSP AFMATCHSTATIC:AFMATCHTYPE=AF_SOFTWARE;
  ```
  ```

  RETCODE = 0  操作成功。

  基于软参欺诈场景的统计
  ----------------------
  防欺诈数据库场景ID    匹配上此场景的次数    软参欺诈场景名称                        

  1                     2                     byte629_check_protocol_version          
  2                     2                     byte629_check_protocol_host_different   
  3                     2                     byte629_check_protocol_host_contain_@   
  4                     2                     byte629_check_protocol_more_host        
  5                     2                     byte629_check_protocol_more_xonline_host
  6                     2                     byte629_check_protocol_autostudy        
  7                     2                     byte629_check_protocol_uri_comply_RFC   
  (结果个数 = 7)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-AFMATCHSTATIC.md`
