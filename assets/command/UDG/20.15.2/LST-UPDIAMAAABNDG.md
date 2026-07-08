---
id: UDG@20.15.2@MMLCommand@LST UPDIAMAAABNDG
type: MMLCommand
name: LST UPDIAMAAABNDG（查询Diameter AAA服务器与Diameter AAA服务器绑定关系）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: UPDIAMAAABNDG
command_category: 查询类
applicable_nf:
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- Diameter AAA管理
- 服务器配置
- Diameter AAA服务器和Diameter AAA服务器组的绑定关系
status: active
---

# LST UPDIAMAAABNDG（查询Diameter AAA服务器与Diameter AAA服务器绑定关系）

## 功能

**适用NF：UPF**

此命令用于查询指定Diameter AAA组下的Diameter AAA绑定配置信息或者查询所有Diameter AAA组下的Diameter AAA绑定配置信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GROUPNAME | Diameter AAA组名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Diameter AAA组名。<br>数据来源：本端规划<br>取值范围：不区分大小写，不支持空格。<br>默认值：无<br>配置原则：该参数使用ADD UPDIAMAAAGRP命令配置生成。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPDIAMAAABNDG]] · Diameter AAA服务器组里的Diameter AAA服务器（UPDIAMAAABNDG）

## 使用实例

- 查询名称为“diametergroup”的Diameter AAA组下的Diameter AAA绑定配置信息：
  ```
  %%LST UPDIAMAAABNDG:GROUPNAME="diametergroup";
  ```
  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA服务器与Diameter AAA服务器绑定关系
  ----------------------------------------------
  Diameter AAA组名  =  diametergroup
        服务器类型  =  3GPP AAA服务器
            主机名  =  diameteraaa1
        主备用标记  =  主用
  (结果个数 = 1)
  ---    END
  ```
- 查询所有Diameter AAA组下的Diameter AAA绑定配置信息：
  ```
  %%LST UPDIAMAAABNDG:;
  ```
  ```
  %%
  RETCODE = 0  操作成功
  Diameter AAA服务器与Diameter AAA服务器绑定关系
  ----------------------------------------------
  Diameter AAA组名  服务器类型      主机名        主备用标记  
  diametergroup     3GPP AAA服务器  diameteraaa1  主用        
  diametergroup1    3GPP AAA服务器  diameteraaa1  主用        
  diametergroup1    3GPP AAA服务器  diameteraaa2  备用        
  (结果个数 = 3)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-UPDIAMAAABNDG.md`
