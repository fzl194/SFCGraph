---
id: UDG@20.15.2@MMLCommand@DSP VNFPKGS
type: MMLCommand
name: DSP VNFPKGS（显示网元关联的软件包名称）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: VNFPKGS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 编排管理
- 一键式部署
status: active
---

# DSP VNFPKGS（显示网元关联的软件包名称）

## 功能

该命令用于查询网元关联的软件包名称信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UDG/20.15.2/VNFPKGS]] · 网元关联的软件包名称（VNFPKGS）

## 使用实例

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

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示网元关联的软件包名称（DSP-VNFPKGS）_41791101.md`
