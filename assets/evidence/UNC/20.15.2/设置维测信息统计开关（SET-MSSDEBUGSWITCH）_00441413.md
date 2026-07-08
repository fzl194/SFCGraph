# 设置维测信息统计开关（SET MSSDEBUGSWITCH）

- [命令功能](#ZH-CN_CONCEPT_0000001600441413__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001600441413__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001600441413__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001600441413__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001600441413__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001600441413)

![](设置维测信息统计开关（SET MSSDEBUGSWITCH）_00441413.assets/notice_3.0-zh-cn_2.png)

本命令属于高危命令，操作不当会导致性能下降，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置MSS维测统计信息开关。

#### [注意事项](#ZH-CN_CONCEPT_0000001600441413)

- 该命令执行后立即生效。
- 本功能使能会消耗内存、降低性能且在用户指定的时间之后会自动去使能，去使能之后内存释放、性能恢复。默认时间是30分钟。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001600441413)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001600441413)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |
| DEBUGSWITCH | 开关标记 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关标记。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：关闭。<br>- TRUE：打开。<br>默认值：无 |
| DEBUGTYPE | 开关类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示开关类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- schedule-work：Work精度维测开关。<br>- schedule-group：调度组精度开关。<br>- schedule-queue：调度队列维测开关。<br>- energy-conservation：绿色节能维测开关。<br>- oe-check：保序校验维测开关。<br>- oe-statistics：保序精度维测开关。<br>- timer-event：定时器事件维测开关。<br>- timer-statistics：定时器精度维测开关。<br>- schedule-trace：调度轨迹维测开关。<br>默认值：无 |
| TIME | 维测时间（s） | 可选必选说明：条件可选参数<br>前提条件：该参数在“DEBUGSWITCH”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于表示维测状态持续时间，单位为秒。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～86400。<br>默认值：1800 |

#### [使用实例](#ZH-CN_CONCEPT_0000001600441413)

设置维测信息统计开关打开：

```
SET MSSDEBUGSWITCH:DEBUGSWITCH=TRUE,DEBUGTYPE=schedule-work,RUNAME = "VNODE_VNRS_VNFC_IPU_0064";
```
