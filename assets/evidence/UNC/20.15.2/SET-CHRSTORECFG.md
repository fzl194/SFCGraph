# 设置CHR存盘配置（SET CHRSTORECFG）

- [命令功能](#ZH-CN_MMLREF_0000001126145616__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126145616__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126145616__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126145616__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126145616__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126145616__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126145616)

**适用网元：SGSN、MME**

该命令用于控制系统在上报CHR单据时，配置CHR单据在 ucf 上的存储策略。 ucf 存储CHR单据功能主要应用于没有部署CloudUDN同时又想做本地单据分析的局点，或传输链路中断时将CHR单据本地保存的情况。存储功能打开时 UNC 采集订阅流程的CHR单据发送给 ucf ，并且通知 ucf 存储到本地硬盘中。

#### [注意事项](#ZH-CN_MMLREF_0000001126145616)

- 该命令执行后立即生效。
- 系统初次运行时，会执行系统初始设置值。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126145616)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126145616)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126145616)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STOREALLFLAG | CHR存储开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制CHR单据在<br>ucf<br>上本地存储功能是否打开。存储开关打开时，<br>ucf<br>上会存储<br>UNC<br>发送的全部单据。<br>数据来源：本端规划<br>取值范围：<br>- “OFF(关)”<br>- “ON(开)”<br>系统初始设置值：<br>“OFF(关)”<br>配置原则：<br>- 全量CHR单据不需要在ucf上进行本地存储的时候选择“OFF(关)”。<br>- 全量CHR单据需要在ucf上进行本地存储的时候选择“ON(开)”。 |
| STOREALLTYPE | 存储类型 | 可选必选说明：条件可选参数<br>参数含义：该参数用于配置CHR在<br>ucf<br>上进行存储策略的选择。<br>前提条件：该参数在<br>“CHR存储开关”<br>参数配置为<br>“ON(开)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>- “STORE_ONLY(仅存储)”<br>- “STORE_AND_SEND(存储和转发)”<br>系统初始设置值：<br>“STORE_ONLY(仅存储)”<br>配置原则：<br>- 全量CHR单据只需要在ucf上进行存储，不需要ucf发送给CloudUDN的时候，选择“STORE_ONLY(仅存储)”。<br>- 全量CHR单据需要在ucf上进行存储，同时需要ucf发送给CloudUDN的时候，选择“STORE_AND_SEND(存储和转发)”。 |

#### [使用实例](#ZH-CN_MMLREF_0000001126145616)

配置CHR单据在 ucf 上的存储策略： “CHR存储开关” 设置为 “ON(开)” ， “存储类型” 设置为 “STORE_ONLY(仅存储)” 。

SET CHRSTORECFG: STOREALLFLAG=ON, STOREALLTYPE=STORE_ONLY;
