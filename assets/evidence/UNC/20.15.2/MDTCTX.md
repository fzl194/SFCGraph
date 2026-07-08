# 显示MDT上下文(DSP MDTCTX)

- [命令功能](#ZH-CN_MMLREF_0000001172225515__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172225515__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172225515__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172225515__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172225515__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172225515__1.3.6.1)
- [输出结果说明](#ZH-CN_MMLREF_0000001172225515__1.3.7.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172225515)

**适用网元：MME**

此命令用于查看MDT上下文的相关信息。

#### [注意事项](#ZH-CN_MMLREF_0000001172225515)

- 该命令执行后立即生效。
- 当不存在用户上下文时，该命令查询不到MDT上下文。
- 通过网管直接给MME创建MDT任务需要等用户切换到连接态才可以查询到MDT参数。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172225515)

manage-ug；system-ug；monitor-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172225515)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172225515)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QUERYOPT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询MDT上下文的方式。<br>取值范围：枚举类型。<br>- “BYIMSI（指定IMSI）”：表示根据IMSI查询用户的MDT上下文。<br>- “MDTUSRNUM（MDT用户数）”:表示查询MDT用户数。<br>- “ALL（全部）”：表示全部查询<br>默认值：<br>“BYIMSI（指定IMSI）” |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数为国际移动用户标识。<br>前提条件：该参数在<br>“查询方式”<br>参数配置为指定为<br>“BYIMSI”<br>后生效。<br>取值范围：0~15位十进制数字。<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172225515)

查询IMSI号为123032201000001的用户的MDT上下文的相关信息

DSP MDTCTX: QUERYOPT=BYIMSI, IMSI="123032201000001";

```
+++    usn        2017-12-15 17:40:56+08:00
O&M   #117
%%DSP MDTCTX: QUERYOPT=BYIMSI, IMSI="123032201000001";%%
RETCODE = 0  操作成功

操作结果如下：
--------------
              IMSI  =  
123032201000001

            跟踪号  =  41006
        跟踪触发源  =  HSS
          任务类型  =  Immediate MDT only
      测量区域类型  =  TAI
      测量区域列表  =  123301234; 1230300134; 123300334
          测量方式  =  1
      报告触发类型  =  1
          报告间隔  =  12分钟
          报告次数  =  4
      RSRP事件阈值  =  0
      RSRQ事件阈值  =  0
Logged MDT报告间隔  =  NULL
Logged MDT持续时间  =  NULL
      MDT PLMN列表  =  12330; 12310; 12320
(结果个数 = 1)

---    END
```

#### [输出结果说明](#ZH-CN_MMLREF_0000001172225515)

| 输出项名称 | 输出项解释 |
| --- | --- |
| MDT用户数 | 显示MDT用户数量。<br>取值范围：0~65535。 |
| IMSI | 显示用户的国际移动用户标识，该参数在用户和运用商签约时由运营商指定。<br>取值范围：0~15位十进制数字。 |
| 跟踪号 | 显示跟踪任务标识。<br>取值范围：0~65535。 |
| 跟踪触发源 | 显示跟踪的触发源。<br>取值范围：枚举类型。<br>- “U2020/MAE”：表示出发源为U2020/MAE。<br>- “HSS”：表示出发源为HSS。 |
| 任务类型 | 显示MDT任务的类型。<br>取值范围：枚举类型。<br>- “Immediate MDT only”：表示“仅实时最小化路测”。<br>- “Logged MDT only”：表示“仅非实时最小化路测”。<br>- “Trace only”：表示“仅跟踪”。<br>- “Immediate MDT and Trace”：表示“实时最小化路测并跟踪”。 |
| 测量区域类型 | 显示MDT测量的数据采集区域类型。<br>取值范围：枚举类型。<br>- “ECGI”：表示ECGI类型。<br>- “TAC”：表示TAC类型。<br>- “PLMN_WIDE”：表示PLMN_WIDE类型。<br>- “TAI”：表示TAI类型。<br>- “NULL”：表示无类型。 |
| 测量区域列表 | 显示MDT测量的数据采集区域的列表。<br>取值范围：0~480长度字符串。 |
| 测量方式 | 表示MDT测量的测量方式。<br>取值范围：0~255。<br>- “0”：表示“不选择测量模式”。<br>- “1”：表示“选择测量模式1：RSRP and RSRQ measurement by UE with Periodic， event A2 as reporting triggers。”。<br>- “2”：表示“选择测量模式2：Power Headroom (PH) measurement by UE。”。<br>- “3”：表示“同时选择两个测量模式”。<br>- “4–255”:保留给后续使用 |
| 报告触发类型 | 显示MDT测量的报告触发类型。<br>取值范围：0~255。<br>- “1”：表示“Periodical”。<br>- “2”：表示“Event A2 for LTE”。<br>- “3”：表示“A2 event triggered periodic for LTE”。<br>- “0,4–255”：保留给后续使用 |
| 报告间隔 | 显示UE上报相邻两次测量报告的时间间隔。<br>取值范围：枚举类型。<br>- “120 ms”<br>- “240 ms”<br>- “480 ms”<br>- “640 ms”<br>- “1024 ms”<br>- “2048 ms”<br>- “5120 ms”<br>- “10240 ms”<br>- “1 min”<br>- “6 min”<br>- “12 min”<br>- “30 min”<br>- “60 min” |
| 报告次数 | 显示UE上报周期测量报告的次数。<br>取值范围：枚举类型。<br>- “0”表示1次<br>- “1”表示2次<br>- “2”表示4次<br>- “3”表示8次<br>- “4”表示16次<br>- “5”表示32次<br>- “6”表示64次<br>- “7”表示无限制次数 |
| RSRP事件阈值 | 显示触发RSRP（Reference Signal Received Power）事件的门限。<br>取值范围：0~97 |
| RSRQ事件阈值 | 显示触发RSRQ（Reference Signal Received Quality）事件的门限。<br>取值范围：0~34 |
| Logged MDT报告间隔 | 显示Logged MDT报告间隔。<br>取值范围：枚举类型。<br>- “1.28”<br>- “2.56”<br>- “5.12”<br>- “10.24”<br>- “20.48”<br>- “30.72”<br>- “40.96”<br>- “61.44” |
| Logged MDT持续时间 | 显示Logged MDT持续时间。<br>取值范围：枚举类型。<br>- “600 sec”<br>- “1200 sec”<br>- “2400 sec”<br>- “3600 sec”<br>- “5400 sec”<br>- “7200 sec” |
| MDT PLMN列表 | 显示MDT PLMN列表。<br>取值范围：0~128长度字符串。 |
