---
id: UNC@20.15.2@MMLCommand@OPR NSAVLINFO
type: MMLCommand
name: OPR NSAVLINFO（操作网络切片可用性信息）
nf: UNC
version: 20.15.2
verb: OPR
object_keyword: NSAVLINFO
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片选择管理
- 网络切片可用性信息管理
status: active
---

# OPR NSAVLINFO（操作网络切片可用性信息）

## 功能

**适用NF：AMF**

该命令用于在AMF上操作与NSSF之间的网络切片可用性信息。

NSSF集中管理了运营商的网络切片可用性信息，包括了网络中的跟踪区（TA）列表以及每个跟踪区支持的和限制使用的网络切片。NSSF上的网络切片可用性信息可能来自配置，也可能部分来自AMF的上报。操作员可通过本命令向NSSF上报或者删除网络切片可用性信息。

如果NSSF上的网络切片可用性信息只来自配置，在执行本命令前要确保NSSF的本地配置更新到最新。

此外，为了能及时感知NSSF侧的网络切片信息变化，AMF需要向NSSF提供其所服务的跟踪区列表（通过ADD NFTAI配置）以订阅这些跟踪区的网络切片信息。操作员可通过本命令触发订阅或者去订阅。

## 注意事项

- 该命令执行后立即生效。

- 当“操作类型”取值为“SUBSCRIBE(订阅网络切片可用性信息)”时，本命令执行完成后，建议执行DSP SUBNSAVLINFO查询订阅结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指示网络切片可用性信息的操作方式。<br>数据来源：本端规划<br>取值范围：<br>- “SYNCHRONIZE（同步网络切片可用性信息）”：同步网络切片可用性信息<br>- “DELETE（通知删除网络切片可用性信息）”：通知删除网络切片可用性信息<br>- “SUBSCRIBE（订阅网络切片可用性信息）”：订阅网络切片可用性信息<br>- “CANCEL（取消网络切片可用性信息订阅）”：取消网络切片可用性信息订阅<br>默认值：无<br>配置原则：<br>当本参数取值为“SYNCHRONIZE(同步网络切片可用性信息)”时，表示AMF将从接入网获取的TAI以及该TAI支持的网络切片信息同步给NSSF；<br>当本参数取值为“DELETE(删除网络切片可用性信息)”时，表示AMF通知NSSF不再需要为其维护网络切片可用性信息，即NSSF删除当前为该AMF维护的网络切片可用性信息；<br>当本参数取值为“SUBSCRIBE(订阅网络切片可用性信息)”时，表示AMF携带其服务的TAI列表向NSSF订阅网络切片可用性信息（订阅前需要确保NSSF上存在AMF请求订阅网络切片的可用信息），当这些TAI所支持或者限制的网络切片信息发生变化时，NSSF将通知该AMF；<br>当本参数取值为“CANCEL(取消网络切片可用性信息订阅)”时，表示AMF不再向NSSF订阅网络切片可用性信息，即NSSF上网络切片可用性信息发生变化时，NSSF不再通知该AMF。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSAVLINFO]] · 操作网络切片可用性信息（NSAVLINFO）

## 使用实例

- 批量的NG-RAN基站割接到本AMF后，AMF需要将基站所支持的TA以及TA的网络切片信息同步给NSSF，执行如下命令：
  ```
  OPR NSAVLINFO: OPTYPE=SYNCHRONIZE;
  ```
- 运营商网络中部署了NSSF，当AMF上配置了其所服务的跟踪区列表后，向NSSF订阅上述跟踪区支持和限制的网络切片信息，执行如下命令：
  ```
  OPR NSAVLINFO: OPTYPE=SUBSCRIBE;
  ```
- 当AMF从网络中退服时，首先通知NSSF取消网络切片可用性信息的订阅，随后再通知NSSF删除网络切片可用性信息，执行如下命令：
  ```
  OPR NSAVLINFO: OPTYPE=CANCEL;
  OPR NSAVLINFO: OPTYPE=DELETE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/OPR-NSAVLINFO.md`
