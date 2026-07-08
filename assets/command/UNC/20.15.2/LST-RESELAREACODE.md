---
id: UNC@20.15.2@MMLCommand@LST RESELAREACODE
type: MMLCommand
name: LST RESELAREACODE（查询AMF重选功能区域编码）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESELAREACODE
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF重选功能区域编码
status: active
---

# LST RESELAREACODE（查询AMF重选功能区域编码）

## 功能

**适用NF：AMF**

该命令用于查询指定AMF重选功能的区域编码，或者当前系统中配置的所有区域的基础信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESELAREACODE | AMF重选功能区域编码 | 可选必选说明：可选参数<br>参数含义：该参数用于唯一标识AMF服务的某个区域，该区域由一个或者若干个跟踪区组成。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RESELAREACODE]] · AMF重选功能区域编码（RESELAREACODE）

## 使用实例

- 查询编码为“ReSelZone”的区域信息，执行如下命令：
  ```
  %%LST RESELAREACODE: RESELAREACODE="ReSelZone";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  AMF重选功能区域编码  =  ReSelZone
             描述信息  =  for zone1
  (结果个数 = 1)

  ---    END
  ```
- 查询当前系统的所有区域的基础信息，执行如下命令：
  ```
  %%LST RESELAREACODE:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  AMF重选功能区域编码  描述信息  

  ReSelZone            for zone1    
  ReSelZone2           NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF重选功能区域编码（LST-RESELAREACODE）_70462557.md`
