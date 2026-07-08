---
id: UDG@20.15.2@MMLCommand@LST USERSELPLCY
type: MMLCommand
name: LST USERSELPLCY（查询用户策略选择）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USERSELPLCY
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务运维
- 业务性能统计管理
- 用户策略选择
status: active
---

# LST USERSELPLCY（查询用户策略选择）

## 功能

**适用NF：UPF**

该命令用来查看指定用户选择策略的配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 用户选择策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户选择策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。只能由“-”、“_”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USERSELPLCY]] · 用户策略选择（USERSELPLCY）

## 使用实例

- 查询用户选择策略名为policy1的策略信息：
  ```
  LST USERSELPLCY: POLICYNAME="policy1";
  ```
  ```

  RETCODE = 0  操作成功

  用户选择策略
  ---------------------
            用户选择策略名称  =  policy1
                        策略类型 =  USERANGE
      用户选择策略范围名称  =  range1
      用户选择策略属性名称  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询所有的策略信息：
  ```
  LST USERSELPLCY:;
  ```
  ```

  RETCODE = 0  操作成功

  用户选择策略名称
  ---------------------
  用户选择策略名称  策略类型  用户选择策略范围名称  用户选择策略范围名称 

            policy1      USERANGE     range1             NULL                   
            policy2      USERANGE     NULL               attr1                  
  (结果个数 = 2)
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户策略选择（LST-USERSELPLCY）_83909790.md`
