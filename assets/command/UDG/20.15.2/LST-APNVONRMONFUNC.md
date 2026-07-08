---
id: UDG@20.15.2@MMLCommand@LST APNVONRMONFUNC
type: MMLCommand
name: LST APNVONRMONFUNC（查询VoNR语音质量监控功能开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNVONRMONFUNC
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- VoNR质量监控配置
- APN VoNR语音质量检测功能
status: active
---

# LST APNVONRMONFUNC（查询VoNR语音质量监控功能开关）

## 功能

**适用NF：UPF**

该命令用于查询指定APN实例或者已配置所有APN实例的VoNR语音质量监控功能开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APNVONRMONFUNC]] · VoNR语音质量监控功能开关（APNVONRMONFUNC）

## 使用实例

- 查询指定APN实例的VoNR语音质量监控功能开关：
  ```
  LST APNVONRMONFUNC: APN="apn1.com";
  ```
  ```

  RETCODE = 0  操作成功

  VoNR语音质量监控开关
  --------------------
                       APN  =  apn1.com
  VoNR语音质量监控功能开关  =  使能（开启）
  (结果个数 = 1)
  ---    END
  ```
- 查询整机APN实例的VoNR语音质量监控功能开关：
  ```
  LST APNVONRMONFUNC:;
  ```
  ```

  RETCODE = 0  操作成功

  VoNR语音质量监控开关
  --------------------
  APN       VoNR语音质量监控功能开关  

  apn1.com  使能（开启）              
  apn2.com  使能（开启）              
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNVONRMONFUNC.md`
