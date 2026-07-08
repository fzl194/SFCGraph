---
id: UNC@20.15.2@MMLCommand@LST HTTPOFC
type: MMLCommand
name: LST HTTPOFC（查询HTTP局向）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: HTTPOFC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP局向管理
status: active
---

# LST HTTPOFC（查询HTTP局向）

## 功能

该命令用于查询HTTP局向。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTYPE | 局向类型 | 可选必选说明：必选参数<br>参数含义：该参数用于设置局向类型。<br>数据来源：本端规划<br>取值范围：<br>- “NFTYPE（基于网元类型）”：基于网元类型<br>- “IPGROUP（基于IP组）”：基于IP组<br>默认值：无<br>配置原则：<br>该参数不支持修改。 |
| OFCIDX | 局向索引 | 可选必选说明：可选参数<br>参数含义：该参数用于设置局向索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4095。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [HTTP局向（HTTPOFC）](configobject/UNC/20.15.2/HTTPOFC.md)

## 使用实例

- 查询局向类型为NFTYPE的HTTP局向信息，可以用如下命令：
  ```
  %%LST HTTPOFC: OFCTYPE=NFTYPE;%%
  RETCODE = 0  操作成功

  结果如下
  -------
          局向索引  =  1
          局向类型  =  基于网元类型
      对端网元类型  =  NFTypeSMF
  基于NFTYPE控制项  =  HTRINTF
      本端网元类型  =  INVALID
          局向名称  =  N11
  (结果个数 = 1)

  ---    END
  ```
- 查询局向类型为IPGROUP的HTTP局向信息，可以用如下命令：
  ```
  %%LST HTTPOFC: OFCTYPE=IPGROUP;%%
  RETCODE = 0  操作成功

  结果如下
  -------
        局向索引  =  2
        局向类型  =  基于IP组
            IP组  =  1
  基于IP组控制项  =  HTRIPGRP
    本端网元类型  =  INVALID
        局向名称  =  AMF2SMFIPGRP
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询HTTP局向（LST-HTTPOFC）_86150085.md`
