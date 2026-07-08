---
id: UNC@20.15.2@MMLCommand@SET DEFPRER8QOS
type: MMLCommand
name: SET DEFPRER8QOS（设置缺省的Pre-R8 QoS参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DEFPRER8QOS
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- 全局PreR8 QoS纠错
status: active
---

# SET DEFPRER8QOS（设置缺省的Pre-R8 QoS参数）

## 功能

**适用NF：GGSN**

该命令用于设置UNC的QoS参数。 这些参数决定了UNC能够为每个PDP上下文提供的QoS范围，关于这些参数的具体含义参见协议3GPP TS 23.107。对于各业务类型的相关QoS参数，如果UE请求的QoS属性值为非法值，协商值等于UNC配置的参数值，否则协商值等于请求值；对于各业务类型不涉及的QoS参数，协商值等于请求值。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 上行保证带宽不能大于上行最大带宽。
- 下行保证带宽不能大于下行最大带宽。
- 平均吞吐量不能大于最大吞吐量。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ARPVALUE | DELAYCLASS | DELIVERRORSDU | GBRDL | GBRUL | MAXSDU | MBRDL | MBRUL | MEANTHROUGHPUT | PEAKTHROUGHPUT | PRECEDENCE | RELIABCLASS | RESIDBERBACK | RESIDBERCONV | RESIDBERINT | RESIDBERSTRM | SDUERRRATIOBACK | SDUERRRATIOCONV | SDUERRRATIOINT | SDUERRRATIOSTRM | SIGNALIND | SRCSTATDESC | THP | TRAFFICCLASS | TRANSDELAY |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HIGH | 1 | NO_DETECT | 384 | 384 | 1520 | 384 | 384 | SPED_BESTEFFORT | UP_TO_256K | HIGH | 1 | PARA_6E_8 | PARA_1E_6 | PARA_6E_8 | PARA_1E_6 | PARA_1E_6 | PARA_1E_5 | PARA_1E_6 | PARA_1E_7 | OPTIMIZE | SPEECH | HIGH | CONVERSATIONAL | 10 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ARPVALUE | ARP值 | 可选必选说明：可选参数<br>参数含义：该参数用于设置ARP值。<br>数据来源：本端规划<br>取值范围：<br>- “HIGH（高）”：高优先级。<br>- “NORMAL（中）”：正常优先级。<br>- “LOW（低）”：低优先级。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| DELAYCLASS | 延迟等级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置延迟等级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| DELIVERRORSDU | 发送错误的SDU | 可选必选说明：可选参数<br>参数含义：该参数用于设置发送错误的SDU。<br>数据来源：本端规划<br>取值范围：<br>- “NO_DETECT（不检测）”：不检测错误。<br>- “ERR_DELIV（发送错误）”：发送错误的SDU。<br>- “ERR_NOT_DELIV（不发送错误）”：不发送错误的SDU。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| GBRDL | 下行保证带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置下行保证带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~256000，单位是千比特每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| GBRUL | 上行保证带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置上行保证带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~256000，单位是千比特每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| MAXSDU | 最大SDU长度(字节) | 可选必选说明：可选参数<br>参数含义：该参数用于设置最大SDU长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~1520。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| MBRDL | 下行最大带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置下行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~256000，单位是千比特每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| MBRUL | 上行最大带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置上行最大带宽。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~256000，单位是比特每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| MEANTHROUGHPUT | 平均吞吐量(字节/小时) | 可选必选说明：可选参数<br>参数含义：该参数用于设置平均吞吐量。<br>数据来源：本端规划<br>取值范围：<br>- “SPED_100B（100 字节每小时）”：100 字节每小时。<br>- “SPED_200B（200 字节每小时）”：200 字节每小时。<br>- “SPED_500B（500 字节每小时）”：500 字节每小时。<br>- “SPED_1K（1K字节每小时）”：1K字节每小时。<br>- “SPED_2K（2K字节每小时）”：2K字节每小时。<br>- “SPED_5K（5K字节每小时）”：5K字节每小时。<br>- “SPED_10K（10K字节每小时）”：10K字节每小时。<br>- “SPED_20K（20K字节每小时）”：20K字节每小时。<br>- “SPED_50K（50K字节每小时）”：50K字节每小时。<br>- “SPED_100K（100K字节每小时）”：100K字节每小时。<br>- “SPED_200K（200K字节每小时）”：200K字节每小时。<br>- “SPED_500K（500K字节每小时）”：500K字节每小时。<br>- “SPED_1M（1M字节每小时）”：1M字节每小时。<br>- “SPED_2M（2M字节每小时）”：2M字节每小时。<br>- “SPED_5M（5M字节每小时）”：5M字节每小时。<br>- “SPED_10M（10M字节每小时）”：10M字节每小时。<br>- “SPED_20M（20M字节每小时）”：20M字节每小时。<br>- “SPED_50M（50M字节每小时）”：50M字节每小时。<br>- “SPED_BESTEFFORT（尽力而为）”：最大能力。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| PEAKTHROUGHPUT | 最大吞吐量(字节/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置最大吞吐量。<br>数据来源：本端规划<br>取值范围：<br>- “UP_TO_1K（最大1k字节每秒）”：最大1k字节每秒。<br>- “UP_TO_2K（最大2k字节每秒）”：最大2k字节每秒。<br>- “UP_TO_4K（最大4k字节每秒）”：最大4k字节每秒。<br>- “UP_TO_8K（最大8k字节每秒）”：最大8k字节每秒。<br>- “UP_TO_16K（最大16k字节每秒）”：最大16k字节每秒<br>- “UP_TO_32K（最大32k字节每秒）”：最大32k字节每秒。<br>- “UP_TO_64K（最大64k字节每秒）”：最大64k字节每秒。<br>- “UP_TO_128K（最大128k字节每秒）”：最大128k字节每秒。<br>- “UP_TO_256K（最大256k字节每秒）”：最大256k字节每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| PRECEDENCE | 优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置优先级。<br>数据来源：本端规划<br>取值范围：<br>- “HIGH（高）”：高优先级。<br>- “NORMAL（中）”：正常优先级。<br>- “LOW（低）”：低优先级。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| RELIABCLASS | 可靠性等级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置可靠性等级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~5。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| RESIDBERBACK | Background业务残留比特误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置后台类业务残留比特误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_4E_3（4E-3）”：4E-3<br>- “PARA_1E_5（1E-5）”：1E-5<br>- “PARA_6E_8（6E-8）”：6E-8<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| RESIDBERCONV | Conversation业务残留比特误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置会话类业务残留比特误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_5E_2（5E-2）”：5E-2<br>- “PARA_1E_2（1E-2）”：1E-2<br>- “PARA_5E_3（5E-3）”：5E-3<br>- “PARA_1E_3（1E-3）”：1E-3<br>- “PARA_1E_4（1E-4）”：1E-4<br>- “PARA_1E_5（1E-5）”：1E-5<br>- “PARA_1E_6（1E-6）”：1E-6<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| RESIDBERINT | Interactive业务残留比特误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类业务残留比特误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_4E_3（4E-3）”：4E-3<br>- “PARA_1E_5（1E-5）”：1E-5<br>- “PARA_6E_8（6E-8）”：6E-8<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| RESIDBERSTRM | Streaming业务残留比特误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流类业务残留比特误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_5E_2（5E-2）”：5E-2<br>- “PARA_1E_2（1E-2）”：1E-2<br>- “PARA_5E_3（5E-3）”：5E-3<br>- “PARA_1E_3（1E-3）”：1E-3<br>- “PARA_1E_4（1E-4）”：1E-4<br>- “PARA_1E_5（1E-5）”：1E-5<br>- “PARA_1E_6（1E-6）”：1E-6<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| SDUERRRATIOBACK | Background业务SDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置后台类业务SDU误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_1E_3（1E-3）”：1E-3<br>- “PARA_1E_4（1E-4）”：1E-4<br>- “PARA_1E_6（1E-6）”：1E-6<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| SDUERRRATIOCONV | Conversation业务SDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置会话类业务SDU误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_1E_2（1E-2）”：1E-2<br>- “PARA_7E_3（7E-3）”：7E-3<br>- “PARA_1E_3（1E-3）”：1E-3<br>- “PARA_1E_4（1E-4）”：1E-4<br>- “PARA_1E_5（1E-5）”：1E-5<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| SDUERRRATIOINT | Interactive业务SDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置交互类业务SDU误码率。<br>数据来源：本端规划<br>取值范围：<br>- PARA_1E_3（1E-3）<br>- PARA_1E_4（1E-4）<br>- PARA_1E_6（1E-6）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| SDUERRRATIOSTRM | Streaming业务SDU误码率 | 可选必选说明：可选参数<br>参数含义：该参数用于设置流类业务SDU误码率。<br>数据来源：本端规划<br>取值范围：<br>- “PARA_1E_2（1E-2）”：1E-2<br>- “PARA_7E_3（7E-3）”：7E-3<br>- “PARA_1E_3（1E-3）”：1E-3<br>- “PARA_1E_4（1E-4）”：1E-4<br>- “PARA_1E_5（1E-5）”：1E-5<br>- “PARA_1E_7（1E-7）”：1E-7<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| SIGNALIND | 信令传输优化 | 可选必选说明：可选参数<br>参数含义：该参数用于设置是否对信令传输进行优化。<br>数据来源：本端规划<br>取值范围：<br>- “DONT_OPTIMIZE（不优化）”：不对信令传输进行优化。<br>- “OPTIMIZE（优化）”：对信令传输进行优化。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| SRCSTATDESC | 源统计描述 | 可选必选说明：可选参数<br>参数含义：该参数用于设置源统计描述。<br>数据来源：本端规划<br>取值范围：<br>- “UNKNOWN（未知）”：未知<br>- “SPEECH（语音）”：语音<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| THP | 通信处理优先级 | 可选必选说明：可选参数<br>参数含义：该参数用于设置通信处理优先级。<br>数据来源：本端规划<br>取值范围：<br>- “HIGH（高）”：高优先级。<br>- “NORMAL（中）”：正常优先级。<br>- “LOW（低）”：低优先级。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| TRAFFICCLASS | 业务类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置业务类型。<br>数据来源：本端规划<br>取值范围：<br>- “CONVERSATIONAL（会话类）”：表示用户签约信息中traffic class的级别为会话层面，优先级高。<br>- “STREAMING（流媒体类）”：表示用户签约信息中traffic class的级别为流媒体层面。<br>- “INTERACTIVE（交互类）”：表示用户签约信息中traffic class的级别为交互层面。<br>- “BACKGROUND（后台类）”：表示用户签约信息中traffic class的级别为后台层面。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |
| TRANSDELAY | 传输时延(毫秒) | 可选必选说明：可选参数<br>参数含义：该参数用于设置传输时延。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~4000，单位是毫秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEFPRER8QOS查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEFPRER8QOS]] · 缺省的Pre-R8 QoS参数（DEFPRER8QOS）

## 使用实例

配置QoS缺省配置中的ARPVALUE值为HIGH：

```
SET DEFPRER8QOS:ARPVALUE=HIGH;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-DEFPRER8QOS.md`
