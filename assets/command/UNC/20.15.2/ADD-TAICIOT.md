---
id: UNC@20.15.2@MMLCommand@ADD TAICIOT
type: MMLCommand
name: ADD TAICIOT（增加CIoT能力配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: TAICIOT
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
max_records: 10000
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- CIoT能力配置
status: active
---

# ADD TAICIOT（增加CIoT能力配置）

## 功能

**适用网元：MME**

该命令用于增加指定TAI下eNodeB支持的CIoT能力。用于NB-IoT用户接入时获取eNodeB支持的CIoT能力。

## 注意事项

- 该命令执行后，在用户新的Attach/TAU流程中系统才会识别eNodeB的蜂窝物联网（CIoT）能力。
- 该表最大记录数为10000。
- 组网规划时，同一TAI范围内所有eNodeB的蜂窝物联网（CIoT）能力必须相同，否则在MME内无法配置eNodeB的CIoT能力，可能因CIoT能力协商失败进而导致承载建立失败。
- 如果某一TAI不在本配置中，且该TAI下某一eNodeB携带的RAT TYPE为NB-IoT，则默认该TAI下的所有eNodeB均支持CP CIoT。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEGINTAI | 起始TAI | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个起始跟踪区。<br>数据来源：全网规划<br>取值范围：9～10位的字符串。<br>默认值：无<br>配置原则：<br>- 起始TAI由MCC，MNC，TAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足补0。<br>- 需要统一配置系统中所有eNodeB CIoT能力时，则输入的TAI为“FFFFFFFFFF”。 |
| ENDTAI | 终止TAI | 可选必选说明：可选参数<br>参数含义：该参数用于指定跟踪区标识，标识一个终止跟踪区。<br>数据来源：全网规划<br>取值范围：9～10位的字符串。<br>默认值：无<br>配置原则：<br>- 终止TAI由MCC，MNC，TAC组成。<br>- MCC为3个BCD码字符，MNC为2个或者3个BCD码字符，填写时请遵循实际长度。<br>- TAC编码为16进制数，固定为4位，不足补0。<br>- 输入参数“终止TAI”要大于或者等于“起始TAI”。<br>- 如果未输入“终止TAI”或者输入值等于“起始TAI”，则表示某个固定的TAI。 |
| NBDATATRANSSUPPORT | 窄带数据传输能力指示 | 可选必选说明：可选参数<br>参数含义：该参数用于指定所配置TAI范围内所有eNodeB支持窄带蜂窝物联网（NB CIoT）的能力。<br>数据来源：全网规划<br>取值范围：<br>- “SUPPORT_CP（支持CP CIoT）”<br>- “SUPPORT_UP（支持UP CIoT）”<br>- “SUPPORT_S1U（支持S1-U数据传输）”<br>默认值：无<br>配置原则:根据eNodeB能力配置此参数。如果勾选了<br>“SUPPORT_UP”<br>，则无论<br>“SUPPORT_S1U”<br>是否勾选，均按eNodeB支持S1–U数据传输进行处理。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@TAICIOT]] · CIoT能力配置（TAICIOT）

## 使用实例

假设用户需要配置TAI为308015101～308015201范围内eNodeB的窄带CIoT能力指示为支持CP CIoT：

ADD TAICIOT: BEGINTAI="308015101", ENDTAI="308015201",NBDATATRANSSUPPORT=SUPPORT_CP-1&SUPPORT_UP-0&SUPPORT_S1U-0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-TAICIOT.md`
