---
id: UNC@20.15.2@ConfigObject@NRFSMSFSEGLIST
type: ConfigObject
name: NRFSMSFSEGLIST（SMSF号段白名单）
nf: UNC
version: 20.15.2
object_name: NRFSMSFSEGLIST
object_kind: entity
applicable_nf:
- NRF
status: active
---

# NRFSMSFSEGLIST（SMSF号段白名单）

## 说明

![](增加SMSF号段白名单（ADD NRFSMSFSEGLIST）_21823525.assets/notice_3.0-zh-cn_2.png)

该命令与SET NRFSMSFSEGSW配合使用，在白名单未设置完成时请勿打开此开关，否则携带非白名单中的号段来发现SMSF时，该号段发现参数在匹配时将会被NRF忽略。

**适用NF：NRF**

该命令用于向SMSF号段白名单内增加号段。 若希望使用号段来匹配选择SMSF时，需要将这些号段加入到白名单中，否则未加入的号段请求参数将会被忽略。

## 操作本对象的命令

- [[command/UNC/20.15.2/ADD-NRFSMSFSEGLIST]] · ADD NRFSMSFSEGLIST
- [[command/UNC/20.15.2/LST-NRFSMSFSEGLIST]] · LST NRFSMSFSEGLIST
- [[command/UNC/20.15.2/RMV-NRFSMSFSEGLIST]] · RMV NRFSMSFSEGLIST

## 证据

- 原始手册：`evidence/UNC/20.15.2/NRFSMSFSEGLIST.md`
- 原始手册：`evidence/UNC/20.15.2/NRFSMSFSEGLIST.md`
- 原始手册：`evidence/UNC/20.15.2/NRFSMSFSEGLIST.md`
