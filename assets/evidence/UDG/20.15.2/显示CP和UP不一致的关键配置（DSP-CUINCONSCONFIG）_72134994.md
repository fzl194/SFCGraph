# 显示CP和UP不一致的关键配置（DSP CUINCONSCONFIG）

- [命令功能](#ZH-CN_CONCEPT_0272134994__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0272134994__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0272134994__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0272134994__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0272134994__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0272134994__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0272134994)

**适用NF：PGW-U、UPF**

该命令用来查看当前影响系统的SMF/PGW-C和UPF/PGW-U不一致的部分配置。

#### [注意事项](#ZH-CN_CONCEPT_0272134994)

当SMF/PGW-C发送的消息中携带多个UPF/PGW-U未配置的Service Property信元时，DSP CUINCONSCONFIG命令仅显示第一个未配置的Service Property信元。

#### [操作用户权限](#ZH-CN_CONCEPT_0272134994)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0272134994)

无。

#### [使用实例](#ZH-CN_CONCEPT_0272134994)

查询SMF/PGW-C和UPF/PGW-U不一致的配置：

```
DSP CUINCONSCONFIG:;
```

```

RETCODE = 0  操作成功

CP和UP不一致的配置
---------------------------------------
Result  =  
No    CP Node ID Type    CP Node ID Value    IE/Cfg Type         Cause                        IE/Cfg Name
1     IPV4               192.168.10.10       Common Policy       Unknown_IE_Name              test 
2     IPV4               192.168.10.10       Predefined Rule     Unknown_IE_Name              11116667
3     IPV4               192.168.10.10       Service Property    Unknown_IE_Name              sp_1   
4     IPV4               192.168.10.10       Service Property    Exceeded_Specifications             
(Number of results = 1)

---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0272134994)

| 输出项名称 | 输出项解释 |
| --- | --- |
| CP Node ID Type | 表示SMF/PGW-C的IP地址类型。 |
| CP Node ID Value | 表示SMF/PGW-C的IP地址。 |
| IE/Cfg Type | 信元名称。 |
| Cause | 触发“ALM-81054 CP和UP关键配置不一致”的原因。原因包含Unknown_IE_Name和Exceeded_Specifications。其中Unknown_IE_Name表示SMF/PGW-C发送的消息中携带的信元无法匹配上UPF/PGW-U的配置；Exceeded_Specifications为SMF/PGW-C发送的消息中携带的Service Property信元记录数超过最大值10个。 |
| IE/Cfg Name | 信元携带的配置名称。 |
