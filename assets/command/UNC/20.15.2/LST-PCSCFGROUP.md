---
id: UNC@20.15.2@MMLCommand@LST PCSCFGROUP
type: MMLCommand
name: LST PCSCFGROUP（查询P-CSCF组配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PCSCFGROUP
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
- P-CSCF组
status: active
---

# LST PCSCFGROUP（查询P-CSCF组配置）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询p-cscf组信息。

## 注意事项

查询指定P-CSCF组的配置信息时，必须输入P-CSCF组名。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | P-CSCF组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定P-CSCF组的名字，在系统内唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFGROUP]] · P-CSCF组配置（PCSCFGROUP）

## 使用实例

- 查询指定p-cscf组配置记录，如果没有配置，查询记录为零：
  ```
  LST PCSCFGROUP:GROUPNAME="mygroup";
  RETCODE = 0  操作成功。

  P-CSCF组配置信息:
  -----------------
      P-CSCF组名  =  mygroup
      IP地址版本  =  IPV4
      P-CSCF获取方式  =  本地分配
      查询方式  =  P-CSCF组
  (结果个数 = 1)
  ---    END
  ```
- 查询整机p-cscf组配置记录，如果没有配置，查询记录为零：
  ```
  LST PCSCFGROUP:;
  RETCODE = 0  操作成功。

  P-CSCF组配置信息:
  -----------------
  P-CSCF组名    IP地址版本     P-CSCF获取方式   查询方式  

  mygroup        IPV4          本地分配          P-CSCF组              
  test           IPV4          本地分配          P-CSCF组
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询P-CSCF组配置（LST-PCSCFGROUP）_09654405.md`
