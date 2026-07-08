---
id: UNC@20.15.2@MMLCommand@LST AREAMEM
type: MMLCommand
name: LST AREAMEM（查询跟踪区成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AREAMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 通用区域成员管理
status: active
---

# LST AREAMEM（查询跟踪区成员）

## 功能

**适用NF：AMF**

该命令用于查询指定区域或者系统中配置的所有区域的跟踪区成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREACODE | 区域编码 | 可选必选说明：可选参数<br>参数含义：该参数用于标识AMF服务的某区域范围。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>AREACODE参数依赖于AREACODE命令的AREACODE参数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AREAMEM]] · 跟踪区成员（AREAMEM）

## 使用实例

- 查询编码为“jq001.pd006.sh.mcc123.mnc45”的区域成员信息，执行如下命令：
  ```
  %%LST AREAMEM: AREACODE="jq001.pd006.sh.mcc123.mnc45";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
           区域编码  =  jq001.pd006.sh.mcc123.mnc45
                MCC  =  460
                MNC  =  03
   跟踪区编码起始值  =  120101
   跟踪区编码结束值  =  120101
           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的所有区域的信息，执行如下命令：
  ```
  %%LST AREAMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
           区域编码  =  jq001.pd006.sh.mcc123.mnc45
                MCC  =  460
                MNC  =  03
   跟踪区编码起始值  =  120101
   跟踪区编码结束值  =  120101
           描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AREAMEM.md`
