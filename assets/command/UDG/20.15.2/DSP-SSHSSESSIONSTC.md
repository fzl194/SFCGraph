---
id: UDG@20.15.2@MMLCommand@DSP SSHSSESSIONSTC
type: MMLCommand
name: DSP SSHSSESSIONSTC（显示SSH服务器的会话统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SSHSSESSIONSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- SSH调测
status: active
---

# DSP SSHSSESSIONSTC（显示SSH服务器的会话统计信息）

## 功能

该命令用于查询SSH服务器的会话统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SSHSSESSIONSTC]] · SSH服务器的会话统计信息（SSHSSESSIONSTC）

## 使用实例

查询SSH服务器的会话统计信息：

```
DSP SSHSSESSIONSTC:;
```

```

RETCODE = 0  操作成功

结果如下
------------------------
             会话索引  =  0
 与CAMLCSI组件的通道ID = 137487
               通道ID  =  135171
               用户名  =  admin
            Trace信息  =  StartTime:2016-8-4:20-58-23. sock setopt(0)->snd sshver(0)->rev sshver(0)->snd keyinit(0)->rev keyinit(0)->rev gexreq(0)->snd gexgrp(0)->rev gexinit(0)->snd gexreply(0)->snd newkeys(0)->rev newkeys(0)->snd svcreq(0)->snd svcacp(0)->rev userauthreq(0)->snd authfailpsd(0)->rev userauthreq(0)->snd aaaauthreq(0)->snd authsucc(0)->rev chnlopen(0)->snd chnlcfirm(0)->rev chnlreq(0)->snd chnlsucc(0)->rev chnlreq(0)->snd camlcntreq(0)->rev camlcntrsp(0)->snd subscribereq(0)->snd chnlsucc(0)->END
            Socket状态 =  SOCKCONN_STATE_UP
    最近5秒钟数据统计 =  Received packets from client: total-bytes=1507, total-count=12, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
    最近1分钟数据统计 =  Received packets from client: total-bytes=2507, total-count=112, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
    最近5分钟数据统计 =  Received packets from client: total-bytes=3507, total-count=212, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
         所有数据统计 =  Received packets from client: total-bytes=9507, total-count=912, ignore-count=0. Received packets from camls: total-bytes=0, total-count=0, ignore-count=0. Sent packets to client: total-bytes=0, total-count=0, congestion-count=0. Sent packets to camls: total-bytes=0, total-count=0, failed-bytes=0, failed-count=0.
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SSHSSESSIONSTC.md`
