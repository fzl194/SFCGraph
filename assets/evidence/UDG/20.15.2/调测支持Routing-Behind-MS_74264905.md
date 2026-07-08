# 调测支持Routing Behind MS

- [操作场景](#ZH-CN_OPI_0274264905__1.3.1)
- [必备事项](#ZH-CN_OPI_0274264905__1.3.2)
- [操作步骤](#ZH-CN_OPI_0274264905__1.3.3)

## [操作场景](#ZH-CN_OPI_0274264905)

当运营商部署Routing Behind MS功能时，需对 UDG 的Routing Behind MS功能进行调测，确保本功能可以正常使用。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0274264905)

前提条件

- 请仔细阅读[GWFD-110910 支持Routing Behind MS特性概述](GWFD-110910 支持Routing Behind MS特性概述_74264899.md)。
- 完成[激活支持Routing Behind MS](激活支持Routing Behind MS_74264904.md)。
- AAA Server上为无线路由器（MS/UE）后的设备（PC）配置了IPv4网段地址。
- MS/UE上配置了与AAA Server相同的网段地址。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| APN | APN名称（APN） | apn1 | 已配置数据中获取 | 取自<br>[激活支持Routing Behind MS](激活支持Routing Behind MS_74264904.md)<br>中配置的APN实例名。 |
| IP地址 | - | 10.11.11.1～10.11.11.10 | 与对端协商 | 取自AAA Server上配置的IPv4网段地址，用于MS/UE侧PC地址分配。 |
| IP地址 | - | 10.12.12.2 | 与对端协商 | PDN侧设备地址。 |

工具

- 测试终端
- 两台测试PC（一台与无线路由器联通，一台部署在PDN侧）
- OM Portal跟踪工具

## [操作步骤](#ZH-CN_OPI_0274264905)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令，查询License中是否允许使用支持Routing Behind MS。
  ```
  LST LICENSESWITCH:LICITEM="LKV3G5RBMS01";
  ```
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 2](#ZH-CN_OPI_0274264905__step10476194711114)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
2. 在 OM Portal上 [UDG N4接口跟踪](../../../../../网络运维/日常维护/UDG基础运维操作/创建消息跟踪/创建接口跟踪/UDG N4接口跟踪_88792205.md) ，在 “参数配置” 栏输入用户IMSI 。
3. 测试终端 使用“apn1”的 “APN” 接入网络。
4. MS/UE侧PC访问PDN侧IP地址为 **10.12.12.2** 的PC。
    - 如果访问成功，请执行[步骤 5](#ZH-CN_OPI_0274264905__step4)。
    - 如果访问失败，请调测UDG的Web浏览功能。
5. 查询MS/UE侧PC地址，使用PDN侧PC访问该地址。
    - 如果访问成功，Routing Behind MS功能正常，调测结束。
    - 如果访问失败，请执行[步骤 6](#ZH-CN_OPI_0274264905__step20418274171)。
6. 执行 [**LST APNADDRESSATTR**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话地址管理/APN的地址分配属性配置/查询ApnAddressAttr配置（LST APNADDRESSATTR）_86527108.md) 命令，该APN的Routing Behind MS功能是否使能。
  ```
  LST APNADDRESSATTR: APN="apn1";
  ```
  ```
  RETCODE = 0  操作成功。
  APN的地址分配信息 
  -----------------
                             APN名称  =  apn1.com
                          手机后路由  =  使能   
                                    ......  
  (结果个数 = 1) 
  ---    END
  ```
    - 如果APN的“手机后路由”为“使能”，请执行[步骤 7](#ZH-CN_OPI_0274264905__step1071434763511)。
    - 如果APN的“手机后路由”为“不使能”，请参考[激活支持Routing Behind MS](激活支持Routing Behind MS_74264904.md)重新配置后再次执行[步骤 3](#ZH-CN_OPI_0274264905__step19124153015128)。
7. 查看N4接口跟踪任务中的 PFCP Session Establishment Request 消息是否携带 “FRAMEDROUTE” 属性值。
    - 如果消息携带“FRAMEDROUTE”属性值，且属性值与数据规划一致，请执行[步骤 8](#ZH-CN_OPI_0274264905__step1720243112116)。
    - 如果消息携带“FRAMEDROUTE”属性值，但属性值与数据规划不一致，请在AAA Server上按数据规划重新配置后再次执行[步骤 3](#ZH-CN_OPI_0274264905__step19124153015128)。
    - 如果消息未携带“FRAMEDROUTE”属性值，请联系AAA Server设备的技术人员，检查AAA Server上的数据配置。
8. 查看 测试终端 上配置的地址段是否与AAA Server的配置相同。
    - 如果配置相同，请执行[步骤 9](#ZH-CN_OPI_0274264905__step42841220155514)。
    - 如果配置不同，请修改测试终端上网段配置后再次执行[步骤 3](#ZH-CN_OPI_0274264905__step19124153015128)。
9. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务，执行 [步骤 3](#ZH-CN_OPI_0274264905__step19124153015128) 并保存报文。
    b. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    c. 收集并保存上述所有查询信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
