---
id: UDG@20.15.2@MMLCommand@LST APNNONIPFUNC
type: MMLCommand
name: LST APNNONIPFUNC（查询APN Non-IP功能配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: APNNONIPFUNC
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
- M2M管理
- APN的Non-IP配置
status: active
---

# LST APNNONIPFUNC（查询APN Non-IP功能配置）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询指定APN的网关Non-IP功能。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@APNNONIPFUNC]] · APN Non-IP功能配置（APNNONIPFUNC）

## 使用实例

- 显示指定APN的网关Non-IP功能状态：
  ```
  LST APNNONIPFUNC:APN="apn1.com";
  ```
  ```

  RETCODE = 0  操作成功。

  APN Non-IP功能配置
  ------------------
                 APN  =  apn1.com
  APN Non-IP功能开关  =  使能
          用户端口号  =  5638
  (结果个数 = 1)
  ---    END
  ```
- 查询整机APN的网关Non-IP功能状态：
  ```
  LST APNNONIPFUNC:;
  ```
  ```

  RETCODE = 0  操作成功。

  APN Non-IP功能配置
  ------------------
  APN           APN Non-IP功能开关    用户端口号
     
  apn1.com      使能                  5638      
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-APNNONIPFUNC.md`
