# 显示MultiDNN参数（LST MULTIDNNPARA）

- [命令功能](#ZH-CN_CONCEPT_0000202570853530__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000202570853530__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000202570853530__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000202570853530__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000202570853530__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000202570853530__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000202570853530)

**适用NF：PGW-U、UPF**

查询MultiDNN参数。

#### [注意事项](#ZH-CN_CONCEPT_0000202570853530)

无。

#### [操作用户权限](#ZH-CN_CONCEPT_0000202570853530)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000202570853530)

无。

#### [使用实例](#ZH-CN_CONCEPT_0000202570853530)

使用LST MULTIDNNPARA命令查询MultiDNN参数：

```
LST MULTIDNNPARA:;
```

```

RETCODE = 0  Operation succeeded

MultiDNN Parameter
------------------
                        MultiDNN Function Switch  =  ENABLE
                           IPv4 NAT ALG Protocol  =  FTP Protocol&RTSP Protocol
                           IPv6 NAT ALG Protocol  =  FTP Protocol
           Flow Control Interval for Reports (s)  =  2
                             Actions for Packets  =  Discard
                    UE IP Address Conflict Check  =  ENABLE
                       UE IP Reallocation Switch  =  ENABLE
            Number of UE IP Address Reallocation  =  1000
     Policy for Handling UE IP Address Conflicts  =  BYPASS
Check Interval for the Campus Resource Threshold  =  240
                       N4 Report MultiDNN Switch  =  ENABLE
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000202570853530)

参见SET MULTIDNNPARA的参数说明。
