---
id: UNC@20.15.2@MMLCommand@LST APNPFCPCMPT
type: MMLCommand
name: LST APNPFCPCMPT（查询指定APN的PFCP私有信元携带配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNPFCPCMPT
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- 基于APN的PFCP私有信元管理
status: active
---

# LST APNPFCPCMPT（查询指定APN的PFCP私有信元携带配置）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询指定APN的PFCP私有信元携带配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：<br>输入的APN名称需要符合APN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”；该参数取值应与ADD APN命令中参数“APN”保持一致，使用该前需通过ADD APN添加一组记录。 |

## 操作的配置对象

- [指定APN的PFCP私有信元携带配置（APNPFCPCMPT）](configobject/UNC/20.15.2/APNPFCPCMPT.md)

## 使用实例

- 查询APN名称为“huawei.com”时，PFCP私有信元携带配置：
  ```
  %%LST APNPFCPCMPT: APN="huawei.com";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                    APN名称  =  huawei.com
  SMF给SGW-U携带承载级CreateQer信元控制开关  =  ENABLE
                SMF给UPF携带Qci信元控制开关  =  ENABLE
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的PFCP私有信元携带配置：
  ```
  %%LST APNPFCPCMPT:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称         SMF给SGW-U携带承载级CreateQer信元控制开关  SMF给UPF携带Qci信元控制开关

  huawei.com      ENABLE                                     ENABLE                      
  huawei2.com     DISABLE                                    INHERIT
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询指定APN的PFCP私有信元携带配置（LST-APNPFCPCMPT）_93587564.md`
