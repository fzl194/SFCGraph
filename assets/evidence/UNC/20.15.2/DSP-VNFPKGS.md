# 显示网元关联的软件包名称（DSP VNFPKGS）

- [命令功能](#ZH-CN_MMLREF_0000001741791101__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001741791101__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001741791101__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001741791101__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001741791101__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001741791101)

该命令用于查询网元关联的软件包名称信息。

## [注意事项](#ZH-CN_MMLREF_0000001741791101)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001741791101)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001741791101)

无

## [使用实例](#ZH-CN_MMLREF_0000001741791101)

假如运营商想要查询当前环境已上传的软件包名称，调用以下命令可以查询已上传的软件包名称。

```
%%DSP VNFPKGS:;%%
RETCODE = 0  操作成功

结果如下
--------
软件包名称                                       

t4-device-plugin-fst-manage                      
unc-to-24.1.rc1.b061-tosca-std-edge-arm          
om-service-fst-manage                            
unc-24.1.rc1.b061-tosca-vdm-share-bond-edge-arm  
trm-fst-manage                                   
net-24.1.rc1.b061-tosca-testapp-2u-1822-edge     
unc-24.1.rc1.b084-tosca-ueg-plus-bond-edge-arm   
alarmnotifyservice-fst-manage                    
tosca-csp-network-24.1.rc1.b030-ex               
extension-controller-manager-fst-manage          
unc-24.1.rc1.b061-tosca-ueg-plus-bond-edge-arm   
cfeapiserver-fst-manage                          
tosca-csp-24.1.rc1.b030-ex                       
om-network-service-fst-manage                    
provision-controller-manager-fst-manage          
(结果个数 = 15)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001741791101)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 软件包名称 | 该参数用于表示软件包名称。 |
