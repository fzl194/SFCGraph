---
id: UDG@20.15.2@MMLCommand@LST USERSELATTR
type: MMLCommand
name: LST USERSELATTR（显示用户选择属性）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERSELATTR
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 用户选择属性
status: active
---

# LST USERSELATTR（显示用户选择属性）

## 功能

**适用NF：UPF**

该命令用来查询用户选择策略的属性配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NAME | 用户选择属性集合配置名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置规则名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，单位是字节。只能由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：name必须是已经添加。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERSELATTR]] · 用户选择属性（USERSELATTR）

## 使用实例

- 查询名为test用户选择属性列表信息：
  ```
  LST USERSELATTR: NAME="test";
  ```
  ```

  RETCODE = 0 Operation succeeded

  用户选择属性列表
  --------------------------
  名字 = test
  属性编号 = 0
  用户属性类型 = N2TAC
  起始ID = 0x000001
  截止ID = 0x000002
  (结果个数= 1)
  ```
- 查询所有的用户选择属性列表信息：
  ```
  LST USERSELATTR:;
  ```
  ```

  RETCODE = 0  Operation succeeded

  用户选择属性列表
  --------------------------
  名字 = test
  属性编号 = 0
  用户属性类型 = N2TAC
  起始ID = 0x000001
  截止ID = 0x000002
  (结果个数= 1)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示用户选择属性（LST-USERSELATTR）_86133380.md`
