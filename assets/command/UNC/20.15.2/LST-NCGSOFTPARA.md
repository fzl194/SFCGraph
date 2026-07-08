---
id: UNC@20.15.2@MMLCommand@LST NCGSOFTPARA
type: MMLCommand
name: LST NCGSOFTPARA（查询NCG软参）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NCGSOFTPARA
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# LST NCGSOFTPARA（查询NCG软参）

## 功能

**适用NF：NCG**

该命令用于查询NCG的软件参数信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- Dw（双字）<br>- Bit（比特）<br>- Byte（字节）<br>- String（字符串）<br>默认值：无<br>配置原则：无 |
| DWORDNUM | Dword索引 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件可选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1500。<br>默认值：无<br>配置原则：无 |
| BITNUM | Bit索引 | 可选必选说明：该参数在"DT"配置为"Bit"时为条件可选参数。<br>参数含义：该参数表示Bit类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4000。<br>默认值：无<br>配置原则：无 |
| BYTENUM | Byte索引 | 可选必选说明：该参数在"DT"配置为"Byte"时为条件可选参数。<br>参数含义：该参数表示Byte类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1200。<br>默认值：无<br>配置原则：无 |
| STRINGNUM | String索引 | 可选必选说明：该参数在"DT"配置为"String"时为条件可选参数。<br>参数含义：该参数表示String类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~30。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCGSOFTPARA]] · NCG软参（NCGSOFTPARA）

## 使用实例

- 查询NCG软件参数，数据类型是“Dw”，Dword索引是“1”
  ```
  LST NCGSOFTPARA: DT=Dw, DWORDNUM=1;
  RETCODE = 0  执行成功

  操作结果如下:
  -------------------------
       数据类型  =  双字
   软参记录索引  =  1
     软参记录值  =  3
  (结果个数 = 1)

  ---    END
  ```
- 查询NCG软件参数，数据类型是“Bit”，Bit索引是“1”
  ```
  LST NCGSOFTPARA: DT=Bit, BITNUM=1;
  RETCODE = 0  执行成功

  操作结果如下:
  -------------------------
       数据类型  =  比特
   软参记录索引  =  1
     软参记录值  =  1
  (结果个数 = 1)

  ---    END
  ```
- 查询NCG软件参数，数据类型是“Byte”，Byte索引是“1”
  ```
  LST NCGSOFTPARA: DT=Byte, BYTENUM=1;
  RETCODE = 0  执行成功

  操作结果如下:
  -------------------------
       数据类型  =  字节
   软参记录索引  =  1
     软参记录值  =  3
  (结果个数 = 1)

  ---    END
  ```
- 查询NCG软件参数，数据类型是“String”，String索引是“1”
  ```
  LST NCGSOFTPARA: DT=String, STRINGNUM=1;
  RETCODE = 0  执行成功

  操作结果如下:
  -------------------------
       数据类型  =  字符串
   软参记录索引  =  1
     软参记录值  =  ncg_service
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NCG软参（LST-NCGSOFTPARA）_06469322.md`
