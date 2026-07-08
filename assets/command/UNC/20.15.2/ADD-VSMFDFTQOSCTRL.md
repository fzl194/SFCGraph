---
id: UNC@20.15.2@MMLCommand@ADD VSMFDFTQOSCTRL
type: MMLCommand
name: ADD VSMFDFTQOSCTRL（增加VSMF的Default QoS Flow配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: VSMFDFTQOSCTRL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- VSMF QoS管理
- VPLMN QoS协商
status: active
---

# ADD VSMFDFTQOSCTRL（增加VSMF的Default QoS Flow配置）

## 功能

**适用NF：SMF**

该命令用来增加V-SMF的Default QoS Flow配置。在V-SMF插入或改变流程中，V-SMF会将本地配置的Default QoS Flow参数，通过信元VplmnQoS发送给H-SMF，H-SMF再将VplmnQoS透传给PCF。PCF收到VplmnQos携带的QoS参数之后，经过跟本地签约的QoS参数协商之后，正式下发Default QoS Flow的Qos参数给H-SMF，H-SMF再下发给V-SMF。V-SMF收到H-SMF返回的QoS参数之后，跟本地配置的Default Qos参数进行比较，如果H-SMF传递的QoS参数超出预置范围（如5QI不在允许列表、Session-AMBR超出最大值等），V-SMF按QoS协商失败处理，拒绝V-SMF插入或改变流程。

## 注意事项

- 命令执行后只对新接入用户生效。

- 最多可输入2048条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成QoS控制的移动国家码信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成QoS控制的移动网号信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |
| CTRLTYPE | 控制类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS控制的类型。<br>数据来源：全网规划<br>取值范围：<br>- DNN_LEVEL（DNN级别）<br>- GLOBAL_LEVEL（整系统级别）<br>默认值：无<br>配置原则：无 |
| DNN | DNN | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。<br>默认值：无<br>配置原则：无 |
| DFTQOSTYPE | 缺省QoS类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组成QoS控制的缺省QoS类型。<br>数据来源：全网规划<br>取值范围：<br>- NONGBR（Non-GBR）<br>- GBR（GBR）<br>默认值：无<br>配置原则：无 |
| QOS5QI | 标准5QI | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成QoS控制的5QI。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~9，65~67，69~76，79~80，82~86。<br>默认值：无<br>配置原则：无 |
| ARPPL | ARP的优先级别 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的ARP优先级。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~15。<br>默认值：10<br>配置原则：无 |
| ARPPCI | ARP的抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的ARP抢占能力。<br>数据来源：全网规划<br>取值范围：<br>- NOT_PREEMPT（不抢占）<br>- MAY_PREEMPT（抢占）<br>默认值：NOT_PREEMPT<br>配置原则：无 |
| ARPPVI | ARP的被抢占能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的ARP被抢占能力。<br>数据来源：全网规划<br>取值范围：<br>- NOT_PREEMPTABLE（不可抢占）<br>- PREEMPTABLE（可抢占）<br>默认值：PREEMPTABLE<br>配置原则：无 |
| AMBRUL | 上行Session AMBR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的上行Session AMBR。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：10000000<br>配置原则：无 |
| AMBRDL | 下行Session AMBR(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定组成QoS控制的下行Session AMBR。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：10000000<br>配置原则：无 |
| MFBRUL | 上行最大速率 (千比特/秒) | 可选必选说明：该参数在"DFTQOSTYPE"配置为"GBR"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的上行最大速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：无 |
| MFBRDL | 下行最大速率 (千比特/秒) | 可选必选说明：该参数在"DFTQOSTYPE"配置为"GBR"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的下行最大速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：无 |
| GFBRUL | 上行保证速率 (千比特/秒) | 可选必选说明：该参数在"DFTQOSTYPE"配置为"GBR"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的上行保证速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：无 |
| GFBRDL | 下行保证速率 (千比特/秒) | 可选必选说明：该参数在"DFTQOSTYPE"配置为"GBR"时为条件必选参数。<br>参数含义：该参数用于指定组成QoS控制的GBR QoS Flow的下行保证速率。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~65000000。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [VSMF的Default QoS Flow配置（VSMFDFTQOSCTRL）](configobject/UNC/20.15.2/VSMFDFTQOSCTRL.md)

## 使用实例

- 如果想实现同一个PLMN的所有DNN都采用相同的QoS策略，执行如下命令：
  ```
  ADD VSMFDFTQOSCTRL: MCC="460", MNC="00", CTRLTYPE=GLOBAL_LEVEL, DFTQOSTYPE=NONGBR, QOS5QI=5, ARPPL=1, ARPPCI=NOT_PREEMPT, ARPPVI=PREEMPTABLE, AMBRUL=1000, AMBRDL=1000;
  ```
- 如果还想实现对同一个PLMN内特定DNN（例如ims）采用特殊的QoS策略，执行如下命令：
  ```
  ADD VSMFDFTQOSCTRL: MCC="460", MNC="00", CTRLTYPE=DNN_LEVEL, DNN="ims", DFTQOSTYPE=NONGBR, QOS5QI=9, ARPPL=1, ARPPCI=MAY_PREEMPT, ARPPVI=PREEMPTABLE, AMBRUL=1000, AMBRDL=1000;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加VSMF的Default-QoS-Flow配置（ADD-VSMFDFTQOSCTRL）_81785814.md`
