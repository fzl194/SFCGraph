# 查询Iu模式接入限制参数(LST IUARD)

- [命令功能](#ZH-CN_MMLREF_0000001126305288__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305288__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305288__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305288__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305288__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305288__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126305288__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305288)

**适用网元：SGSN**

该命令用于查询Iu模式接入限制参数。

#### [注意事项](#ZH-CN_MMLREF_0000001126305288)

无。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305288)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305288)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305288)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定用户范围的信息。<br>取值范围：<br>- “ALL_USER(所有用户)”：表示该指定用户范围为所有用户。<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”：表示该用户范围为指定IMSI前缀。<br>- “SPECIAL_IMSI_RANGE(指定IMSI范围)”：表示该用户范围为指定IMSI范围。<br>默认值：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定IMSI前缀的信息。使用时按照IMSI最长匹配进行查询。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“SPECIAL_IMSIPRE(指定IMSI前缀)”<br>时生效。<br>取值范围：1~15位数字<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定用户的IMSI。<br>前提条件：该参数在<br>“SUBRANGE（用户范围）”<br>设置为<br>“SPECIAL_IMSI_RANGE(指定IMSI范围)”<br>时生效。<br>取值范围：1~15位数字<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305288)

1. 查询所有Iu模式接入限制参数记录：
  LST IUARD:;
  ```
  %%LST IUARD:;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
   用户范围      IMSI前缀  APNNI   卡类型       启用签约ARD  控制类型  原因值          自定义原因值

   所有用户      NULL      *       SIM         否           拒绝      GPRS服务被禁止  NULL        
   指定IMSI前缀  123456    *       SIM         否           拒绝      GPRS服务被禁止  NULL        
  (结果个数 = 2)

  ---    END
  ```
2. 查询用户范围为ALL_USER的Iu模式接入限制参数记录：
  LST IUARD: SUBRANGE=ALL_USER;
  ```
  %%LST IUARD: SUBRANGE=ALL_USER;%%
  RETCODE = 0  操作成功。

  查询结果如下
  --------------
      用户范围  =  所有用户
         APNNI  =  *
        卡类型  =  SIM
   启用签约ARD  =  否
      控制类型  =  拒绝
        原因值  =  GPRS服务被禁止
  自定义原因值  =  NULL
  (结果个数 = 1)

  ---    END
  ```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126305288)

参考命令 [**ADD IUARD**](增加Iu模式接入限制参数(ADD IUARD)_72345073.md) 的参数标识。
