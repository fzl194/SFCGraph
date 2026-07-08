---
id: UDG@20.15.2@MMLCommand@LST APNIMSATTR
type: MMLCommand
name: LST APNIMSATTR（查询ApnImsAttr配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNIMSATTR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VOLTE管理
- APN的IMS属性
status: active
---

# LST APNIMSATTR（查询ApnImsAttr配置）

## 功能

**适用NF：UPF**

命令用来查询APN的IMS属性信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ApnImsAttr配置（APNIMSATTR）](configobject/UDG/20.15.2/APNIMSATTR.md)

## 使用实例

- 显示当前APN huawei.com的IMS属性信息：
  ```
  LST APNIMSATTR: APN="huawei.com";
  ```
  ```

  RETCODE = 0  操作成功。

  APN的IMS配置信息
  ----------------
           APN名称  =  huawei.com
           IMS开关  =  使能
  信令空口增强开关  =  使能
   (结果个数 = 1)
  ---    END
  ```
- 显示当前所有APN的IMS属性信息：
  ```
  LST APNIMSATTR:;
  ```
  ```

  RETCODE = 0  操作成功

  APN的IMS配置信息
  ----------------
  APN名称        IMS开关  

  testapn.com  使能         
  huawei.com     使能        
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询ApnImsAttr配置（LST-APNIMSATTR）_86527128.md`
