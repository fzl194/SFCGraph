# 查询NF属性冲突核验参数（LST NRFVERIFYPARA）

- [命令功能](#ZH-CN_MMLREF_0000001135636455__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001135636455__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001135636455__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001135636455__1.3.5)
- [输出结果说明](#ZH-CN_MMLREF_0000001135636455__1.3.6)

## [命令功能](#ZH-CN_MMLREF_0000001135636455)

**适用NF：NRF**

该命令用于查询NF属性冲突核验参数。

## [注意事项](#ZH-CN_MMLREF_0000001135636455)

无

#### [操作用户权限](#ZH-CN_MMLREF_0000001135636455)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001135636455)

无

## [使用实例](#ZH-CN_MMLREF_0000001135636455)

查询NF属性冲突核验参数：

```
LST NRFVERIFYPARA:;
%%LST NRFVERIFYPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
                     起始位置  =  4
                         长度  =  3
             NF间冲突核验属性  =  IMSI&MSISDN
NF和跨NRF路由数据冲突核验属性  =  IMSI&MSISDN
                 每秒核验步长  =  10
             核验超时时长(秒)  =  60
       核验结果老化时长(分钟)  =  5
     最大核验失败属性元素个数  =  1
(结果个数 = 1)

---    END
```

## [输出结果说明](#ZH-CN_MMLREF_0000001135636455)

| 输出项名称 | 输出项解释 |
| --- | --- |
| 起始位置 | 该参数表示NF实例标识中大区及省份信息的起始位置。 |
| 长度 | 该参数表示NF实例标识中大区及省份信息的长度。 |
| NF间冲突核验属性 | 该参数表示本NRF管理的NF间属性冲突核验中需要核验的属性，勾选表示系统会对此属性对应的NF进行核验，如果存在同类型的其他NF的属性值与当前NF属性值相同，而这些NF的实例标识中对应的大区及省份信息与当前NF不一致，则判断当前NF存在NF间属性冲突。<br>NRF支持核验的属性如下：<br>IMSI（涉及UDM，UDR，PCF，AUSF，CHF，CUSTOM_OCS，SMSF）。<br>MSISDN（涉及UDM，UDR，PCF，CUSTOM_OCS，CHF，SMSF）。<br>ROUTINGINDICATOR（涉及UDM，AUSF）。<br>TAI（涉及SMF，AMF，NWDAF）。<br>IPV6PREFIX（涉及BSF）。 |
| NF和跨NRF路由数据冲突核验属性 | 该参数表示NF数据和跨NRF寻址信息冲突核验中需要核验的属性，勾选表示系统会对此属性对应的NF进行核验，如果存在跨NRF寻址信息与当前NF属性值相同，则判断存在NF属性与跨NRF寻址信息冲突。<br>NRF支持核验的属性如下：<br>IMSI（涉及UDM，UDR，PCF，AUSF，CHF，CUSTOM_OCS，SMSF）。<br>MSISDN（涉及UDM，UDR，PCF，CUSTOM_OCS，CHF，SMSF）。<br>ROUTINGINDICATOR（涉及UDM，AUSF）。<br>TAI（涉及SMF，AMF，NWDAF）。<br>IPV6PREFIX（涉及BSF）。 |
| 每秒核验步长 | 该参数表示属性冲突核验时每秒核验NF属性值个数上限，保证NRF处理平滑，防止消耗CPU过多。 |
| 核验超时时长(秒) | 该参数表示单个NF核验的最长时长，对单个NF进行属性核验时，如果超过此时长还未核验完成，NRF会将该NF的核验结果设置为超时。 |
| 核验结果老化时长(分钟) | 该参数表示NF核验结果的老化时长，对于超过老化时长的核验结果在系统中删除。 |
| 最大核验失败属性元素个数 | 该参数表示NRF判断某属性存在冲突的最大元素个数，针对某个属性的核验过程中，如果核验存在冲突的元素个数超过该参数的值，NRF停止核验，返回核验不通过。 |
