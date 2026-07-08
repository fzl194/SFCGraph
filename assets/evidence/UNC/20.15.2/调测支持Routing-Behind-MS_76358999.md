# 调测支持Routing Behind MS

- [操作场景](#ZH-CN_OPI_0276358999__1.3.1)
- [必备事项](#ZH-CN_OPI_0276358999__1.3.2)
- [操作步骤](#ZH-CN_OPI_0276358999__1.3.3)

## [操作场景](#ZH-CN_OPI_0276358999)

当运营商部署Routing Behind MS功能时，需对Routing Behind MS功能进行调测，确保本功能可以正常使用。

> **说明**
> 适用于GGSN-C、SGW-C、PGW-C、SMF。

## [必备事项](#ZH-CN_OPI_0276358999)

前提条件

- 请仔细阅读[WSFD-205101 支持Routing Behind MS特性概述](WSFD-205101 支持Routing Behind MS特性概述_76358997.md)。
- 完成[激活支持Routing Behind MS](激活支持Routing Behind MS_76358998.md)。
- 完成[调测非透明接入](../WSFD-011305 Radius鉴权接入/调测Radius鉴权接入/调测非透明接入_95351131.md)。
- AAA Server上为无线设备（MS/UE）的下挂终端设备（PC）配置了IPv4网段地址。
- MS/UE上配置了与AAA Server相同的网段地址。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| APN | APN名称（APN） | huawei.com | 已配置数据中获取 | 取自<br>[激活支持Routing Behind MS](激活支持Routing Behind MS_76358998.md)<br>中配置的APN实例名。 |
| IP地址 | - | 10.11.11.1～10.11.11.10 | 与对端协商 | 取自AAA Server上配置的IPv4网段地址，用于MS/UE侧PC地址分配。 |
| IP地址 | - | 10.12.12.2 | 与对端协商 | PDN侧设备地址。 |

工具

- 测试终端
- 两台测试PC（一台与无线路由器联通，一台部署在PDN侧）
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0276358999)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09651570.md) 命令，查询License中是否允许使用支持Routing Behind MS。
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0276358999__step10476194711114)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09654190.md)命令打开本特性对应的License配置开关。
2. 在 OM Portal上建立N4接口跟踪，在 “参数配置” 栏输入用户IMSI 。
3. 测试终端 使用“huawei.com”的 “APN” 接入网络。
4. MS/UE侧PC访问PDN侧IP地址为 **10.12.12.2** 的PC。
    - 如果访问成功，请执行[步骤 5](#ZH-CN_OPI_0276358999__step4)。
    - 如果访问失败，请参考调测OM Portal浏览功能。
5. 查询MS/UE侧PC地址，使用PDN侧PC访问该地址。
    - 如果访问成功，Routing Behind MS功能正常，调测结束。
    - 如果访问失败，请执行[步骤 6](#ZH-CN_OPI_0276358999__step20418274171)。
6. 执行 [**LST APNADDRESSATTR**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/APN管理/基于APN的地址管理控制参数/查询基于APN的地址分配属性（LST APNADDRESSATTR）_09651663.md) 命令， 该APN的Routing Behind MS功能是否使能。
  ```
  LST APNADDRESSATTR: APN="huawei.com";
  RETCODE = 0  操作成功。
  APN的地址分配信息 
  -----------------
                             APN名称  =  huawei.com
                          手机后路由  =  使能   
                                    ......  
  (结果个数 = 1) 
  ---    END
  ```
    - 如果APN的“手机后路由”为“使能”，请执行[8](#ZH-CN_OPI_0276358999__cmd571354733510)。
    - 如果APN的“手机后路由”为“不使能”，请参考[激活支持Routing Behind MS](激活支持Routing Behind MS_76358998.md)重新配置后再次执行[步骤 3](#ZH-CN_OPI_0276358999__step19124153015128)。
7. 执行 **[LST SMCOMMFUNC](../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/会话协议参数管理/会话管理拓展功能/通用会话管理拓展功能/查询通用会话拓展功能（LST SMCOMMFUNC）_08433262.md)** 命令， 手机后路由功能是否使能。
  ```
  LST SMCOMMFUNC;
  RETCODE = 0  操作成功。
  结果如下
  -----------------
                  手机后路由功能开关  =  使能
                                    ......  
  (结果个数 = 1) 
  ---    END
  ```
    - 如果“手机后路由功能开关”为“使能”，请执行[8](#ZH-CN_OPI_0276358999__cmd571354733510)。
    - 如果“手机后路由功能开关”为“不使能”，请参考[激活支持Routing Behind MS](激活支持Routing Behind MS_76358998.md)重新配置后再次执行[步骤 3](#ZH-CN_OPI_0276358999__step19124153015128)。
8. 查看N4接口跟踪任务中的 PFCP Session Establishment Request 消息是否携带 “FRAMEDROUTE” 属性值。
    - 如果消息携带“FRAMEDROUTE”属性值，且属性值与数据规划一致，请执行[9](#ZH-CN_OPI_0276358999__cmd020210332113)。
    - 如果消息携带“FRAMEDROUTE”属性值，但属性值与数据规划不一致，请在AAA Server上按数据规划重新配置后再次执行[步骤 3](#ZH-CN_OPI_0276358999__step19124153015128)。
    - 如果消息未携带“FRAMEDROUTE”属性值，请联系AAA Server设备的技术人员，检查AAA Server上的数据配置。
9. 查看 测试终端 上配置的地址段是否与AAA Server的配置相同。
    - 如果配置相同，请执行[10](#ZH-CN_OPI_0276358999__cmd1128419207559)。
    - 如果配置不同，请修改测试终端上网段配置后再次执行[步骤 3](#ZH-CN_OPI_0276358999__step19124153015128)。
10. 收集信息并寻求技术支持。
    a. 执行 **[EXP MML](../../../../../OM参考/命令/UNC MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md)** 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集并保存上述所有查询信息。
    c. 收集归纳所有信息并联系华为技术支持解决。
