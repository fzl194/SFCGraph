# 查询PCF业务服务区的绑定关系（LST PCFSSCOPEBIND）

- [命令功能](#ZH-CN_MMLREF_0000001088377444__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001088377444__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001088377444__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001088377444__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001088377444__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001088377444)

**适用NF：SMF、PGW-C、GGSN**

该命令用于查询PCF业务服务区的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0000001088377444)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001088377444)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001088377444)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BINDNAME | 绑定名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定记录的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：无 |
| SSCOPEID | 服务区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定服务区标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不区分大小写，转为小写存储。<br>默认值：无<br>配置原则：<br>配置的SSCOPEID必须是ADD PCFSSCOPE命令已配置的SSCOPEID。 |

## [使用实例](#ZH-CN_MMLREF_0000001088377444)

- 查询BINDNAME为towna的记录。
  ```
  LST PCFSSCOPEBIND: BINDNAME="towna";
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```
- 查询SSCOPEID为citya的记录。
  ```
  LST PCFSSCOPEBIND: SSCOPEID="citya";
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```
- 查询BINDNAME为towna，SSCOPEID为citya的记录。
  ```
  LST PCFSSCOPEBIND: BINDNAME="towna", SSCOPEID="citya";
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```
- 查询所有记录。
  ```
  LST PCFSSCOPEBIND:;
  RETCODE = 0  操作成功

  结果如下
  --------
         绑定名称  =  towna
       服务区标识  =  citya
         绑定类型  =  用户TAI范围
  用户TAI区域名称  =  tai2
  (结果个数 = 1)

  ---    END
  ```

## [输出结果说明](#ZH-CN_MMLREF_0000001088377444)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 绑定名称 | 该参数用于指定绑定记录的名称。 |
| 服务区标识 | 该参数用于指定服务区标识。 |
| 绑定类型 | 该参数用于指定和服务区标识绑定的数据类型。 |
| 用户TAI区域名称 | 该参数用于指定用户TAI区域名称。 |
