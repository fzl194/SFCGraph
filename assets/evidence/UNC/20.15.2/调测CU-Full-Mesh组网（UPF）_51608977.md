# 调测CU Full Mesh组网（UPF）

- [操作场景](#ZH-CN_OPI_0000001151608977__1.3.1)
- [必备事项](#ZH-CN_OPI_0000001151608977__1.3.2)
- [操作步骤](#ZH-CN_OPI_0000001151608977__1.3.3)

## [操作场景](#ZH-CN_OPI_0000001151608977)

SMF和UPF采用Full Mesh组网时，需要调测该功能，确保用户可以正常接入。

## [必备事项](#ZH-CN_OPI_0000001151608977)

前提条件

- 请仔细阅读[SMF&UPF容灾方案](../../../SMF&UPF容灾方案_01470590.md)。
- 完成[激活CU Full Mesh组网（UPF）](激活CU Full Mesh组网（UPF）_51809001.md)。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 用户信息查询 | 用户IMSI（IMSI） | 460000123456789 | 测试终端自带 | - |
| 测试终端使用的APN | APN实例名（APN） | apn-test | 已配置数据中获取 | 取自已配置的APN实例名。 |

工具

- 测试终端
- OM Portal

## [操作步骤](#ZH-CN_OPI_0000001151608977)

1. 测试终端使用“apn-test”DNN发起接入网络请求。
2. 执行 **DSP SESSIONINFO** 命令，查询 测试终端是否成功激活 。
  ```
  DSP SESSIONINFO:QUERYTYPE=IMSI,IMSI="460000123456789";
  ```
  ```
  ......

  -------------------------------
                                   IMSI  =  460000123456789
                                       ......              
                               PDP type  =  IPv4 
                                       ......    
                       IPv4 PDP address  =  10.10.10.1         
                                       ......    
                               APN name  =  apn-test
                                       ......       
  (Number of results = 1)
  ---    END
  ```
    - 如果是，执行[步骤 3](#ZH-CN_OPI_0000001151608977__step3)。
    - 如果否，请检查并重新配置。
3. 执行 **DSP CPINFO** 命令，查询UP对接的多个CP状态。
  ```
  DSP CPINFO: QUERYTYPE=NODEID, CPNODEIDTYPE=FQDN, CPNODEFQDN="CP1";
  DSP CPINFO: QUERYTYPE=NODEID, CPNODEIDTYPE=FQDN, CPNODEFQDN="CP2";
  ```
    - 如果状态是UP或DOWN，执行[步骤 4](#ZH-CN_OPI_0000001151608977__step4)。
    - 如果状态是UNKNOW，则检查并重新配置。
4. 执行 **LST CPTEIDUALLOC** 命令，查询是否配置U面本地分配F-TEID。
  ```
  LST CPTEIDUALLOC:;
  ```
    - 如果是（取值为DISABLE），则调测完成。
    - 如果否（取值为ENABLE），请检查并重新配置。如果仍未能解决，请执行[步骤 5](#ZH-CN_OPI_0000001151608977__step7)。
5. 收集信息并寻求技术支持。
    a. 在OMPortal上创建用户跟踪任务 并保存报文。
    b. 执行 **EXP MML** 命令将当前配置数据导出为MML脚本文件并保存。
    c. 收集并保存上述所有查询信息。
    d. 收集归纳所有信息并联系华为技术支持解决。
