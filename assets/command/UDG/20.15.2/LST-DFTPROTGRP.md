---
id: UDG@20.15.2@MMLCommand@LST DFTPROTGRP
type: MMLCommand
name: LST DFTPROTGRP（查询默认协议组）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: DFTPROTGRP
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 三四层规则管理
- 协议组
status: active
---

# LST DFTPROTGRP（查询默认协议组）

## 功能

**适用NF：PGW-U、UPF**

该命令用于查询默认协议组。当运营商希望检索默认协议组设置，以便灵活配置自定义协议和规则等配置项，则执行该命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTQRYOPTYPE | 协议查询操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议查询操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFIC：查询指定默认协议组。<br>- ALL：查询所有默认协议组。<br>- NAME：查询所有默认协议组名称。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTQRYOPTYPE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于指定协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [默认协议组（DFTPROTGRP）](configobject/UDG/20.15.2/DFTPROTGRP.md)

## 使用实例

- 假如运营商需要查询默认协议组“database”的详细设置：
  ```
  LST DFTPROTGRP:PROTQRYOPTYPE=SPECIFIC,PROTGROUPNAME="database";
  ```
  ```

  RETCODE = 0  操作成功。

  默认协议组信息
  --------------
  协议组名称    协议名称       子协议名称 

  database      cddb           cddb       
  database      ldap           ldap       
  database      mysql          mysql      
  database      postgresql     postgresql 
  database      sparebackup    sparebackup
  database      sql_server     sql_server 
  database      tds            tds        
  database      tns            tns        
  (结果个数 = 8)
  ---    END
  ```
- 假如运营商需要查看所有默认协议组：
  ```
  LST DFTPROTGRP:PROTQRYOPTYPE=NAME;
  ```
  ```

  RETCODE = 0  操作成功。

  默认协议组信息
  --------------
  协议组名称            

  database              
  email                 
  file_access           
  game                  
  im                    
  mobile                
  network_administration
  network_storage       
  others                
  p2p                   
  remote_connectivity   
  stock                 
  streaming             
  tunneling             
  voip                  
  web_browsing          
  (结果个数 = 16)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询默认协议组（LST-DFTPROTGRP）_82837345.md`
