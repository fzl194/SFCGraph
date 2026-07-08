---
id: UNC@20.15.2@MMLCommand@LST AMFINFO
type: MMLCommand
name: LST AMFINFO（查询AMF信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFINFO
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- AMF
- AMF信息管理
status: active
---

# LST AMFINFO（查询AMF信息）

## 功能

**适用NF：AMF**

该命令用于查询AMF实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AMFINSTANCENAME | AMF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于在UNC系统中唯一指定某个AMF实例。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。可输入的字符有字母、十进制数字、"_"和“-”，例如，AMF_Instance_0。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFINFO]] · AMF信息（AMFINFO）

## 使用实例

- 查询“AMF实例名称”为“AMF_Instance_0”的AMF信息，执行如下命令：
  ```
  %%LST AMFINFO: AMFINSTANCENAME="AMF_Instance_0";%%
  RETCODE = 0  操作成功

  结果如下
  --------
    AMF实例名称  =  AMF_Instance_0
        AMF名称  =  AMF1.CLUSTER1.NET2.AMF.5GC.MNC003.MCC460.3GPPNETWORK.ORG
  PLMN间AMF名称  =  NULL
       相对容量  =  255
       描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询全量AMF的信息，执行如下命令：
  ```
  %%LST AMFINFO:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
    AMF实例名称  =  AMF_Instance_0
        AMF名称  =  AMF1.CLUSTER1.NET2.AMF.5GC.MNC003.MCC460.3GPPNETWORK.ORG
  PLMN间AMF名称  =  NULL
       相对容量  =  255
       描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF信息（LST-AMFINFO）_09653129.md`
