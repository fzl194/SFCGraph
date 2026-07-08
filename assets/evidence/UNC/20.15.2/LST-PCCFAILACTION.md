# 查询PCC故障处理（LST PCCFAILACTION）

- [命令功能](#ZH-CN_CONCEPT_0000201133684768__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201133684768__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201133684768__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201133684768__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201133684768__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000201133684768__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201133684768)

**适用NF：PGW-C、SMF**

该命令用来查询PCC故障处理动作。

#### [注意事项](#ZH-CN_CONCEPT_0000201133684768)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000201133684768)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201133684768)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000201133684768)

查询PCC故障处理：

```
LST PCCFAILACTION:;
```

```

RETCODE = 0  操作成功

PCC故障处理参数
---------------
                    选择PCRF/PCF失败动作  =  缺省
 选择PCRF/PCF失败回滚为Local PCC用户类型  =  回滚为本地PCC用户
选择PCRF/PCF失败回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
                 Initial流程故障处理动作  =  激活失败
  Initial流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
 Initial流程故障回滚为RADIUS PCC用户类型  =  回滚为本地PCC用户
                  Update流程故障处理动作  =  继续与PCRF/PCF交互
   Update流程故障回滚为Local PCC用户类型  =  回滚为本地PCC用户
                  流量上报失败时处理动作  =  使用UPDATEFAILACT参数配置
                         SCP故障重选开关  =  SCP故障不进行重选
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000201133684768)

参见SET PCCFAILACTION的参数说明。
