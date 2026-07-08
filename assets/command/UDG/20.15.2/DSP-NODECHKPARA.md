---
id: UDG@20.15.2@MMLCommand@DSP NODECHKPARA
type: MMLCommand
name: DSP NODECHKPARA（查询节点检测参数）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NODECHKPARA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# DSP NODECHKPARA（查询节点检测参数）

## 功能

本命令用于查询节点内存检测、节点CPU过载检测、inotify实例检测、inotify监控检测、节点信号量集检测、节点文件句柄检测、关键部件检测、IP互串冲突预防和智算单元资源检测参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

> **说明**
> - 本命令不支持在BYPASS期间执行。
> - 为了防止大容量场景下NRSAgent同时访问NRSMaster出现性能问题，当NRSAgent启动后会随机暂停一段时间（最多3分钟），建议在NRSAgent启动3分钟后再执行本命令进行查询。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数。<br>参数含义：用于指定需要查询的资源类型。<br>取值范围：<br>- “VM(虚拟机)”：用于虚拟机容器部署场景。<br>- “SERVER(服务器)”：用于裸机容器部署场景。<br>默认值：无。<br>配置原则：虚拟机容器部署场景，需要设置为<br>“VM(虚拟机)”<br>。 |
| PARAMTYPE | 参数类型 | 可选必选说明：该参数在<br>“RESTYPE”<br>配置为<br>“VM(虚拟机)”<br>时为条件必选参数。<br>参数含义：用于指定虚拟机容器部署场景需要查询的参数类型。<br>取值范围：<br>- “CHKNODEMEM(节点内存检测)”<br>- “CHKNODECPU(节点CPU过载检测)”<br>- “CHKINOTIFYINSTANCE(inotify实例检测)”<br>- “CHKINOTIFYWATCH(inotify监控检测)”<br>- “CHKNODESEMARRAY(节点信号量集检测)”<br>- “CHKNODEFILEHANDLE(节点文件句柄检测)”<br>- “CHKPORT(网卡检测)”<br>- “CHKIPROUTE(IP路由检测)”<br>- “CHKKEYFILE(关键文件检测)”<br>- “CHKPART(分区过载检测)”<br>- “CHKPROC(进程数检测)”<br>- “CHKINODE(inode使用率检测)”<br>- “CHKCNTSTOR(容器存储空间检测)”<br>- “CHKIPCONFLICT(IP互串冲突预防)”<br>- “CHKSMCU(智算单元资源检测)”<br>默认值：无。<br>配置原则：无。 |
| APPID | 网元ID | 可选必选说明：该参数在<br>“PARAMTYPE”<br>配置为<br>“CHKNODEMEM(节点内存检测)”<br>、<br>“CHKNODECPU(节点CPU过载检测)”<br>、<br>“CHKINOTIFYINSTANCE(inotify实例检测)”<br>、<br>“CHKINOTIFYWATCH(inotify监控检测)”<br>、<br>“CHKNODESEMARRAY(节点信号量集检测)”<br>或<br>“CHKNODEFILEHANDLE(节点文件句柄检测)”<br>其中之一时为条件必选参数。<br>参数含义：用于指定虚拟机容器部署场景系统需要查询的网元ID。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：可以通过单击<br>OM Portal<br>的<br>“首页”<br>查询网元ID。 |
| VDUTYPE | 虚拟机类型 | 可选必选说明：该参数在<br>“PARAMTYPE”<br>配置为任一取值时为条件可选参数。<br>参数含义：用于指定虚拟机容器部署场景系统需要查询节点内存检测参数、CPU过载检测参数、inotify实例检测参数、inotify监控检测参数、节点信号量集检测参数和节点文件句柄检测等参数的虚拟机类型。<br>取值范围：无。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示查询所有节点的信息。<br>- 虚拟机容器部署场景，用户可以通过[**DSP NODE**](节点查询（DSP NODE）_71678755.md)命令查看相应的虚拟机类型。 |
| PARAMTYPE_SV | 参数类型 | 可选必选说明：该参数在<br>“RESTYPE”<br>配置为<br>“SERVER(服务器)”<br>时为条件必选参数。<br>参数含义：无。<br>取值范围：<br>- “CHKNODECPU(节点CPU过载检测)”<br>- “CHKINOTIFYINSTANCE(inotify实例检测)”<br>- “CHKINOTIFYWATCH(inotify监控检测)”<br>- “CHKNODESEMARRAY(节点信号量集检测)”<br>- “CHKNODEFILEHANDLE(节点文件句柄检测)”<br>- “CHKPORT(网卡检测)”<br>- “CHKIPROUTE(IP路由检测)”<br>- “CHKKEYFILE(关键文件检测)”<br>- “CHKPART(分区过载检测)”<br>- “CHKPROC(进程数检测)”<br>- “CHKINODE(inode使用率检测)”<br>- “CHKCNTSTOR(容器存储空间检测)”<br>- “CHKIPCONFLICT(IP互串冲突预防)”<br>- “CHKNODEMEMFAULT(节点内存故障检测)”<br>- “CHKSMCU(智算单元资源检测)”<br>默认值：无。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| SERVERNAME | 服务器名称 | 可选必选说明：该参数在<br>“PARAMTYPE_SV”<br>配置为任一取值时为条件可选参数。<br>参数含义：无。<br>取值范围：无。<br>默认值：无。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| NODENAME | 节点名称 | 可选必选说明：该参数在<br>“PARAMTYPE”<br>配置为任一取值时为条件可选参数。<br>参数含义：用于指示虚拟机容器部署场景系统需要查询哪个节点的检测参数。<br>取值范围：不超过128位字符串。<br>默认值：无。<br>配置原则：<br>- 若不输入，则表示查询所有节点的信息。<br>- 虚拟机容器部署场景，用户可以通过[**DSP NODE**](节点查询（DSP NODE）_71678755.md)命令查看相应的节点名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NODECHKPARA]] · 节点检测参数（NODECHKPARA）

## 使用实例

1. 查询“网元ID”为“0”的所有节点“节点内存检测”参数信息。
  ```
  %%DSP NODECHKPARA: RESTYPE=VM, PARAMTYPE=CHKNODEMEM, APPID=0;%%
  RETCODE = 0  操作成功
  操作结果如下
  ------------------------ 
  资源类型      参数类型      网元ID  虚拟机类型  节点名称       节点IP        检测开关  检测阈值（%）  

  虚拟机        节点内存检测  0       CSP_B       10.0.0.3       10.0.0.3       开启        66             
  虚拟机        节点内存检测  0       CSP_C       10.0.0.2       10.0.0.2       开启        66             
  虚拟机        节点内存检测  0       CSP_A       10.0.0.1       10.0.0.1       开启        66 
  (结果个数 = 3)

  ---    END
  ```
2. 查询“网元ID”为“0”，“虚拟机类型”为“CSP_A”的“节点CPU过载检测”参数信息。
  ```
  %%DSP NODECHKPARA: RESTYPE=VM, PARAMTYPE=CHKNODECPU, APPID=0, VDUTYPE="CSP_A";%%
  RETCODE = 0  操作成功
  
  操作结果如下 
  ------------
           资源类型  =  虚拟机
           参数类型  =  节点CPU过载检测
             网元ID  =  0
         虚拟机类型  =  CSP_A
           节点名称  =  10.0.0.1
             节点IP  =  10.0.0.1
           检测开关  =  开启
      检测阈值（%）  =  85
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NODECHKPARA.md`
