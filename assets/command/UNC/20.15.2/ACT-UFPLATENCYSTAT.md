---
id: UNC@20.15.2@MMLCommand@ACT UFPLATENCYSTAT
type: MMLCommand
name: ACT UFPLATENCYSTAT（激活UFP逐包转发时延度量开关）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: UFPLATENCYSTAT
command_category: 动作类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 时延统计
status: active
---

# ACT UFPLATENCYSTAT（激活UFP逐包转发时延度量开关）

## 功能

![](激活UFP逐包转发时延度量开关（ACT UFPLATENCYSTAT）_04560596.assets/notice_3.0-zh-cn_2.png)

使用该命令打开时延度量开关会影响PAE转发性能。如果当前吞吐量已接近PAE转发性能上限，开启时延度量会导致收包不及时进而导致丢包。

该命令用于打开或关闭逐包转发时延度量开关。

## 注意事项

- 该命令执行后立即生效。

- 当时延较大，大于10ms时，测量时延的周期需小于1小时，否则可能出现测量时延不准确的问题。
- 该命令不会进行配置恢复，即SDRE容器复位后不会重新打开时延度量开关。
- 该命令不支持配置导出。
- 开启场景仅支持2U1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LATENCYSWITCH | 开关 | 可选必选说明：必选参数<br>参数含义：该参数表示逐包转发时延度量开关的打开或关闭。<br>数据来源：本端规划<br>取值范围：<br>- “ENABLE（开）”：时延度量开关打开<br>- “DISABLE（关）”：时延度量开关关闭<br>默认值：无<br>配置原则：无 |
| VLANID | 虚拟局域网ID | 可选必选说明：该参数在"LATENCYSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数表示需要匹配的报文的多个虚拟局域网ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~1024。<br>默认值：无<br>配置原则：<br>最多可配置16个VlanID，每个VlanID的取值范围是0~4095，它们之间用竖线“\|”分割。 |
| DURATION | 时长 | 可选必选说明：该参数在"LATENCYSWITCH"配置为"ENABLE"时为条件必选参数。<br>参数含义：该参数表示时延度量的配置时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1440，单位是分钟。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UFP逐包转发时延度量开关（UFPLATENCYSTAT）](configobject/UNC/20.15.2/UFPLATENCYSTAT.md)

## 使用实例

开启或关闭PAE逐包转发时延度量功能：

```
+++    UNC/*MEID:0 MENAME:project-v6*/        2024-01-24 11:47:10
O&M    #122
%%ACT UFPLATENCYSTAT: LATENCYSWITCH=ENABLE, VLANID="0|4095|4095|258", DURATION=121;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/激活UFP逐包转发时延度量开关（ACT-UFPLATENCYSTAT）_04560596.md`
