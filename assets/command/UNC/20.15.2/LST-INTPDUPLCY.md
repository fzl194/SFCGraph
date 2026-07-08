---
id: UNC@20.15.2@MMLCommand@LST INTPDUPLCY
type: MMLCommand
name: LST INTPDUPLCY（查询异网漫游PDU会话重建策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: INTPDUPLCY
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF漫游功能控制
- 异网漫游PDU会话重建策略管理
status: active
---

# LST INTPDUPLCY（查询异网漫游PDU会话重建策略）

## 功能

**适用NF：AMF**

该命令用户查询异网漫游用户的PDU会话重建策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PDU会话重建策略生效的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “INTERNAT_ROAM_USER（所有异网漫游用户）”：所有异网漫游用户。<br>- “IMSI_PREFIX（IMSI前缀）”：指定IMSI前缀的异网漫游用户。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI的异网漫游用户。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件可选参数。<br>参数含义：该参数用于指定PDU会话重建策略的用户IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件可选参数。<br>参数含义：该参数用于指定PDU会话重建策略的用户IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/INTPDUPLCY]] · 异网漫游PDU会话重建策略（INTPDUPLCY）

## 使用实例

- 查询系统中生效范围为“所有异网漫游用户”的PDU会话重建策略，执行如下命令：
  ```
  %%LST INTPDUPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
            用户范围  =  所有异网漫游用户
            IMSI前缀  =  NULL
                IMSI  =  NULL
    语音会话重建策略  =  进入空闲态后重建
  非语音会话重建策略  =  进入空闲态后重建
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的PDU回哈重建策略，执行如下命令：
  ```
  %%LST INTPDUPLCY:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
            用户范围  =  所有异网漫游用户
            IMSI前缀  =  NULL
                IMSI  =  NULL
    语音会话重建策略  =  进入空闲态后重建
  非语音会话重建策略  =  进入空闲态后重建
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询异网漫游PDU会话重建策略（LST-INTPDUPLCY）_63346301.md`
