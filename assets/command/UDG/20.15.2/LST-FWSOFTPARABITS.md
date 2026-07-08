---
id: UDG@20.15.2@MMLCommand@LST FWSOFTPARABITS
type: MMLCommand
name: LST FWSOFTPARABITS（查询ServiceFabric软参比特位）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FWSOFTPARABITS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软参配置管理
status: active
---

# LST FWSOFTPARABITS（查询ServiceFabric软参比特位）

## 功能

该命令用于查询软件参数，查询结果以二进制形式输出。同时，该命令也支持查询指定软件参数中某个比特位的值。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARATYPE | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- DWORD（双字）<br>- DWORD_EX（扩展双字）<br>默认值：无<br>配置原则：无 |
| DWORDNUM | DWORD参数索引 | 可选必选说明：可选参数<br>参数含义：该参数表示Common Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~2048。<br>默认值：无<br>配置原则：无 |
| POSITION | 比特位 | 可选必选说明：可选参数<br>参数含义：该参数表示软件参数比特位的位置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FWSOFTPARABITS]] · ServiceFabric软参比特位（FWSOFTPARABITS）

## 使用实例

- 查询当前软参记录索引为1，比特位为1的公共双字类型软参的设置情况：
  ```
  LST FWSOFTPARABITS: PARATYPE=DWORD, DWORDNUM=1, POSITION=1;
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         数据类型  =  双字
  软参记录索引  =  1
            比特位  =  1
   软参记录值  =  0
  (结果个数  = 1)

  ---    END
  ```
- 查询当前软参记录索引为空，比特位为空的公共双字类型软参的设置情况。查询结果中软参记录值的右边第一位记为比特1，例如，软参记录值 = 0000 0000 0000 0000 0000 0000 0000 0001，表示比特1的参数值为1：
  ```
  LST FWSOFTPARABITS: PARATYPE=DWORD;; 
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  数据类型     软参记录索引  比特位  软参记录值                         

  双字  1                 NULL          0000 0000 0000 0000 0000 0000 0000 0000  
  双字  2                 NULL          0000 0000 0000 0000 0000 0000 0000 0000  
  双字  3                 NULL          0000 0000 0000 0000 0000 0000 0000 0000  
  ......   
  双字  2046              NULL          0000 0000 0000 0000 0000 0000 0000 0000  
  双字  2047              NULL          0000 0000 0000 0000 0000 0000 0000 0000  
  双字  2048              NULL          0000 0000 0000 0000 0000 0000 0000 0000  
  (Number of results = 2048) 
  --- END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-FWSOFTPARABITS.md`
