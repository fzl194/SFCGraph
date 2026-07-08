# 显示NRF开工状态（DSP NRFSTARTSTAS）

- [命令功能](#ZH-CN_MMLREF_0209651466__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651466__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651466__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651466__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0209651466__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0209651466)

**适用NF：NRF**

查询NRF各微服务的开工状态。

## [注意事项](#ZH-CN_MMLREF_0209651466)

无

#### [操作用户权限](#ZH-CN_MMLREF_0209651466)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651466)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示微服务类型。<br>数据来源：全网规划<br>取值范围：<br>- NFM（NFM）<br>- DISC（DISC）<br>- AUTH（AUTH）<br>默认值：无<br>配置原则：无 |
| ACTORNAME | 功能实体名称 | 可选必选说明：可选参数<br>参数含义：该参数表示对应微服务的功能实体名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| STATUS | 开工状态 | 可选必选说明：可选参数<br>参数含义：该参数表示对应微服务功能实体的开工状态。开工状态完全正常经历三个阶段分别为阶段一、阶段二、阶段三，阶段三完成后开工状态为正常状态。<br>数据来源：全网规划<br>取值范围：<br>- OK（状态正常）<br>- STAGE1（阶段一）<br>- STAGE2（阶段二）<br>- STAGE3（阶段三）<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209651466)

查询所有NRF各微服务的开工状态：

```
%%DSP NRFSTARTSTAS:;%%
RETCODE = 0  执行成功

结果如下
------------------------
微服务类型         功能实体名称                                            状态        

NFM                nfm/cellcore/cell-service-NfmExecSvc/NfmDomainSet1      状态正常 
NFM                nfm/cellcore/cell-service-NfmExecSvc/NfmDomainSet0      状态正常  
NFM                nfm/cellcore/cell-service-NfmExecSvc/NfmDomainSet2      状态正常   
NFM                nfm/cellcore/cell-service-NfmExecSvc                    状态正常   
AUTH               auth/cellcore/cell-service-AuthExecSvc                  阶段一     
AUTH               auth/cellcore/cell-service-AuthExecSvc/AuthDomainSet0   状态正常   
AUTH               auth/cellcore/cell-service-AuthExecSvc/AuthDomainSet1   状态正常   
DISC               ctrl/cellcore/cell-service-DiscCtrlSvc                  状态正常   
NFM                ctrl/cellcore/cell-service-NfmCtrlSvc                   阶段三   
AUTH               ctrl/cellcore/cell-service-AuthCtrlSvc                  状态正常   
(结果个数 = 10)
```

## [输出结果说明](#ZH-CN_MMLREF_0209651466)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 微服务类型 | 该参数表示微服务类型。<br>取值说明：<br>- NFM（NFM）<br>- DISC（DISC）<br>- AUTH（AUTH） |
| 功能实体名称 | 该参数表示对应微服务的功能实体名称。 |
| 开工状态 | 该参数表示对应微服务功能实体的开工状态。开工状态完全正常经历三个阶段分别为阶段一、阶段二、阶段三，阶段三完成后开工状态为正常状态。<br>取值说明：<br>- OK（状态正常）<br>- STAGE1（阶段一）<br>- STAGE2（阶段二）<br>- STAGE3（阶段三） |
