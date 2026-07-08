---
id: UNC@20.15.2@MMLCommand@LST EPLMNGRPMEM
type: MMLCommand
name: LST EPLMNGRPMEM（查询等价PLMN组成员）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPLMNGRPMEM
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 运营商管理
- 等价PLMN组成员管理
status: active
---

# LST EPLMNGRPMEM（查询等价PLMN组成员）

## 功能

**适用NF：AMF**

该命令用于查询等价PLMN组成员。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPIDX | 等价PLMN组号 | 可选必选说明：可选参数<br>参数含义：该参数用于标识等价PLMN组，通过命令ADD EPLMNGRP进行配置。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成等价PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示组成等价PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPLMNGRPMEM]] · 等价PLMN组成员（EPLMNGRPMEM）

## 使用实例

- 查询系统中“等价PLMN组号”为“0”的等价PLMN成员信息，执行如下命令：
  ```
  %%LST EPLMNGRPMEM: GRPIDX=0;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  等价PLMN组号  =  0
    移动国家码  =  123
      移动网号  =  89
      描述信息  =  add eplmn 12389 for 12345L
  (结果个数 = 1)

  ---    END
  ```
- 查询系统中配置的等价PLMN成员信息，执行如下命令：
  ```
  %%LST EPLMNGRPMEM:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  等价PLMN组号  =  0
    移动国家码  =  460
      移动网号  =  01
      描述信息  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询等价PLMN组成员（LST-EPLMNGRPMEM）_09653779.md`
