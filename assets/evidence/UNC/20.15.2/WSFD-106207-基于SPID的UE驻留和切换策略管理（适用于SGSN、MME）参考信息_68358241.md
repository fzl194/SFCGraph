# WSFD-106207 基于SPID的UE驻留和切换策略管理（适用于SGSN、MME）参考信息

- [命令](#ZH-CN_CONCEPT_0168358241__1.3.1.1)
- [告警](#ZH-CN_CONCEPT_0168358241__1.3.2.1)
- [软参](#ZH-CN_CONCEPT_0168358241__1.3.3.1)
- [测量指标](#ZH-CN_CONCEPT_0168358241__1.3.4.1)

#### [命令](#ZH-CN_CONCEPT_0168358241)

本特性相关的MML命令如下：

- [**增加RFSP配置(ADD RFSP)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/增加RFSP配置(ADD RFSP)_26305350.md)
- [**删除RFSP配置(RMV RFSP)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/删除RFSP配置(RMV RFSP)_72345137.md)
- [**修改RFSP配置(MOD RFSP)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/修改RFSP配置(MOD RFSP)_26145540.md)
- [**查询RFSP配置(LST RFSP)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/RFSP管理/RFSP策略管理/RFSP参数配置/查询RFSP配置(LST RFSP)_72225221.md)
- [**增加Iu接口RNC信息(ADD RNC)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/增加Iu接口RNC信息(ADD RNC)_26146040.md)
- [**删除Iu接口RNC信息(RMV RNC)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/删除Iu接口RNC信息(RMV RNC)_72225719.md)
- [**修改Iu接口RNC信息(MOD RNC)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/修改Iu接口RNC信息(MOD RNC)_26305850.md)
- [**查询Iu接口RNC信息(LST RNC)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Iu接口管理/Iu接口RNC信息/查询Iu接口RNC信息(LST RNC)_72345641.md)
- [**设置S1接口兼容性(SET S1CMPT)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/S1接口管理/S1接口兼容性/设置S1接口兼容性(SET S1CMPT)_72345837.md)
- [**增加信令实体(ADD NSE)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/信令实体管理/增加信令实体(ADD NSE)_26146028.md)
- [**删除信令实体(RMV NSE)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/信令实体管理/删除信令实体(RMV NSE)_72225707.md)
- [**修改信令实体(MOD NSE)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/信令实体管理/修改信令实体(MOD NSE)_26305838.md)
- [**查询信令实体（LST NSE）**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/信令实体管理/查询信令实体（LST NSE）_72345629.md)
- [**增加NSE属性模板(ADD GBNSECFGPARA)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/Gb自动配置管理/NSE属性模板管理/增加NSE属性模板(ADD GBNSECFGPARA)_26146004.md)
- [**删除NSE属性模板(RMV GBNSECFGPARA)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/Gb自动配置管理/NSE属性模板管理/删除NSE属性模板(RMV GBNSECFGPARA)_72225683.md)
- [**修改NSE属性模板(MOD GBNSECFGPARA)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/Gb自动配置管理/NSE属性模板管理/修改NSE属性模板(MOD GBNSECFGPARA)_26305814.md)
- [**查询NSE属性模板(LST GBNSECFGPARA)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/Gb接口管理/Gb自动配置管理/NSE属性模板管理/查询NSE属性模板(LST GBNSECFGPARA)_72345605.md)
- [**设置移动性管理扩展功能(SET MMFUNC)**](../../../../../../OM参考/命令/UNC MML命令/业务服务管理/Pre 5G接入业务管理/控制面管理/移动性管理/MM扩展功能管理/设置移动性管理扩展功能(SET MMFUNC)_26145512.md)

#### [告警](#ZH-CN_CONCEPT_0168358241)

本特性无相关告警。

#### [软参](#ZH-CN_CONCEPT_0168358241)

本特性无相关软参。

#### [测量指标](#ZH-CN_CONCEPT_0168358241)

本特性无相关测量指标。
