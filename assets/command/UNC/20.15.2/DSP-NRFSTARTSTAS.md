---
id: UNC@20.15.2@MMLCommand@DSP NRFSTARTSTAS
type: MMLCommand
name: DSP NRFSTARTSTAS（显示NRF开工状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NRFSTARTSTAS
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF维测管理
status: active
---

# DSP NRFSTARTSTAS（显示NRF开工状态）

## 功能

**适用NF：NRF**

查询NRF各微服务的开工状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CSTYPE | 微服务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示微服务类型。<br>数据来源：全网规划<br>取值范围：<br>- NFM（NFM）<br>- DISC（DISC）<br>- AUTH（AUTH）<br>默认值：无<br>配置原则：无 |
| ACTORNAME | 功能实体名称 | 可选必选说明：可选参数<br>参数含义：该参数表示对应微服务的功能实体名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |
| STATUS | 开工状态 | 可选必选说明：可选参数<br>参数含义：该参数表示对应微服务功能实体的开工状态。开工状态完全正常经历三个阶段分别为阶段一、阶段二、阶段三，阶段三完成后开工状态为正常状态。<br>数据来源：全网规划<br>取值范围：<br>- OK（状态正常）<br>- STAGE1（阶段一）<br>- STAGE2（阶段二）<br>- STAGE3（阶段三）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NRF开工状态（NRFSTARTSTAS）](configobject/UNC/20.15.2/NRFSTARTSTAS.md)

## 使用实例

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

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示NRF开工状态（DSP-NRFSTARTSTAS）_09651466.md`
