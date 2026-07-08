# 设置VoLTE AMR编解码的语音质量采用的评估方式（SET VOLTEMOSEVAL）

- [命令功能](#ZH-CN_CONCEPT_0000201463433475__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000201463433475__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000201463433475__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000201463433475__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000201463433475__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000201463433475)

**适用NF：PGW-U**

该命令用于设置VoLTE AMR编解码的语音质量采用的评估方式。

#### [注意事项](#ZH-CN_CONCEPT_0000201463433475)

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | EVALTYPE |
| --- | --- |
| 初始值 | POLQA_SWB_AMR |

#### [操作用户权限](#ZH-CN_CONCEPT_0000201463433475)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000201463433475)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EVALTYPE | 评估方式 | 可选必选说明：必选参数<br>参数含义：用于配置VoLTE AMR编解码的语音质量采用的评估方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- POLQA_SWB_AMR：UPF采用POLQA SWB拟合标准对AMR-WB和AMR-NB编解码的VoLTE语音业务进行MOS评估。<br>- POLQA_NB_AMR：UPF采用POLQA NB拟合标准对AMR-WB和AMR-NB编解码的VoLTE语音业务进行MOS评估。<br>- POLQA_SWB_AMRWB_NB_AMRNB：UPF采用POLQA SWB拟合标准对AMR-WB编解码的VoLTE语音业务进行MOS评估，采用POLQA NB拟合标准对AMR-NB编解码的VoLTE语音业务进行MOS评估。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0000201463433475)

设置UPF采用POLQA NB拟合标准对AMR-WB和AMR-NB编解码的VoLTE语音业务进行MOS评估：

```
SET VOLTEMOSEVAL: EVALTYPE=POLQA_NB_AMR;
```
