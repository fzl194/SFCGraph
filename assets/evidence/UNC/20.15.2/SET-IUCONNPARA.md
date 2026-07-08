# 设置Iu连接控制参数(SET IUCONNPARA)

- [命令功能](#ZH-CN_MMLREF_0000001126145514__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145514__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145514__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145514__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145514__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145514__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145514)

**适用网元：SGSN**

该命令用于设置Iu连接控制策略。

#### [注意事项](#ZH-CN_MMLREF_0000001126145514)

- 系统初次运行时，会执行系统初始设置值。
- 此命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145514)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145514)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145514)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLLWNTWHUTPDP | Follow on without PDP场景Iu连接管理 （s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Attach或Rau流程中UE在Request消息中携带"Follow-on request pending"标志，且网络侧无激活的PDP上下文时，Iu连接控制策略。<br>数据来源：整网规划<br>取值范围：0～300，65535<br>系统初始设置值：10。<br>配置原则：<br>- 0：表示立即释放。<br>- 65535：表示不释放。<br>- 其它：表示等待设定时长后再释放Iu连接。<br>说明：参数修改为0会导致Release Command sent success和Release Complete received指标大幅上升。 |
| FLLWNWTHPDP | Follow on with PDP场景Iu连接管理 （s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Attach或Rau流程中UE在Request消息中携带<br>“Follow-on request pending”<br>标志，且网络侧存在激活的PDP上下文时，Iu连接控制策略。<br>数据来源：整网规划<br>取值范围：0～300，65535<br>系统初始设置值：10。<br>配置原则：<br>- 0：表示立即释放。<br>- 65535：表示不释放。<br>- 其它：表示等待设定时长后再释放Iu连接。<br>说明：参数修改为0会导致Release Command sent success和Release Complete received指标大幅上升。 |
| NOFLLWNTWHUTPDP | No follow on without PDP场景Iu连接管理 （s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Attach或Rau流程中UE在Request消息中携带<br>“No follow-on request pending”<br>标志，且网络侧无激活的PDP上下文时，Iu连接控制策略。<br>数据来源：整网规划<br>取值范围：0～300，65535<br>系统初始设置值：0。<br>配置原则：<br>- 0：表示立即释放。<br>- 65535：表示不释放。<br>- 其它：表示等待设定时长后再释放Iu连接。<br>说明：参数修改为65535会导致Release Command sent success和Release Complete received指标大幅下降。 |
| NOFLLWNWTHPDP | No follow on with PDP场景Iu连接管理 （s） | 可选必选说明：可选参数<br>参数含义：该参数用于指定Attach或Rau流程中UE在Request消息中携带<br>“No follow-on request pending”<br>标志，且网络侧存在激活的PDP上下文时，Iu连接控制策略。<br>数据来源：整网规划<br>取值范围：0～300，65535<br>系统初始设置值：0。<br>配置原则：<br>- 0：表示立即释放。<br>- 65535：表示不释放。<br>- 其它：表示等待设定时长后再释放Iu连接。<br>说明：参数修改为65535会导致Release Command sent success和Release Complete received指标大幅下降。 |
| SMS | SMS流程Iu连接管理（s） | 可选必选说明：可选参数<br>参数含义：该参数用于控制短信流程结束后的Iu连接控制策略。<br>数据来源：整网规划<br>取值范围：0～300，65535<br>系统初始设置值：65535。<br>配置原则：<br>- 0：表示立即释放。<br>- 65535：表示不释放。<br>- 其它：表示等待设定时长后再释放Iu连接。<br>说明：参数修改为0会导致Release Command sent success和Release Complete received指标大幅下降。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145514)

设置Iu连接控制策略：

SET IUCONNPARA: FLLWNTWHUTPDP=80, FLLWNWTHPDP=60, NOFLLWNTWHUTPDP=50, NOFLLWNWTHPDP=40, SMS=300;
