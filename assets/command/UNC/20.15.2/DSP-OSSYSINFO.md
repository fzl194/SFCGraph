---
id: UNC@20.15.2@MMLCommand@DSP OSSYSINFO
type: MMLCommand
name: DSP OSSYSINFO（查询OS系统信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSSYSINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 容器管理
status: active
---

# DSP OSSYSINFO（查询OS系统信息）

## 功能

该命令用于查询OS的系统信息。

> **说明**
> 该命令仅在 Full-stack 虚机场景下支持。
>
> 本文档中所涉及的所有版本号仅为示例，具体操作时请以实际版本号为准。

## 注意事项

若执行 **DSP OSSYSINFO** 返回结果中某节点 “运行类型” 为 “None” ，请联系华为技术支持。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| TYPE | 资源类型 | 可选必选说明：必选参数。<br>参数含义：用于指示需要查询的OS系统资源类型信息。<br>取值范围：<br>- “CNTENGINE(容器引擎)”<br>- “NICDRV(网卡驱动)”<br>- “DRVPKG(驱动包)”<br>默认值：无。<br>配置原则：无。 |
| NODEIP | 节点IP | 可选必选说明：可选参数。<br>参数含义：用于指示OS系统需要查询哪个节点的资源类型信息。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示查询所有节点的对应资源类型信息。<br>- 可以通过[**DSP NODE**](../节点管理/节点查询（DSP NODE）_71678755.md)命令查询节点IP地址。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSSYSINFO]] · OS系统信息（OSSYSINFO）

## 使用实例

1. 查询 “资源类型” 为 “CNTENGINE(容器引擎)” 的所有节点OS系统信息：

```
%%DSP OSSYSINFO: TYPE=CNTENGINE;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
资源类型  节点IP    运行类型    

容器引擎  10.0.0.0  Docker     
容器引擎  10.0.0.1  Docker     
容器引擎  10.0.0.2  Docker     
(结果个数 = 3)  

---    END
```

2. 查询 “资源类型” 为 “CNTENGINE(容器引擎)” ， “节点IP” 为 “10.0.0.0” 的节点OS系统信息：

```
%%DSP OSSYSINFO: TYPE=CNTENGINE, NODEIP="10.0.0.0";%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
资源类型  =  容器引擎   
  节点IP  =  10.0.0.0 
运行类型  =  Docker 
(结果个数 = 1)  

---    END
```

3. 查询 “资源类型” 为 “NICDRV(网卡驱动)” 的所有节点OS系统信息：

> **说明**
> 查询结果中的 “驱动版本” 为字符串形式，长度范围是1~32。

```
%%DSP OSSYSINFO: TYPE=NICDRV;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
资源类型  节点IP           网卡信息                                   驱动名称    驱动版本  

网卡驱动  10.0.0.0         Virtio: Virtio network device [1af4:1000]  virtio_net  1.0.0     
网卡驱动  10.0.0.1         Virtio: Virtio network device [1af4:1000]  virtio_net  1.0.0     
网卡驱动  10.0.0.2         Virtio: Virtio network device [1af4:1000]  virtio_net  1.0.0     
(结果个数 = 3)

---    END
```

4. 查询 “资源类型” 为 “NICDRV(网卡驱动)” ， “节点IP” 为 “10.0.0.0” 的节点OS系统信息：

```
%%DSP OSSYSINFO: TYPE=NICDRV, NODEIP="10.0.0.0";%% 
RETCODE = 0  操作成功  

操作结果如下 
------------  
  资源类型  =  网卡驱动
    节点IP  =  10.0.0.0
  网卡信息  =  Virtio: Virtio network device [1af4:1000]
  驱动名称  =  virtio_net
  驱动版本  =  1.0.0
(结果个数 = 1)

---    END
```

5. 查询 “资源类型” 为 “DRVPKG(驱动包)” 的所有节点OS系统信息：

```
%%DSP OSSYSINFO: TYPE=DRVPKG;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
资源类型  节点IP           软件包名称                                     

驱动包    10.0.0.0         5G_Core_VFDriver_5.4-3.6.8.1_v2r12_8.2.tar.gz                                              
驱动包    10.0.0.1         5G_Core_VFDriver_5.4-3.6.8.1_v2r12_8.2.tar.gz  
驱动包    10.0.0.2         5G_Core_VFDriver_5.4-3.6.8.1_v2r12_8.2.tar.gz
(结果个数 = 3)  

---    END
```

6. 查询 “资源类型” 为 “DRVPKG(驱动包)” ， “节点IP” 为 “10.0.0.0” 的节点OS系统信息：

```
%%DSP OSSYSINFO: TYPE=DRVPKG, NODEIP="10.0.0.0";%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
  资源类型  =  驱动包
    节点IP  =  10.0.0.0
软件包名称  =  5G_Core_VFDriver_5.4-3.6.8.1_v2r12_8.2.tar.gz
(结果个数 = 1) 

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSSYSINFO.md`
