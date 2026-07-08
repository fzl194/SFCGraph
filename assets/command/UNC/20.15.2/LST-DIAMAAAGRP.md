---
id: UNC@20.15.2@MMLCommand@LST DIAMAAAGRP
type: MMLCommand
name: LST DIAMAAAGRP（查询Diameter AAA服务器组）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DIAMAAAGRP
command_category: 查询类
applicable_nf:
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA组
status: active
---

# LST DIAMAAAGRP（查询Diameter AAA服务器组）

## 功能

**适用NF：PGW-C**

该命令用于查询Diameter AAA组配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DIAMAAAGRP]] · Diameter AAA服务器组（DIAMAAAGRP）

## 使用实例

- 当存在一条Diameter AAA组配置时，查询Diameter AAA组配置信息：
  ```
  %%LST DIAMAAAGRP:;%%
  RETCODE = 0  操作成功

  Diameter AAA组
  --------------
         Diameter AAA组名  =  diametergroup
  PDN GW Identity携带方式  =  P-GW主机名
  (结果个数 = 1)

  ---    END
  ```
- 当存在多条Diameter AAA组配置时，查询Diameter AAA组配置信息：
  ```
  %%LST DIAMAAAGRP:;%%
  RETCODE = 0  操作成功

  Diameter AAA组
  --------------
  Diameter AAA组名  PDN GW Identity携带方式  

  diametergroup     P-GW主机名               
  diametergroup1    P-GW IP地址              
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Diameter-AAA服务器组（LST-DIAMAAAGRP）_64343881.md`
