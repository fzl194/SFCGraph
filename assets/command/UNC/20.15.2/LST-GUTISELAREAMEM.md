---
id: UNC@20.15.2@MMLCommand@LST GUTISELAREAMEM
type: MMLCommand
name: LST GUTISELAREAMEM（查询GUTI选网功能区域成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GUTISELAREAMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域GUTI选网功能管理
- GUTI选网功能区域成员
status: active
---

# LST GUTISELAREAMEM（查询GUTI选网功能区域成员）

## 功能

**适用NF：AMF**

该命令用于查询指定GUTI选网功能的区域或者系统中配置的所有GUTI选网功能的区域的跟踪区成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GUTISELAREACODE | GUTI选网功能区域编码 | 可选必选说明：可选参数<br>参数含义：该参数用于标识AMF服务的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>GUTISELAREACODE参数依赖于ADD GUTISELAREACODE命令的GUTISELAREACODE参数。 |

## 操作的配置对象

- [GUTI选网功能区域成员（GUTISELAREAMEM）](configobject/UNC/20.15.2/GUTISELAREAMEM.md)

## 使用实例

- 查询编码为“GUTISelZone”的区域成员信息，执行如下命令：
  ```
  %%LST GUTISELAREAMEM:;%%
  RETCODE = 0  操作成功

  The result is as follows
  ------------------------
  GUTI选网功能区域编码  =  GUTISelZone
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
  %%LST GUTISELAREAMEM:;%%
  RETCODE = 0  操作成功

  The result is as follows
  ------------------------
  GUTI选网功能区域编码  MCC  MNC  跟踪区编码起始值  跟踪区编码结束值  描述信息  

  GUTISelZone            123  45   120101            120101            NULL         
  GUTISelZone2           123  001  123456            123456            NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GUTI选网功能区域成员（LST-GUTISELAREAMEM）_13939877.md`
