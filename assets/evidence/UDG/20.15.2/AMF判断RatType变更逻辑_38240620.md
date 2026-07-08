# AMF判断RatType变更逻辑

RedCap用户在接入过程中，会涉及到能力变更的场景，原因如下：

- AMF上RedCap功能开关发生变化。
- 切换AMF时，老侧AMF上下文中携带RedCap指示位信息变化。
- 用户接入核心网时，gNodeB带给AMF的RedCap指示位信息变化。

AMF会结合以上三种原因，对RaTtype是否发生变化进行判断。具体判断逻辑如 [表1 AMF判断RatType是否变化场景](#ZH-CN_TOPIC_0000001538240620__table928154213598) 所示。对于连接态会话，AMF随流程消息通知SMF；对于空闲态会话，AMF通知SMF策略受 **SET AMFREDCAPFUNC** 的参数 **NTYSMFPLCY** 控制，与RedCap功能开关无关。

*表1 AMF判断RatType是否变化场景*

| 输入条件1：<br>设置新侧AMF RedCap功能开关（<br>**SET AMFREDCAPFUNC**<br>） | 输入条件2：<br>老侧AMF是否向新侧AMF传递RedCap指示位 | 输入条件3：<br>HANDOVER REQUEST ACKNOWLEDGE/INITIAL UE MESSAGE/PATH SWITCH REQUEST是否携带RedCap Indication信元 | 新侧AMF针对RatType取值的判断结果 | 核心网处理逻辑 |
| --- | --- | --- | --- | --- |
| 关 | YES | 携带 | RedCap->NR | 新侧AMF和周边网元将用户当作普通NR处理。 |
| 关 | NO | 不携带 | RedCap->NR | 新侧AMF和周边网元将用户当作普通NR处理。 |
| 关 | NO（老侧AMF不支持RedCap） | 携带 | 保持NR | 新侧AMF不感知RatType变更，和周边网元仍将用户作NR处理。 |
| 关 | NO（老侧AMF不支持RedCap） | 不携带 | 保持NR | 新侧AMF和周边网元将用户当作普通NR处理。 |
| 开 | YES | 携带 | 保持RedCap | RatType不变更，AMF和SMF不需要向周边网元更新。 |
| 开 | YES | 不携带 | RedCap->NR | 发生RatType变更，AMF和SMF在后续流程中会通知周边网元。 |
| 开 | NO | 不携带 | 保持NR | 此为普通NR用户切换，无特殊处理。 |
| 开 | NO（老侧AMF不支持RedCap） | 携带 | NR->RedCap | 发生RatType变更，AMF和SMF在后续流程中会通知周边网元。 |
