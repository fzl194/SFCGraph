# 查询默认协议组（LST DFTPROTGRP）

- [命令功能](#ZH-CN_CONCEPT_0182837345__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837345__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837345__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837345__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837345__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837345__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837345)

**适用NF：PGW-U、UPF**

该命令用于查询默认协议组。当运营商希望检索默认协议组设置，以便灵活配置自定义协议和规则等配置项，则执行该命令。

#### [注意事项](#ZH-CN_CONCEPT_0182837345)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837345)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837345)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTQRYOPTYPE | 协议查询操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定协议查询操作类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SPECIFIC：查询指定默认协议组。<br>- ALL：查询所有默认协议组。<br>- NAME：查询所有默认协议组名称。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTQRYOPTYPE”配置为“SPECIFIC”时为必选参数。<br>参数含义：该参数用于指定协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837345)

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

#### [输出结果说明](#ZH-CN_CONCEPT_0182837345)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 子协议名称 | 协议组包含的子协议的名字。 |

其余输出项请参见ADD PROTOCOLGROUP的参数说明。
