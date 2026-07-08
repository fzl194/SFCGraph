---
id: UNC@20.15.2@ConfigObject@NRFPKGRATIO
type: ConfigObject
name: NRFPKGRATIO（NRF内外包长比例）
nf: UNC
version: 20.15.2
object_name: NRFPKGRATIO
object_kind: global_setting
applicable_nf:
- NRF
status: active
---

# NRFPKGRATIO（NRF内外包长比例）

## 说明

![](设置NRF内外包长比例（SET NRFPKGRATIO）_35636467.assets/notice_3.0-zh-cn_2.png)

SET NRFBIGPKGPARA中MAXPKGSIZE配置不为0且RATIO参数配置过大，NRF会误判服务发现响应报文大小，导致服务发现失败。

**适用NF：NRF**

该命令用于配置指定NFType对应的内部报文长度和http接口json原始报文长度的比例系数，用于支撑NRF对不同消息进行最大报文长度的处理判断，详细处理规则请参考SET NRFBIGPKGPARA命令中MAXPKGSIZE参数的描述。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-NRFPKGRATIO]] · LST NRFPKGRATIO
- [[command/UNC/20.15.2/SET-NRFPKGRATIO]] · SET NRFPKGRATIO

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFPKGRATIO.md`
- 原始手册：`evidence/UNC/20.15.2/NRFPKGRATIO.md`
