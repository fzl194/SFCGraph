---
id: UNC@20.15.2@MMLCommand@SET NODECHKPARA
type: MMLCommand
name: SET NODECHKPARA（设置节点检测参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NODECHKPARA
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 设备管理
- 节点管理
status: active
---

# SET NODECHKPARA（设置节点检测参数）

## 功能

![](设置节点检测参数（SET NODECHKPARA）_95265008.assets/notice_3.0-zh-cn_2.png)

如果设置参数不合理可能会误报告警或影响网络通信， 请根据业务实际情况进行合理设置。

本命令用于设置节点内存检测、节点CPU过载检测、inotify实例检测、inotify监控检测、节点信号量集检测、节点文件句柄检测、关键部件检测和IP互串冲突预防、智算单元资源检测参数。

> **说明**
> 该命令仅在Full-stack虚机场景下支持。

## 注意事项

- 本命令不支持在BYPASS期间执行。
- 本命令若按照“虚拟机类型”配置后再次按照“网元ID”配置，则不覆盖该网元下的“虚拟机类型”的配置。
- 该命令存在系统初始记录，参数的初始设置值如下：

| 资源类型 | 参数类型 | 检测开关 | 检测阈值（%） | 自愈开关 | 预防开关 | 温度过载检测阈值（℃） | 内存使用率检测阈值（%） | 智算单元Core使用率检测阈值（%） | 视频编码率检测阈值（%） | 视频解码率检测阈值（%） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| VM(虚拟机) | CHKNODEMEM(节点内存检测) | 关闭 | 98 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKNODECPU(节点CPU过载检测) | 关闭 | 98 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKINOTIFYINSTANCE(inotify实例检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKINOTIFYWATCH(inotify监控检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKNODESEMARRAY(节点信号量集检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKNODEFILEHANDLE(节点文件句柄检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKPORT(网卡检测) | 开启 | NA | 开启 | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKIPROUTE(IP路由检测) | 开启 | NA | 开启 | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKKEYFILE(关键文件检测) | 开启 | NA | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKPART(分区过载检测) | 开启 | 90 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKPROC(进程数检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKINODE(inode使用率检测) | 开启 | 80 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKCNTSTOR(容器存储空间检测) | 开启 | 85 | NA | NA | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKIPCONFLICT(IP互串冲突预防) | NA | NA | NA | 开启 | NA | NA | NA | NA | NA |
| VM(虚拟机) | CHKSMCU(智算单元资源检测) | 开启 | NA | NA | NA | 107 | 90 | 100 | 100 | 100 |

> **说明**
> 当参数类型为 “CHKNODEMEM(节点内存检测)” 或 “CHKNODECPU(节点CPU过载检测)” 时， “检测开关” 和 “检测阈值（%）” 的初始设置值支持产品定制，可以通过VNFD进行初始设置值的修改。
>
> 当参数类型为 “CHKIPCONFLICT(IP互串冲突预防)” ，同时 “预防开关” 配置为 “ON(开启预防)” 时，有如下约束：
>
> - 在部署成功后的20分钟内若未刷新集群内各节点静态邻居表，在此期间发生的IP互串冲突无法预防。
> - 如果已产生IP互串冲突，则扩容、重建、重启或重装后的节点无法预防IP互串冲突。
> - 如果NRSMaster所在的两个节点同时下电，NRSAgent将会在4分钟后删除本节点的静态邻居表。
> - 防互串功能无法预防两个冲突IP都在集群外部或都在集群内部的IP互串冲突，无法预防管理面与数据面之间的IP互串冲突。
> - 如果集群间发生IP互串冲突，则已实现防护串功能的集群内消息可以正常发送，但无法预防其他集群发送的互串消息。
> - 如果集群内IP地址变更，10秒内集群内所有节点上的静态邻居表将会刷新正确。如果此时节点上的NRSAgent微服务产生故障，则静态邻居表不能正确刷新会导致网络暂时不通。
> - 集群内节点数量大于10个时，如果节点的IP信息在30秒内连续变更，只有前3次IP变更可以快速通知各节点刷新静态邻居表，之后变更的IP信息在1分钟内通知到各节点并刷新静态邻居表。

“CHKNODEMEM(节点内存检测)” 和 “CHKNODECPU(节点CPU过载检测)” 参数与VNFD中配置的对应关系如下：

| 参数类型 | 参数名称 | 对应VNFD中配置 |
| --- | --- | --- |
| CHKNODEMEM(节点内存检测) | 检测开关 | node_mem_switch |
| CHKNODEMEM(节点内存检测) | 检测阈值（%） | node_mem_threshold_level1 |
| CHKNODECPU(节点CPU过载检测) | 检测开关 | node_cpu_switch |
| CHKNODECPU(节点CPU过载检测) | 检测阈值（%） | node_cpu_threshold_level1 |

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| RESTYPE | 资源类型 | 可选必选说明：必选参数。<br>参数含义：用于指定需要设置的资源类型。<br>取值范围：<br>- “VM(虚拟机)”：用于虚拟机容器部署场景。<br>- “SERVER(服务器)”：用于裸机容器部署场景。<br>默认值：无。<br>配置原则：虚拟机容器部署场景，需要设置为<br>“VM(虚拟机)”<br>。 |
| PARAMTYPE | 参数类型 | 可选必选说明：该参数在<br>“资源类型”<br>配置为<br>“VM(虚拟机)”<br>时为条件必选参数。<br>参数含义：用于指定虚拟机容器部署场景需要设置的参数类型。<br>取值范围：<br>- “CHKNODEMEM(节点内存检测)”<br>- “CHKNODECPU(节点CPU过载检测)”<br>- “CHKINOTIFYINSTANCE(inotify实例检测)”<br>- “CHKINOTIFYWATCH(inotify监控检测)”<br>- “CHKNODESEMARRAY(节点信号量集检测)”<br>- “CHKNODEFILEHANDLE(节点文件句柄检测)”<br>- “CHKPORT(网卡检测)”<br>- “CHKIPROUTE(IP路由检测)”<br>- “CHKKEYFILE(关键文件检测)”<br>- “CHKPART(分区过载检测)”<br>- “CHKPROC(进程数检测)”<br>- “CHKINODE(inode使用率检测)”<br>- “CHKCNTSTOR(容器存储空间检测)”<br>- “CHKIPCONFLICT(IP互串冲突预防)”<br>- “CHKSMCU(智算单元资源检测)”<br>默认值：无。<br>配置原则：无。 |
| APPID | 网元ID | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEM(节点内存检测)”<br>、<br>“CHKNODECPU(节点CPU过载检测)”<br>、<br>“CHKINOTIFYINSTANCE(inotify实例检测)”<br>、<br>“CHKINOTIFYWATCH(inotify监控检测)”<br>、<br>“CHKNODESEMARRAY(节点信号量集检测)”<br>或<br>“CHKNODEFILEHANDLE(节点文件句柄检测)”<br>其中之一时为条件必选参数。<br>参数含义：用于指定虚拟机容器部署场景系统需要设置的网元ID。<br>取值范围：0～65535<br>默认值：无。<br>配置原则：可以通过单击<br>OM Portal<br>的<br>“首页”<br>查询网元ID。 |
| VDUTYPE | 虚拟机类型 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEM(节点内存检测)”<br>、<br>“CHKNODECPU(节点CPU过载检测)”<br>、<br>“CHKINOTIFYINSTANCE(inotify实例检测)”<br>、<br>“CHKINOTIFYWATCH(inotify监控检测)”<br>、<br>“CHKNODESEMARRAY(节点信号量集检测)”<br>或<br>“CHKNODEFILEHANDLE(节点文件句柄检测)”<br>其中之一时为条件必选参数。<br>参数含义：用于指定虚拟机容器部署场景系统需要设置节点内存检测参数、CPU过载检测参数、inotify实例检测参数、inotify监控检测参数、节点信号量集检测参数、节点文件句柄检测参数的虚拟机类型。<br>取值范围：无。<br>默认值：无。<br>配置原则：虚拟机容器部署场景，用户可以通过<br>[**DSP NODE**](节点查询（DSP NODE）_71678755.md)<br>命令查看相应的虚拟机类型。 |
| PARAMTYPE_SV | 参数类型 | 可选必选说明：该参数在<br>“资源类型”<br>配置为<br>“SERVER(服务器)”<br>时为条件必选参数。<br>参数含义：无。<br>取值范围：<br>- “CHKNODEMEM(节点内存检测)”<br>- “CHKNODECPU(节点CPU过载检测)”<br>- “CHKINOTIFYINSTANCE(inotify实例检测)”<br>- “CHKINOTIFYWATCH(inotify监控检测)”<br>- “CHKNODESEMARRAY(节点信号量集检测)”<br>- “CHKNODEFILEHANDLE(节点文件句柄检测)”<br>- “CHKPORT(网卡检测)”<br>- “CHKIPROUTE(IP路由检测)”<br>- “CHKKEYFILE(关键文件检测)”<br>- “CHKPART(分区过载检测)”<br>- “CHKPROC(进程数检测)”<br>- “CHKINODE(inode使用率检测)”<br>- “CHKCNTSTOR(容器存储空间检测)”<br>- “CHKIPCONFLICT(IP互串冲突预防)”<br>- “CHKNODEMEMFAULT(节点内存故障检测)”<br>- “CHKSMCU(智算单元资源检测)”<br>默认值：无。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| SERVERNAME | 服务器名称 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEM(节点内存检测)”<br>、<br>“CHKNODECPU(节点CPU过载检测)”<br>、<br>“CHKINOTIFYINSTANCE(inotify实例检测)”<br>、<br>“CHKINOTIFYWATCH(inotify监控检测)”<br>、<br>“CHKNODESEMARRAY(节点信号量集检测)”<br>或<br>“CHKNODEFILEHANDLE(节点文件句柄检测)”<br>其中之一时为条件可选参数。<br>参数含义：无。<br>取值范围：无。<br>默认值：无。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| SWITCH | 检测开关 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEM(节点内存检测)”<br>、<br>“CHKNODECPU(节点CPU过载检测)”<br>、<br>“CHKINOTIFYINSTANCE(inotify实例检测)”<br>、<br>“CHKINOTIFYWATCH(inotify监控检测)”<br>、<br>“CHKNODESEMARRAY(节点信号量集检测)”<br>、<br>“CHKNODEFILEHANDLE(节点文件句柄检测)”<br>、<br>“CHKPART(分区过载检测)”<br>、<br>“CHKPROC(进程数检测)”<br>、<br>“CHKINODE(inode使用率检测)”<br>或<br>“CHKCNTSTOR(容器存储空间检测)”<br>其中之一时为条件必选参数。<br>参数含义：用于设置是否开启检测。<br>取值范围：<br>- “ON(开启检测)”：开启。<br>- “OFF(关闭检测)”：关闭。<br>默认值：无。<br>配置原则：<br>- 在“参数类型”配置为“CHKNODEMEM(节点内存检测)”时，当节点内存使用率超过检测阈值后会检测出节点内存不足并上报告警[ALM-135647 节点内存不足](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135647 节点内存不足_47422893.md)。<br>- 在“参数类型”配置为“CHKNODEMEM(节点内存检测)”时，当节点内存使用率超过检测阈值或配置的大页内存与实际大页内存不一致时，会检测出节点内存不足并上报告警[ALM-135647 节点内存不足](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135647 节点内存不足_47422893.md)。<br>- 在“参数类型”配置为“CHKNODECPU(节点CPU过载检测)”时，当节点CPU使用率超过检测阈值后会检测出节点CPU过载并上报告警[ALM-135649 节点CPU过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135649 节点CPU过载_59733361.md)。<br>- 在“参数类型”配置为“CHKINOTIFYINSTANCE(inotify实例检测)”、“CHKINOTIFYWATCH(inotify监控检测)”、“CHKNODESEMARRAY(节点信号量集检测)”、“CHKNODEFILEHANDLE(节点文件句柄检测)”时，当节点资源占用率超过检测阈值后会检测出节点资源过载并上报告警[ALM-135700 节点资源过载](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135700 节点资源过载_72776152.md)。<br>- 在“参数类型”配置为“CHKPART(分区过载检测)”时，当节点的分区使用率超过阈值后会检测出节点分区过载并上报[ALM-135637 分区过载监控](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135637 分区过载监控_87668216.md)告警。<br>- 在“参数类型”配置为“CHKPROC(进程数检测)”时，当节点的进程数超过所设置的阈值后会检测出进程数过载并上报[ALM-135638 OS进程数监控](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135638 OS进程数监控_14380968.md)告警。<br>- 在“参数类型”配置为“CHKINODE(inode使用率检测)”时，当节点的inode使用率超过所设置的阈值后会检测出inode使用过载并上报[ALM-135639 inode使用率监控](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135639 inode使用率监控_14380969.md)告警。<br>- 在“参数类型”配置为“CHKCNTSTOR(容器存储空间检测)”时，当节点的容器存储空间使用率超过所设置的阈值后会检测出节点容器存储空间过载并上报[ALM-135640容器存储空间监控](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135640 容器存储空间监控_87760981.md)告警。 |
| CHKSWITCH | 检测开关 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKPORT(网卡检测)”<br>、<br>“CHKIPROUTE(IP路由检测)”<br>或<br>“CHKKEYFILE(关键文件检测)”<br>其中之一时为条件必选参数。<br>参数含义：用于设置是否开启检测。<br>取值范围：<br>- “ON(开启检测)”：开启。<br>- “OFF(关闭检测)”：关闭。<br>默认值：无。<br>配置原则：<br>- 在“参数类型”配置为“CHKPORT(网卡检测)”时，当节点的网卡故障时会检测出网卡故障并上报[ALM-135634 网口故障](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135634 网口故障_14380966.md)告警。<br>- 在“参数类型”配置为“CHKIPROUTE(IP路由检测)”时，当节点的IP路由故障时会检测出IP路由故障并上报[ALM-135635 IP路由异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135635 IP路由异常_87760983.md)告警。<br>- 在“参数类型”配置为“CHKKEYFILE(关键文件检测)”时，当节点的关键文件丢失或损坏时会检测出关键文件丢失或损坏并上报[ALM-135636 关键文件异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135636 关键文件异常_14380967.md)告警。 |
| SMCUCHEKSWITCH | 检测开关 | 可选必选说明：该参数在<br>**“参数类型”**<br>配置为<br>“CHKSMCU(智算单元资源检测)”<br>为条件必选参数。<br>参数含义：用于设置是否开启检测。<br>取值范围：<br>- “ON(开启检测)”：开启。<br>- “OFF(关闭检测)”：关闭。<br>默认值：无。<br>配置原则：<br>- 在“参数类型”配置为“CHKSMCU(智算单元资源检测)”时，当智算单元资源异常时会上报[ALM-135704 智算单元资源异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135704 智算单元资源异常_85035040.md)告警。 |
| REPSWITCH | 自愈开关 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKPORT(网卡检测)”<br>或<br>“CHKIPROUTE(IP路由检测)”<br>其中之一时为条件必选参数。<br>参数含义：用于设置是否开启自愈开关。<br>取值范围：<br>- “ON(开启自愈)”：开启。<br>- “OFF(关闭自愈)”：关闭。<br>默认值：无。<br>配置原则：<br>- 在“参数类型”配置为“CHKPORT(网卡检测)”时，且其对应的CHKSWITCH为打开时，当网卡故障后会自愈修复。<br>- 在“参数类型”配置为“CHKIPROUTE(IP路由检测)”时，且其对应的CHKSWITCH为打开时，IP路由丢失后会自动修复。“CHKIPROUTE(IP路由检测)”的自愈依赖于“CHKPORT(网卡检测)”的自愈，因此需要将“CHKPORT(网卡检测)”的自愈开关打开。 |
| THRESHOLD | 检测阈值（%） | 可选必选说明：当参数<br>“参数类型”<br>配置为<br>“CHKNODEMEM(节点内存检测)”<br>、<br>“CHKNODECPU(节点CPU过载检测)”<br>、<br>“CHKINOTIFYINSTANCE(inotify实例检测)”<br>、<br>“CHKINOTIFYWATCH(inotify监控检测)”<br>、<br>“CHKNODESEMARRAY(节点信号量集检测)”<br>、<br>“CHKNODEFILEHANDLE(节点文件句柄检测)”<br>、<br>“CHKPART(分区过载检测)”<br>、<br>“CHKPROC(进程数检测)”<br>、<br>“CHKINODE(inode使用率检测)”<br>或<br>“CHKCNTSTOR(容器存储空间检测)”<br>其中之一，同时<br>“SWITCH”<br>配置为<br>“ON(开启检测)”<br>时为条件必选参数。<br>参数含义：用于设置告警上报的检测阈值。<br>取值范围：1~100<br>默认值：无。<br>配置原则：在<br>“参数类型”<br>配置为<br>“CHKPART(分区过载检测)”<br>、<br>“CHKPROC(进程数检测)”<br>、<br>“CHKINODE(inode使用率检测)”<br>、<br>“CHKCNTSTOR(容器存储空间检测)”<br>时，取值范围为50~100。 |
| PRVTSWITCH | 预防开关 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKIPCONFLICT(IP互串冲突预防)”<br>时为条件必选参数。<br>参数含义：用于设置是否开启IP互串冲突预防开关。<br>取值范围：<br>- “ON(开启预防)”：开启。<br>- “OFF(关闭预防)”：关闭。<br>默认值：无。<br>配置原则：<br>- 在“参数类型”配置为“CHKIPCONFLICT(IP互串冲突预防)”，同时“PRVTSWITCH(预防开关)”配置为“ON(开启预防)”时，NRSAgent服务会配置静态邻居表预防二层网络互串冲突。 |
| CHEKSWITCH | 检测开关 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEMFAULT(节点内存故障检测)”<br>时为条件必选参数。<br>参数含义：用于设置是否开启<br>“CHKNODEMEMFAULT(节点内存故障检测)”<br>的开关。<br>取值范围：<br>- “ON(开启检测)”：打开检测开关。<br>- “OFF(关闭检测)”：关闭检测开关。<br>默认值：<br>“ON(开启检测)”<br>。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| DURATION | 检测时长（小时） | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEMFAULT(节点内存故障检测)”<br>，同时<br>“CHEKSWITCH”<br>配置为<br>“ON(开启检测)”<br>时为条件必选参数。<br>参数含义：联合<br>**“故障次数”**<br>使用，用于设置ALM-135701 节点内存故障告警上报的检测阈值。例如该参数与<br>**“故障次数”**<br>均为默认值时表示：当24小时内检测到系统发生不低于2次的MCE故障时，上报ALM-135701 节点内存故障告警。<br>取值范围：1~48。<br>默认值：24。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| COUNT | 故障次数 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEMFAULT(节点内存故障检测)”<br>，同时<br>“CHEKSWITCH”<br>配置为<br>“ON(开启检测)”<br>时为条件必选参数。<br>参数含义：联合<br>**“检测时长（小时）”**<br>使用，用于设置ALM-135701 节点内存故障告警上报的检测阈值。例如该参数与<br>**“检测时长（小时）”**<br>均为默认值时表示：当24小时内检测到系统发生不低于2次的MCE故障时，上报ALM-135701 节点内存故障告警。<br>取值范围：1~10。<br>默认值：2。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| CECOUNT | CE故障次数 | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKNODEMEMFAULT(节点内存故障检测)”<br>，同时<br>“CHEKSWITCH”<br>配置为<br>“ON(开启检测)”<br>时为条件必选参数。<br>参数含义：用于设置ALM-135702 节点内存亚健康告警（仅涉及告警原因为CE风暴）上报的检测阈值。<br>取值范围：1~100。<br>默认值：6。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| TRAFFIC | 流量过载阈值（%） | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKPORT(网卡检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135634 网口故障](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135634 网口故障_14380966.md)<br>告警上报的流量过载检测阈值。<br>取值范围：1~99。<br>默认值：85。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| PORTERROR | 错包检测阈值（%） | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKPORT(网卡检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135634 网口故障](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135634 网口故障_14380966.md)<br>告警上报的错包率检测阈值。<br>取值范围：0.01~99.99，最多5个字符。<br>默认值：60。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| DROP | 丢包检测阈值（%） | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKPORT(网卡检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135634 网口故障](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135634 网口故障_14380966.md)<br>告警上报的丢包率检测阈值。<br>取值范围：0.01~99.99，最多5个字符。<br>默认值：60。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| TEMP | 温度过载检测阈值（℃） | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKSMCU(智算单元资源检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135704 智算单元资源异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135704 智算单元资源异常_85035040.md)<br>告警上报的温度过载检测阈值。<br>取值范围：1~200。<br>默认值：107。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| MEM | 内存使用率检测阈值（%） | 可选必选说明：该参数在<br>“参数类型”<br>配置为<br>“CHKSMCU(智算单元资源检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135704 智算单元资源异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135704 智算单元资源异常_85035040.md)<br>告警上报的内存使用率检测阈值。<br>取值范围：1~100。<br>默认值：90。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| UTILIZATION | 智算单元Core使用率检测阈值（%） | 可选必选说明：该参数在<br>**“参数类型”**<br>配置为<br>“CHKSMCU(智算单元资源检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135704 智算单元资源异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135704 智算单元资源异常_85035040.md)<br>告警上报的智算单元Core使用率检测阈值。<br>取值范围：1~100。<br>默认值：100。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| VENC | 视频编码率检测阈值（%） | 可选必选说明：该参数在<br>**“参数类型”**<br>配置为<br>“CHKSMCU(智算单元资源检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135704 智算单元资源异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135704 智算单元资源异常_85035040.md)<br>告警上报的视频编码率检测阈值。<br>取值范围：1~100。<br>默认值：100。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |
| VEDC | 视频解码率检测阈值（%） | 可选必选说明：该参数在<br>**“参数类型”**<br>配置为<br>“CHKSMCU(智算单元资源检测)”<br>时为条件必选参数。<br>参数含义：用于设置<br>[ALM-135704 智算单元资源异常](../../../../../../网络运维/故障处理/UNC告警处理/平台告警/ALM-135704 智算单元资源异常_85035040.md)<br>告警上报的视频解码率检测阈值。<br>取值范围：1~100。<br>默认值：100。<br>配置原则：虚拟机容器部署场景无需配置该参数。 |

## 操作的配置对象

- [节点检测参数（NODECHKPARA）](configobject/UNC/20.15.2/NODECHKPARA.md)

## 使用实例

1. 设置“网元ID”为“0”的所有节点“节点内存检测”参数信息。
  ```
  %%SET NODECHKPARA: RESTYPE=VM, PARAMTYPE=CHKNODEMEM, APPID=0, SWITCH=ON, THRESHOLD=85;%%
  RETCODE = 0  操作成功  

  操作结果如下 
  ------------          
       资源类型  =  虚拟机     
       参数类型  =  节点内存检测          
       详细信息  =  操作成功 
  (结果个数 = 1)  

  ---    END
  ```
2. 设置“网元ID”为“0”，“虚拟机类型”为“CSP_A”的“节点CPU过载检测”参数信息。
  ```
  %%SET NODECHKPARA: RESTYPE=VM, PARAMTYPE=CHKNODECPU, APPID=0, VDUTYPE="CSP_A", SWITCH=ON, THRESHOLD=70;%% 
  RETCODE = 0  操作成功
  
  操作结果如下 
  ------------          
       资源类型  =  虚拟机
       参数类型  =  节点CPU过载检测          
       详细信息  =  操作成功 
  (结果个数 = 1)
  
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置节点检测参数（SET-NODECHKPARA）_95265008.md`
