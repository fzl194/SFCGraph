# Step 1b: MD 提取 vs kgdata 对比报告

## 总览

- UDG 命令数: 4576
- UNC 命令数: 8498
- MD 解析成功: 13074
- MD 解析失败: 0
- 无文件: 0

## UDG 字段对比（kgdata vs MD）

### command_function

| 指标 | 值 |
|---|---|
| 总数 | 4576 |
| kgdata为空 | 0 |
| MD为空 | 0 |
| 两者都为空 | 0 |
| 完全匹配 | 3343 |
| 相似(>80%) | 1193 |
| 差异较大(<80%) | 40 |
| **匹配率** | **99.1%** |

差异样例 (40 条):

- **UDG:SET NETSUBHEALTH** (diff(0.54))
  - kgdata(147): 修改网络亚健康参数有可能导致误报告警或漏报告警，业务报文丢失可能无法及时发现，请慎重使用该命令。 本命令用于设置网络亚健康参数，也可以在OM Portal菜单界面选择 “ 监控分析 &gt; 节点健康
  - md(370): ! 修改网络亚健康参数有可能导致误报告警或漏报告警，业务报文丢失可能无法及时发现，请慎重使用该命令。 本命令用于设置网络亚健康参数，也可以在OM Portal菜单界面选择 “ 监控分析 > 节点健康检

- **UDG:STR NODE** (diff(0.54))
  - kgdata(149): 本命令用于启动网元下指定名称的节点。 该命令仅在Full-stack虚机场景下支持。 在存储故障期间，执行本命令启动已关闭的节点，该节点以及节点中的容器和进程，在存储故障恢复前都无法启动。 执行该命令
  - md(391): 本命令用于启动网元下指定名称的节点。 > 说明 > 该命令仅在Full-stack虚机场景下支持。 > > - 在存储故障期间，执行本命令启动已关闭的节点，该节点以及节点中的容器和进程，在存储故障恢复

- **UDG:LST VNFMINFO** (diff(0.52))
  - kgdata(36): 该命令用于查询网元与VNFM的对接信息。 该命令仅在非TCA场景下支持。
  - md(102): 该命令用于查询网元与VNFM的对接信息。 > 说明 > 该命令仅在非TCA场景下支持。 > 说明 > VNFM组网信息为IPV6+IPV4双栈场景时，该命令中的主节点IP、备节点IP为IPV6的地址信

- **UDG:LST SUPPRESSALM** (diff(0.70))
  - kgdata(128): 本命令用于查询系统内闪断振荡被抑制告警，查询结果为最新产生的被抑制告警。 如果需要修改闪断或振荡参数，可在OM Portal中依次单击 “ 监控分析 &gt; 告警管理 &gt; 告警配置 ” ，然后
  - md(214): 本命令用于查询系统内闪断振荡被抑制告警，查询结果为最新产生的被抑制告警。 > 说明 > 如果需要修改闪断或振荡参数，可在OM Portal中依次单击 “ 监控分析 > 告警管理 > 告警配置 ” ，然

- **UDG:SET NEWCERTSWITCH** (diff(0.20))
  - kgdata(225): 命令执行期间系统内部证书将进行切换，在此过程中通信会发生中断，节点CPU利用率会上涨20%~30%左右，证书切换完成后CPU利用率恢复正常。请确保系统处于低负载状态，节点平均CPU利用率不要超过50%
  - md(1974): ! 命令执行期间系统内部证书将进行切换，在此过程中通信会发生中断，节点CPU利用率会上涨20%~30%左右，证书切换完成后CPU利用率恢复正常。请确保系统处于低负载状态，节点平均CPU利用率不要超过5

### notes

| 指标 | 值 |
|---|---|
| 总数 | 4576 |
| kgdata为空 | 6 |
| MD为空 | 839 |
| 两者都为空 | 2 |
| 完全匹配 | 2068 |
| 相似(>80%) | 2432 |
| 差异较大(<80%) | 74 |
| **匹配率** | **98.4%** |

差异样例 (74 条):

- **UDG:SET RUDISKPARTITION** (diff(0.76))
  - kgdata(345): 该命令执行后立即生效。 系统中支持的磁盘分区以网元部署的实际情况为准。 空间不足告警上报阈值缺省值为50，空间不足告警恢复阈值缺省值为100。 root分区使用率过载重要级别告警上报阈值缺省值为95%
  - md(451): - 该命令执行后立即生效。 - 系统中支持的磁盘分区以网元部署的实际情况为准。 - 空间不足告警上报阈值缺省值为50，空间不足告警恢复阈值缺省值为100。 - root分区使用率过载重要级别告警上报阈

- **UDG:SET ISUPODCPUTHD** (diff(0.79))
  - kgdata(79): 该命令执行后立即生效。 该命令最大记录数为1。 该命令存在系统初始记录，参数的初始设置值如下表： 参数标识 WARNTHD RECVTHD 初始值 80 70
  - md(121): - 该命令执行后立即生效。 - 该命令最大记录数为1。 - 该命令存在系统初始记录，参数的初始设置值如下表： | 参数标识 | WARNTHD | RECVTHD | | --- | --- | --

- **UDG:SET DBSTARTPARAS** (diff(0.59))
  - kgdata(486): 该命令执行后30秒内生效。 该命令存在系统初始记录，参数的初始设置值如下表： 集群类型 参数 参数值 普通集群 老化时间阈值 2100 普通集群 对象老化扫描间隔 1200 普通集群 强制老化时长 4
  - md(710): - 该命令执行后30秒内生效。 - 该命令存在系统初始记录，参数的初始设置值如下表： | 集群类型 | 参数 | 参数值 | | --- | --- | --- | | 普通集群 | 老化时间阈值 |

- **UDG:INNERPING** (diff(0.80))
  - kgdata(403): 该命令执行后立即生效。 当前存在三类PING调测命令： PING 、 INNERPING 、 NGPING ，差异如下。 PING ：该命令用于排查本网元 外联口IP 与对端设备之间是否可以PING通
  - md(485): - 该命令执行后立即生效。 - 当前存在三类PING调测命令：PING、INNERPING、NGPING，差异如下。 - PING：该命令用于排查本网元外联口IP与对端设备之间是否可以PING通。 -

- **UDG:SET MPLSSITE** (diff(0.79))
  - kgdata(319): 该命令执行后立即生效。 将MPLS开关或LDP开关置为DISABLE后，会导致MPLS或LDP功能不可用，并且所有历史MPLS或LDP配置全部删除。 如果修改LSR ID，所有与LSR ID相关的服务
  - md(377): - 该命令执行后立即生效。 - 将MPLS开关或LDP开关置为DISABLE后，会导致MPLS或LDP功能不可用，并且所有历史MPLS或LDP配置全部删除。 - 如果修改LSR ID，所有与LSR I

### permission

| 指标 | 值 |
|---|---|
| 总数 | 4576 |
| kgdata为空 | 233 |
| MD为空 | 233 |
| 两者都为空 | 233 |
| 完全匹配 | 4343 |
| 相似(>80%) | 0 |
| 差异较大(<80%) | 0 |
| **匹配率** | **100.0%** |

### examples

| 指标 | 值 |
|---|---|
| 总数 | 4576 |
| kgdata为空 | 1 |
| MD为空 | 0 |
| 两者都为空 | 0 |
| 完全匹配 | 16 |
| 相似(>80%) | 4541 |
| 差异较大(<80%) | 19 |
| **匹配率** | **99.6%** |

差异样例 (19 条):

- **UDG:DSP DEVMODFSM** (diff(0.77))
  - kgdata(381): 显示资源单元上指定组件的模块状态机信息： DSP DEVMODFSM:RUNAME="CSDB_OM_RU_0001",COMPTYPE=DEVMA ,SERVICEINSTANCE="vnfc" ;
  - md(370): 显示资源单元上指定组件的模块状态机信息：  DSP DEVMODFSM:RUNAME="CSDB_OM_RU_0001",COMPTYPE=DEVMA ,SERVICEINSTANCE="vnfc" 

- **UDG:MOD KEYCHAINKEYID** (diff(0.71))
  - kgdata(255): 修改Keychain ospf Key ID为1的配置，时间模式每周，发送时间修改为每周一到周五，接收时间修改为每周一至周日： MOD KEYCHAINKEYID:KEYCHAINNAME="ospf
  - md(217): 修改Keychain ospf Key ID为1的配置，时间模式每周，发送时间修改为每周一到周五，接收时间修改为每周一至周日：  MOD KEYCHAINKEYID:KEYCHAINNAME="osp

- **UDG:ADD PERITIMERANGE** (diff(0.79))
  - kgdata(367): 假设运营商需要配置系统的业务在周一的10点到11点生效，则按如下命令进行配置： ADD PERITIMERANGE:TIMERANGENAME="t1",PERITMRANGESEQ=1,PERITI
  - md(359): - 假设运营商需要配置系统的业务在周一的10点到11点生效，则按如下命令进行配置：  ADD PERITIMERANGE:TIMERANGENAME="t1",PERITMRANGESEQ=1,PER

- **UDG:DSP RESNOSBASEIFSTATUS** (diff(0.68))
  - kgdata(249): 查询所有资源的NOS Base网口状态及IP信息： DSP RESNOSBASEIFSTATUS:; RETCODE = 0 操作成功 结果如下: --------- 资源名称 接口名称 接口状态 接
  - md(488): - 查询所有资源的NOS Base网口状态及IP信息：  DSP RESNOSBASEIFSTATUS:;   RETCODE = 0 操作成功 结果如下: --------- 资源名称 接口名称 接

- **UDG:DSP RESNOSBASEIFSTAT** (diff(0.67))
  - kgdata(417): 查询VNFP的所有资源的NOS Base平面网络报文统计信息： DSP RESNOSBASEIFSTAT:; RETCODE = 0 操作成功 结果如下: --------- 资源名称 接收的报文数目
  - md(820): - 查询VNFP的所有资源的NOS Base平面网络报文统计信息：  DSP RESNOSBASEIFSTAT:;   RETCODE = 0 操作成功 结果如下: --------- 资源名称 接收

## UNC 提取统计

| 字段 | 有值数 | 总数 | 覆盖率 |
|---|---|---|---|
| command_function | 8498 | 8498 | 100.0% |
| notes | 4440 | 8498 | 52.2% |
| permission | 6370 | 8498 | 75.0% |
| examples | 8495 | 8498 | 100.0% |

