# 查询协议五元组老化时间（LST PROTFAGETIME）

- [命令功能](#ZH-CN_CONCEPT_0182837298__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837298__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837298__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837298__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837298__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0182837298__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837298)

**适用NF：PGW-U、UPF**

该命令用于显示配置的协议组、协议相关的五元组老化时间信息。

#### [注意事项](#ZH-CN_CONCEPT_0182837298)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0182837298)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837298)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLLEVEL | 协议等级 | 可选必选说明：可选参数<br>参数含义：该参数用于显示配置的协议组、协议级别。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- PROTOCOLGROUP：协议组级别。<br>- PROTOCOL：协议级别。<br>默认值：无<br>配置原则：无 |
| PROTGROUPNAME | 协议组名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOLGROUP”时为必选参数。<br>参数含义：该参数用于设置协议组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的默认协议组，可以通过工程命令smctrldsp protocol-list查询。 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“PROTOCOLLEVEL”配置为“PROTOCOL”时为必选参数。<br>参数含义：该参数用于设置协议名称。数据源为系统支持识别的所有类型的协议、子协议。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令smctrldsp protocol-list查询。 |

#### [使用实例](#ZH-CN_CONCEPT_0182837298)

- 查询配置的协议组五元组老化时间的一条记录：
  ```
  LST PROTFAGETIME:PROTOCOLLEVEL=PROTOCOLGROUP,PROTGROUPNAME="p2p";
  ```
  ```

  RETCODE = 0  操作成功。

  协议五元组节点老化时间信息
  --------------------------
        协议等级  =  Protocol Group
        协议名称  =  NULL
      协议组名称  =  p2p
  老化时间（秒）  =  60
  (结果个数 = 1)
  ---    END
  ```
- 查询配置的协议组五元组老化时间的所有记录：
  ```
  LST PROTFAGETIME:;
  ```
  ```

  RETCODE = 0  操作成功。

  协议五元组节点老化时间信息
  --------------------------
  协议等级          协议名称    协议组名称    老化时间（秒）

  Protocol          http        NULL          20            
  Protocol Group    NULL        p2p           60            
  (结果个数 = 2)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0182837298)

参见ADD PROTFAGETIME的参数说明。
