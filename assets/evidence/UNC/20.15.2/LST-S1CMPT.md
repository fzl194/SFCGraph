# 查询S1接口兼容性(LST S1CMPT)

- [命令功能](#ZH-CN_MMLREF_0000001126146238__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126146238__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126146238__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126146238__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126146238__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126146238__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126146238__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126146238)

**适用网元：MME**

该命令用于查询S1接口兼容性。

#### [注意事项](#ZH-CN_MMLREF_0000001126146238)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126146238)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126146238)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126146238)

无。

#### [使用实例](#ZH-CN_MMLREF_0000001126146238)

查询S1接口兼容配置，运行如下命令：

LST S1CMPT:;

```
%%LST S1CMPT:;%%
RETCODE = 0  操作成功

操作结果如下
------------
                  是否支持Register LAI信元  =  不支持
                       发送所有MME服务PLMN  =  否
                  eNodeB是否支持祖冲之算法  =  是
                  是否携带Time to Wait信元  =  否
         NAS transport消息是否携带SPID信元  =  是
          NAS TRANSPORT消息是否携带HRL信元  =  是
                     Masked IMEISV发送范围  =  所有eNodeB
                Next Paging Area Scope开关  =  否
                是否携带NR Restriction信元  =  是
   是否携带NR UE Security Capabilities信元  =  是
                  是否携带Security Context  =  是
         是否携带NR Restriction in 5GS信元  =  否
是否携带Core Network Type Restrictions信元  =  否
                     是否支持S1 Part Reset  =  不支持
                 是否携带GUAMI映射的GUMMEI  =  否
                   是否携带GUMMEI Type信元  =  否
      是否携带Warning Area Coordinates信元  =  否
  是否携带Extended UE Identity Index Value  =  否
是否携带Management Based MDT PLMN List信元  =  否
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126146238)

请参考命令 [**SET S1CMPT**](设置S1接口兼容性(SET S1CMPT)_72345837.md) 的参数标识。
