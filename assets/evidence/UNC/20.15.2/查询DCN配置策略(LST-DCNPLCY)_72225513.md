# 查询DCN配置策略(LST DCNPLCY)

- [命令功能](#ZH-CN_MMLREF_0000001172225513__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225513__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225513__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225513__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225513__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225513__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225513__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225513)

**适用网元：MME**

该命令用于查询不同范围内用户的DCN配置策略参数。

#### [注意事项](#ZH-CN_MMLREF_0000001172225513)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225513)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225513)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225513)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待增加DCN策略的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “IMSI_PRE(指定IMSI前缀)”<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定IMSI前缀以区分不同的用户群。<br>前提条件：该参数在<br>“用户范围”<br>参数配置为<br>“IMSI_PRE(指定IMSI前缀)”<br>后生效。<br>数据来源：本端规划<br>取值范围：5~15位十进制数字字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225513)

1. 查询 “IMSI前缀” 为 “123003” 的用户的DCN策略参数：
  LST DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="123003";
  ```
  %%LST DCNPLCY: SUBRANGE=IMSI_PRE, IMSIPRE="123003";%%
  RETCODE = 0  操作成功

  操作结果如下
  --------------
               用户范围  =  指定IMSI前缀
               IMSI前缀  =  123003
                DCN开关  =  打开
  源侧UE USAGE TYPE策略  =  是
  UE USAGE TYPE获取策略  =  本地获取
          UE USAGE TYPE  =  100
           网关选择策略  =  使用
  (结果个数 = 1)

  ---    END
  ```
2. 查询配置表中所有用户的DCN策略参数：
  LST DCNPLCY:;
  ```
  %%LST DCNPLCY:;%%
  RETCODE = 0  操作成功

  操作结果如下
  --------------
   用户范围      IMSI前缀  DCN开关  源侧UE USAGE TYPE策略  UE USAGE TYPE获取策略  UE USAGE TYPE   网关选择策略

   指定IMSI前缀  123003    打开     是                     本地获取               100             使用      
   所有用户      NULL      打开     是                     HSS获取                NULL            使用
  (结果个数 = 2)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225513)

参见 [**ADD DCNPLCY**](增加DCN配置策略(ADD DCNPLCY)_26305642.md) 的参数说明。
