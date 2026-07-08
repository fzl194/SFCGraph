---
id: UNC@20.15.2@MMLCommand@LST DNNGRP
type: MMLCommand
name: LST DNNGRP（查询DNN群组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNNGRP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 通用配置管理
- DNN群组标识管理
status: active
---

# LST DNNGRP（查询DNN群组）

## 功能

**适用NF：AMF**

该命令用于查询DNN群组信息。

## 注意事项

如果要查询DNN群组下的DNN列表，请使用LST DNNGRPMEM。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNGRPID | DNN群组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于标识一个DNN群组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNGRP]] · DNN群组（DNNGRP）

## 使用实例

- 查询系统中“DNN群组标识”为“BIG_GROUP”的DNN群组，执行如下命令：
  ```
  %%LST DNNGRP: DNNGRPID="BIG_GROUP";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  DNN群组标识  =  BIG_GROUP
     描述信息  =  for SMF selection
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中当前配置的DNN群组，执行如下命令：
  ```
  %%LST DNNGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  DNN群组标识   描述信息        

  1             NULL               
  BIG_GROUP     for SMF selection  
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNNGRP.md`
