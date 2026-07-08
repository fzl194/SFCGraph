---
id: UNC@20.15.2@MMLCommand@LST APNPCCFUNC
type: MMLCommand
name: LST APNPCCFUNC（查询APN PCC功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNPCCFUNC
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- 基本功能
- APN控制
status: active
---

# LST APNPCCFUNC（查询APN PCC功能）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询指定APN的动态PCC功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNPCCFUNC]] · APN PCC功能（APNPCCFUNC）

## 使用实例

- 查询APN isp的动态PCC功能状态：
  ```
  LST APNPCCFUNC:APN="isp";
  ```
  ```

  RETCODE = 0  操作成功。

  APN PCC功能参数
  ---------------
              APN名称  =  isp
  本地用户动态PCC功能  =  使能
  漫游用户动态PCC功能  =  继承全局配置
  拜访用户动态PCC功能  =  继承全局配置
          PCC模板名称  =  pcctp1
          选择PCF方式  =  NULL
  (结果个数 = 1)
  ---    END
  ```
- 查询所有APN的动态PCC功能状态：
  ```
  LST APNPCCFUNC:;
  ```
  ```
  %%
  RETCODE = 0  操作成功。

  APN PCC功能参数
  ---------------
  APN名称      本地用户动态PCC功能  漫游用户动态PCC功能  拜访用户动态PCC功能  PCC模板名称  选择PCF方式  

  apn          继承全局配置         继承全局配置         继承全局配置         NULL         NULL         
  apn01        继承全局配置         继承全局配置         继承全局配置         NULL         NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNPCCFUNC.md`
