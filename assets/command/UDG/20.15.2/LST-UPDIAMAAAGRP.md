---
id: UDG@20.15.2@MMLCommand@LST UPDIAMAAAGRP
type: MMLCommand
name: LST UPDIAMAAAGRP（查询Diameter AAA服务器组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDIAMAAAGRP
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA组
status: active
---

# LST UPDIAMAAAGRP（查询Diameter AAA服务器组）

## 功能

**适用NF：UPF**

该命令用于查询Diameter AAA组配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPDIAMAAAGRP]] · Diameter AAA服务器组（UPDIAMAAAGRP）

## 使用实例

- 当存在一条Diameter AAA组配置时，查询Diameter AAA组配置信息：
  ```
  %%LST UPDIAMAAAGRP:;
  ```
  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA组
  --------------
         Diameter AAA组名  =  diametergroup
  (结果个数 = 1)
  ---    END
  ```
- 当存在多条Diameter AAA组配置时，查询Diameter AAA组配置信息：
  ```
  %%LST UPDIAMAAAGRP:;
  ```
  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA组
  --------------
  Diameter AAA组名
  diametergroup
  diametergroup1
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询Diameter-AAA服务器组（LST-UPDIAMAAAGRP）_45195204.md`
