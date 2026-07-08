# 调测支持Null-MSISDN

- [操作场景](#ZH-CN_OPI_0168358210__1.3.1)
- [必备事项](#ZH-CN_OPI_0168358210__1.3.2)
- [操作步骤](#ZH-CN_OPI_0168358210__1.3.3)

## [操作场景](#ZH-CN_OPI_0168358210)

UNC 支持不携带MSISDN的用户进行基本的业务。本操作介绍了通过调测手段检查 UNC 是否正确配置该功能的过程。

> **说明**
> 适用于 SGSN、 GGSN、 MME、SGW-C、PGW-C、AMF、SMF。

## [必备事项](#ZH-CN_OPI_0168358210)

前提条件

- 请仔细阅读[WSFD-106012 支持Null-MSISDN特性概述](WSFD-106012 支持Null-MSISDN特性概述_68358206.md)。
- 完成[激活支持Null-MSISDN（适用于SGSN/MME）](激活支持Null-MSISDN（适用于SGSN_MME）_68358209.md)。
- 完成[激活支持Null-MSISDN（适用SMF/GGSN/SGW-C/PGW-C）](激活支持Null-MSISDN（适用SMF_GGSN_SGW-C_PGW-C）_76486798.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | 用户IMSI号（IMSI） | 460000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN名称（APN） | apn-test | 已配置数据中获取 | 取自<br>[激活支持Null-MSISDN（适用SMF/GGSN/SGW-C/PGW-C）](激活支持Null-MSISDN（适用SMF_GGSN_SGW-C_PGW-C）_76486798.md)<br>中配置的APN实例名。<br>说明：APN数据仅限GGSN/SGW-C/PGW-C场景使用。 |

工具

OM Portal跟踪

## [操作步骤](#ZH-CN_OPI_0168358210)

- 调测支持Null-MSISDN业务。
    1. 进入 “MML命令行-UNC” 窗口。
    2. 执行[**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md)命令查询License配置开关是否已打开。
          - 如果“SWITCH”为“ENABLE”，请执行[3](#ZH-CN_OPI_0168358210__p1432111826180642)。
          - 如果“SWITCH”为“DISABLE”，请执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
    3. 创建用户跟踪。
      参数选择如下：
          - IMSI：被跟踪用户的IMSI。
          - 其它参数：选择默认值。
    4. 用户发起附着及激活流程。
      > **说明**
      > 针对GGSN/SGW-C/PGW-C场景，无MSISDN的测试终端使用“apn-test”APN发起接入网络请求。
    5. 查看跟踪结果。
          - 预期结果：Create PDP Context Request消息中不携带MSISDN。
          - 异常结果：Create PDP Context Request消息中携带MSISDN。
            参考 [激活支持Null-MSISDN（适用于SGSN/MME）](激活支持Null-MSISDN（适用于SGSN_MME）_68358209.md) 或者 [激活支持Null-MSISDN（适用SMF/GGSN/SGW-C/PGW-C）](激活支持Null-MSISDN（适用SMF_GGSN_SGW-C_PGW-C）_76486798.md) 并重新配置。
- 查询用户MM及SM上下文。
  [**DSP COMMMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/融合接入业务管理/融合用户数据库管理/显示移动性管理上下文的相关信息（DSP COMMMCTX）_58365337.md) : QUERYOPT=BYIMSI, IMSI="IMSI";
  ```
  %%DSP COMMMCTX: QUERYOPT=BYIMSI, IMSI="460000123456789";%%
  RETCODE = 0  操作成功

  MM上下文信息：
  ----------------
             ............

                          MSISDN  =  Null

             ............

  ---    END
  ```
    - 预期结果： “MSISDN” 为 “Null” 。
    - 异常结果： “MSISDN” 不为 “Null” 。
      异常结果处理：参考 [激活支持Null-MSISDN（适用于SGSN/MME）](激活支持Null-MSISDN（适用于SGSN_MME）_68358209.md) 或者 [激活支持Null-MSISDN（适用SMF/GGSN/SGW-C/PGW-C）](激活支持Null-MSISDN（适用SMF_GGSN_SGW-C_PGW-C）_76486798.md) 并重新配置。
  [**DSP SMCTX**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/系统管理/用户数据库管理/显示承载上下文(DSP SMCTX)_72226033.md) : QUERYOPT=BYIMSI, IMSI="IMSI", IDTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;
  ```
  %%DSP SMCTX:QUERYOPT=BYIMSI, IMSI="460000123456789", IDTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=5;%%
  RETCODE = 0  操作成功
  SM上下文信息：
  ----------------
             ............

                          MSISDN  =  Null

             ............

  ---    END
  ```
    - 预期结果： “MSISDN” 为 “Null” 。
    - 异常结果： “MSISDN” 不为 “Null” 。
      异常结果处理：参考 [激活支持Null-MSISDN（适用于SGSN/MME）](激活支持Null-MSISDN（适用于SGSN_MME）_68358209.md) 或者 [激活支持Null-MSISDN（适用SMF/GGSN/SGW-C/PGW-C）](激活支持Null-MSISDN（适用SMF_GGSN_SGW-C_PGW-C）_76486798.md) 并重新配置。
