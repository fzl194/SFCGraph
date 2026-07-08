# IP Diff-Serv到3GPP QoS映射

UNC 支持从IP Diff-Serv到3GPP QoS的映射。所有进入 UNC 的报文，其外部优先级标记（如DSCP）都被映射为内部优先级（以Diff-Serv的服务等级和颜色表示）； UNC 发出报文时，将内部优先级映射为外部优先级。

3GPP QoS参数可以映射到DSCP值，映射是可配置的。

- UMTS QoS参数与DSCP的映射
  UMTS分组网络在接入IP承载网时，UNC通过UMTS QoS参数到IP DiffServ的映射来保证与IP承载网中QoS策略的一致性，缺省映射关系如 [表1](#ZH-CN_TOPIC_0166859960__tab001) 所示。
  *表1 UMTS QoS参数到DSCP的映射关系表*

  | UMTS QoS参数 | UMTS QoS参数 | UMTS QoS参数 | UMTS QoS参数 | DSCP |
  | --- | --- | --- | --- | --- |
  | Traffic Class | 通信处理优先级 | 信令传输优化 | 源统计描述符 | DSCP |
  | 会话类 | - | - | speech | EF |
  | 会话类 | - | - | unknown | AF31 |
  | 流类 | - | - | unknown | AF31 |
  | 流类 | - | - | unknown | AF41 |
  | 交互类 | 1 | 是 | - | EF |
  | 交互类 | 1 | 否 | - | AF21 |
  | 交互类 | 2 | 否 | - | AF21 |
  | 交互类 | 3 | 否 | - | AF11 |
  | 背景类 | - | - | - | BE |
  *表2 R99 QoS、ARP与DSCP的缺省映射关系（GU QoS）*

  | Traffic Class | ARP Value | ARP Value | ARP Value | ARP Value |
  | --- | --- | --- | --- | --- |
  | Traffic Class | 1 | 2 | 3 | Universal |
  | Conversation | EF | EF | EF | EF |
  | StreamingGBR(More25Kbps) | AF31 | AF31 | AF31 | AF31 |
  | StreamingGBR(Less25KbpsStreamingGBRLess25Kbps) | AF31 | AF31 | AF31 | AF31 |
  | InteractiveTrafficPri1 | AF11 | AF11 | AF11 | AF11 |
  | InteractiveTrafficPri2 | AF12 | AF12 | AF12 | AF12 |
  | InteractiveTrafficPri3 | AF13 | AF13 | AF13 | AF13 |
  | Background | BE | BE | BE | BE |
- QCI/5QI与DSCP的映射
  EPS/5GC分组网络在接入IP承载网时， UNC 通过QCI/5QI到IP DiffServ的映射来保证与IP承载网中QoS策略的一致性，缺省映射关系如 [表3](#ZH-CN_TOPIC_0166859960__tab01) 所示。
  *表3 QCI/5QI、ARP与DSCP的缺省映射关系（EPS/5GC QoS）*

  | QCI/5QI Value | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level | ARP Priority Level |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | QCI/5QI Value | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
  | 1 | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF |
  | 2 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 |
  | 3 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 | AF31 |
  | 4 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 | AF41 |
  | 5 | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF | EF |
  | 6 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 |
  | 7 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 | AF21 |
  | 8 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 | AF11 |
  | 9 | BE | BE | BE | BE | BE | BE | BE | BE | BE | BE | BE | BE | BE | BE | BE |
  UNC 支持9类标准QCI/5QI业务类型，可为不同的用户提供具有差异性的业务：

  - QCI/5QI为1类和5类的业务，以EF方式转发。
    - QCI/5QI为2、3、4、6、7和8类的业务，以AF方式转发。
    - QCI/5QI为9类的业务，以BE方式转发。
