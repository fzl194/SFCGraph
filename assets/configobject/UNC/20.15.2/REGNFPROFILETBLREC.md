---
id: UNC@20.15.2@ConfigObject@REGNFPROFILETBLREC
type: ConfigObject
name: REGNFPROFILETBLREC（注册NF的Profile表记录）
nf: UNC
version: 20.15.2
object_name: REGNFPROFILETBLREC
object_kind: entity
applicable_nf:
- NRF
status: active
---

# REGNFPROFILETBLREC（注册NF的Profile表记录）

## 说明

![](删除注册NF的Profile表记录（DEL REGNFPROFILETBLREC）_09651506.assets/notice_3.0-zh-cn_2.png)

该命令将会删除注册NF的Profile表记录，错误执行后导致网元信息缺失。

**适用NF：NRF**

该命令用于删除注册到NRF上的NF的profile表记录，NF Profile在NRF上会分表存储，当确认NRF中存储的NF的Profile信息异常或者冗余影响周边网元业务异常时，可使用该命令删除NF的Profile表记录。为防止误删，该命令需要专业维护人员确认后才可执行，具体NF的Profile表信息可以通过DSP NGCOMMONDBG命令查询。

## 操作本对象的命令

- [[command/UNC/20.15.2/DEL-REGNFPROFILETBLREC]] · DEL REGNFPROFILETBLREC

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除注册NF的Profile表记录（DEL-REGNFPROFILETBLREC）_09651506.md`
