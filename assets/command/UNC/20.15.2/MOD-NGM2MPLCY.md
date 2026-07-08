---
id: UNC@20.15.2@MMLCommand@MOD NGM2MPLCY
type: MMLCommand
name: MOD NGM2MPLCY（修改5G M2M策略参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NGM2MPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G M2M管理
- 5G M2M策略参数配置
status: active
---

# MOD NGM2MPLCY（修改5G M2M策略参数）

## 功能

**适用NF：AMF**

该命令用于修改5G M2M的策略参数。

## 注意事项

下次注册流程生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定M2M策略的用户范围。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_USER（所有用户）”：所有用户。<br>- “HOME_USER（本网用户）”：本网用户。<br>- “FOREIGN_USER（外网用户）”：外网用户。<br>- “IMSI_PREFIX（IMSI前缀）”：IMSI前缀。<br>- “SPECIFIC_IMSI（指定IMSI）”：指定IMSI。<br>默认值：无<br>配置原则：无 |
| IMSIPRE | IMSI前缀 | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。<br>参数含义：该参数用于指定M2M策略用户的IMSI前缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是5~14。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"SUBRANGE"配置为"SPECIFIC_IMSI"时为条件必选参数。<br>参数含义：该参数用于指定M2M策略用户的IMSI（完整IMSI）。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是15。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| FEATURECOND | 特征条件组合 | 可选必选说明：必选参数<br>参数含义：该参数用于指定匹配M2M策略的特征条件组合。<br>当本参数配置为“DNN(指定DNN)”，则使用DNNNI参数的配置值在用户签约数据smfSelData中所有切片下的DNN列表中进行匹配；<br>数据来源：全网规划<br>取值范围：<br>- “NONE（不指定特征条件）”：不指定特征条件。<br>- “DNN（指定DNN）”：指定DNN。<br>默认值：无<br>配置原则：无 |
| DNNNI | 数据网络名称 | 可选必选说明：该参数在"FEATURECOND"配置为"DNN"时为条件必选参数。<br>参数含义：该参数用于指定M2M策略的DNNNI。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。可输入的字符有字母、十进制数字、“-”和“.”，并且开头和结尾只能是数字或者字母。不能出现连续两个“.”。字母大小写不敏感。<br>默认值：无<br>配置原则：<br>该参数来源于用户签约数据。 |
| EDRXSW | eDRX开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启支持终端省电eDRX模式。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无<br>配置原则：无 |
| NREDRXSUBPRI | NR模式EDRX寻呼周期签约优先 | 可选必选说明：该参数在"EDRXSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指示是否优先使用签约的eDRX参数（eDRX周期和寻呼窗口）作为NR用户的eDRX参数。当本参数设置为“YES（是）”时，AMF优先使用签约数据中的eDRX参数，签约数据中不存在eDRX周期时，再使用“NR模式寻呼周期”和“NR模式寻呼时间窗口”参数的配置值作为NR用户的eDRX参数。当本参数设置为“NO（否）”时，直接使用“NR模式寻呼周期”和“NR模式寻呼时间窗口时长”参数的配置值作为NR用户的eDRX参数。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无<br>配置原则：无 |
| NRECL | NR模式寻呼周期 | 可选必选说明：该参数在"EDRXSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定NR模式寻呼周期。<br>数据来源：全网规划<br>取值范围：<br>- “USE_UE_REQUEST（使用UE请求值）”：使用UE请求值。<br>- “SECONDS_2_56（2.56秒）”：2.56秒。<br>- “SECONDS_5_12（5.12秒）”：5.12秒。<br>- “SECONDS_10_24（10.24秒）”：10.24秒。<br>- “SECONDS_20_48（20.48秒）”：20.48秒。<br>- “SECONDS_40_96（40.96秒）”：40.96秒。<br>- “SECONDS_81_92（81.92秒）”：81.92秒。<br>- “SECONDS_163_84（163.84秒）”：163.84秒。<br>- “SECONDS_327_68（327.68秒）”：327.68秒。<br>- “SECONDS_655_36（655.36秒）”：655.36秒。<br>- “SECONDS_1310_72（1310.72秒）”：1310.72秒。<br>- “SECONDS_2621_44（2621.44秒）”：2621.44秒。<br>- “SECONDS_5242_88（5242.88秒）”：5242.88秒。<br>- “SECONDS_10485_76（10485.76秒）”：10485.76秒。<br>默认值：无<br>配置原则：<br>如果本参数配置了“USE_UE_REQUEST”，则参数“NR模式寻呼时间窗口时长”必须配置为“USE_UE_REQUEST”，本参数配置值不能小于“NR模式寻呼时间窗口时长”配置值。<br>3GPP协议定义，NR模式寻呼周期小于等于10.24s时，没有NR模式寻呼时间窗口时长。因此当本参数配置的寻呼周期大于10.24s时，“NR模式寻呼时间窗口时长”参数才生效。 |
| NRPTW | NR模式寻呼时间窗口时长 | 可选必选说明：该参数在"EDRXSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于指定NR模式寻呼时间窗口时长。<br>数据来源：全网规划<br>取值范围：<br>- “USE_UE_REQUEST（使用UE请求值）”：使用UE请求值。<br>- “SECONDS_1_28（1.28秒）”：1.28秒。<br>- “SECONDS_2_56（2.56秒）”：2.56秒。<br>- “SECONDS_3_84（3.84秒）”：3.84秒。<br>- “SECONDS_5_12（5.12秒）”：5.12秒。<br>- “SECONDS_6_4（6.4秒）”：6.4秒。<br>- “SECONDS_7_68（7.68秒）”：7.68秒。<br>- “SECONDS_8_96（8.96秒）”：8.96秒。<br>- “SECONDS_10_24（10.24秒）”：10.24秒。<br>- “SECONDS_11_52（11.52秒）”：11.52秒。<br>- “SECONDS_12_8（12.8秒）”：12.8秒。<br>- “SECONDS_14_08（14.08秒）”：14.08秒。<br>- “SECONDS_15_36（15.36秒）”：15.36秒。<br>- “SECONDS_16_64（16.64秒）”：16.64秒。<br>- “SECONDS_17_92（17.92秒）”：17.92秒。<br>- “SECONDS_19_20（19.20秒）”：19.20秒。<br>- “SECONDS_20_48（20.48秒）”：20.48秒。<br>- “SECONDS_21_76（21.76秒）”：21.76秒。<br>- “SECONDS_23_04（23.04秒）”：23.04秒。<br>- “SECONDS_24_32（24.32秒）”：24.32秒。<br>- “SECONDS_25_6（25.6秒）”：25.6秒。<br>- “SECONDS_26_88（26.88秒）”：26.88秒。<br>- “SECONDS_28_16（28.16秒）”：28.16秒。<br>- “SECONDS_29_44（29.44秒）”：29.44秒。<br>- “SECONDS_30_72（30.72秒）”：30.72秒。<br>- “SECONDS_32（32秒）”：32秒。<br>- “SECONDS_33_28（33.28秒）”：33.28秒。<br>- “SECONDS_34_56（34.56秒）”：34.56秒。<br>- “SECONDS_35_84（35.84秒）”：35.84秒。<br>- “SECONDS_37_12（37.12秒）”：37.12秒。<br>- “SECONDS_38_4（38.4秒）”：38.4秒。<br>- “SECONDS_39_68（39.68秒）”：39.68秒。<br>- “SECONDS_40_96（40.96秒）”：40.96秒。<br>- “PTW_NOT_EXIST（寻呼时间窗口时长不存在）”：寻呼时间窗口时长不存在。<br>默认值：无<br>配置原则：<br>如果本参数配置了“USE_UE_REQUEST”，则参数“NR模式寻呼周期”必须配置为“USE_UE_REQUEST”，本参数配置值不能大于“NR模式寻呼周期”配置值。<br>如果“NR模式寻呼周期”配置的值不是“USE_UE_REQUEST”时，本参数若不设置，默认值为“SECONDS_1_28（1.28秒）”。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGM2MPLCY]] · 5G M2M策略参数（NGM2MPLCY）

## 使用实例

IMSI前缀为123456且指定DNN作为匹配条件的M2M策略，修改eDRX协商策略为不使用签约的eDRX参数，直接使用UE请求的eDRX参数，执行如下命令：

```
MOD NGM2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123456", FEATURECOND=DNN, DNNNI="DNNa", NREDRXSUBPRI=NO, NRECL=USE_UE_REQUEST, NRPTW=USE_UE_REQUEST;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NGM2MPLCY.md`
