# 设置QBC计费全局参数（SET QBCGLBPARA）

- [命令功能](#ZH-CN_MMLREF_0000001181248674__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001181248674__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001181248674__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001181248674__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001181248674)

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置QBC计费全局参数。

## [注意事项](#ZH-CN_MMLREF_0000001181248674)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| QFSTARTRPT | QFTRIGGERFILL | QFTIMECALC |
| --- | --- | --- |
| NOREPORT | DISABLE | PACKETTRIGGERED |

#### [操作用户权限](#ZH-CN_MMLREF_0000001181248674)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001181248674)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QFSTARTRPT | 激活阶段QoSFlow上报模式 | 可选必选说明：可选参数<br>参数含义：控制用户激活阶段是否上报QoSFlow信息给CHF。<br>数据来源：本端规划<br>取值范围：<br>- “NOREPORT（不上报）”：用户激活时不上报QoSFlow信息。<br>- “REPORT（上报）”：用户激活时上报QoSFlow信息。<br>- “ONLYRPTDFTQF（仅缺省QoSFlow上报）”：用户激活时仅上报缺省QoSFlow信息。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QBCGLBPARA查询当前参数配置值。<br>配置原则：无 |
| QFTRIGGERFILL | QoSFlow级Trigger填写方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置当仅对PDU会话有效的Trigger发生时，生成的QFI容器是否携带同PDU会话一样的Trigger。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE（不使能）”：当仅对PDU会话有效的Trigger发生时，生成的QosFlow容器中不携带同PDU会话一样的Trigger<br>- “ENABLE（使能）”：当仅对PDU会话有效的Trigger发生时，生成的QosFlow容器中携带同PDU会话一样的Trigger<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QBCGLBPARA查询当前参数配置值。<br>配置原则：<br>缺省时，SMF按Trigger的实际生效粒度携带在PDU会话级或QoSFlow级。<br>当CHF期望在仅对PDU会话有效的Trigger发生且无QoSFlow级Trigger发生时，生成的QFI容器中也携带同PDU会话一样的Trigger，可以使能该功能。 |
| QFTIMECALC | QoSFlow时长计算方式 | 可选必选说明：可选参数<br>参数含义：该参数用于设置CP指示UP QoSFlow的时长计费方式。<br>数据来源：本端规划<br>取值范围：<br>- “PACKETTRIGGERED（PACKETTRIGGERED）”：统计周期内收到第一个数据包到最后一个数据包的时长<br>- “CONTINUOUS（CONTINUOUS）”：从收到URR开始计算连续时长<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST QBCGLBPARA查询当前参数配置值。<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001181248674)

配置激活阶段QoSFlow上报模式为上报：

```
SET QBCGLBPARA: QFSTARTRPT=REPORT;
```
