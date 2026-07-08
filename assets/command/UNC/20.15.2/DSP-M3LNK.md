---
id: UNC@20.15.2@MMLCommand@DSP M3LNK
type: MMLCommand
name: DSP M3LNK（显示M3UA信令链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: M3LNK
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- M3UA管理
- M3UA链路
status: active
---

# DSP M3LNK（显示M3UA信令链路状态）

## 功能

**适用网元：SGSN、MME、SMSF**

该命令用于查询M3UA信令链路状态。

## 注意事项

- 查询M3UA信令链路状态的方式有四种：全部(ALL)、链路(LINK)、目的实体(DSP)、链路状态(STATUS)。
- 如果不输入任何参数，则表示查询系统内所有SGP进程上的M3UA信令链路。
- 按照目的实体方式查询时，输入参数中的网络指示语、目的实体编码、本地实体编码必须同时输入，或者同时不输入。
- 在一次查询多条链路状态时，如果查询结果中某条链路的状态信息全部显示为NULL，则表明这条链路所在的SGP进程故障。
- 按照链路状态方式查询时，如果返回“RU状态或类型不对”，则说明所有正常SGP进程上都没有符合查询状态的链路，或者所有SGP进程故障。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询方式。<br>取值范围：<br>- “ALL(全部)”<br>- “LINK(链路)”<br>- “DSP(目的实体)”<br>- “STATUS(链路状态)”<br>默认值：<br>“ALL(全部)” |
| RUNAME | RU名称 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“LINK(链路)”<br>值后生效。<br>数据来源：整网规划。<br>取值范围：0~63 位字符串<br>默认值：无 |
| LNK | 链路号 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定M3UA链路号。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“LINK(链路)”<br>值后生效。<br>数据来源：本端规划<br>取值范围：0~1279（数值型）<br>默认值：无<br>说明：此链路号在系统范围内唯一。 |
| LSX | 链路集索引 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设定M3UA链路所属的M3UA链路集。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“LINK(链路)”<br>值后生效。<br>取值范围：0~1279（数值型）<br>默认值：无 |
| LKN | 链路名 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置链路名称，标识M3UA链路。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“LINK(链路)”<br>值后生效。<br>取值范围：长度不超过32的字符串<br>默认值：无 |
| DEX | 目的实体索引 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设定待查询链路所到达的目的实体索引。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“DSP(目的实体)”<br>值后生效。<br>取值范围：0~1279（数值型）<br>默认值：无 |
| NI | 网络指示语 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设定待查询链路所到达目的实体所属的信令网。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“DSP(目的实体)”<br>值后生效。<br>取值范围：<br>- “INT(国际网)”<br>- “INTB(国际备用网)”<br>- “NAT(国内网)”<br>- “NATB(国内备用网)”<br>默认值：无 |
| DPC | 目的实体编码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设定目的实体编码。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“DSP(目的实体)”<br>值后生效。<br>取值范围：长度不超过8的字符串<br>默认值：无 |
| OPC | 本地实体编码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设定本地实体编码。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“DSP(目的实体)”<br>值后生效。<br>取值范围：长度不超过8的字符串<br>默认值：无 |
| LNKSTATE | 链路状态 | 可选必选说明：条件可选参数<br>参数含义：该参数用于查询M3UA链路时需要匹配的状态，即只有符合该状态的链路才显示。<br>前提条件：此参数在<br>“SRT”<br>参数配置为<br>“STATUS(链路状态)”<br>值后生效。<br>取值范围：<br>- “ACT(激活)”<br>- “INACT(去活)”<br>- “DOWN(SCTP偶联已建立)”<br>- “UNEST(SCTP偶联未建立)”<br>- “CONG(拥塞)”<br>- “MANLOC(人工锁定)”<br>- “MANREL(人工释放)”<br>默认值：无<br>说明：这些链路状态都是常态，在异常的常态下参考ALM 80633告警帮助进行处理。 |

## 操作的配置对象

- [M3UA信令链路（M3LNK）](configobject/UNC/20.15.2/M3LNK.md)

## 使用实例

1. 按照“全部(ALL)”方式查询M3UA链路的状态：
  DSP M3LNK: SRT=ALL;
  ```
  %%DSP M3LNK: SRT=ALL;%%
  RETCODE = 0  操作成功。

  查询M3UA链路状态
  ----------------
  RU名称            链路号      进程号        链路状态          偶联ID            是否锁定  手工去活             手工释放          链路拥塞          入流数目      出流数目       SLS                                             

  LINK_SP_RU_0066    3           0             激活              5                 否        否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  LINK_SP_RU_0066    182         0             SCTP偶联未建立    597               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    74          0             SCTP偶联未建立    598               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    75          0             SCTP偶联未建立    600               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    79          0             SCTP偶联未建立    599               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    121         4             SCTP偶联未建立    291               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    2           4             SCTP偶联未建立    288               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    71          4             SCTP偶联未建立    289               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    72          4             SCTP偶联未建立    287               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    73          4             SCTP偶联未建立    290               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    78          4             SCTP偶联未建立    286               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    4           3             SCTP偶联未建立    269               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    5           3             SCTP偶联未建立    268               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    10          3             SCTP偶联未建立    267               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    161         3             SCTP偶联未建立    272               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    183         3             SCTP偶联未建立    270               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    141         3             SCTP偶联未建立    271               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    1           1             激活              7                 否        否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  LINK_SP_RU_0066    7           1             SCTP偶联未建立    129               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    8           1             SCTP偶联未建立    127               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    181         1             SCTP偶联未建立    126               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    76          1             SCTP偶联未建立    128               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    70          1             SCTP偶联未建立    125               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    51          2             激活              7                 否        否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  LINK_SP_RU_0066    6           2             SCTP偶联未建立    640               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    9           2             SCTP偶联未建立    3                 否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    190         2             SCTP偶联未建立    639               否        否                   否                否                0             0              NULL                                            
  LINK_SP_RU_0066    77          2             SCTP偶联未建立    2                 否        否                   否                否                0             0              NULL                                            
  (结果个数 = 28)
  ---    END
  ```
2. 按照“链路(LINK)”方式查询USN_VSU1上链路号为3的M3UA链路的状态：
  DSP M3LNK: SRT=LINK, RUNAME="USN_SP_RU_0066", LNK=3;
  ```
  %%DSP M3LNK: SRT=LINK, RUNAME="
  USN_SP_RU_0066
  ", LNK=3;%%
  RETCODE = 0  操作成功。

  查询M3UA链路状态
  ----------------
            RU名称  =  USN_SP_RU_0066
            链路号  =  3
            进程号  =  0
          链路状态  =  激活
            偶联ID  =  5
           是否锁定 =  否
           手工去活 =  否
            手工释放=  否
          链路拥塞  =  否
          入流数目  =  10
           出流数目 =  10
               SLS  =  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
  (结果个数 = 1)
  ---    END
  ```
3. 按照“目的信令点(DSP)”方式查询目的实体索引为1对应的M3UA链路的状态：
  DSP M3LNK: SRT=DSP, DEX=1;
  ```
  %%DSP M3LNK: SRT=DSP, DEX=1;%%
  RETCODE = 0  操作成功。

  查询M3UA链路状态
  ----------------
            RU名称  =  USN_SP_RU_0066
            链路号  =  1
            进程号  =  1
          链路状态  =  激活
            偶联ID  =  605
          是否锁定  =  否
          手工去活  =  否
          手工释放  =  否
          链路拥塞  =  否
          入流数目  =  10
          出流数目  =  10
               SLS  =  00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
  (结果个数 = 1)
  ---    END
  ```
4. 按照“链路状态(STATUS)”方式查询处于"激活"状态的M3UA链路：
  DSP M3LNK: SRT=STATUS, LNKSTATE=ACT;
  ```
  %%DSP M3LNK: SRT=STATUS, LNKSTATE=ACT;%%
  RETCODE = 0  操作成功。

  查询M3UA链路状态
  ----------------
  RU名称            链路号      进程号       链路状态       偶联ID             是否锁定   手工去活             手工释放          链路拥塞         入流数目       出流数目       SLS                                             

  LINK_SP_RU_0066    2           0            激活           348                否         否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  LINK_SP_RU_0066    1           1            激活           605                否         否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  LINK_SP_RU_0066    3           3            激活           336                否         否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  LINK_SP_RU_0066    51          2            激活           223                否         否                   否                否                10            10             00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F 
  (结果个数 = 4)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示M3UA信令链路状态(DSP-M3LNK)_72345907.md`
