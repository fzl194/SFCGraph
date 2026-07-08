# 显示NSSF开工状态（DSP NSSFSTARTSTAS）

- [命令功能](#ZH-CN_MMLREF_0264343869__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0264343869__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0264343869__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0264343869__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0264343869__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0264343869)

**适用NF：NSSF**

查询NSSF微服务的开工状态。

## [注意事项](#ZH-CN_MMLREF_0264343869)

无

#### [操作用户权限](#ZH-CN_MMLREF_0264343869)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0264343869)

无

## [使用实例](#ZH-CN_MMLREF_0264343869)

查询所有NSSF微服务的开工状态：

```
%%DSP NSSFSTARTSTAS:;%%
RETCODE = 0  执行成功

结果如下
------------------------
微服务类型         功能实体名称                                            开工状态        

NSSF               nssf/cellcore/cell-service-NssfExecSvc                  状态正常 
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet2   状态正常  
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet3   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet4   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet5   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet0   状态正常
NSSF               nssf/cellcore/cell-service-NssfExecSvc/NssfDomainSet1   状态正常
NSSF               ctrl/cellcore/cell-service-NssfCtrlSvc                  状态正常
(结果个数 = 8)
```

## [输出结果说明](#ZH-CN_MMLREF_0264343869)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 微服务类型 | 该参数表示微服务类型。<br>取值说明：<br>- NSSF（NSSF） |
| 功能实体名称 | 该参数表示对应微服务的功能实体名称。 |
| 开工状态 | 该参数表示对应微服务功能实体的开工状态。开工状态完全正常经历三个阶段分别为阶段一、阶段二、阶段三，阶段三完成后开工状态为正常状态。<br>取值说明：<br>- OK（状态正常）<br>- STAGE1（阶段一）<br>- STAGE2（阶段二）<br>- STAGE3（阶段三） |
