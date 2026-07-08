---
id: UDG@20.15.2@MMLCommand@SET RPTGLBPARA
type: MMLCommand
name: SET RPTGLBPARA（设置报表功能全局参数）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: RPTGLBPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 业务报表管理
- 报表功能管理
- 报表全局参数
status: active
---

# SET RPTGLBPARA（设置报表功能全局参数）

## 功能

**适用NF：UPF**

![](设置报表功能全局参数（SET RPTGLBPARA）_06561546.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响系统性能。

此命令用于设置业务报表全局参数。当运营商部署业务报表业务时使用。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | FLOWSAMPLERATE | NEID | TCPINSIGHTSAMRT | URLRPTCTRL | SRVLOADCTRL | TLSNAMEINFORPTCTRL | URLRPTLEN | SIGADDR | UPTCPRTTEXCETHR | DNTCPRTTEXCETHR | GWADDR |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 初始值 | 100 | 1 | 1000 | FULL_REPORTING | ENABLE | DISABLE | URL_LEN_DEFAULT | SMF_N4_INF | 0 | 0 | UPF_N4_INF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWSAMPLERATE | 流的识别抽样率 | 可选必选说明：可选参数<br>参数含义：该参数用于全局配置流抽样率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000，单位是千分比。<br>默认值：无<br>配置原则：抽样率配置越大对性能影响越大，修改抽样率前请评估对系统性能的影响。 |
| NEID | 网元标识 | 可选必选说明：可选参数<br>参数含义：该参数用于配置报表数据采集设备的网元标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无<br>配置原则：无 |
| TCPINSIGHTSAMRT | TCP业务分析上报功能流抽样率 | 可选必选说明：可选参数<br>参数含义：该参数用于配置TCP传输层质量分析上报功能的流抽样率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000，单位是千分比。<br>默认值：无<br>配置原则：抽样率配置越大对性能影响越大，修改抽样率前请评估对系统性能的影响。 |
| URLRPTCTRL | 控制URL上报功能 | 可选必选说明：可选参数<br>参数含义：该参数用于控制URL上报功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FULL_REPORTING：全量上报。<br>- HOST：只上报主机的URL。<br>默认值：无<br>配置原则：无 |
| SRVLOADCTRL | 根据负载选择服务器控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否根据负载选择服务器的功能。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| TLSNAMEINFORPTCTRL | Tls名字信息上报控制开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置是否上报Tls协议名字信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能（关闭）。<br>- ENABLE：使能（开启）。<br>默认值：无<br>配置原则：无 |
| URLRPTLEN | URL上报长度 | 可选必选说明：可选参数<br>参数含义：该参数配置URL上报的最大长度。<br>数据来源：本端规划<br>取值范围：<br>- URL_LEN_DEFAULT：URL默认上报长度。<br>- URL_LEN_127_BYTES：URL最大上报127字节。<br>- URL_LEN_1280_BYTES：URL最大上报1280字节。<br>- URL_LEN_4096_BYTES：URL最大上报4096字节。<br>默认值：无<br>配置原则：无 |
| SIGADDR | 控制上报的信令面地址来源 | 可选必选说明：可选参数<br>参数含义：该参数用于控制上报的信令面地址来源。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- SMF_N4_INF：SMF的N4接口地址。<br>- SMF_N4_SGSN：通过N4私有扩展获取的SMF对端信令地址。<br>默认值：无<br>配置原则：无 |
| UPTCPRTTEXCETHR | 上行TCP业务时延异常阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于配置Server侧TCP业务的异常RTT阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295，单位是ms。<br>默认值：无<br>配置原则：<br>- 该参数使用SET RPTGLBPARA命令配置生成。<br>- Server侧TCP业务的异常RTT阈值范围过大，配置阈值过小，上报消息增加，影响性能。 |
| DNTCPRTTEXCETHR | 下行TCP业务时延异常阈值 | 可选必选说明：可选参数<br>参数含义：该参数用于配置Ran侧TCP业务的异常RTT阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~4294967295，单位是ms。<br>默认值：无<br>配置原则：<br>- 该参数使用SET RPTGLBPARA命令配置生成。<br>- Ran侧TCP业务的异常RTT阈值范围过大，配置阈值过小，上报消息增加，影响性能。 |
| GWADDR | 控制上报的网关设备地址来源 | 可选必选说明：可选参数<br>参数含义：该参数用于控制上报的网关设备地址来源。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- UPF_N4_INF：UPF的N4接口地址。<br>- SMF_N4_GGSN：通过N4私有扩展获取的SMF本端信令地址。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@RPTGLBPARA]] · 业务报表全局参数（RPTGLBPARA）

## 使用实例

设置网元ID为1：

```
SET RPTGLBPARA:NEID=1;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-RPTGLBPARA.md`
