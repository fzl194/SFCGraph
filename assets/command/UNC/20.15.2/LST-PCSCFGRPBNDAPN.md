---
id: UNC@20.15.2@MMLCommand@LST PCSCFGRPBNDAPN
type: MMLCommand
name: LST PCSCFGRPBNDAPN（查询APN和P-CSCF组关联关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCSCFGRPBNDAPN
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF组与APN关联关系
status: active
---

# LST PCSCFGRPBNDAPN（查询APN和P-CSCF组关联关系）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询APN与P-CSCF组之间的关系。可基于IMSI/MSISDN号段查询。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IMSI/MSISDN号段名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：<br>该参数使用ADD PCSCFIMSISDNSEG命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFGRPBNDAPN]] · APN和P-CSCF组关联关系（PCSCFGRPBNDAPN）

## 使用实例

- 查询指定APN下所有的P-CSCF组绑定关系：
  ```
  LST PCSCFGRPBNDAPN: APN="huawei.com";
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称     IMSI/MSISDN号段名称  缺省标记         优先级  主IPv4P-CSCF组  备IPv4P-CSCF组  主IPv6P-CSCF组  备IPv6P-CSCF组  

  huawei.com  NULL                 缺省             0       mygroup         NULL            NULL            NULL            
  huawei.com  mypcscfimsisdnseg    IMSI/MSISDN号段  1       mygroup         NULL            NULL            NULL            
  (结果个数 = 2)

  ---    END
  ```
- 查询APN下指定号段和P-CSCF组绑定关系：
  ```
  LST PCSCFGRPBNDAPN: APN="huawei.com", IMSIMSISDNSEG="mypcscfimsisdnseg";
  RETCODE = 0  操作成功

  结果如下
  --------
              APN名称  =  huawei.com
  IMSI/MSISDN号段名称  =  mypcscfimsisdnseg
             缺省标记  =  IMSI/MSISDN号段
               优先级  =  1
       主IPv4P-CSCF组  =  mygroup
       备IPv4P-CSCF组  =  NULL
       主IPv6P-CSCF组  =  NULL
       备IPv6P-CSCF组  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PCSCFGRPBNDAPN.md`
