# 查询NP端口状态（DSP NPPORT）

- [命令功能](#ZH-CN_TOPIC_0271028287__1.3.1.1)
- [注意事项](#ZH-CN_TOPIC_0271028287__1.3.2.1)
- [操作用户权限](#ZH-CN_TOPIC_0271028287__1.3.3.1)
- [参数说明](#ZH-CN_TOPIC_0271028287__1.3.4.1)
- [使用实例](#ZH-CN_TOPIC_0271028287__1.3.5.1)
- [输出结果说明](#ZH-CN_TOPIC_0271028287__1.3.6.1)

#### [命令功能](#ZH-CN_TOPIC_0271028287)

该命令用于显示NP端口状态信息。

#### [注意事项](#ZH-CN_TOPIC_0271028287)

该命令仅适用于NP卡加速模式场景。

#### [操作用户权限](#ZH-CN_TOPIC_0271028287)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_TOPIC_0271028287)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU编号 | 可选必选说明：必选参数。<br>参数含义：RU编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～4294967294。<br>默认值：无。<br>配置原则：使用<br>[DSP RU](../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询RU编号。 |

#### [使用实例](#ZH-CN_TOPIC_0271028287)

显示RUID为68的NP端口状态信息：

```
DSP NPPORT: RUID=68;
```

```
RETCODE = 0  操作成功

结果如下
--------
NP端口名称    虚拟网口名称  网口功能  物理状态  链路状态  Mac地址            附加信息   

100G/NP0/12   NULL          NULL      UP        UP        NA                 CPU0       
100G/NP0/142  NULL          NULL      UP        UP        NA                 CPU1       
100G/NP0/0    NULL          E/W       UP        UP        64:2c:ac:6d:62:65  P4         
100G/NP0/130  NULL          E/W       UP        UP        64:2c:ac:6d:62:66  P3         
100G/NP0/4    eth8          S/N       DOWN      INVALID   64:2c:ac:6d:62:67  P2         
100G/NP0/134  eth9          S/N       DOWN      INVALID   64:2c:ac:6d:62:68  P1         
25G/NP0/8     eth10         S/N       DOWN      INVALID   64:2c:ac:6d:62:69  P6         
25G/NP0/138   eth11         S/N       DOWN      INVALID   64:2c:ac:6d:62:6a  P5         
25G/NP0/9     eth12         S/N       DOWN      INVALID   64:2c:ac:6d:62:6b  P8         
25G/NP0/139   eth13         S/N       DOWN      INVALID   64:2c:ac:6d:62:6c  P7
25G/NP0/10    NULL          NULL      UP        UP        NA                 6603/itf9  
25G/NP0/11    NULL          NULL      UP        UP        NA                 6603/itf8  
25G/NP0/140   NULL          NULL      UP        UP        NA                 6603/itf7  
25G/NP0/141   NULL          NULL      UP        UP        NA                 6603/itf6  
25G/NP0/16    NULL          NULL      UP        UP        NA                 6603/itf5  
25G/NP0/17    NULL          NULL      UP        UP        NA                 6603/itf4  
25G/NP0/146   NULL          NULL      UP        UP        NA                 6603/itf3  
25G/NP0/147   NULL          NULL      UP        UP        NA                 6603/itf2  
(结果个数 = 18)

---    END
```

#### [输出结果说明](#ZH-CN_TOPIC_0271028287)

| 输出项名称 | 输出项解释 |
| --- | --- |
| NP端口名称 | NP的端口名称。 |
| 虚拟网口名称 | NP端口对应到容器里的网口名称。<br>外联口在容器里有对应网口，内联口与级联口没有对应网口。 |
| 网口功能 | - 外联口为S/N<br>- 级联口为E/W |
| 物理状态 | NP端口的物理状态。<br>物理状态枚举类型：<br>- UP：端口物理UP。<br>- DOWN：端口物理DOWN。 |
| 链路状态 | NP端口的链路状态。<br>链路状态枚举类型：<br>- UP：链路已链接。<br>- DOWN：链路已中断。<br>- INVALID：链路状态无效。<br>- SUBHEALTHY：链路亚健康。 |
| Mac地址 | NP端口的Mac地址。 |
| 附加信息 | NP端口对应的面板号信息或NP端口对应的对端硬件面板号信息。 |
