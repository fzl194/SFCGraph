# 查询用户模板组（LST USRPROFGROUP）

- [命令功能](#ZH-CN_CONCEPT_0209897222__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0209897222__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0209897222__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0209897222__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0209897222__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0209897222__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0209897222)

**适用NF：PGW-C、SMF**

此命令用于查询UsrProfGroup。如果不输入UserProfGName，则查询系统中所有UsrProfGroup。

#### [注意事项](#ZH-CN_CONCEPT_0209897222)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0209897222)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0209897222)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户模板组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0209897222)

- 显示指定名称的UsrProfGroup配置：
  ```
  LST USRPROFGROUP:USERPROFGNAME="userprofg1";
  ```
  ```

  RETCODE = 0  操作成功。

  用户模板组信息
  --------------
   用户模板组名称  =  userprofg1
     用户模板数目  =  0
  用户PCC模板数目  =  0
  (结果个数 = 1)
  ---    END
  ```
- 显示所有UsrProfGroup配置：
  ```
  LST USRPROFGROUP:;
  ```
  ```

  RETCODE = 0  操作成功

  用户模板组信息
  --------------
  用户模板组名称  用户模板数目  用户PCC模板数目  

  userprofg1      0             0                
  userprofg2      0             0                
  (结果个数 = 2)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0209897222)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户模板数目 | 用于指定用户模板数量。 |
| 用户PCC模板数目 | 用于指定用户PCC模板数量。 |

其余输出项请参见ADD USRPROFGROUP的参数说明。
