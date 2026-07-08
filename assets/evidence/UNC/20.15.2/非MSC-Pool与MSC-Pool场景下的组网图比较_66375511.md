# 非MSC Pool与MSC Pool场景下的组网图比较

非MSC Pool场景下的CSFB组网如 [图1](#ZH-CN_TOPIC_0166375511__fig_01) 所示。

**图1** 非MSC Pool场景下的组网图

<br>

![](非MSC Pool与MSC Pool场景下的组网图比较_66375511.assets/zh-cn_image_0170797311_2.png "点击放大")

> **说明**
> [图1](#ZH-CN_TOPIC_0166375511__fig_01) 中MSC需要支持CSFB。

[图1](#ZH-CN_TOPIC_0166375511__fig_01) 描述了非MSC Pool场景下的CSFB组网图，其中包括两个位置区LA11、LA21，六个属于同一MME下的Tracking area：TA11、TA12、TA13、TA21、TA22、TA23。 TA11、TA12、TA13属于一个TA list，TA21、TA22、TA23属于一个TA list。

MSC Pool场景下的CSFB组网图，如 [图2](#ZH-CN_TOPIC_0166375511__fig_02) 所示。

**图2** MSC Pool场景下的组网图

<br>

![](非MSC Pool与MSC Pool场景下的组网图比较_66375511.assets/zh-cn_image_0170793258_2.png "点击放大")

[图2](#ZH-CN_TOPIC_0166375511__fig_02) 描述了MSC Pool场景下的CSFB组网图，共包括一个位置区LA1，三个属于同一MME下的Tracking area：TA1、TA2、TA3。TA1、TA2、TA3同属于一个TA list。

如 [图1](#ZH-CN_TOPIC_0166375511__fig_01) 与 [图2](#ZH-CN_TOPIC_0166375511__fig_02) 所示可以看出，MSC Pool场景下与非MSC Pool场景下对MSC要求不同，具体差异如 [表1](#ZH-CN_TOPIC_0166375511__table_05) 所示。

*表1 MSC Pool场景下与非MSC Pool场景下对MSC要求的差异*

| 组网场景 | 对MSC的要求 |
| --- | --- |
| 非MSC POOL | 所有的MSC都需要升级支持CSFB。 |
| MSC POOL | 在MSC pool中，支持CSFB的MSC可以服务于整个MSC pool内，因此通过部署MSC Pool可实现避免全网MSC升级支持CSFB。MSC pool场景下，至少需要升级两个MSC支持CSFB。如<br>[图2](#ZH-CN_TOPIC_0166375511__fig_02)<br>中由5个MSC组成的Pool中仅两个MSC升级支持CSFB，即与MME有SGs连接的两个MSC。 |
