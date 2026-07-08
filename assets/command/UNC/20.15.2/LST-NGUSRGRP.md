---
id: UNC@20.15.2@MMLCommand@LST NGUSRGRP
type: MMLCommand
name: LST NGUSRGRP（查询5G用户群）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGUSRGRP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- 用户群组标识管理
status: active
---

# LST NGUSRGRP（查询5G用户群）

## 功能

**适用NF：AMF**

该命令用于查询5G用户群记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USRGRPID | 用户群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定5G用户群标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGUSRGRP]] · 5G用户群（NGUSRGRP）

## 使用实例

- 查询标识为20的5G用户群记录，执行如下命令：
  ```
  %%LST NGUSRGRP: USRGRPID=20;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  用户群组标识  =  20
      描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中5G用户群记录，执行如下命令：
  ```
  %%LST NGUSRGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  用户群组标识  描述信息  

  1             group1       
  20            NULL         
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NGUSRGRP.md`
