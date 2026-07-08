---
id: UDG@20.15.2@MMLCommand@DSP GRETNLINFO
type: MMLCommand
name: DSP GRETNLINFO（查询GRE隧道诊断信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: GRETNLINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- GRE调测
status: active
---

# DSP GRETNLINFO（查询GRE隧道诊断信息）

## 功能

该命令用于查询GRE隧道诊断信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLNAME | 隧道名称 | 可选必选说明：可选参数<br>参数含义：该参数用来指定诊断GRE隧道接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GRETNLINFO]] · GRE隧道诊断信息（GRETNLINFO）

## 使用实例

查询GRE隧道诊断信息：

```
DSP GRETNLINFO:TNLNAME="tunnel1";
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
        诊断信息数据

        ------------------------------------------------------------------------
          IfIdx:      13          SmFBit:     53765       SmFBitLast: 53765
          TnlId:      13          TnlNameId:  1           SrcAddr:    0
          SrcVrf:     4294967295  SrcIfIdx:   0           DestAddr:   0
          DestVrf:    0           Period:     0           Retry:      0
          TunnelVrf:  0           TunnelMtu:  1500        FeNodGrpId: 4294967295
          PathMtu:    0           ConfigMtu:  1500        TableMtu:   1500
          TnlType:    5           SrcType:    1           NextHop:    0
          CardId:     255         KeyType:    0           DOIfMtu:    0
          StatEnable: 0
          stSrc6Addr:        ::
          stDest6Addr:       ::
          stNextHop6Addr:    ::
          Gre:        0x7ff1ec1e538c
          Vr:         0x7ff1ec24e11c
          RetryTimer: 0x0
          KTxTimer:   0x0
          RetransCnt: 0           LastTime:   0           RecAckFlag: 0
          DataCFlag:  3           RefFlag:    1           DoingPFlag: 0
          SockHandle: 0x0
          SmFactor:   53765
          SrcIp:      0           SrcVrf:     4294967295  MTU:        1500
          TnlVrf:     0           DbgBitMap:  0           ProductPaf: 0
          PathMTimer: 0x0
          SmFactorBits History:
          [10 18:48:36:359]  53765
          [10 18:48:36:358]  53761
          [10 18:48:36:358]  49665
          [10 18:48:36:358]  33281
          [00 00:00:00:000]  0
          [00 00:00:00:000]  0
          [00 00:00:00:000]  0
          [00 00:00:00:000]  0
          [00 00:00:00:000]  0
          [00 00:00:00:000]  0

        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-GRETNLINFO.md`
