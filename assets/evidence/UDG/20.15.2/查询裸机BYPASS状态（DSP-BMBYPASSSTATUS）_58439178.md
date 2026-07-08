# 查询裸机BYPASS状态（DSP BMBYPASSSTATUS）

- [命令功能](#ZH-CN_MMLREF_0000001558439178__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001558439178__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001558439178__1.3.3)
- [使用实例](#ZH-CN_MMLREF_0000001558439178__1.3.4)
- [输出结果说明](#ZH-CN_MMLREF_0000001558439178__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001558439178)

本命令用于查询裸机场景下Pod当前的BYPASS状态。

- 若需要查询所有裸机场景下Pod的BYPASS状态，只需要输入“网元ID”即可。
- 若需要查询指定裸机场景下Pod的BYPASS状态，需要输入“网元ID”和“Pod名称”参数。

> **说明**
> 该命令仅在Full-stack裸机场景下支持。

> **说明**
> 无。

## [参数说明](#ZH-CN_MMLREF_0000001558439178)

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| DST_APP_ID | 网元ID | 可选必选说明：必选参数。<br>参数含义：用于指示系统需要查询指定网元ID下的Pod BYPASS状态。<br>“网元ID”<br>获取方式为：点击<br>“首页”<br>，查看<br>“应用ID”<br>即可。<br>取值范围：0～65535。<br>默认值：无。<br>配置原则：无。 |
| DST_POD_NAME | Pod名称 | 可选必选说明：可选参数<br>参数含义：用于指示系统需要查询哪个Pod的BYPASS状态。用户可以通过<br>[**DSP POD**](../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>命令查看相应的Pod名称。<br>取值范围：不超过127位字符串。<br>默认值：无。<br>配置原则：无。 |

## [使用实例](#ZH-CN_MMLREF_0000001558439178)

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

## [输出结果说明](#ZH-CN_MMLREF_0000001558439178)

命令执行正常，会返回命令执行成功的提示信息。输出结果说明如 [表1](#ZH-CN_MMLREF_0000001558439178__table149221250144917) 所示。

命令执行异常，会返回提示对应的失败信息。错误码列表如 [表2](#ZH-CN_MMLREF_0000001558439178__table698716490471) 所示。

*表1 输出项说明*

| 输出项名称 | 输出项解释 |
| --- | --- |
| 网元ID | 用于返回查询网元的ID。 |
| Pod名称 | 用于返回查询的Pod名称 |
| 查询状态 | 用于返回本Pod查询是否成功。 |
| 手工进入BYPASS | 用于查询当前Pod是否设置手动进入Bypass。<br>取值范围：<br>- “No”：用于返回当前Pod未设置手动进入Bypass。<br>- “Yes”：用于返回当前Pod设置了手动进入Bypass。 |
| BYPASS状态 | 用于返回查询的Pod当前所处的BYPASS状态。<br>取值范围：<br>- “Normal”：用于返回当前Pod的Bypass状态为非Bypass状态。<br>- “Bypass”：用于返回当前Pod的Bypass状态为Bypass状态。 |
| 详细信息 | 用于返回成功和失败的详细信息。 |

*表2 错误码列表*

| 错误码 | 错误码解释 | 原因分析 | 处理建议 |
| --- | --- | --- | --- |
| 20023 | 操作失败 | 设置失败。 | 请联系<br>华为<br>技术支持。 |
| 20024 | 查不到相应数据或不支持该查询条件 | 没有符合条件的查询结果。 | 请联系<br>华为<br>技术支持。 |
| 20025 | 此命令只在裸机场景下生效 | 此场景非裸机场景。 | 请联系<br>华为<br>技术支持。 |
| 20026 | 部分成功 | 部分后端节点响应失败。 | 请联系<br>华为<br>技术支持。 |
