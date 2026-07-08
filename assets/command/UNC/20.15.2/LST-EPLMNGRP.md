---
id: UNC@20.15.2@MMLCommand@LST EPLMNGRP
type: MMLCommand
name: LST EPLMNGRP（查询等价PLMN组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPLMNGRP
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 等价PLMN组管理
status: active
---

# LST EPLMNGRP（查询等价PLMN组）

## 功能

**适用NF：AMF**

该命令用于查询等价PLMN组。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 等价PLMN组号 | 可选必选说明：可选参数<br>参数含义：该参数用于在UNC系统内唯一标识一个等价PLMN组。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [等价PLMN组（EPLMNGRP）](configobject/UNC/20.15.2/EPLMNGRP.md)

## 使用实例

- 查询系统中“等价PLMN组号”为“0”的等价PLMN组信息，执行如下命令：
  ```
  %%LST EPLMNGRP: GRPIDX=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  等价PLMN组号  =  0
      PLMN索引  =  0
  用户群组标识  =  0
  跟踪区域组ID  =  3
      描述信息  =  for ServingPLMN 12345
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中配置的等价PLMN组信息，执行如下命令：
  ```
  %%LST EPLMNGRP:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  等价PLMN组号  =  0
      PLMN索引  =  0
  用户群组标识  =  0
  跟踪区域组ID  =  3
      描述信息  =  for ServingPLMN 12345
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询等价PLMN组（LST-EPLMNGRP）_09651354.md`
