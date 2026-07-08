---
id: UDG@20.15.2@MMLCommand@LST USRATTRCOND
type: MMLCommand
name: LST USRATTRCOND（查询用户属性过滤条件）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: USRATTRCOND
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 用户属性管理
- 配置用户属性过滤条件
status: active
---

# LST USRATTRCOND（查询用户属性过滤条件）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询用户属性过滤条件。

## 注意事项

如果不输入用户属性过滤条件名称，表示查询系统中所有过滤条件。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONDNAME | 过滤条件名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| ITEMID | 过滤条件项目索引 | 可选必选说明：可选参数<br>参数含义：该参数用于设置用户过滤条件项目索引。<br>数据来源：本端规划<br>取值范围：整数类型 ，取值范围是1~4294967295。<br>默认值：无<br>配置原则：无 |
| CONTENTTYPE | 内容类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤条件内容类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- USER_PROFILE：用户模板。<br>- APN：APN。<br>- RAT：RAT类型。<br>- MSISDN：MSISDN。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USRATTRCOND]] · 用户属性过滤条件（USRATTRCOND）

## 使用实例

- 假如运营商需要查询名称为user_cond1的用户属性过滤条件：
  ```
  %%LST USRATTRCOND: CONDNAME="user_cond1";
  ```
  ```
  %%
  RETCODE = 0  操作成功

  用户属性过滤条件
  ----------------
      过滤条件名称  =  user_cond1
  过滤条件项目索引  =  1
          内容类型  =  USERPROFILE
           APN名称  =  NULL
      用户模板名称  =  up1
           RAT类型  =  RESERVED
            MSISDN  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 假如运营商需要查询所有的用户属性过滤条件：
  ```
  %%LST USRATTRCOND:;
  ```
  ```
  %%
  RETCODE = 0  操作成功

  用户属性过滤条件
  ----------------
  过滤条件名称  过滤条件项目索引  内容类型     APN名称  用户模板名称  RAT类型   MSISDN  

  user_cond1    1                 USERPROFILE  NULL     up1           RESERVED  NULL    
  user_cond2    1                 USERPROFILE  NULL     up1           RESERVED  NULL    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询用户属性过滤条件（LST-USRATTRCOND）_42287009.md`
