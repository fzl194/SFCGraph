---
id: UDG@20.15.2@MMLCommand@LST TLSPSK
type: MMLCommand
name: LST TLSPSK（查询预共享密钥信息）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: TLSPSK
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP安全管理
- HTTP TLS预共享密钥管理
status: active
---

# LST TLSPSK（查询预共享密钥信息）

## 功能

该命令用于查询预共享密钥信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PSKIDX | 索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS预共享密钥的记录索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |
| PSKGRPIDX | 预共享密钥组索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定TLS预共享密钥组的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>与<br>[**ADD TLSPSKGRP**](../HTTP TLS预共享密钥组管理/增加TLS预共享密钥组（ADD TLSPSKGRP）_07789673.md)<br>中配置的预共享密钥组索引保持一致。 |
| PSKID | 预共享密钥标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定预共享密钥的密钥ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~128。<br>默认值：无<br>配置原则：<br>该参数与“HTTP模式”参数组合，唯一标识一个预共享密钥记录，不能重复配置，而且大小写敏感。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@TLSPSK]] · 预共享密钥（TLSPSK）

## 使用实例

- 查询所有预共享密钥信息执行如下命令：
  ```
  %%LST TLSPSK:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                                 索引  =  1
                     预共享密钥组索引  =  1
                                 模式  =  服务端模式
                       预共享密钥标识  =  psktest
                   预共享密钥内容类型  =  16进制ASCII码
                                 描述  =  NULL
  (结果数量 = 1)

  ---    END
  ```
- 查询索引为1的预共享密钥信息执行如下命令：
  ```
  %%LST TLSPSK: PSKIDX=1;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
                                 索引  =  1
                     预共享密钥组索引  =  1
                                 模式  =  服务端模式
                       预共享密钥标识  =  psktest
                   预共享密钥内容类型  =  16进制ASCII码
                                 描述  =  NULL
  (结果数量 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-TLSPSK.md`
