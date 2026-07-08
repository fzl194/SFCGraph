---
id: UNC@20.15.2@MMLCommand@LST TSTPCFBINDING
type: MMLCommand
name: LST TSTPCFBINDING（查询拨测用户和PCF的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: TSTPCFBINDING
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- PCF发现和选择管理
- PCF拨测管理
status: active
---

# LST TSTPCFBINDING（查询拨测用户和PCF的绑定关系）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询拨测用户和PCF的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数来源于ADD APN中的“APN名称”参数， 需要符合APN命名规则。 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：本参数用于指定用户IMSI。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是6~15。每个字符只能是十进制数字。<br>默认值：无<br>配置原则：<br>该参数不支持号段前缀匹配。 |
| PCFINSTANCEID | PCF实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定PCF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~50。构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，大小写敏感。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [拨测用户和PCF的绑定关系（TSTPCFBINDING）](configobject/UNC/20.15.2/TSTPCFBINDING.md)

## 使用实例

- 查询IMSI是"123456789012345"，APN是"testAPn"的用户激活到PCFINSTANCEID是“testPcfInstanceId”的PCF的配置。
  ```
  LST TSTPCFBINDING:APN="testAPN",IMSI="123456789012345";
  RETCODE = 0  操作成功

  结果如下
  --------
      APN名称  =  testAPn
         IMSI  =  123456789012345
  PCF实例标识  =  tstPcfInstanceId
  (结果个数 = 1)

  ---    END
  ```
- 查询所有配置。
  ```
  LST TSTPCFBINDING:;
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称  IMSI            PCF实例标识  

  apn2     32345678901234  tstid        
  apn2     42345678901234  tstid       
  apn2     52345678901234  tstid     
  apn2     62345678901234  tstid  
  apn2     72345678901234  tstid   
  (结果个数 = 5)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询拨测用户和PCF的绑定关系（LST-TSTPCFBINDING）_77037096.md`
