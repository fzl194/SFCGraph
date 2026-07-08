# WSFD-104506 支持Direct Tunnel功能参考信息

- [命令](#ZH-CN_TOPIC_0191527824__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0191527824__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0191527824__1.3.3.1)
- [性能指标](#ZH-CN_TOPIC_0191527824__1.3.4.1)

#### [命令](#ZH-CN_TOPIC_0191527824)

本特性相关的MML命令如下：

- [**增加Iu接口RNC信息(ADD RNC)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)
- **[修改Iu接口RNC信息(MOD RNC)](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/修改Iu接口RNC信息(MOD RNC)_26305850.md)**
- **[增加GGSN属性配置信息(ADD GGSNCHARACT)](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/GTP-C接口管理/GnGp-GGSN_S5_S8接口管理/GGSN属性/增加GGSN属性配置信息(ADD GGSNCHARACT)_72225613.md)**
- [**增加IMSI Direct Tunnel配置(ADD IMSIDT)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/Direct Tunnel管理/增加IMSI Direct Tunnel配置(ADD IMSIDT)_72345647.md)
- [**增加APNNI Direct Tunnel配置(ADD APNNIDT)**](../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/网络管理/Direct Tunnel管理/增加APNNI Direct Tunnel配置(ADD APNNIDT)_72345645.md)

#### [告警](#ZH-CN_TOPIC_0191527824)

本特性无相关告警。

#### [软参](#ZH-CN_TOPIC_0191527824)

本特性无相关软参。

#### [性能指标](#ZH-CN_TOPIC_0191527824)

本特性相关的测量指标如下：

- Iu模式会话激活
    - 117459480 Iu模式激活One Tunnel PDP成功次数
    - 117459482 Iu模式激活One Tunnel PDP失败次数
- Iu模式隧道相关
    - 117471113 Iu模式One Tunnel会话转换成Two Tunnel会话成功次数
    - 117471114 Iu模式Two Tunnel会话转换成One Tunnel会话成功次数
    - 117471115 Iu模式One Tunnel会话转换成Two Tunnel会话失败次数
    - 117471116 Iu模式Two Tunnel会话转换成One Tunnel会话失败次数
