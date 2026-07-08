---
id: UDG@20.15.2@ConfigObject@NODECHKPARA
type: ConfigObject
name: NODECHKPARA（节点检测参数）
nf: UDG
version: 20.15.2
object_name: NODECHKPARA
object_kind: global_setting
status: active
---

# NODECHKPARA（节点检测参数）

## 说明

![](设置节点检测参数（SET NODECHKPARA）_95265008.assets/notice_3.0-zh-cn.png)

如果设置参数不合理可能会误报告警或影响网络通信， 请根据业务实际情况进行合理设置。

本命令用于设置节点内存检测、节点CPU过载检测、inotify实例检测、inotify监控检测、节点信号量集检测、节点文件句柄检测、关键部件检测和IP互串冲突预防、智算单元资源检测参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

> **说明**
> - 本命令不支持在BYPASS期间执行。
> - 本命令若按照“虚拟机类型”配置后再次按照“网元ID”配置，则不覆盖该网元下的“虚拟机类型”的配置。
> - 该命令存在系统初始记录，参数的初始设置值如下：
>
> | 资源类型 | 参数类型 | 检测开关 | 检测阈值（%） | 自愈开关 | 预防开关 | 温度过载检测阈值（℃） | 内存使用率检测阈值（%） | 智算单元Core使用率检测阈值（%） | 视频编码率检测阈值（%） | 视频解码率检测阈值（%） |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | VM(虚拟机) | CHKNODEMEM(节点内存检测) | 关闭 | 98 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKNODECPU(节点CPU过载检测) | 关闭 | 98 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKINOTIFYINSTANCE(inotify实例检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKINOTIFYWATCH(inotify监控检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKNODESEMARRAY(节点信号量集检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKNODEFILEHANDLE(节点文件句柄检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKPORT(网卡检测) | 开启 | NA | 开启 | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKIPROUTE(IP路由检测) | 开启 | NA | 开启 | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKKEYFILE(关键文件检测) | 开启 | NA | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKPART(分区过载检测) | 开启 | 90 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKPROC(进程数检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKINODE(inode使用率检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKCNTSTOR(容器存储空间检测) | 开启 | 85 | NA | NA | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKIPCONFLICT(IP互串冲突预防) | NA | NA | NA | 开启 | NA | NA | NA | NA | NA |
> | VM(虚拟机) | CHKSMCU(智算单元资源检测) | 开启 | NA | NA | NA | 107 | 90 | 100 | 100 | 100 |
>
> > **说明**
> > 当参数类型为 “CHKNODEMEM(节点内存检测)” 或 “CHKNODECPU(节点CPU过载检测)” 时， “检测开关” 和 “检测阈值（%）” 的初始设置值支持产品定制，可以通过VNFD进行初始设置值的修改。
> >
> > 当参数类型为 “CHKIPCONFLICT(IP互串冲突预防)” ，同时 “预防开关” 配置为 “ON(开启预防)” 时，有如下约束：
> >
> > - 在部署成功后的20分钟内若未刷新集群内各节点静态邻居表，在此期间发生的IP互串冲突无法预防。
> > - 如果已产生IP互串冲突，则扩容、重建、重启或重装后的节点无法预防IP互串冲突。
> > - 如果NRSMaster所在的两个节点同时下电，NRSAgent将会在4分钟后删除本节点的静态邻居表。
> > - 防互串功能无法预防两个冲突IP都在集群外部或都在集群内部的IP互串冲突，无法预防管理面与数据面之间的IP互串冲突。
> > - 如果集群间发生IP互串冲突，则已实现防护串功能的集群内消息可以正常发送，但无法预防其他集群发送的互串消息。
> > - 如果集群内IP地址变更，10秒内集群内所有节点上的静态邻居表将会刷新正确。如果此时节点上的NRSAgent微服务产生故障，则静态邻居表不能正确刷新会导致网络暂时不通。
> > - 集群内节点数量大于10个时，如果节点的IP信息在30秒内连续变更，只有前3次IP变更可以快速通知各节点刷新静态邻居表，之后变更的IP信息在1分钟内通知到各节点并刷新静态邻居表。
>
> “CHKNODEMEM(节点内存检测)” 和 “CHKNODECPU(节点CPU过载检测)” 参数与VNFD中配置的对应关系如下：
>
> | 参数类型 | 参数名称 | 对应VNFD中配置 |
> | --- | --- | --- |
> | CHKNODEMEM(节点内存检测) | 检测开关 | node_mem_switch |
> | CHKNODEMEM(节点内存检测) | 检测阈值（%） | node_mem_threshold_level1 |
> | CHKNODECPU(节点CPU过载检测) | 检测开关 | node_cpu_switch |
> | CHKNODECPU(节点CPU过载检测) | 检测阈值（%） | node_cpu_threshold_level1 |

## 操作本对象的命令

- [[command/UDG/20.15.2/DSP-NODECHKPARA]] · DSP NODECHKPARA
- [[command/UDG/20.15.2/SET-NODECHKPARA]] · SET NODECHKPARA

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询节点检测参数（DSP-NODECHKPARA）_42184981.md`
- 原始手册：`evidence/UDG/20.15.2/设置节点检测参数（SET-NODECHKPARA）_95265008.md`
