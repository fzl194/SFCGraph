---
id: UNC@20.15.2@MMLCommand@DSP MEASSTAT
type: MMLCommand
name: DSP MEASSTAT（查询话统指标测量状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MEASSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计
status: active
---

# DSP MEASSTAT（查询话统指标测量状态）

## 功能

该命令用于获得网元上的话统指标的测量状态，包含采集端、汇聚端的测量信息。

## 注意事项

无。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数。<br>参数含义：标识网元ID。<br>取值范围：0~65535。<br>默认值：无。<br>配置原则：可以通过<br>[**LST ME**](../../系统管理/版本信息/查询网元配置信息（LST ME）_47084797.md)<br>命令查询获取。 |
| METRICID | 测量指标ID | 可选必选说明：必选参数。<br>参数含义：测量指标ID。<br>取值范围：字符串类型，长度不超过256个字符。<br>默认值：无。<br>配置原则：可以通过<br>[**LST MEASUNIT**](查询测量指标模型(LST MEASUNIT)_47814449.md)<br>命令查询获取。支持最多6个测量指标ID，以&字符分割，不能以&结尾，且属于同一个测量单元。例如 1&2&3。 |
| MOIID | 对象实例ID | 可选必选说明：必选参数。<br>参数含义：对象实例ID。<br>取值范围：字符串类型，长度不超过256个字符。<br>默认值：无。<br>配置原则：可以通过<br>[**DSP MEASOBJ**](查询话统测量对象实例(DSP MEASOBJ)_01094728.md)<br>命令查询获取。 |
| SOURCE | 数据源 | 可选必选说明：必选参数。<br>参数含义：标识查询的话统指标测量状态的数据来源。<br>取值范围：<br>- COLLECTION_END(采集端)<br>- CONVERGENCE_END(汇聚端)<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MEASSTAT]] · 话统指标测量状态（MEASSTAT）

## 使用实例

1. 查询网元采集端话统指标信息：
  ```
  %%DSP MEASSTAT: MEID=88, METRICID="141100300", MOIID="Moc30-1", SOURCE=COLLECTION_END;%%
  RETCODE = 0  操作成功

  测量采集端信息
  --------------
  测量服务          测量服务实例           测量服务实例IP                   查询状态  测量指标ID  测量指标名称  周期(秒)  测量状态    指标值  

  TestforJAVASDK01  TestForCSPPerfService  fc00:2000:3000:fc00:2000:0:0:6a  成功      141100300   指标300       5         无测量指标  NULL    
  TestforJAVASDK01  TestForCSPPerfService  fc00:2000:3000:fc00:2000:0:0:6a  成功      141100300   指标300       60        无测量指标  NULL    
  TestforJAVASDK01  TestForCSPPerfService  fc00:2000:3000:fc00:2000:0:0:6a  成功      141100300   指标300       300       无测量指标  NULL    
  TestforJAVASDK01  TestForCSPPerfService  fc00:2000:3000:fc00:2000:0:0:89  成功      141100300   指标300       5         无测量指标  NULL    
  TestforJAVASDK01  TestForCSPPerfService  fc00:2000:3000:fc00:2000:0:0:89  成功      141100300   指标300       60        无测量指标  NULL    
  TestforJAVASDK01  TestForCSPPerfService  fc00:2000:3000:fc00:2000:0:0:89  成功      141100300   指标300       300       无测量指标  NULL    
  TestforJAVASDK01  testforjavasdk02       fc00:2000:3000:fc00:2000:0:0:6a  成功      141100300   指标300       5         无测量任务  NULL    
  TestforJAVASDK01  testforjavasdk02       fc00:2000:3000:fc00:2000:0:0:6a  成功      141100300   指标300       60        无测量任务  NULL    
  TestforJAVASDK01  testforjavasdk02       fc00:2000:3000:fc00:2000:0:0:6a  成功      141100300   指标300       300       正常        0.000     
  TestforJAVASDK01  testforjavasdk02       fc00:2000:3000:fc00:2000:0:0:89  成功      141100300   指标300       5         无测量任务  NULL    
  TestforJAVASDK01  testforjavasdk02       fc00:2000:3000:fc00:2000:0:0:89  成功      141100300   指标300       60        无测量任务  NULL    
  TestforJAVASDK01  testforjavasdk02       fc00:2000:3000:fc00:2000:0:0:89  成功      141100300   指标300       300       正常        0.000     
  (结果个数 = 12)

  ---    END
  ```
2. 查询网元汇聚端话统指标信息：
  ```
  %%DSP MEASSTAT: MEID=88, METRICID="141100300", MOIID="Moc30-1", SOURCE=CONVERGENCE_END;%%
  RETCODE = 0  操作成功

  测量汇聚端信息
  --------------
  汇聚服务实例                  查询状态  周期(秒)  开始时间             测量指标ID  测量指标名称  测量状态  指标值  

  fc00:2000:3000:fc00:2000::15  成功      300       2021-08-11 19:10:00  141100300   指标300       正常      0.000   
  fc00:2000:3000:fc00:2000::4   成功      NULL      NULL                 NULL        NULL          NULL      NULL    
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话统指标测量状态(DSP-MEASSTAT)_47694525.md`
