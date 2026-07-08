---
id: UDG@20.15.2@ConfigObject@NEWCERTSWITCH
type: ConfigObject
name: NEWCERTSWITCH（证书开关状态）
nf: UDG
version: 20.15.2
object_name: NEWCERTSWITCH
object_kind: global_setting
status: active
---

# NEWCERTSWITCH（证书开关状态）

## 说明

![](设置证书开关状态（SET NEWCERTSWITCH）_10015761.assets/notice_3.0-zh-cn.png)

命令执行期间系统内部证书将进行切换，在此过程中通信会发生中断，节点CPU利用率会上涨20%~30%左右，证书切换完成后CPU利用率恢复正常。请确保系统处于低负载状态，节点平均CPU利用率不要超过50%，业务高峰期需谨慎执行。

设置证书开关状态，此命令用于开启或关闭证书变革相关功能。

- 命令开启，将更新内部通信证书，开启证书过期逃生能力，MAE可管理网元外部证书等。
- 命令关闭，将更新内部通信证书，关闭证书过期逃生能力，网元外部证书无法在MAE管理等。

> **说明**
> - [**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令触发证书开关切换，请至少等待1~3分钟，MML页面恢复正常后，使用[**LST NEWCERTSWITCH**](查询证书开关状态（LST NEWCERTSWITCH）_59336676.md)命令查询证书开关切换任务结果。请在查询证书开关切换成功，业务建链恢复之后再执行其他操作。
> - 执行此命令会导致OM Portal上部分服务（MMLService、ICS、SOAP、CSPHAService、NRSAgent（三方场景、Full-stack裸机场景不涉及）、OSAgent（三方场景、Full-stack裸机场景不涉及）、SERVICECENTER、Febs）上报[ALM-5521 服务中心和服务通信故障](../../../../../../网络运维/故障处理/Framework告警/ALM-5521 服务中心和服务通信故障_56836829.md)告警。GaussDB概率上报[ALM-126000 GaussDB组件故障](../../../../../../网络运维/故障处理/Framework告警/ALM-126000 GaussDB组件故障_55292276.md)和[ALM-126006 GaussDB主备同步异常](../../../../../../网络运维/故障处理/Framework告警/ALM-126006 GaussDB主备同步异常_62136776.md)告警。SOAP概率上报[ALM-5525 容器资源过载](../../../../../../网络运维/故障处理/Framework告警/ALM-5525 容器资源过载_30760606.md)告警。Kafka概率上报[ALM-126080 Kafka组件故障](../../../../../../网络运维/故障处理/Framework告警/ALM-126080 Kafka组件故障_02642638.md)告警。
> - 执行此命令会导致OM Portal上的部分服务（MMLService、ICS、SOAP、CSPHAService、NRSAgent（三方场景、Full-stack裸机场景不涉及）、OSAgent（三方场景、Full-stack裸机场景不涉及）、SERVICECENTER）重启加载证书，因此节点的CPU利用率会上涨20%~30%左右，证书切换完成之后CPU利用率会逐渐恢复正常。请在执行此命令前，确保系统处于低负载状态，节点平均CPU利用率不要超过50%，防止在切换过程中由于CPU利用率上涨导致业务受损。
> - 在大容量环境上执行此命令会导致CSE所在节点的CPU变高一段时间，概率上报资源过载相关告警，原因是在证书开关切换过程中所有的微服务会和CSE断链重连导致负载较高，证书开关切换完成之后CPU会逐渐恢复正常，相关告警也会清除，为正常的业务场景，无实际功能影响。
> - 执行此命令涉及证书更新处理，过程中会造成短时间的服务通信中断，影响包含前台页面显示异常，MML命令无法执行，网管对接中断以及10s内的业务呼损等异常，在[**LST NEWCERTSWITCH**](查询证书开关状态（LST NEWCERTSWITCH）_59336676.md)命令查询开关切换成功之后会自动恢复。
> - [**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令需要在稳态环境下执行，例外场景只包含证书变革能力带来对系统不可修复的影响时，需要通过[**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令关闭证书开关进行应急逃生。因此除例外场景，通过[**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令开启/关闭证书开关时，需确保环境无影响业务功能的活动告警（可联系华为技术支持进行确认是否存在影响业务功能的活动告警）。扩缩容、重建、复位、动态上下线，时间跳变，网络亚健康，Bypass等关键操作或高危命令完成后需至少等待10分钟，才可以再次进行证书开关切换操作。
> - 禁止频繁切换证书开关，在[**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)执行后，[**LST NEWCERTSWITCH**](查询证书开关状态（LST NEWCERTSWITCH）_59336676.md)命令查询证书开关切换任务结果成功时，10分钟后可再次执行。如果[**LST NEWCERTSWITCH**](查询证书开关状态（LST NEWCERTSWITCH）_59336676.md)命令查询证书开关切换任务结果失败，请联系华为技术支持。
> - 系统退出bypass状态，10分钟内切换证书开关会上报服务相关的[ALM-5521 服务中心和服务通信故障](../../../../../../网络运维/故障处理/Framework告警/ALM-5521 服务中心和服务通信故障_56836829.md)告警。请在10分钟后进行证书开关状态切换的操作。
> - 升级完成之后，若在观察期内曾执行[**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令将开关状态由关修改为开，则需要再次执行[**SET NEWCERTSWITCH**](设置证书开关状态（SET NEWCERTSWITCH）_10015761.md)命令将开关重新关闭，保持开关状态与完成升级后一致，方可执行回退操作。
> - 关闭证书开关时，会自动关闭证书过期逃生开关，打开证书开关时，会自动打开证书过期逃生开关。
> - 该命令不支持配置导入。
> - 打开证书开关后，在MAE管理网元外部证书时，需要先手动在MAE的“ 安全 > 证书管理 > 核心网网元证书管理 ”的设备证书页面、信任证书页面和吊销列表页面进行同步操作。
> - 初始部署场景下开关默认为开启状态。
> - 该命令存在系统初始记录，参数的初始设置值如下：
>   | CERTSWITCH |
>   | --- |
>   | ON（打开） |

## 操作本对象的命令

- [[command/UDG/20.15.2/LST-NEWCERTSWITCH]] · LST NEWCERTSWITCH
- [[command/UDG/20.15.2/SET-NEWCERTSWITCH]] · SET NEWCERTSWITCH

## 证据

- 原始手册：`evidence/UDG/20.15.2/NEWCERTSWITCH.md`
- 原始手册：`evidence/UDG/20.15.2/NEWCERTSWITCH.md`
