# SGsAP链路异常场景下的CSFB业务恢复

当MME检测到SGsAP链路异常会发起尝试建链，多次尝试都无法成功建链后，上报 **ALM-80597 SGsAP链路故障** 告警；当MME与MSC/VLR的链路全部故障时，上报 **ALM-14033 SGs口对端不可达** 告警，同时启动自动迁移，将该MSC上的用户迁移到其他正常的MSC上。

自动迁移阶段：

- 触发自动迁移，识别归属于不可用MSC上的用户，MME下发“IMSI detach”类型的detach请求 ，在用户重新联合TAU时，MME将该用户选择到其他的MSC上，实现用户迁移。

当SGsAP链路恢复，MME停止自动迁移，系统启动回退过程。在UE发起联合附着、周期跟踪区更新、联合TAU时，系统强制执行Location Update更新，并且MME将已迁移到其他MSC上的UE重新分配到原MSC上。

自动迁移用户和回退过程如 [图1](#ZH-CN_TOPIC_0166375515__fig3) 所示。

**图1** 自动迁移用户和回退过程

<br>

![](SGsAP链路异常场景下的CSFB业务恢复_66375515.assets/zh-cn_image_0170800266_2.png "点击放大")
