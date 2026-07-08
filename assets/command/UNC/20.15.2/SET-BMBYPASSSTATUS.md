---
id: UNC@20.15.2@MMLCommand@SET BMBYPASSSTATUS
type: MMLCommand
name: SET BMBYPASSSTATUS（设置裸机BYPASS状态）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BMBYPASSSTATUS
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass状态管理
status: active
---

# SET BMBYPASSSTATUS（设置裸机BYPASS状态）

## 功能

![](设置裸机BYPASS状态（SET BMBYPASSSTATUS）_58599098.assets/notice_3.0-zh-cn_2.png)

设置进入BYPASS状态后，仅最小维护通道功能可用；设置退出BYPASS状态前请确认 [ALM-135552 节点存储亚健康](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135552 节点存储亚健康_57945194.md) 告警已经恢复，请慎重使用该命令。

本命令用于手动设置裸机场景下Pod当前BYPASS状态。

- 若需要设置所有裸机场景下Pod的BYPASS状态，只需要输入“网元ID”即可。
- 若需要设置指定裸机场景下Pod的BYPASS状态，需要输入“网元ID”和“Pod名称”参数。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

## 注意事项

- 该命令仅限系统管理员可以执行。
- BYPASS状态存在系统初始记录，参数的初始设置值如下：

| 参数名称 | 设置初始值 |
| --- | --- |
| BYPASS状态 | Normal |

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| SST_APP_ID | 网元ID | 可选必选说明：必选参数<br>参数含义：用于指示系统需要设置指定网元ID下的Pod的BYPASS状态。<br>“网元ID”<br>获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |
| SST_SET_TYPE | 设置BYPASS状态类型 | 可选必选说明：必选参数<br>参数含义：用于指示系统需要设置的BYPASS状态。<br>取值范围：<br>- “enter(进入BYPASS)”<br>- “exit(退出BYPASS)”<br>默认值：无。<br>配置原则<br>- 本命令配置原则是根据当前存储对业务的影响来选择进入和退出BYPASS状态，存储状态可参考<br>[ALM-135552 节点存储亚健康](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135552 节点存储亚健康_57945194.md)<br>。<br>- 在发生节点<br>[ALM-135552 节点存储亚健康](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135552 节点存储亚健康_57945194.md)<br>时，用户可根据当前存储对业务的影响来选择是否需要进入BYPASS，如果需要手动进入BYPASS，则选择enter。<br>- 在节点[ALM-135552 节点存储亚健康](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135552 节点存储亚健康_57945194.md)消失时，用户可根据当前存储对业务的影响来选择是否需要退出BYPASS，如果需要手动退出BYPASS，则选择exit。 |
| SST_POD_NAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要设置哪个Pod的BYPASS状态。用户可以通过<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>命令查看相应的Pod名称。<br>取值范围：不超过127位字符串。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BMBYPASSSTATUS]] · 裸机BYPASS状态（BMBYPASSSTATUS）

## 使用实例

1. 按照网元ID设置BYPASS状态。
  ```
  %%SET BMBYPASSSTATUS: SST_APP_ID=0, SST_SET_TYPE=enter;%%
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  网元ID  Pod名称           设置类型      详细信息    
  0       messagetrace-1    进入Bypass    Success    
  0       runlog-0          进入Bypass    Success    
  0       mmlservice-1      进入Bypass    Success    
  0       omlb-0            进入Bypass    Success   
  (结果个数 = 4)  
  ---    END 
  ```
2. 按照PodName设置BYPASS状态。
  ```
  %%SET BMBYPASSSTATUS: SST_APP_ID=0, SST_SET_TYPE=enter, SST_POD_NAME="runlog-0";%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------         
    网元ID  =  0        
   Pod名称  =  runlog-0  
  设置类型  =  进入Bypass
  详细信息  =  Success  
  (结果个数 = 1)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-BMBYPASSSTATUS.md`
