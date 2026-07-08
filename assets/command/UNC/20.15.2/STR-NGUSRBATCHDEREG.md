---
id: UNC@20.15.2@MMLCommand@STR NGUSRBATCHDEREG
type: MMLCommand
name: STR NGUSRBATCHDEREG（启动批量去注册任务）
nf: UNC
version: 20.15.2
verb: STR
object_keyword: NGUSRBATCHDEREG
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 用户数据库管理
status: active
---

# STR NGUSRBATCHDEREG（启动批量去注册任务）

## 功能

![](启动批量去注册任务（STR NGUSRBATCHDEREG）_35636469.assets/notice_3.0-zh-cn_2.png)

当批量去注册用户时，CPU和内存使用率会升高，和周边网元交互消息量增大，待去注册完成后，系统会恢复正常。

若修改默认扫描速率(每DS 1个/秒)，请联系华为技术支持，根据系统负荷评估批量去注册的速率。

**适用NF：AMF**

该命令用于启动批量去注册任务。

## 注意事项

- 该命令执行后立即生效。

- 该命令只去注册当前系统已有用户，即不会去注册该命令下发之后新注册的用户。
- 该命令不会限制用户再次注册，如果启动批量去注册任务后，不希望用户再次注册到本系统，需要增加接入限制相关配置。
- 该命令执行后开始扫描用户，当用户为eDRX用户且不在寻呼窗口时，AMF执行隐式去注册流程。
- 连续执行STR NGUSRBATCHDEREG命令，会停止原去注册任务，执行新的去注册任务。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RMVTYPE | 删除类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定识别去注册用户的条件类型。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（无条件类型）”：无条件去注册全部用户。<br>- “PEER_NODE_TYPE（对端网元类型）”：按对端网元类型去注册用户。<br>- “DNN_SNSSAI（DNN和SNSSAI）”：用户的DNN和SNSSAI满足配置条件则去注册用户。<br>- “TAIRANGE（TAI范围）”：用户当前位置在配置的TAI范围内则去注册用户。<br>- “HOMEPLMN（归属地PLMN）”：用户的归属地PLMN满足配置条件则去注册用户。<br>默认值：无<br>配置原则：无 |
| NODETYPE | 对端网元类型 | 可选必选说明：该参数在"RMVTYPE"配置为"PEER_NODE_TYPE"时为条件必选参数。<br>参数含义：该参数用于指定去注册用户所在的对端网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “UDM（UDM）”：UDM<br>默认值：无<br>配置原则：无 |
| NFID | NF实例标识 | 可选必选说明：该参数在"RMVTYPE"配置为"PEER_NODE_TYPE"时为条件必选参数。<br>参数含义：该参数用于指定去注册用户所在的NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>可以通过执行DSP NFCACHE命令，查询指定NF类型对应的NF实例标识。 |
| MATCHTYPE | DNN和SNSSAI的匹配方式 | 可选必选说明：该参数在"RMVTYPE"配置为"DNN_SNSSAI"时为条件必选参数。<br>参数含义：该参数用于指定按DNN_SNSSAI去注册用户时的DNN和SNSSAI的匹配方式。<br>数据来源：全网规划<br>取值范围：<br>- “MATCH_BY_SUBDATA（按签约数据匹配DNN和SNSSAI）”：用户签约的DNN和SNSSAI满足配置条件，则去注册用户。<br>- “MATCH_BY_PDUSESSION（按PDU会话匹配DNN和SNSSAI）”：用户PDU会话使用的DNN和SNSSAI满足配置条件，则去注册用户。<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"RMVTYPE"配置为"DNN_SNSSAI"时为条件必选参数。<br>参数含义：该参数用于指定按DNN_SNSSAI去注册用户时的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>“*”表示通配符，如果DNN为“*”，表示不限定DNN作为去注册条件。 |
| ISNSSAI | 是否匹配S-NSSAI | 可选必选说明：该参数在"RMVTYPE"配置为"DNN_SNSSAI"时为条件必选参数。<br>参数含义：该参数用于指定按DNN_SNSSAI去注册用户时是否匹配S-NSSAI。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：<br>设置为“YES”时，匹配S-NSSAI和DNN。<br>设置为“NO”时，仅匹配DNN。 |
| SST | 切片业务类型 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件必选参数。<br>参数含义：该参数用于指定按DNN_SNSSAI去注册用户时的网络切片的业务类型信息。<br>网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识是可选的。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：该参数在"ISNSSAI"配置为"YES"时为条件可选参数。<br>参数含义：该参数用于指定按DNN_SNSSAI去注册用户时的切片细分标识。<br>网络切片标识（S-NSSAI）由切片业务类型（SST）和切片细分标识（SD）两部分组成，其中切片细分标识是可选的。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该值若不设置，默认值为FFFFFF。表示按DNN_SNSSAI去注册用户时不匹配SD。 |
| MCC | 移动国家码 | 可选必选说明：该参数在"RMVTYPE"配置为"TAIRANGE"时为条件必选参数。<br>参数含义：该参数用于指定按TAIRANGE去注册用户时TAI范围的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。本参数由3个十进制数字组成。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：该参数在"RMVTYPE"配置为"TAIRANGE"时为条件必选参数。<br>参数含义：该参数用于指定按TAIRANGE去注册用户时TAI范围的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。本参数由2~3个十进制数字组成。<br>默认值：无<br>配置原则：无 |
| TACSTART | TAC起始号段 | 可选必选说明：该参数在"RMVTYPE"配置为"TAIRANGE"时为条件必选参数。<br>参数含义：该参数用于指定按TAIRANGE去注册用户时TAC的起始号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。<br>默认值：无<br>配置原则：<br>TAC的终止号段需要不小于TAC的起始号段。 |
| TACEND | TAC终止号段 | 可选必选说明：该参数在"RMVTYPE"配置为"TAIRANGE"时为条件必选参数。<br>参数含义：该参数用于指定按TAIRANGE去注册用户时TAC的终止号段。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。采用十六进制表示（无须输入“0x”前缀），只能由数字（0-9），字母（A-F、a-f）组成。<br>默认值：无<br>配置原则：<br>TAC的终止号段需要不小于TAC的起始号段。 |
| HOMEMCC | 归属地移动国家码 | 可选必选说明：该参数在"RMVTYPE"配置为"HOMEPLMN"时为条件必选参数。<br>参数含义：该参数用于指定按HOMEPLMN去注册用户时，用户归属地的移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。本参数由3个十进制数字组成。<br>默认值：无<br>配置原则：无 |
| HOMEMNC | 归属地移动网号 | 可选必选说明：该参数在"RMVTYPE"配置为"HOMEPLMN"时为条件必选参数。<br>参数含义：该参数用于指定按HOMEPLMN去注册用户时，用户归属地的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。本参数由2~3个十进制数字组成。<br>默认值：无<br>配置原则：无 |
| SCANRATE | 扫描速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定DS每秒扫描的用户数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~20，单位是个每秒。<br>默认值：1<br>配置原则：<br>DS个数 × 扫描速率 = 整系统扫描速率。<br>DS个数来源于如下命令输出结果中记录个数：<br>DSP FRAMEDBG: DBGSTR="UeamCtrlSvc coordinator all";<br>如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。 |
| DEREGTYPE | 去注册类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户的去注册类型。<br>数据来源：全网规划<br>取值范围：<br>- “REREG_REQ（需要重新注册）”：用户需要重新注册。<br>- “REREG_NOTREQ（无需重新注册）”：用户无需重新注册。<br>默认值：REREG_NOTREQ<br>配置原则：无 |
| DEREGCAUSE | 去注册原因值 | 可选必选说明：该参数在"DEREGTYPE"配置为"REREG_NOTREQ"时为条件可选参数。<br>参数含义：该参数用于指定用户去注册的原因值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~111。<br>默认值：111<br>配置原则：<br>参数取值为0，表示不使用特殊指定原因值，发起去注册时系统将默认下发#111（Protocol error unspecified）原因值。<br>去注册原因对终端行为的影响参见协议3GPP TS 24.501 Network-initiated de-registration procedure completion by the UE章节描述。<br>具体终端的响应行为可能会随终端品牌和型号有所不同。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGUSRBATCHDEREG]] · 批量去注册任务（NGUSRBATCHDEREG）

## 使用实例

部分地市UDM故障情况下，为了保证用户业务正常进行，AMF需要快速触发用户回到4G，可以针对归属故障UDM的用户启动批量去注册任务。筛选去用户的扫描速率为1个/秒，执行如下命令：

```
STR NGUSRBATCHDEREG:RMVTYPE=PEER_NODE_TYPE,SCANRATE=1,DEREGTYPE=REREG_NOTREQ,DEREGCAUSE=27,NODETYPE=UDM,NFID="udm_instance_0";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/STR-NGUSRBATCHDEREG.md`
