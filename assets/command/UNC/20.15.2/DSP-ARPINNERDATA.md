---
id: UNC@20.15.2@MMLCommand@DSP ARPINNERDATA
type: MMLCommand
name: DSP ARPINNERDATA（查询ARP内部信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ARPINNERDATA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- ARP
status: active
---

# DSP ARPINNERDATA（查询ARP内部信息）

## 功能

该命令用于查看ARP内部信息。

## 注意事项

- 参数CID只能是ARP组件号。
- 参数PID可以是LDM、SOCK、FES、IFM、EUM、RGM、LLA的进程号。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INFOTYPE | 信息类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询信息的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ArpByIP：根据IP地址查询表项。<br>- BlackBox：根据进程号查询表项。<br>- FesInfo：查询fes相关表项。<br>- Global：查询全局表项。<br>- IfData：根据接口索引查询表项。<br>- IfPolicy：根据接口索引查询表项。<br>- Local：查询本地表项。<br>- Partner：可根据进程号查询表项。<br>- PipeInfo：查询管道表项。<br>- ProbeInfoByMember：查询成员口探测表项。<br>- ProbeInfoBySession：查询探测会话表项。<br>- AttackMacList：查询攻击者MAC链。<br>- MacConflict：查询MAC冲突次数。<br>默认值：无 |
| IPADDRESS | IP地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“INFOTYPE”配置为“ArpByIP”、“ProbeInfoBySession” 或 “AttackMacList”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“INFOTYPE”配置为“ProbeInfoByMember”时为可选参数。<br>参数含义：该参数用于显示指定IPv4地址的内部信息。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。<br>默认值：无 |
| PID | 进程号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“INFOTYPE”配置为“BlackBox”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“INFOTYPE”配置为“Partner”时为可选参数。<br>参数含义：该参数用于显示指定进程号的内部信息。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“INFOTYPE”配置为“IfData”、“IfPolicy”、“ProbeInfoByMember”、“ProbeInfoBySession” 或 “AttackMacList”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“INFOTYPE”配置为“ArpByIP”时为可选参数。<br>参数含义：该参数用于显示指定接口名的内部信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |
| CID | 组件号 | 可选必选说明：可选参数<br>参数含义：该参数用于显示指定组件号的内部信息。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。<br>默认值：无 |
| MEMBERIFNAME | 成员口名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“INFOTYPE”配置为“ProbeInfoByMember”时为必选参数。<br>可选必选说明：条件可选参数<br>前提条件：该参数在“INFOTYPE”配置为“ProbeInfoBySession”时为可选参数。<br>参数含义：该参数用于显示指定成员口的内部信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ARPINNERDATA]] · ARP内部信息（ARPINNERDATA）

## 使用实例

- 查看ArpByIP类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=ArpByIP,IPADDRESS="10.1.1.1",IFNAME="Ethernet64/0/3",CID="0x8077000e";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
            IpAddr            = 0xc0a82739
            ArpType           = 0x4
            VrfIndex          = 0x1
            VrIndex           = 0x0
            IfIndex           = 0x5
            WorkIfIndex       = 0x0
            uiWorkMainIfIndex = 0x0
            FlowId            = 0xffffffff
            NetRole           = 0x0
            UnAgeing          = 0x0
            BridgeID          = 0x0
            PeVid             = 0x0
            CeVid             = 0x0
            EgressNickName    = 0x0
            MacAddr           = 00E0-FC12-3456
            ArpStatusFlag     = 0x2
            ItermVer          = 0x0
            FixFlag           = 0x0
            DelFlag           = 0x0
            FlushFilterFlag   = 0x0
            TblControlFlag    = 0x0
            AskTimes          = 0x0
            LastUpdateTick    = 0x0
            SendAckUnlockTime = 0x0
            TimeoutType       = 0x0
            Encaptype         = 0x0
            BridgeType        = 0x0
            UpDateFlag        = 0x0
            ExpireTime (s)    = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看BlackBox类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=BlackBox,PID="8065000d";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息

            ARP Cid:0x8077000e
          =========================================================
            11-08 21:53:49:951 Receive component status change to : 0 (0:aval, 1:unaval)

            11-08 21:53:59:450 Receive pipe open request. pipeId = 1074266133 .

            11-08 21:53:59:450 Receive pipe open respond. pipeId = 524310, result = 0.

            11-08 21:53:59:952 Receive pipe open request. pipeId = 1074266135 .

            11-08 21:53:59:952 Receive pipe open respond. pipeId = 524312, result = 0.

          (结果个数 = 5)
          ---    END
  ```
- 查看FesInfo类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=FesInfo;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            CommPid         = 0x6a0013
            MsgTranNo       = 0
            RealSeqNo       = 8
            BatchSeqNo      = 5
            UpdateArpCnt    = 6
            DelArpCnt       = 0
            IsEventSent     = 1
            TblId           = 108
            InSmooth        = 5
            TblId           = 7
            InSmooth        = 5

          (结果个数 = 1)
          ---    END
  ```
- 查看Global类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=Global;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            VrID            = 0
            SysLearnStrict  = 0
            SysArpFixType   = 0
            SysDropGratArp  = 0
            ArpSrcMacCheck  = 0
            LogTrapTime     = 0
            IsVrSpecConfig  = 0
            MaxArpEntry     = 131072
            StaticArpNum    = 0
            DynArpNum       = 6
            FakeArpNum      = 0
            ProbeEnable     = 1
            ProbeMode       = 0
            ProbeTimes      = 3
            ProbeInterval   = 5
            ExpireTime      = 1200
            FakeExpireTime  = 3
            ConvergeMode    = 2
            ACLHandle       = 0
            GrattsEnable    = 0
            LooseLearnEn    = 0
            LoopSndGratArp  = 0
            SuppTime        = 0
            pktSrvHandle    = 2
            pktSrvSockStat  = 1
            pktSrvSockStep  = 2
            DupMacEnable    = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看IfData类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=IfData,IFNAME="Ethernet64/0/3";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            IfIndex          = 0x5
            VrIndex          = 0x0
            VrfIndex         = 0x1
            GroupId          = 0x80000003
            MainIfIndex      = 0x0
            IfPhyType        = 0x1a
            SubIfVlanType    = 0x0
            MacAddr          = 00E0-FC12-3456
            IfServType       = 0x0
            IfStatus         = 0xd
            AuthFlag         = 0x0
            IpUnnumber       = 0x0
            ArpProxyFlag     = 0x0
            ArpBCastEnable   = 0x0
            ArpProbeEnable   = 0x0
            ArpProbeMode     = 0x0
            ArpProbeTimes    = 0x3
            ArpProbeInterval = 0x5
            ArpExpireTime    = 0x4b0
            ArpFakeTime      = 0x3
            ArpDynNum        = 0x6
            ArpStaNum        = 0x0
            ArpStrictLearn   = 0x3
            ArpLearnCheck    = 0x0
            ArpMacValid      = 0x0
            DropGratArp      = 0x0
            ArpFixType       = 0x0
            Portflag         = 0x0
            IfVlanID         = 0x0
            WaitSendNum      = 0x0
            TblDelMode       = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看IfPolicy类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=IfPolicy,IFNAME="Ethernet64/0/3";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息

            ARP Cid:0x8077000e
          =========================================================
            uiIpAddr       = 0xc0a80000
            NetMask        = 0xffff0000
            MacAddr        = 00E0-FC12-3456
            TblCnt         = 0x1
            MatchType      = 0x2
            PolicyType     = 0x1

            uiIpAddr       = 0xc0a82739
            NetMask        = 0xffff0000
            MacAddr        = 00E0-FC12-3457
            TblCnt         = 0x1
            MatchType      = 0x1
            PolicyType     = 0x1

          (结果个数 = 2)
          ---    END
  ```
- 查看Local类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=Local;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            CompPid          = 0x77000a
            CompCid          = 0x8077000e
            MastCompCid      = 0x8077000e
            SlaveCompCid     = 0x80770070
            CompWorkMode     = 0x0
            CompHaStage      = 0x2
            RecoveryFlag     = 0x0
            NodeId           = 0x0
            LrID             = 0x0
            HInitErr         = 0x0
            CpuOverState     = 0x1
            RcvTotalPkt      = 0x26
            TimeoutRate      = 0x0
            TimeoutNum       = 0x0
            TimerPrecision   = 0x1
            TimerQueueNum    = 0x4b1
            BrasTimerQueueNum= 0x0
            TimerMaxTimeOut  = 0x4b0
            TimerMoudleID    = 0x1
            TimerCurrQueue   = 0x4a0
            BrasTimerCurQueue= 0x0
            TimerCnt         = 0xc048
            TimerCreateErr   = 0x0
            LastTimeL        = 0x2ef4dca
            LastTimeH        = 0x0
            SendGratArp      = 0x0
            IfLearnMaxNum    = 0x10000
            DbgFlag          = 0x0
            FlushProbeNum    = 0x0
            DynArpEntryNum   = 0x6
            StaArpEntryNum   = 0x0
            DynArpNumMax     = 0x20000
            StaArpNumMax     = 0x4000
            UserTraceNum     = 0x0
            MissAmerNum      = 0x0
            ArpNodesCnt      = 0x8
            UserTraceNodesCnt= 0x0
            ArpSockCount     = 0x2
            Index = 0x0, val = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看Partner类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=Partner;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            ComType          = 0x78
            Pid              = 0x780008
            LrId             = 0x0
            VrId             = 0x0
            NodeId           = 0x1ff01
            CompStatus       = 0x0
            ServiceState     = 0x0
            PushState        = 0x0
            SeqErrAckState   = 0x0
            BatchSeqNo       = 0x1
            ItemVer          = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看PipeInfo类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=PipeInfo;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息

            ARP Cid:0x8077000e
          =========================================================
            LLA SendPipeId      = 0x80013
            LLA SendServiceId   = 0x8077000e
            LLA SendPipeStatus  = 0x2
            LLA RevPipeId       = 0x0
            LLA RevServiceId    = 0x0
            Pid                 = 0x780008
            RevPipeId           = 0xc0200001
            RevServiceId        = 0x3
            SendPipeId          = 0x0
            SendServiceId       = 0x0
            SendPipeStatus      = 0x0

            Pid                 = 0x8065000d
            RevPipeId           = 0xffffffff
            RevServiceId        = 0x0
            SendPipeId          = 0x0
            SendServiceId       = 0x0
            SendPipeStatus      = 0x0

            Pid                 = 0x780009
            RevPipeId           = 0xc008002a
            RevServiceId        = 0x3
            SendPipeId          = 0x0
            SendServiceId       = 0x0
            SendPipeStatus      = 0x0

          (结果个数 = 3)
          ---    END
  ```
- 查看AttackMacList类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=AttackMacList,IPADDRESS="10.1.1.1",IFNAME="Ethernet67/0/6";
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x80770090
          =========================================================
           ======================================================
           IfIndex          = 19
           IpAddress        = 167837953
           TrustMac         = 00E0-FC12-3459
           TrustMacCount    = 6
           ==============================================
           ConflictMac      = 00E0-FC12-345A
           Count            = 23
           ==============================================
           ConflictMac      = 00E0-FC12-345B
           Count            = 22
           ======================================================

          (结果个数 = 1)
          ---    END
  ```
- 查看MacConflict类型表项信息：
  ```
  DSP ARPINNERDATA:INFOTYPE=MacConflict;
  ```
  ```

          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x80770090
          =========================================================
           ======================================================
           IfIndex          = 19
           IpAddress        = 167837953
           VrfIndex         = 0
           ConflictCount    = 187
           ======================================================

          (结果个数 = 1)
          ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ARPINNERDATA.md`
