---
id: UNC@20.15.2@ConfigObject@SEGFILE
type: ConfigObject
name: SEGFILE（号段文件）
nf: UNC
version: 20.15.2
object_name: SEGFILE
object_kind: action
applicable_nf:
- NRF
status: active
---

# SEGFILE（号段文件）

## 说明

**适用NF：NRF**

该命令用于加载IMSI、MSISDN、IMSIRT和MSISDNRT号段文件，加载成功后，号段文件会存储在号段数据备表中。

号段文件导入方式为：登录华为操作维护系统（OM Portal），通过“系统->文件传输->NRF号段导入文件”上传导入。

当运营商希望通过在NRF上配置服务提供方NF支持的大量IMSI、MSISDN、IMSIRT和MSISDNRT号段信息时，需要号段文件方式，避免手动逐条执行号段配置命令，提高效率。

系统通过A、B两个表实现号段文件的号段配置，A、B表状态分别互为主备，系统使用的当前系统的主表，表示某一NF支持的某类型的号段信息，对应的当前备表状态的表用于后续刷新NF支持的号段信息。初始时，两个表内容为空。系统只使用标识为主表中的号段配置数据，如果需要刷新号段配置数据（号段文件承载），新号段文件先通过此命令加载到当前备表，然后通过ACT SEGFILE命令将备表激活成主表，同时主表变成备表，此时系统开始使用新的号段配置数据。后续号段配置数据刷新方式同理。

号段文件需要符合一定格式要求，详细请联系华为技术支持。

## 操作本对象的命令

- [[command/UNC/20.15.2/ACT-SEGFILE]] · ACT SEGFILE
- [[command/UNC/20.15.2/CHK-SEGFILE]] · CHK SEGFILE
- [[command/UNC/20.15.2/EXP-SEGFILE]] · EXP SEGFILE
- [[command/UNC/20.15.2/LOD-SEGFILE]] · LOD SEGFILE

## 证据

- 原始手册：`evidence/UNC/20.15.2/加载号段文件（LOD-SEGFILE）_09653034.md`
- 原始手册：`evidence/UNC/20.15.2/导出号段文件（EXP-SEGFILE）_09654176.md`
- 原始手册：`evidence/UNC/20.15.2/检查导入号段配置文件合法性（CHK-SEGFILE）_50738958.md`
- 原始手册：`evidence/UNC/20.15.2/激活号段文件（ACT-SEGFILE）_09654192.md`
