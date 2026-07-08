# 设置Bi口IPCONVERGENCE开关（SET IPCONVERGENCE）

- [命令功能](#ZH-CN_CONCEPT_0000001336016493__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001336016493__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0000001336016493__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0000001336016493__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0000001336016493__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0000001336016493__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001336016493)

![](设置Bi口IPCONVERGENCE开关（SET IPCONVERGENCE）_36016493.assets/notice_3.0-zh-cn_2.png)

属于高危命令，如果操作不当会导致话单业务严重受损，执行前请务必联系华为技术支持。

**适用NF：NCG**

该命令用于设置Bi口IP收敛功能。允许将多个RU上的话单汇聚到一个RU上，以此来解决扩容场景下计费中心需要多次适配的情况。

#### [注意事项](#ZH-CN_CONCEPT_0000001336016493)

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 该命令执行后，需在“话单存储(CDRSTOR)”命令的“最终话单文件名命名规则”中增加“增加模块名信息(%a或%A)”或“增加模块号信息(%B)”，防止话单汇聚时被覆盖。
- Bi收敛开关打开后，配置话单备份任务或话单分发PUSH任务前，需在每一个RUID上配置Omi或Bi&Omi的IP地址。
- 该命令最大记录数为1。
- 该命令存在系统初始设置记录，参数的初始设置值如下表：

| IPCONVERGENCESWITCH |
| --- |
| OFF |

#### [本地用户权限](#ZH-CN_CONCEPT_0000001336016493)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0000001336016493)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001336016493)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPCONVERGENCESWITCH | Bi口IPCONVERGENCE 开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置Bi口IPCONVERGENCE开关状态。数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001336016493)

设置Bi口IPCONVERGENCE开关状态为开启：

```
SET IPCONVERGENCE: IPCONVERGENCESWITCH=ON;
```
