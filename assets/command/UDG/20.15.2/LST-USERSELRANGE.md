---
id: UDG@20.15.2@MMLCommand@LST USERSELRANGE
type: MMLCommand
name: LST USERSELRANGE（显示用户选择范围列表）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERSELRANGE
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 用户选择范围
status: active
---

# LST USERSELRANGE（显示用户选择范围列表）

## 功能

**适用NF：UPF**

该命令用来查询用户选择范围的属性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 用户选择范围名称 | 可选必选说明：可选参数<br>参数含义：用户选择范围集合配置名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，单位是字节。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：name 必须是已添加。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERSELRANGE]] · 用户选择范围列表（USERSELRANGE）

## 使用实例

- 查询名为test用户选择属性列表信息：
  ```
  LST USERSELRANGE：NAME ="test";
  ```
  ```
 
  RETCODE = 0   Operation succeeded

  用户选择属性列表
  --------------------------
  名字 = test
  用户范围类型 = APN
  APN = test.apn
  SNSSAI = NULL
  (结果个数= 1)
  ```
- 查询所有的策略配置信息：
  ```
  LST USERSELRANGE:;
  ```
  ```

  RETCODE = 0  Operation succeeded
  用户选择属性列表
  --------------------------
  名字 = test
  用户范围类型 = APN
  APN = test.apn
  SNSSAI = NULL
  (结果个数= 1)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-USERSELRANGE.md`
