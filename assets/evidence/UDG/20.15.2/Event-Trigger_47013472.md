# Event Trigger

PCC架构中定义了Event Trigger，当相应事件发生时，PGW-C/SMF触发对应Event Trigger，并向PCRF/PCF申请更新策略。PGW-C/SMF支持通过URR（使用量上报规则）设置PGW-U/UPF的上报事件触发点如 [表1](Event Trigger_47013472.md#ZH-CN_TOPIC_0147013472__table0587115364813) 所示。

*表1 网络使用的Event Trigger*

| Event Trigger | 含义 | 关联IE |
| --- | --- | --- |
| PERIO (Periodic Reporting) | UPF基于PGW-C/SMF下发的URR中定义的测量周期定时发起上报流程。 | Measurement Period |
| VOLTH (Volume Threshold) | UPF基于PGW-C/SMF下发的URR中定义的流量阈值，在业务使用量超过阈值时发起上报流程。 | Volume Threshold |
| TIMTH (Time Threshold) | UPF基于PGW-C/SMF下发的URR中定义的时长阈值，在业务使用时长超过阈值时发起上报流程。 | Time Threshold |
| QUHTI (Quota Holding Time) | UPF基于PGW-C/SMF下发的URR中定义的配额保持时间，在配额下发时长超过阈值时发起上报流程。 | Quota Holding Time |
| START (Start of Traffic) | UPF基于PGW-C/SMF下发的URR中定义的业务开始Trigger，在感知到业务开始时发起上报流程。 | NA |
| STOPT (Stop of Traffic) | UPF基于PGW-C/SMF下发的URR中定义的业务结束Trigger，在感知到业务结束时发起上报流程。 | NA |
| DROTH (Dropped DL Traffic Threshold) | UPF基于PGW-C/SMF下发的URR中定义的下行业务丢包阈值，在因下行缓存超规格丢包数超过阈值时发起上报流程。 | Dropped DL Traffic Threshold |
| LIUSA (Linked Usage Reporting) | UPF基于PGW-C/SMF下发的URR中定义的关联URR ID，在关联URR因故发起上报时协同触发上报。 | Linked URR ID |
| VOLQU (Volume Quota) | UPF基于PGW-C/SMF下发的URR中定义的流量配额，在业务使用量配额耗尽时发起上报流程。 | Volume Quota |
| TIMQU (Time Quota) | UPF基于PGW-C/SMF下发的URR中定义的时长阈值，在业务使用时长配额耗尽时发起上报流程。 | Time Quota |
| ENVCL (Envelope Closure) | UPF基于PGW-C/SMF下发的URR中定义的信封测量周期，在信封关闭时发起上报流程。 | NA |
| MACAR (MAC Addresses Reporting) | UPF基于PGW-C/SMF下发的URR中定义的MAC地址上报信息，在检测UE发起的上行报文的源MAC地址时发起上报流程。 | NA |
| EVETH (Event Threshold) | UPF基于PGW-C/SMF下发的URR中定义的事件阈值，在业务使用的事件数超过事件阈值时发起上报流程。 | Event Information |
