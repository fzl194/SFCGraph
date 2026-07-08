---
id: UNC@20.15.2@MMLCommand@LST APNUPRECOVER
type: MMLCommand
name: LST APNUPRECOVER（查询指定UPF的APN级别链路故障恢复处理）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNUPRECOVER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP故障管理
- N4接口故障恢复处理
status: active
---

# LST APNUPRECOVER（查询指定UPF的APN级别链路故障恢复处理）

## 功能

**适用NF：SMF**

该命令用于在UPF主备容灾场景下，查询指定UPF的APN级别链路故障恢复处理。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置APN名称。该参数已经通过ADD APN命令中的APN参数配置。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需在ADD APN中进行配置。 |
| MASTERUPFID | 主UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置主UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写。不支持配置单空格。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNUPRECOVER]] · 指定UPF的APN级别链路故障恢复处理（APNUPRECOVER）

## 使用实例

- 查询所有APN下配置的所有主UPF的链路故障恢复处理：
  ```
  %%LST APNUPRECOVER:;%%
  RETCODE = 0	 操作成功

  结果如下
  --------
  APN名称            主UPF实例名称               UP链路故障恢复处理模式                  备UPF实例名称
  apn1               master_upf_1                Back Migration                          back_upf_1                           
  apn2               master_upf_2                Back Migration                          back_upf_2
  (结果个数 = 2)

  ---	   END
  ```
- 查询指定APN为“apn1”下配置的所有主UPF的链路故障恢复处理：
  ```
  %%LST APNUPRECOVER:APN="apn1";%%
  RETCODE = 0	 操作成功

  结果如下
  --------
                          APN名称    =    apn1 
                    主UPF实例名称    =    master_upf_1 
           UP链路故障恢复处理模式    =    Back Migration          
                    备UPF实例名称    =    back_upf_1                                   
  (结果个数 = 1)

  ---	   END
  ```
- 查询指定主UPF为“master_upf_2”下配置的所有APN的链路故障恢复处理：
  ```
  %%LST APNUPRECOVER:MASTERUPFID="master_upf_2";%%
  RETCODE = 0	 操作成功

  结果如下
  --------
  APN名称            主UPF实例名称               UP链路故障恢复处理模式                  备UPF实例名称
  apn1               master_upf_2                No Handling                              
  apn2               master_upf_2                Back Migration                          back_upf_2
  (结果个数 = 2)

  ---	   END
  ```
- 查询APN为“apn1”，主UPF为“master_upf_1”的链路故障恢复处理：
  ```
  %%LST APNUPRECOVER:APN="apn1",MASTERUPFID="master_upf_1";%%
  RETCODE = 0	 操作成功

  结果如下
  --------
                          APN名称    =    apn1 
                    主UPF实例名称    =    master_upf_1 
           UP链路故障恢复处理模式    =    Back Migration          
                    备UPF实例名称    =    back_upf_1                          
  (结果个数 = 1)

  ---	   END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNUPRECOVER.md`
