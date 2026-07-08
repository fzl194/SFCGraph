---
id: UNC@20.15.2@MMLCommand@LST DEACTQFPLCY
type: MMLCommand
name: LST DEACTQFPLCY（查询去活用户面专有QoS Flow策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DEACTQFPLCY
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话策略管理
- 5GC QoS Flow管理拓展功能
status: active
---

# LST DEACTQFPLCY（查询去活用户面专有QoS Flow策略）

## 功能

**适用NF：SMF**

该命令用于查询去活用户面专有QoS Flow策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGAPCAUSEGROUP | NgApCause组 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF接收到的AMF发送的去激活用户面请求消息中携带的NGAP原因值组。原因值组定义参考3GPP TS 38.413中Cause的定义。<br>数据来源：本端规划<br>取值范围：<br>- RADIO_NETWORK（Radio Network Layer）<br>- TRANSPORT（Transport Layer）<br>- NAS（NAS）<br>- PROTOCOL（Protocol）<br>- MISC（Miscellaneous）<br>- INVALID（未携带）<br>默认值：无<br>配置原则：无 |
| NGAPCAUSEVALUE | NgApCause值 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF接收到的AMF发送的去激活用户面请求消息中携带的NGAP原因值。参考3GPP TS 38.413中Cause定义。<br>当NGAPCAUSEGROUP值为RADIO_NETWORK时，值如下：<br>0-未指定。<br>1-TXnRELOCOverall超时。<br>2-Handover成功。<br>3-NG-RAN产生原因释放。<br>4-5GC产生原因释放。<br>5-切换取消。<br>6-部分切换。<br>7-目标5GC/NG-RAN节点或目标系统切换失败。<br>8-切换目标不允许。<br>9-TNGRELOCoverall超时。<br>10-TNGRELOCprep超时。<br>11-小区不可用。<br>12-未知目标ID。<br>13-目标小区无可用无线资源。<br>14-未知的本地UE NGAP ID。<br>15-远端UE NGAP ID不一致。<br>16-由于无线原因需要切换。<br>17-时间关键原因切换。<br>18-资源优化切换。<br>19-降低服务小区负载。<br>20-用户不活动。<br>21-UE无线连接丢失。<br>22-无线资源不可用。<br>23-QoS组合非法。<br>24-无线接口流程失败。<br>25-与其他流程交互。<br>26-未知PDU会话ID。<br>27-未知的QoS流ID。<br>28-PDU会话ID多实例。<br>29-QoS Flow ID多实例。<br>30-不支持加密算法和/或完整性保护算法。<br>31-NG系统内切换触发。<br>32-NG系统间切换触发。<br>33-Xn切换触发。<br>34-不支持5QI值。<br>35-用户上下文迁移。<br>36-IMS语音EPS回落或RAT回落触发。<br>37-UP完整性保护无法实现。<br>38-UP保密保护无法实现。<br>39-切片不支持。<br>40-UE处于RRC_INACTIVE状态不可达。<br>41-重定向。<br>42-切片下资源不可用。<br>43-UE最大完整性保护速率原因。<br>44-核心网检测到移动性导致的释放。<br>当NGAPCAUSEGROUP值为TRANSPORT时，值如下：<br>0-传输资源不可用。<br>1-未指定。<br>当NGAPCAUSEGROUP取值为NAS时，值如下：<br>0-正常释放。<br>1-认证失败。<br>2-注销。<br>3-未指定。<br>当NGAPCAUSEGROUP值为PROTOCOL时，值如下：<br>0-传输语法错误。<br>1-抽象语法错误（拒绝）。<br>2-抽象语法错误（忽略和通知）。<br>3-消息与接收方状态不兼容。<br>4-语义错误。<br>5-抽象语法错误（构造错误消息）。<br>6-未指定。<br>当NGAPCAUSEGROUP取值为MISC时，值如下：<br>0-控制处理过载。<br>1-用户面处理资源不足。<br>2-硬件故障。<br>3-运维干预。<br>4-未知PLMN。<br>5-未指定。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>当NGAPCAUSEGROUP值为INVALID时，本参数值只能输入0。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEACTQFPLCY]] · 去活用户面专有QoS Flow策略（DEACTQFPLCY）

## 使用实例

查询去活用户面专有QoS Flow策略，执行命令如下：

```
LST DEACTQFPLCY:;
RETCODE = 0  操作成功

结果如下
--------
NgApCause值  专有GBR类型QoS Flow处理策略  延迟释放专有GBR类型QoS Flow时长(秒)  NgApCause组          

20           不释放专有QoS Flow           10                                   Radio Network Layer  
41           不释放专有QoS Flow           10                                   Radio Network Layer  
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询去活用户面专有QoS-Flow策略（LST-DEACTQFPLCY）_92022694.md`
