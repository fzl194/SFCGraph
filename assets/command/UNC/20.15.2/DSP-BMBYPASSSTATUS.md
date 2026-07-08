---
id: UNC@20.15.2@MMLCommand@DSP BMBYPASSSTATUS
type: MMLCommand
name: DSP BMBYPASSSTATUS（查询裸机BYPASS状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BMBYPASSSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- Bypass状态管理
status: active
---

# DSP BMBYPASSSTATUS（查询裸机BYPASS状态）

## 功能

本命令用于查询裸机场景下Pod当前的BYPASS状态。

- 若需要查询所有裸机场景下Pod的BYPASS状态，只需要输入“网元ID”即可。
- 若需要查询指定裸机场景下Pod的BYPASS状态，需要输入“网元ID”和“Pod名称”参数。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DST_APP_ID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要查询指定网元ID下的Pod BYPASS状态。<br>“网元ID”<br>获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |
| DST_POD_NAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要查询哪个Pod的BYPASS状态。用户可以通过<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>命令查看相应的Pod名称。<br>取值范围：不超过127位字符串。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BMBYPASSSTATUS]] · 裸机BYPASS状态（BMBYPASSSTATUS）

## 使用实例

1. 按照网元ID查询BYPASS状态。
  ```
  %%DSP BMBYPASSSTATUS: DST_APP_ID=0;%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  网元ID  Pod名称            查询状态  手工进入BYPASS  BYPASS状态      详细信息    
  0       messagetrace-1     Success   No              Normal          Success    
  0       runlog-0           Success   No              Normal          Success    
  0       mmlservice-1       Success   No              Normal          Success    
  0       omlb-0             Success   No              Normal          Success   
  (结果个数 = 4)  
  ---    END 
  ```
2. 按照PodName查询BYPASS状态。
  ```
  %%DSP BMBYPASSSTATUS: DST_APP_ID=0, DST_POD_NAME="runlog-0";%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------         
          网元ID  =  0        
         Pod名称  =  runlog-0       
        查询状态  =  Success 
  手工进入BYPASS  =  No 
      BYPASS状态  =  Normal       
        详细信息  =  Success 
  (结果个数 = 1)  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-BMBYPASSSTATUS.md`
