---
id: UNC@20.15.2@MMLCommand@DSP SFETABLESTC
type: MMLCommand
name: DSP SFETABLESTC（显示SFE表项统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFETABLESTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE表项统计
status: active
---

# DSP SFETABLESTC（显示SFE表项统计信息）

## 功能

该命令用于显示SFE表项统计信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数表示资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SFETABLESTC]] · SFE表项统计信息（SFETABLESTC）

## 使用实例

显示指定资源单元的SFE表项统计信息：

```
DSP SFETABLESTC:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
表ID        表名称              记录数量          单条记录大小    最大记录数量

0           RE                  8                36             122880           
1           NHP                 0                40             262144           
2           AIB                 0                28             786432           
3           IPAT                0                60             64               
4           ICIB                0                64             262144           
5           EPAT                0                48             64               
6           ECIB                0                76             262144           
7           PHB                 144              8              1024             
8           BA                  160              8              2048             
9           NST                 5                28             262144           
10          VPN                 2                12             4096             
11          BFD-PKT             0                108            1024             
12          IPV4&IPV6 TUNNEL    0                80             4096             
13          FEI-BFD-ERECV       0                28             1024             
14          PORT                0                12             16               
15          FEI-SEC-CAR         1                160            512              
16          CTRLVID             0                12             65536            
17          FEI-SEC-SWITCH      1                12             5                
18          AT                  0                20             65536            
20          VLANIF BD           0                40             32768            
24          ND                  0                16             65536            
25          RE6                 0                36             122880           
26          NST6                0                28             262144           
27          NHLFE               0                52             331776           
28          MPLSARP             0                32             65536            
29          NHP6                0                840            262144           
30          GPHB                0                8              64               
31          Fabric-Tunnel       0                8              1024             
32          BFD-ERECV           0                16             1024             
33          BFD-ISEND           0                68             1024             
34          Trunk               0                176            1024             
35          MRE                 0                52             2048             
36          MRT                 0                12             2048             
37          MIB                 0                32             1024             
38          TB-MASK             0                40             2048             
40          ARP                 0                36             131072           
41          ARP-REPLY           0                28             2048             
42          BE                  0                80             65536            
43          BFD-IRECV           0                40             5120             
44          BFD-ERECV-HASH      0                8              1024             
45          GREIDX              0                20             4096             
46          IQVCT               0                68             8192             
47          MEB                 0                8              2048             
48          MFIB4               0                16             2048             
49          ND-FAST-REPLY       0                40             1024             
50          DHCP BIND           0                32             4096             
51          VRRP                0                12             4096             
52          VIRIP               0                12             4096             
53          CPACL               0                104            4096                            
57          DLP                 0                52             2048             
58          ARPSFG              0                44             4096             
59          NDH                 0                32             131072           
60          IPSEC-TUNNEL        0                20             10240            
61          IPV6-GREIDX         0                44             1024             
62          LOCAL-IP            0                24             2048             
63          ELB                 0                44             2048             
64          FIB4                8                20             122880           
65          FIB6                0                8              122880           
(结果个数 = 61)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFETABLESTC.md`
