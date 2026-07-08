# 显示差异化服务信息(DSP DIFFSERVICE)

- [命令功能](#ZH-CN_MMLREF_0000001126145676__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145676__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145676__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145676__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145676__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145676__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001126145676__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145676)

**适用网元：SGSN**

该命令用于查询系统运行过程中差异化服务信息，包括系统中正在运行的不同用户级别用户个数和不同用户级别业务级别的用户差异服务用户接入和PDP接入的情况。

#### [注意事项](#ZH-CN_MMLREF_0000001126145676)

如果输入RU名称和进程号，就查询这个SPP进程上的当前的差异化服务信息；如果没有输入RU名称和进程号，则查询系统所有的差异化服务的信息。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145676)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145676)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145676)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名称。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：本端规划<br>取值范围：1～63位字符串<br>默认值：无 |
| PROCNO | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于显示业务进程所属的SPP进程序号。<br>数据来源：本端规划<br>取值范围：0～20<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145676)

查询整系统差异化服务信息：

DSP DIFFSERVICE:;

```
%%DSP DIFFSERVICE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
2G 高端用户 = 0
2G 普通用户 = 0
2G 低端用户 = 0
3G 高端用户 = 0
3G 普通用户 = 0
3G 低端用户 = 0
仍有后续报告输出
---    END

%%DSP DIFFSERVICE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
用户级别     2G用户接入     3G用户接入

高端用户     允许接入       允许接入
普通用户     允许接入       允许接入
低端用户     允许接入       允许接入 
仍有后续报告输出
---    END

%%DSP DIFFSERVICE:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
用户级别     业务级别                   2G PDP接入     3G PDP接入
                                                   
高端用户     Conversation               允许接入       允许接入
高端用户     StreamingGBRMore25Kbps     允许接入       允许接入
高端用户     StreamingGBRLess24Kbps     允许接入       允许接入
高端用户     InteractiveTrafficPri1     允许接入       允许接入
高端用户     InteractiveTrafficPri2     允许接入       允许接入
高端用户     InteractiveTrafficPri3     允许接入       允许接入
高端用户     Background                 允许接入       允许接入
普通用户     Conversation               允许接入       允许接入
普通用户     StreamingGBRMore25Kbps     允许接入       允许接入
普通用户     StreamingGBRLess24Kbps     允许接入       允许接入
普通用户     InteractiveTrafficPri1     允许接入       允许接入
普通用户     InteractiveTrafficPri2     允许接入       允许接入
普通用户     InteractiveTrafficPri3     允许接入       允许接入
普通用户     Background                 允许接入       允许接入
低端用户     Conversation               允许接入       允许接入
低端用户     StreamingGBRMore25Kbps     允许接入       允许接入
低端用户     StreamingGBRLess24Kbps     允许接入       允许接入
低端用户     InteractiveTrafficPri1     允许接入       允许接入
低端用户     InteractiveTrafficPri2     允许接入       允许接入
低端用户     InteractiveTrafficPri3     允许接入       允许接入
低端用户     Background                 允许接入       允许接入
(结果个数 = 25)
共有3个报告
---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001126145676)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 用户级别 | 该参数用于指定表示用户签约QoS属性中的分配保留优先级（Allocation/Retention Priority）。<br>取值说明：<br>- “ HIGHLEVELUSER(高端用户)”：分配保留优先级等于1。<br>- “ NORMALUSER(普通用户)”：分配保留优先级等于2。<br>- “LOWLEVELUSER(低端用户)”：分配保留优先级等于3。 |
| 业务级别 | 该参数表示PDP的业务级别，由用户PDP上下文QoS中的流量等级（Traffic class）、下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。<br>取值说明：<br>- “ CONVERSATION(Conversation)”：流量等级为Conversational class。<br>- “STREAMINGGBRMORE25KBPS(StreamingGBRMore25Kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。<br>- “ STREAMINGGBRLESS24KBPS(StreamingGBRLess24Kbps)”：流量等级为Streaming class，下行保证速率小于25kbit/s。<br>- “ INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。<br>- “ INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。<br>- “INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。<br>- “ BACKGROUND(Background)”：流量等级为Background class。<br>- “NONE(None)”：通用业务级别，表示该用户没有业务级别，设置的门限就是该用户级别所有业务级别的门限。 |
| 2G用户接入 | 是否允许2G用户接入。<br>取值说明：<br>- “允许接入”<br>- “拒绝接入” |
| 3G用户接入 | 是否允许3G用户接入。<br>取值说明：<br>- “允许接入”<br>- “拒绝接入” |
| 2G PDP接入 | 是否允许2G PDP接入。<br>取值说明：<br>- “允许接入”<br>- “拒绝接入” |
| 3G PDP接入 | 是否允许3G PDP接入。<br>取值说明：<br>- “允许接入”<br>- “拒绝接入” |
