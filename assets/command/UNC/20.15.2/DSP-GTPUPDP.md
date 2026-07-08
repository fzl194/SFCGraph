---
id: UNC@20.15.2@MMLCommand@DSP GTPUPDP
type: MMLCommand
name: DSP GTPUPDP（显示用户面PDP上下文信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPUPDP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- 用户数据库管理
status: active
---

# DSP GTPUPDP（显示用户面PDP上下文信息）

## 功能

**适用网元：SGSN**

该命令用于查询指定激活用户的PDP上下文信息。

## 注意事项

此功能用于快速定位问题和解决故障，在使用过程中不可避免的使用到用户的某些个人数据，如IMSI、IP地址。建议您遵从国家的相关法律执行该任务，并采取足够的措施以确保用户的个人数据受到充分的保护。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：该参数用于指定国际移动用户标识。该参数在全球范围内唯一标识一个移动用户。<br>取值范围：0~15位BCD码<br>默认值：无 |
| NSAPI | NSAPI | 可选必选说明：可选参数<br>参数含义：该参数用于指定网络业务接入点标识。<br>取值范围：5~15<br>默认值：无<br>说明：此参数的取值可以在用户跟踪里查询得到。 |
| PDPTYPE | 上下文主备状态 | 可选必选参数说明：可选参数<br>参数含义：该参数用于指示上下文的主备状态<br>取值范围：<br>- “MASTER（主用上下文）”<br>- “STANDBY(备用上下文)”<br>默认值：MASTER（主用上下文） |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUPDP]] · 用户面PDP上下文信息（GTPUPDP）

## 使用实例

1. 查询一个已经激活的PDP上下文，IMSI为123035200000015, NSAPI为5：
  DSP GTPUPDP: IMSI="123035200000015", NSAPI=5;
  ```
  %%DSP GTPUPDP: IMSI="123035200000015", NSAPI=5;%%
  RETCODE = 0  操作成功。

  查询结果如下
  ------------
                                     NSAPI  =  5
                                    RU名称  =  USN_SP_RU_0067
                              板内进程序号  =  0
                                  GTPU段号  =  1
                              GTPU段内索引  =  1
                    SGSN给Iu接口分配的Teid  =  0x24004001
                    SGSN给Gn接口分配的Teid  =  0x64004001
                              SGSN是否改变  =  否
                            数据重排序要求  =  否
                        是否网络请求的激活  =  否
                       是否MS发起的QoS修改  =  否
                              动态地址标志  =  动态地址
                               Tunnel 类型  =  Two tunnels
                        One tunnel缓存模式  =  缓存
              Two tunnels 切换到one tunnel  =  否
                             PDP表有效标志  =  有效
                                   RAB状态  =  有效
                                  RAU 类型  =  无切换
                                  转发状态  =  TS_GTPU_CTRL
                       主机上下文Qchat标志  =  否
              本端Iu接口的用户面IP地址索引  =  0x0
                  本端Iu接口的用户面IP地址  =  192.168.52.1
           本端Gn/Gp接口的用户面IP地址索引  =  0x0
                本端GnGp接口的用户面IP地址  =  192.168.52.1
         本端Gn SGSN接口的用户面IP地址索引  =  0x0
             本端Gn SGSN接口的用户面IP地址  =  192.168.52.1
                     GGSN 信令面IP地址索引  =  0x1
                         GGSN 信令面IP地址  =  192.168.52.14
                 对端SGSN 用户面IP地址索引  =  0xFFFFFFFF
                     对端SGSN 用户面IP地址  =  NULL
                          计费网关地址索引  =  0xFFFFFFFF; 0xFFFFFFFF
                              计费网关地址  =  NULL; NULL
                                    SM段号  =  47
                          SM上下文的CB表号  =  2147483672
                             上行计费容器A  =  0
                             下行计费容器A  =  0
                             上行计费容器B  =  0
                             下行计费容器B  =  0
                                  计费阈值  =  1000
                           APN网络标识索引  =  0
                               APN网络标识  =  HUAWEI52
                            运营商标识索引  =  0x0
                                运营商标识  =  MNC123.MCC123.GPRS
                                   PDP类型  =  IPV4
                               PDP计费属性  =  0x0800(Normal Billing)
                         请求的QoS业务等级  =  QoS流类
                         协商的QoS业务等级  =  QoS流类
                               APN选择模式  =  MS或网络提供APN，已签约检验
                是否重选Iu接口用户面IP地址  =  否
                              计费控制状态  =  话单已创建，处于正常状态
                            空闲定时器属性  =  空闲不去
                                  PF进程号  =  0x21000411
                                 GIB表索引  =  0x1
           PDP最近一次收到流量报告的Tick数  =  142880
                    话单使用的网络标识索引  =  4294967295
                        话单使用的网络标识  =  NULL
                  话单使用的运营商标识索引  =  0xFFFFFFFF
                      话单使用的运营商标识  =  NULL
  	                     APNNI表计数  =  1
                               APNOI表计数  =  1
                                   RNC标识  =  12303F105
                                   PDP地址  =  192.168.39.16
                       GFU分配的转发表索引  =  0x24004001
                             PDP状态机状态  =  2
                          给用户分配的带宽  =  0
                 A容器的上行已经申报的流量  =  0
                 A容器的下行已经申报的流量  =  0
                 B容器的上行已经申报的流量  =  0
                 B容器的下行已经申报的流量  =  0
                开始转发下行数据定时器句柄  =  0
                停止转发切换数据定时器句柄  =  0
                        GTPU控制定时器句柄  =  0
                          GTPU当前操作流程  =  16843011
                备份校验用GTPU当前操作流程  =  16843011
                             PDP激活时间戳  =  142795
               PDP上下文上一次核查的时间戳  =  0
    PDP上下文上一次向SM发送ERR IND的时间戳  =  0
                              智能手机类型  =  16
            SGSN分配给SGSN的数据面流量标识  =  20488     
            SGSN分配给GGSN的数据面流量标识  =  12296                             
                          PF是否缓存数据包  =  是
                                重排序标志  =  是
                        切换时数据目的实体  =  No FWD
                              下行是否缓存  =  Trans
                          去Gb方向是否缓存  =  Drop only
                         去RNC方向是否缓存  =  Drop only
                        去SGSN方向是否缓存  =  Drop only
                               Qos服务等级  =  QoS流类
                                    可靠性  =  SNDCP without Ack
                                出跟踪标志  =  关闭
                                入跟踪标志  =  关闭
                           到SGSN的GTP版本  =  GTP V1
                                接入网类型  =  3G
                          标识表项是否可用  =  GIB Valid
                           到GGSN的GTP版本  =  GTP V1
                GGSN的目的IP对应的路径索引  =  23
                  GGSN路径中的对端GGSN地址  =  192.168.52.15
                            GGSN的目的TEID  =  0x989689
                          GGSN数据面流标识  =  0
                                       TOS  =  72
                 RNC的目的IP对应的路径索引  =  24
                    RNC路径中的对端RNC地址  =  192.168.52.112
                             RNC的目的TEID  =  0x1000000B
                            SGSN的目的TEID  =  0x0
                SGSN的目的IP对应的路径索引  =  4294967295
                          SGSN数据面流标识  =  0
                                    GB段号  =  4294967295
                                GB段内索引  =  4294967295
                              序号检查标志  =  No
                               RAB重建标志  =  No
  将下行数据包（包括缓存包）转为切换包标志  =  No
                              流量上报阈值  =  1024000
                                  计费标识  =  878407278
                     A容器上行计费流量统计  =  1024
                     A容器下行计费流量统计  =  1024
                 A容器上行计费流量统计备份  =  0
                 A容器下行计费流量统计备份  =  0
                     B容器上行计费流量统计  =  0
                     B容器下行计费流量统计  =  0
                 B容器上行计费流量统计备份  =  0
                 B容器下行计费流量统计备份  =  0
                    最近收到病毒报文时间戳  =  0
                          源IP地址错误统计  =  0
                                  染毒标记  =  No
                            上行序号期望值  =  0
                            下行序号期望值  =  0
                          上行接收序号记录  =  0
                          下行接收序号记录  =  0
                            合法性校验字段  =  287529183
                            停止转发指示字  =  0
                用于用户跟踪的全流程跟踪ID  =  15
                           是否是QChat用户  =  否
                            TEID中的随机数  =  4
     此上下文的接收队列编号，0xff表示无效,  =  255
                          下行缓存队列标识  =  32678
                          切换缓存队列标识  =  32678
                                接收的包数  =  0
                              接收的字节数  =  0
               上行DepartureTimestamp(L32)  =  2358270011
               上行DepartureTimestamp(H32)  =  0
                          上行TokenContent  =  363931761
                            上行PtokenAll0  =  1692705
                            上行PtokenAll1  =  3385411
                          上行令牌桶的大小  =  365624433
               下行DepartureTimestamp(L32)  =  2343356438
               下行DepartureTimestamp(H32)  =  0
                          下行TokenContent  =  363931761
                            下行PtokenAll0  =  1692705
                            下行PtokenAll1  =  3385411
                          下行令牌桶的大小  =  365624433
                          源IP地址错误统计  =  0
                          病毒特征匹配次数  =  0
                                  扫描次数  =  0
                         上次RAB重建时间戳  =  4294367296
        单用户实时性能统计对应统计表项索引  =  65535
                                       TID  =  1230352000000155
                         临时保存GGSN TEID  =  0x989689
                         临时保存SGSN TEID  =  0x0
                          临时保存RNC TEID  =  0x1000000B
                                 PFP自旋锁  =  1
                           GIB表Tunnel类型  =  Two tunnels
                    上行数据包倒换主备类型  =  未发生倒换
                    下行数据包倒换主备类型  =  未发生倒换
                          用户数传统计开关  =  不进行数传统计
                            跟踪重定向开关  =  跟踪重定向开关关闭
                            上下文主备状态  =  主用上下文
                        主备上下文是否一致  =  NULL
  (结果个数 = 1)

  ---    END
  ```
2. 查询一个已经激活的PDP上下文，IMSI为123030320000001，NSAPI不输入，返回对应的NSAPI列表：
  DSP GTPUPDP: IMSI="123030320000001";
  ```
  %%DSP GTPUPDP: IMSI="123030320000001";%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
          PDP地址 = 192.168.3.4
            NSAPI = 5
      APN网络标识 = ggsn12.com
  (结果个数 = 1)

  ---    END
  ```
3. 查询一个未激活的IMSI为123030320000001：
  DSP GTPUPDP: IMSI="123030320000001";
  ```
  %%DSP GTPUPDP: IMSI="123030320000001";%%
  RETCODE = 18518  

  没有查到相应的结果
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTPUPDP.md`
