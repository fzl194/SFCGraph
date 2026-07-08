---
id: UNC@20.15.2@MMLCommand@DSP MSSQUEINFO
type: MMLCommand
name: DSP MSSQUEINFO（查询队列总体信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MSSQUEINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- MSS
- MSS资源管理统计查询
status: active
---

# DSP MSSQUEINFO（查询队列总体信息）

## 功能

该命令用于查询MSS模块队列总体信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSSQUEINFO]] · 队列总体信息（MSSQUEINFO）

## 使用实例

查询队列总体信息：

```
DSP MSSQUEINFO: RUNAME="VNODE_VNRS_VNFC_IPU_0066";
```

```

RETCODE = 0  操作成功。

结果如下
--------
队列编号      队列名称                队列属性         队列长度    队列深度    接管进程回收次数

0x0           ufpSchWorkQ0            private          4095        0           NULL
0x1           DebugTimerCallback      private          4095        0           NULL
0x2           SFE_FEI_QUEUE           private          1023        0           NULL
0x3           FEI_SFE_QUEUE           private          1023        0           NULL
0x4           ufpSchWorkQ1            private          4095        0           NULL
0x5           ufpSchWorkQ2            private          4095        0           NULL
0x6           msgque_fal_to_agt       private          16383       0           NULL
0x7           msgque_agt_to_fal       private          16383       0           NULL
0x8           Sfe2LdmPktQue000        private          16383       0           NULL
0x9           Sfe2LdmPktQue001        private          16383       0           NULL
0xA           Sfe2LdmPktQue002        private          16383       0           NULL
0xB           Sfe2LdmPktQue003        private          16383       0           NULL
0xC           SFE_CP_CAR_QUEUE0       private          511         0           NULL
0xD           SFE_CP_CAR_QUEUE1       private          511         0           NULL
0xE           SFE_CP_CAR_QUEUE2       private          511         0           NULL
0xF           SFE_CP_CAR_QUEUE3       private          511         0           NULL
0x80000000    loop_vchannel_send_0    pbuffer share    1023        0           0
0x80000001    loop_vchannel_recv_0    pbuffer share    1023        0           0
0x80000002    loop_vchannel_send_1    pbuffer share    1023        0           0
0x80000003    loop_vchannel_recv_1    pbuffer share    1023        0           0
0x80000004    loop_vchannel_send_2    pbuffer share    1023        0           0
0x80000005    loop_vchannel_recv_2    pbuffer share    1023        0           0
0x80000006    dp_to_dp_pkt            pbuffer share    2047        0           4
0x80000007    fei_to_dp_pkt           pbuffer share    2047        0           4
0x80000008    fei_to_dp_msg           pbuffer share    2047        0           0
0x80000009    pae_pmtu_recv_Q         pbuffer share    4095        0           0
0x8000000A    cp_car_que_0            pbuffer share    511         0           0
0x8000000B    cp_car_que_1            pbuffer share    511         0           0
0x8000000C    loop_vchannel_send_3    pbuffer share    1023        0           0
0x8000000D    loop_vchannel_recv_3    pbuffer share    1023        0           0
0x8000000E    sfe-pae-fab_send_0      pbuffer share    32767       0           1
0x8000000F    sfe-pae-fab_recv_0      pbuffer share    32767       0           0
0x80000010    sfe-pae-fab_send_1      pbuffer share    32767       0           1
0x80000011    sfe-pae-fab_recv_1      pbuffer share    32767       0           0
0x80000012    sfe-pae-fab_send_2      pbuffer share    32767       0           1
0x80000013    sfe-pae-fab_recv_2      pbuffer share    32767       0           0
0x80000014    sfe-pae-fab_send_3      pbuffer share    32767       0           1
0x80000015    sfe-pae-fab_recv_3      pbuffer share    32767       0           0
0x80000016    sfe-pae-ext_send_0      pbuffer share    32767       0           1
0x80000017    sfe-pae-ext_recv_0      pbuffer share    32767       0           0
0x80000018    sfe-pae-ext_send_1      pbuffer share    32767       0           1
0x80000019    sfe-pae-ext_recv_1      pbuffer share    32767       0           0
0x8000001A    sfe-pae-ext_send_2      pbuffer share    32767       0           1
0x8000001B    sfe-pae-ext_recv_2      pbuffer share    32767       0           0
0x8000001C    sfe-pae-ext_send_3      pbuffer share    32767       0           1
0x8000001D    sfe-pae-ext_recv_3      pbuffer share    32767       0           0
0x8000001E    sfe-pae-tnl_send_0      pbuffer share    32767       0           0
0x8000001F    sfe-pae-tnl_recv_0      pbuffer share    32767       0           0
0x80000020    sfe-pae-tnl_send_1      pbuffer share    32767       0           0
0x80000021    sfe-pae-tnl_recv_1      pbuffer share    32767       0           0
0x80000022    sfe-pae-tnl_send_2      pbuffer share    32767       0           0
0x80000023    sfe-pae-tnl_recv_2      pbuffer share    32767       0           0
0x80000024    sfe-pae-tnl_send_3      pbuffer share    32767       0           0
0x80000025    sfe-pae-tnl_recv_3      pbuffer share    32767       0           0
0x80000026    MSG_1001_Alert_Queue    pbuffer share    2047        0           4
(结果个数 = 55)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询队列总体信息（DSP-MSSQUEINFO）_49961898.md`
