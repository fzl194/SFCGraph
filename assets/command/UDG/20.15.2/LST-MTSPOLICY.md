---
id: UDG@20.15.2@MMLCommand@LST MTSPOLICY
type: MMLCommand
name: LST MTSPOLICY（查询消息跟踪限制）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: MTSPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# LST MTSPOLICY（查询消息跟踪限制）

## 功能

本命令用于查询对消息跟踪能力的限制。

> **说明**
> 无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数。<br>参数含义：标识网元ID，可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。<br>取值范围：0~65535<br>默认值：无。<br>配置原则：无。 |
| POLICYTYPE | 规则类型 | 可选必选说明：可选参数。<br>参数含义：限制消息跟踪的规则类型。<br>取值范围：<br>- DISABLE_BY_TYPE(限制跟踪类型)<br>- DISABLE_BY_SERVICE(限制服务名称)<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@MTSPOLICY]] · 消息跟踪限制（MTSPOLICY）

## 使用实例

查询跟踪消息限制：

```
%%LST MTSPOLICY:;%%
RETCODE = 0  操作成功
消息跟踪限制（限制跟踪类型）
----------------------------
网元ID  跟踪类型  
10      1002      
10      3001      
10      22222     
(结果个数 = 3)

消息跟踪限制（限制服务名称） 
------------------------   
网元ID    =  12 
跟踪类型  =  60905 
服务名称  =  CSPGoCommonServiceDemo 
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-MTSPOLICY.md`
