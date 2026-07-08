# 显示SFE报文统计信息（DSP SFEPKTSTAT）

- [命令功能](#ZH-CN_CONCEPT_0000001550120990__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550120990__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550120990__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550120990__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550120990__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550120990__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550120990)

该命令用于显示SFE报文统计信息。

可以显示的报文计数包括：被丢弃的报文计数(discard)；准备上送CP的报文计数(tocp)；SFE中的报文缓存个数(cache)；入SFE报文个数(in)；出SFE报文个数(out)。

#### [注意事项](#ZH-CN_CONCEPT_0000001550120990)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550120990)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550120990)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询统计信息的资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |
| PKTTYPE | 报文类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的统计信息类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- fei_sub_discard：被SFE丢弃的报文计数。<br>- fei_sub_tocp：准备上送CP的报文计数。<br>- fei_sub_cache：SFE中的报文缓存计数。<br>- fei_sub_in：入SFE报文计数。<br>- fei_sub_out：出SFE报文计数。<br>默认值：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550120990)

- 显示指定资源单元的SFE报文计数：
  ```
  DSP SFEPKTSTAT:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```
  ```
  RETCODE = 0  操作成功

  结果如下
  -------------------------
  RU名称                      报文类型        报文子类型           报文计数         报文原因码        报文时延（us）        最近30分钟丢弃报文计数        当前周期丢弃报文计数        最近30分钟报文计数        当前周期报文计数
                                                                                                                                                    
  VNODE_VNRS_VNFC_IPU_0064    入SFE报文       from interface       113              0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    入SFE报文       from cp              1                0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    入SFE报文       from self            0                0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    入SFE报文       from reasm           0                0                 0                     0                             0                           0                         0         
  VNODE_VNRS_VNFC_IPU_0064    入SFE报文       from multicore       0                0                 0                     0                             0                           0                         0      
  VNODE_VNRS_VNFC_IPU_0064    入SFE报文       from nat             0                0                 0                     0                             0                           0                         0      
  VNODE_VNRS_VNFC_IPU_0064    出SFE报文       send to interface    0                0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    出SFE报文       send to cp           88               0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    出SFE报文       send to reasm        0                0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    出SFE报文       send to multicore    0                0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    出SFE报文       send to nat          0                0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    出SFE报文       discard              26               0                 0                     0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    报文缓存计数    cache                0                0                 0                     0                             0                           0                         0
  (结果个数 = 13)
  ---    END
  ```
- 显示指定资源单元的SFE报文丢弃计数：
  ```
  DSP SFEPKTSTAT: PKTTYPE= fei_sub_discard, RUNAME="VNODE_VNRS_VNFC_IPU_0064";
  ```
  ```
  RETCODE = 0  操作成功

  显示报文类型信息:                                                
  --------------------------------                                                
  RU名称                      报文类型    报文子类型                                        报文计数         报文原因码       报文时延 (us)        最近30分钟丢弃报文计数        当前周期丢弃报文计数        最近30分钟报文计数        当前周期报文计数
                                                                                                                    
  VNODE_VNRS_VNFC_IPU_0064    丢弃报文    VFP_CAUSE_DROP_I_L2I_IPAT_READFAIL                879              500              0                    0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    丢弃报文    VFP_CAUSE_DROP_LAYERZERO_MAC_TYPE_ERR_NOTLOCAL    1508             577              0                    0                             0                           0                         0
  VNODE_VNRS_VNFC_IPU_0064    丢弃报文    VFP_CAUSE_DROP_BFD_ERECV_END                      534              676              0                    0                             0                           0                         0
  (结果个数 = 1)
  ---    END
  ```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550120990)

| 输出项名称 | 输出项解释 |
| --- | --- |
| RU名称 | 用于指定待查询统计信息的资源单元名称。 |
| 报文类型 | 用于指定待查询的统计信息类型。 |
| 报文子类型 | 报文来源的子类型。 |
| 报文计数 | 报文统计计数。 |
| 报文原因码 | 报文原因码，0表示无效值。 |
| 报文时延（us） | 用于报文时延。 |
| 最近30分钟丢弃报文计数 | 用于表明最近30分钟丢弃报文计数。 |
| 当前周期丢弃计数 | 用于表明当前周期丢弃报文计数。 |
| 最近30分钟报文计数 | 用于表明最近30分钟报文计数。 |
| 当前周期报文计数 | 用于表明当前周期报文计数。 |
