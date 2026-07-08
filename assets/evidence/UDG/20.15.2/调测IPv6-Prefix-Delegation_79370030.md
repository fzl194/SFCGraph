# 调测IPv6 Prefix Delegation

- [操作场景](#ZH-CN_OPI_0279370030__1.3.1)
- [必备事项](#ZH-CN_OPI_0279370030__1.3.2)
- [操作步骤](#ZH-CN_OPI_0279370030__1.3.3)

## [操作场景](#ZH-CN_OPI_0279370030)

用户激活分IPv6代理前缀时，需要调测该功能，确保用户可以正常接入。

> **说明**
> 适用于PGW-U、UPF。

## [必备事项](#ZH-CN_OPI_0279370030)

前提条件

- 请仔细阅读 [GWFD-020406 IPv6 Prefix Delegation](../GWFD-020406 IPv6 Prefix Delegation_79370033.md) 。
- 完成[激活外部网元地址分配的IPv6 Prefix Delegation功能](激活外部网元地址分配的IPv6 Prefix Delegation功能_80269177.md)或[激活本地地址池分配的IPv6 Prefix Delegation功能](激活本地地址池分配的IPv6 Prefix Delegation功能_79965349.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | 用户IMSI（IMSI） | 460000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN/DNN实例名（APN） | apn-test2 | 已配置数据中获取 | - |

工具

测试终端

## [操作步骤](#ZH-CN_OPI_0279370030)

1. 打开接入侧/DN侧镜像接口上的第三方抓包工具，准备抓取测试终端的出入报文。
2. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令，查询IPv6 Prefix Delegation的特性开关是否打开。
  [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) : LICITEM="LKV3G5P6PD01";
    - 如果“SWITCH”为“ENABLE”，请执行[步骤 3](#ZH-CN_OPI_0279370030__step182501326201116)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
3. 测试终端使用“apn-test2”APN发起接入网络请求。
4. 执行 [**DSP SESSIONINFO**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/会话管理/会话信息管理/会话信息查询/显示用户上下文（DSP SESSIONINFO）_86526407.md) 命令，查看 测试终端的IP地址是否在 UDG 本地规划的地址池内 。
  ```
  DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
  ```
  ```
  ......
  -------------------------------
                                   IMSI  =  460000123456789
                                       ......         
                                    APN  =  apn-test2
                                       ......								
                               PDP Type  =  IPv6 
                                       ......    
                      IPv6 Address type  =  
  UPF ALLOC IP ADDRESS

                       IPv6 PDP address  =  fc00:0:0:fcee:0:0:0:0
                  IPV6 Delegated Prefix  =  
  fc00:0:0:fcee:0:0:0:0/63

                                       ......       
  (Number of results = 1)
  ---    END
  ```
    - 如果测试终端激活成功，且使用的“IPv6 PDP address”和“IPV6 Delegated Prefix”在规划的地址池内，测试终端接入成功，调测结束。
    - 如果测试终端激活成功，但使用的“IPv6 PDP address”不在规划的地址池内，执行[步骤 5](#ZH-CN_OPI_0279370030__step7)。
5. 收集信息并寻求技术支持。
    a. 在OM Portal上创建用户跟踪任务 并保存报文。
    b. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    c. 收集并保存上述所有查询信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
