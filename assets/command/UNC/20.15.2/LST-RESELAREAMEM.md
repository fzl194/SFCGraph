---
id: UNC@20.15.2@MMLCommand@LST RESELAREAMEM
type: MMLCommand
name: LST RESELAREAMEM（查询AMF重选功能区域成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RESELAREAMEM
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
- AMF重选功能区域成员
status: active
---

# LST RESELAREAMEM（查询AMF重选功能区域成员）

## 功能

**适用NF：AMF**

该命令用于查询指定AMF重选功能的区域或者系统中配置的所有AMF重选功能的区域的跟踪区成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESELAREACODE | AMF重选功能区域编码 | 可选必选说明：可选参数<br>参数含义：该参数用于标识AMF服务的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>RESELAREACODE参数依赖于RESELAREACODE命令的RESELAREACODE参数。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@RESELAREAMEM]] · AMF重选功能区域成员（RESELAREAMEM）

## 使用实例

- 查询编码为“ReSelZone”的区域成员信息，执行如下命令：
  ```
  %%LST RESELAREAMEM:;%%
  RETCODE = 0  操作成功

  The result is as follows
  ------------------------
  AMF重选功能区域编码  =  ReSelZone
                  MCC  =  123
                  MNC  =  45
     跟踪区编码起始值  =  120101
     跟踪区编码结束值  =  120101
             描述信息  =  NULL
  (结果个数 = 2)

  ---    END
  ```
- 查询系统中当前配置的所有区域的信息，执行如下命令：
  ```
  %%LST RESELAREAMEM:;%%
  RETCODE = 0  操作成功

  The result is as follows
  ------------------------
  AMF重选功能区域编码  MCC  MNC  跟踪区编码起始值  跟踪区编码结束值  描述信息  

  ReSelZone            123  45   120101            120101            NULL         
  ReSelZone2           123  001  123456            123456            NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RESELAREAMEM.md`
