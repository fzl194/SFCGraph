---
id: UDG@20.15.2@MMLCommand@LST RPTPOLICY
type: MMLCommand
name: LST RPTPOLICY（查询基于策略的业务报表开关）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: RPTPOLICY
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 业务报表管理
- 报表本地策略管理
- 报表业务策略
status: active
---

# LST RPTPOLICY（查询基于策略的业务报表开关）

## 功能

**适用NF：PGW-U、UPF**

此命令用于查询基于策略的业务报表开关。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| POLICYNAME | 策略名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定报表功能使用的策略名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RPTPOLICY]] · 基于策略的报表开关（RPTPOLICY）

## 使用实例

- 运营商需要查询指定策略的业务报表参数。指定策略名称为“policy01”：
  ```
  LST RPTPOLICY: POLICYNAME="policy01";
  ```
  ```

  RETCODE = 0 操作成功

  基于策略的报表开关信息
  ----------------------
          策略名称 = policy01
   用户选择策略类型 = 选择所有用户
   用户选择策略名称 = NULL
       业务报表开关 = 不使能
         全局优先级 = 100
   用户选择策略索引 = NULL
  (结果个数 = 1)

  --- END
  ```
- 运营商需要查询所有策略的业务报表参数：
  ```
  LST RPTPOLICY:;
  ```
  ```

  RETCODE = 0 操作成功

  基于策略的报表开关信息
  -------------------
  策略名称  用户选择策略类型  用户选择策略名称  业务报表开关  全局优先级  用户选择策略索引  

  policy01  ANY               NULL              使能          100         NULL                 
  policy02  SPECIFIC          userpolicy01      使能          1           1                 
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-RPTPOLICY.md`
