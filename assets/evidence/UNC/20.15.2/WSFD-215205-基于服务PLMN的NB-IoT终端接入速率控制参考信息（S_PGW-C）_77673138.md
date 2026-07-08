# WSFD-215205 基于服务PLMN的NB-IoT终端接入速率控制参考信息（S/PGW-C）

- [命令](#ZH-CN_TOPIC_0277673138__1.3.1.1)
- [告警](#ZH-CN_TOPIC_0277673138__1.3.2.1)
- [软参](#ZH-CN_TOPIC_0277673138__1.3.3.1)
- [测量指标](#ZH-CN_TOPIC_0277673138__1.3.4.1)

#### [命令](#ZH-CN_TOPIC_0277673138)

本特性相关的MML命令如下：

- [**SET PLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/Serving PLMN速率控制配置/设置Serving PLMN速率控制配置（SET PLMNRATECTRL）_64343918.md)
- [**LST PLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/Serving PLMN速率控制配置/查询Serving PLMN速率控制配置（LST PLMNRATECTRL）_64343890.md)
- [**SET APNPLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/设置APN Serving PLMN速率控制配置（SET APNPLMNRATECTRL）_64343912.md)
- [**LST APNPLMNRATECTRL**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/接入管理/速率控制/PLMN速率控制/APN Serving PLMN速率控制/查询APN Serving PLMN速率控制配置（LST APNPLMNRATECTRL）_64343876.md)
- [**ADD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/增加DCC模板（ADD DCCTEMPLATE）_09896923.md)
- [**MOD DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/修改DCC模板（MOD DCCTEMPLATE）_09896924.md)
- [**RMV DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/删除DCC模板（RMV DCCTEMPLATE）_09896925.md)
- [**LST DCCTEMPLATE**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/在线计费/信用控制/信用控制模板/查询DCC模板（LST DCCTEMPLATE）_09896933.md)
- [**ADD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/增加话单字段模板（ADD CDRFIELDTEMP）_09896890.md)
- [**MOD CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/修改话单字段模板（MOD CDRFIELDTEMP）_09896891.md)
- [**RMV CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/删除话单字段模板（RMV CDRFIELDTEMP）_09896892.md)
- [**LST CDRFIELDTEMP**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/话单字段控制/话单字段模板/查询话单字段模板（LST CDRFIELDTEMP）_09896893.md)
- [**SET OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/配置离线计费话单参数（SET OFCCDRPARA）_09896905.md)
- [**LST OFCCDRPARA**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线公共参数/显示离线计费话单参数（LST OFCCDRPARA）_09896906.md)
- [**ADD DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/增加Diameter字典加载路径（ADD DIAMDICTPATH）_09897247.md)
- [**MOD DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/修改Diameter字典加载路径（MOD DIAMDICTPATH）_09897248.md)
- [**RMV DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/删除Diameter字典加载路径（RMV DIAMDICTPATH）_09897249.md)
- [**LST DIAMDICTPATH**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/接口管理/计费和策略接口管理/Diameter管理/Diameter字典管理/加载路径/查询Diameter字典加载路径（LST DIAMDICTPATH）_09897250.md)
- [**SET CONTAINERTRIGGER**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/离线计费基础参数/离线计费模板/配置离线计费容器产生开关（SET CONTAINERTRIGGER）_09896912.md)

#### [告警](#ZH-CN_TOPIC_0277673138)

本特性无相关告警。

#### [软参](#ZH-CN_TOPIC_0277673138)

本特性无相关软参。

#### [测量指标](#ZH-CN_TOPIC_0277673138)

本特性无相关测量指标。
