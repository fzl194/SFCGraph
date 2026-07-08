---
id: UDG@20.15.2@MMLCommand@LST APNALIAS
type: MMLCommand
name: LST APNALIAS（查询ApnAlias配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNALIAS
command_category: 查询类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- APN管理
- 别名APN
status: active
---

# LST APNALIAS（查询ApnAlias配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查看APN别名，当需要查看配置的APN别名和APN名称的对应关系时，使用该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNTYPE | APN类型 | 可选必选说明：必选参数<br>参数含义：该参数决定输入名称是真实APN还是APN别名。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ALIAS_APN：指示输入APN别名。<br>- REAL_APN：指示输入真实APN。<br>默认值：无<br>配置原则：<br>- 如果运营商希望输入真实APN，则把ApnType置成REAL_APN。<br>- 如果运营商希望输入APN别名，则把ApnType置成ALIAS_APN。 |
| ALIASNAME | APN别名的配置 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APNTYPE”配置为“ALIAS_APN”时为必选参数。<br>参数含义：该参数用于指定APN别名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“_”、“#”、“$”和“&”，不区分大小写。<br>默认值：无<br>配置原则：无 |
| APN | APN名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“APNTYPE”配置为“REAL_APN”时为必选参数。<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格及特殊字符“_”、“#”、“$”和“&”，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNALIAS]] · ApnAlias配置（APNALIAS）

## 使用实例

- 当需要查询指定的APN别名时：
  ```
  LST APNALIAS: APNTYPE=ALIAS_APN,ALIASNAME="1";
  ```
  ```

  RETCODE = 0  操作成功。

  APN别名信息
  -----------
            APN别名  =  1
            APN名称  =  ma
        锁定APN别名  =  不使能
  锁定指定spu-group  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 当需要查询指定APN下配置的所有APN别名时，使用该命令：
  ```
  LST APNALIAS: APNTYPE=REAL_APN,APN="ma";
  ```
  ```

  RETCODE = 0  操作成功。

  APN别名信息
  -----------
  APN别名    APN名称    锁定APN别名    锁定指定spu-group

  1          ma         不使能         NULL             
  2          ma         不使能         NULL             
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ApnAlias配置（LST-APNALIAS）_82837025.md`
