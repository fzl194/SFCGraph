# 显示SMF的NodeID（LST CPNODEID）

- [命令功能](#ZH-CN_CONCEPT_0216780318__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0216780318__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0216780318__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0216780318__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0216780318__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0216780318__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0216780318)

**适用NF：PGW-U、UPF**

该命令用于显示指定SMF实例或所有SMF实例的信息。

#### [注意事项](#ZH-CN_CONCEPT_0216780318)

- 该命令执行后只对新激活用户生效。
- 该命令指定SMF实例名称时，表示查询指定SMF实例的信息。不指定SMF实例名称时，表示查询所有SMF实例的信息。

#### [操作用户权限](#ZH-CN_CONCEPT_0216780318)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0216780318)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CPNAME | SMF名称 | 可选必选说明：可选参数<br>参数含义：SMF的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0216780318)

- 查询名为smfnode1的SMF实例的信息：
  ```
  LST CPNODEID: CPNAME="smfnode1";
  ```
  ```

  RETCODE = 0 操作成功。

  SMF信息
  ---------------
                SMF名称  =  smfnode1
  IPv4地址类型的Node Id  =  10.0.0.1
  IPv6地址类型的Node Id  =  ::
      FQDN类型的Node Id  =  NULL
   本地应急接入节点  =  否
  (结果个数 = 1)
  --- END
  ```
- 查询所有SMF实例的信息：
  ```
  LST CPNODEID:;
  ```
  ```

  RETCODE = 0 操作成功。

  SMF信息
  ---------------
  SMF名称  IPv4地址类型的Node Id  IPv6地址类型的Node Id  FQDN类型的Node Id  本地应急接入节点

  smfnode1  10.0.0.1              ::                     NULL               否  
  smfnode2  0.0.0.0               fc00:0:1:1:23::        NULL               否   
  smfnode3  0.0.0.0               ::                     smf3               否  
  (结果个数 = 3)
  --- END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0216780318)

参见ADD CPNODEID的参数说明。
