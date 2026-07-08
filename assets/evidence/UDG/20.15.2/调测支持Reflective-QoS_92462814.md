# 调测支持Reflective QoS

- [操作场景](#ZH-CN_OPI_0292462814__1.3.1)
- [必备事项](#ZH-CN_OPI_0292462814__1.3.2)
- [操作步骤](#ZH-CN_OPI_0292462814__1.3.3)

## [操作场景](#ZH-CN_OPI_0292462814)

当运营商部署支持Reflective QoS功能时，需对支持Reflective QoS功能进行调测，确保该特性正常生效。

> **说明**
> 适用于UPF。

## [必备事项](#ZH-CN_OPI_0292462814)

前提条件

请仔细阅读 [GWFD-020101 支持Reflective QoS](../GWFD-020101 支持Reflective QoS_88816803.md) 。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 测试终端使用的APN | APN名称（APN） | apn-test | 已配置数据中获取 | 已通过<br>[**ADD APN**](../../../../../OM参考/命令/UDG MML命令/用户面服务管理/DN管理/APN管理/APN/添加APN配置（ADD APN）_82837014.md)<br>进行配置。 |

工具

- 测试终端
- OM Portal

## [操作步骤](#ZH-CN_OPI_0292462814)

1. 执行 [**LST LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/查询License配置项开关（LST LICENSESWITCH）_09587900.md) 命令，查询 支持Reflective QoS 对应的License配置开关是否打开。
  ```
  LST LICENSESWITCH
  : LICITEM="LKV3G5SRQS01";
  ```
    - 如果“SWITCH”为“ENABLE”，请执行[2](#ZH-CN_OPI_0292462814__cmd444611061015)。
    - 如果“SWITCH”为“DISABLE”，则执行[**SET LICENSESWITCH**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/License管理/设置License项的开关（SET LICENSESWITCH）_09587387.md)命令打开本特性对应的License配置开关。
2. 在OM Portal上创建 UDG 用户跟踪任务。
3. 测试终端使用“apn-test”发起附着请求，成功接入5G网络。
4. 测试终端下接入的PC进行Web浏览业务。
5. 在 UDG 的跟踪台上查看用户消息跟踪中SMF向UPF发送PFCP Session Establishment Request消息的Create QER信元中是否携带QoS Flow Identifier和Reflective QoS信元。
    - 如果是，请执行[6](#ZH-CN_OPI_0292462814__cmd17789174424710)。
    - 如果否，请执行[7](#ZH-CN_OPI_0292462814__cmd1838194603163836)。
6. 在 UDG 的跟踪台上查看用户消息跟踪中UPF发送到(R)AN方向的下行数据中GTPU扩展头是否携带QoS Flow Identifier和Reflective QoS信元。
    - 如果是，调测结束。
    - 如果否，请执行[7](#ZH-CN_OPI_0292462814__cmd1838194603163836)。
7. 收集信息并寻求技术支持。
    a. 执行 [**EXP MML**](../../../../../OM参考/命令/UDG MML命令/平台服务管理/操作维护/配置管理/配置导出管理/导出MML文件（EXP MML）_47200033.md) 命令将当前配置数据导出为MML脚本文件并保存。
    b. 收集归纳所有信息并联系华为技术支持解决。
