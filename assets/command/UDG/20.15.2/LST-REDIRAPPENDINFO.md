---
id: UDG@20.15.2@MMLCommand@LST REDIRAPPENDINFO
type: MMLCommand
name: LST REDIRAPPENDINFO（查询重定向携带信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: REDIRAPPENDINFO
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 重定向控制
- 重定向公共参数管理
- 重定向携带信息
status: active
---

# LST REDIRAPPENDINFO（查询重定向携带信息）

## 功能

**适用NF：PGW-U、UPF**

此命令用于运营商查询已经配置的重定向携带信息，可以查询原始URL、MSISDN、IMSI、IMEI、MSIP、时间戳信息的携带配置以及对携带MSISDN、IMSI、IMEI、MSIP、时间戳信息的加密算法等。

## 注意事项

输入APPENDINFONAME查询指定记录，如果不输入APPENDINFONAME表示查询所有记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPENDINFONAME | 重定向携带信息名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置重定向携带信息名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不区分大小写，不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@REDIRAPPENDINFO]] · 重定向携带信息（REDIRAPPENDINFO）

## 使用实例

- 查询所有重定向携带信息：
  ```
  LST REDIRAPPENDINFO:;
  ```
  ```

  RETCODE = 0  操作成功

  重定向携带信息
  --------------
  重定向携带信息名称    请求URL名称  IMSI名称  请求URL标识   IMSI携带标识  IMEI携带标识  IMSI密码  时间戳类型  IMEI名称  MSISDN名称  时间戳密码  MSISDN携带标识  MSISDN密码  MSIP携带标识  时间戳携带标识  时间戳加密算法  MSIP名称  时间戳名称  配置域名称  MSISDN加密算法 IMEI密码  IMSI加密算法   IMEI加密算法  MSIP加密算法   MSIP密码  
                                                                                                                                                                                                                                                                                                                                                                                 
  testredirappendinfo   dest_url     imsi      使能（开启）  使能（开启）  使能（开启）  *****     本地时间    imei      msisdn      *****       使能（开启）    *****       使能（开启）  使能（开启）    NONE         msip      u           NULL        NONE       *****     NONE      NONE      NONE      *****     
  testredirappendinfo2  dest_url     imsi      使能（开启）  使能（开启）  使能（开启）  *****     本地时间    imei      msisdn      *****       使能（开启）    *****       使能（开启）  使能（开启）    AES128，有安全风险，不建议使用         msip      u           NULL        AES256，有安全风险，不建议使用       *****     AES256，有安全风险，不建议使用      AES256，有安全风险，不建议使用      AES256，有安全风险，不建议使用     *****     
  (结果个数 = 2)

  ---    END
  ```
- 查询名为“testredirappendinfo”的重定向携带信息：
  ```
  LST REDIRAPPENDINFO: APPENDINFONAME="testredirappendinfo";
  ```
  ```

  RETCODE = 0  操作成功

  重定向携带信息
  --------------
  重定向携带信息名称  =  testredirappendinfo
         请求URL名称  =  dest_url
            IMSI名称  =  imsi
         请求URL标识  =  使能（开启）
        IMSI携带标识  =  使能（开启）
        IMEI携带标识  =  使能（开启）
            IMSI密码  =  *****
          时间戳类型  =  本地时间
            IMEI名称  =  imei
          MSISDN名称  =  msisdn
          时间戳密码  =  *****
      MSISDN携带标识  =  使能（开启）
          MSISDN密码  =  *****
        MSIP携带标识  =  使能（开启）
      时间戳携带标识  =  使能（开启）
      时间戳加密算法  =  NONE
            MSIP名称  =  msip
          时间戳名称  =  u
          配置域名称  =  NULL
      MSISDN加密算法  =  NONE
            IMEI密码  =  *****
        IMSI加密算法  =  NONE
        IMEI加密算法  =  NONE
        MSIP加密算法  =  NONE
            MSIP密码  =  *****
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-REDIRAPPENDINFO.md`
