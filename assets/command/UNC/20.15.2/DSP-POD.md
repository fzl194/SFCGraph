---
id: UNC@20.15.2@MMLCommand@DSP POD
type: MMLCommand
name: DSP POD（POD查询）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: POD
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- Pod管理
status: active
---

# DSP POD（POD查询）

## 功能

该命令用于查询指定Pod名称或类型的Pod信息。

## 注意事项

- 支持输入参数全为空时的全量查询；支持按照Pod类型查询时进行模糊匹配。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：查询Pod服务所在的网元ID，即应用ID。<br>取值范围：长度不超过40的字符串。<br>默认值：无。<br>配置原则：<br>- 可以通过MML命令“LST ME”获取。<br>- 若不输入，表示查询所有网元的Pod信息。 |
| ONREBUILD | 是否待重建 | 可选必选说明：可选参数<br>参数含义：查询pod的待重建状态。<br>取值范围：<br>- OnRebuild(待重建状态)：查询待重建的pod信息。<br>- Normal(正常状态)：查询正常状态的pod信息。<br>默认值：无。<br>配置原则：若不输入，表示查询所有状态的Pod信息。 |
| TYPE | Pod查询类型 | 可选必选说明：可选参数<br>参数含义：查询Pod的方式。<br>取值范围：<br>- byId(Pod名称)：按照Pod名称查询Pod信息。<br>- byType(Pod类型)：按照Pod类型查询Pod信息。<br>默认值：无。<br>配置原则：无。 |
| PODNAME | Pod名称 | 可选必选说明：该参数在<br>“Pod查询类型”<br>取值为<br>“Pod名称”<br>时为必选参数。<br>参数含义：Pod名称。<br>取值范围：字符串类型，字符串长度范围为3~100个字符。<br>默认值：无。<br>配置原则：<br>- 服务实例所在Pod名称，该参数仅在“Pod查询类型”取值为“Pod名称”时有效。<br>- 可以通过执行此命令时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod名称”列表。<br>- 该参数不支持在“Pod名称”列表中模糊匹配查询。 |
| PODTYPE | Pod类型 | 可选必选说明：该参数在<br>“Pod查询类型”<br>取值为<br>“Pod类型”<br>时为必选参数。<br>参数含义：Pod类型。<br>取值范围：字符串类型，字符串长度范围为3~100个字符。<br>默认值：无。<br>配置原则：<br>- 该参数仅在“Pod查询类型”取值为“Pod类型”时有效。<br>- 可以通过执行此命令时不输入“网元ID”且不选择“Pod查询类型”获取所有的“Pod类型”列表。<br>- 该参数支持在“Pod类型”列表中模糊匹配查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/POD]] · POD停止（POD）

## 使用实例

5G中心虚机场景：

1. 根据Pod名称查询Pod信息。
  ```
  %%DSP POD: MEID="0",TYPE=byId, PODNAME="helpcenter-6595bd7fb7-fsqzz";%% 
  RETCODE = 0  操作成功 
 
  操作结果如下 
  ------------ 
      Pod名称  =  helpcenter-6595bd7fb7-fsqzz
      Pod类型  =  helpcenter
      Pod状态  =  Running
     节点名称  =  10.186.125.60
     主机名称  =  803AA02C-2197-E611-AAB1-48D5396401E6
  Pod运行时间  =  3d17h
   是否待重建  =  Normal
  (结果个数 = 1)  

  ---    END
  ```
2. 根据Pod类型查询Pod信息。
  ```
  %%DSP POD: MEID="0",TYPE=byType, PODTYPE="helpcenter";%% 
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------ 
  Pod名称                       Pod类型      Pod状态    节点名称       主机名称                               Pod运行时间   是否待重建
  helpcenter-6595bd7fb7-fsqzz   helpcenter   Running    10.186.125.60  803AA02C-2197-E611-AAB1-48D5396401E6   3d17h         Normal   
  helpcenter-6595bd7fb7-qrqjl   helpcenter   Running    10.186.125.80  3DD7DA93-1D50-008E-E811-91465CB1BACF   3d17h         Normal
  (结果个数 = 2)  

  ---    END
  ```
3. 根据Pod类型模糊匹配查询Pod信息。
  ```
  %%DSP POD: MEID="0",TYPE=byType, PODTYPE="cse";%%
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------ 
  Pod名称                              Pod类型             Pod状态    节点名称        主机名称                              Pod运行时间   是否待重建

  cse-etcd-0                           cse-etcd            Running    10.186.125.102  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         Normal
  cse-etcd-1                           cse-etcd            Running    10.186.125.103  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         Normal
  cse-etcd-2                           cse-etcd            Running    10.186.125.104  92645A88-058E-E611-8891-203DB26977DA  3d18h         Normal
  cse-service-center-5cc56794c4-g95nh  cse-service-center  Running    10.186.125.105  92645A88-058E-E611-8891-203DB26977DA  3d17h         Normal
  cse-service-center-5cc56794c4-lpstl  cse-service-center  Running    10.186.125.106  803AA02C-2197-E611-AAB1-48D5396401E6  3d17h         Normal
  cse-service-center-5cc56794c4-v7fnc  cse-service-center  Running    10.186.125.107  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d17h         Normal
  (结果个数 = 6)  

  ---    END
  ```
4. 查询全量Pod信息。
  ```
  %%DSP POD:;%%
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------ 
  Pod名称                              Pod类型             Pod状态    节点名称        主机名称                              Pod运行时间   是否待重建

  auditlog-6c95885589-pzbfp            auditlog            Running    10.186.125.110  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         Normal
  auditlog-6c95885589-wng6t            auditlog            Running    10.186.125.120  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         Normal
  backupmgr-75886c9d4b-cnjrd           backupmgr           Running    10.186.125.130  92645A88-058E-E611-8891-203DB26977DA  3d18h         Normal
  ......
  zookeeper-1                          zookeeper           Running    10.186.125.140  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         OnRebuild
  zookeeper-2                          zookeeper           Running    10.186.125.150  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         OnRebuild
  (结果个数 = 89)  

  ---    END
  ```
5. 根据Pod名称查询待重建状态Pod信息。
  ```
  %%DSP POD: MEID="0", ONREBUILD=OnRebuild, TYPE=byId, PODNAME="helpcenter-6595bd7fb7-fsqzz";%% 
  RETCODE = 0  操作成功 
 
  操作结果如下 
  ------------ 
      Pod名称  =  helpcenter-6595bd7fb7-fsqzz
      Pod类型  =  helpcenter
      Pod状态  =  Running
     节点名称  =  10.186.125.60
     主机名称  =  803AA02C-2197-E611-AAB1-48D5396401E6
  Pod运行时间  =  3d17h
   是否待重建  =  OnRebuild
  (结果个数 = 1)  

  ---    END
  ```
6. 根据Pod类型查询待重建状态的Pod信息。
  ```
  %%DSP POD: ONREBUILD=OnRebuild, TYPE=byType, PODTYPE="fileserver";%% 
  RETCODE = 0  操作成功  
  操作结果如下 
  ------------ 
  Pod名称       Pod类型     Pod状态  节点名称        主机名称                               Pod运行时间   是否待重建    

  fileserver-0  fileserver  Running  10.101.28.154   803AA02C-2197-E611-AAB1-48D5396401E6   143m          OnRebuild       
  fileserver-1  fileserver  Running  10.101.28.23    92645A88-058E-E611-8891-203DB26977DA   143m          OnRebuild   
  (结果个数 = 2)  

  ---    END
  ```
7. 全量查询待重建状态的Pod信息。
  ```
  %%DSP POD: ONREBUILD=OnRebuild;%%
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------ 
  Pod名称                              Pod类型             Pod状态    节点名称        主机名称                              Pod运行时间   是否待重建

  zookeeper-1                          zookeeper           Running    10.186.125.140  803AA02C-2197-E611-AAB1-48D5396401E6  3d18h         OnRebuild
  zookeeper-2                          zookeeper           Running    10.186.125.150  3DD7DA93-1D50-008E-E811-91465CB1BACF  3d18h         OnRebuild
  (结果个数 = 2)  

  ---    END
  ```

5G中心裸机场景：

1. 根据Pod名称查询Mini Pod信息。
  ```
  %%DSP POD: TYPE=byId, PODNAME="cse-etcd-0";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
      Pod名称  =  cse-etcd-0
      Pod类型  =  cse-etcd
      Pod状态  =  Running
     节点名称  =  csp-c-resourcepool-625b60e6-0-doubleupg04
     主机名称  =  paas-10-186-125-110
  Pod运行时间  =  10h
   是否待重建  =  Normal
  (结果个数 = 1)

  ---    END
  ```
2. 根据Pod名称查询Super Pod信息。
  ```
  %%DSP POD: TYPE=byId, PODNAME="csp-c-resourcepool-625b60e6-0";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
      Pod名称  =  csp-c-resourcepool-625b60e6-0
      Pod类型  =  vnode
      Pod状态  =  Running
     节点名称  =  paas-10-186-125-110
     主机名称  =  paas-10-186-125-110
  Pod运行时间  =  10h
   是否待重建  =  Normal
  (结果个数 = 1)

  ---    END
  ```
3. 根据Pod类型查询Pod信息。
  ```
  %%DSP POD: TYPE=byType, PODTYPE="cse";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  Pod名称                             Pod类型             Pod状态  节点名称                                   主机名称             Pod运行时间   是否待重建

  cse-etcd-0                          cse-etcd            Running  csp-c-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-110  10h           Normal
  cse-etcd-1                          cse-etcd            Running  csp-a-resourcepool-625b60e6-1-doubleupg04  paas-10-186-125-111  10h           Normal
  cse-etcd-2                          cse-etcd            Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-112  10h           Normal
  cse-service-center-969497985-8m8vh  cse-service-center  Running  csp-c-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-110  10h           Normal
  cse-service-center-969497985-9n5bg  cse-service-center  Running  csp-a-resourcepool-625b60e6-1-doubleupg04  paas-10-186-125-111  2d18h         Normal
  cse-service-center-969497985-wcpcl  cse-service-center  Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-112  2d18h         Normal
  dcserimage-0-6c878cdf7b-fthk2       dcserimage-0        Running  csp-a-resourcepool-0af34063-0-doubleupg04  paas-10-186-125-110  4d23h         Normal
  dcserimage-0-6c878cdf7b-wng45       dcserimage-0        Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-111  4d23h         Normal
  (结果个数 = 8)

  ---    END
  ```
4. 根据Pod类型查询vnode类型的Pod信息。
  ```
  %%DSP POD: TYPE=byType, PODTYPE="vnode";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  Pod名称                        Pod类型  Pod状态  节点名称             主机名称             Pod运行时间   是否待重建

  csp-a-resourcepool-625b60e6-0  vnode    Running  paas-10-186-125-110  paas-10-186-125-110  4d23h         Normal
  csp-a-resourcepool-625b60e6-1  vnode    Running  paas-10-186-125-111  paas-10-186-125-111  4d23h         Normal
  csp-c-resourcepool-625b60e6-0  vnode    Running  paas-10-186-125-112  paas-10-186-125-112  10h           Normal
  (结果个数 = 3)

  ---    END
  ```
5. 查询全量Pod信息。
  ```
  %%DSP POD:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  Pod名称                                      Pod类型                     Pod状态  节点名称                                   主机名称             Pod运行时间   是否待重建

  auditlog-775d449666-9zwwl                    auditlog                    Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-110  44h           Normal
  auditlog-775d449666-fdst5                    auditlog                    Running  csp-a-resourcepool-625b60e6-1-doubleupg04  paas-10-186-125-111  44h           Normal
  backupmgr-0                                  backupmgr                   Running  csp-a-resourcepool-625b60e6-0-doubleupg04  paas-10-186-125-112  2d19h         OnRebuild
  csp-a-resourcepool-625b60e6-0                vnode                       Running  paas-10-186-125-110                        paas-10-186-125-110  2d19h         Normal
  csp-a-resourcepool-625b60e6-1                vnode                       Running  paas-10-186-125-111                        paas-10-186-125-111  2d19h         Normal
  csp-c-resourcepool-625b60e6-0                vnode                       Running  paas-10-186-125-112                        paas-10-186-125-112  2d19h         Normal
  ......
  (结果个数 = 98)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/POD查询（DSP-POD）_69830277.md`
