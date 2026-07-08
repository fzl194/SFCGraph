---
id: UDG@20.15.2@MMLCommand@SET IKEGLOBALCONFIG
type: MMLCommand
name: SET IKEGLOBALCONFIG（设置IKE全局配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: IKEGLOBALCONFIG
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- IPSEC功能管理
- IP服务
- IP安全管理
- 互联网密钥交换
- IKE全局配置
status: active
---

# SET IKEGLOBALCONFIG（设置IKE全局配置）

## 功能

![](设置IKE全局配置（SET IKEGLOBALCONFIG）_26032205.assets/notice_3.0-zh-cn.png)

如果安全日志阈值不为0，链路协商失败时，可能会导致日志大量打印，影响问题定位，对业务性能无影响。

该命令用于设置IKE全局配置。

> **说明**
> - 该命令执行后立即生效。
>
> - 需要CPU告警上报阈值大于等于CPU告警恢复阈值，且建议上报阈值大至少10个百分点，否则告警可能会持续上报。
> - 在用户级模板模式场景下NATKLI参数不生效。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | DFBITCLEAR | FRAGBEFOREENCR | TRAFFSADISFLG | TRAFFICSADURTN | TIMESADURTN | ANTIREPLFLG | WINDOWSIZE | DPDTYPE | NUMBER | DOSTHRESHOLD | NATKLI | CPUREPORTTHRES | CPUCLEARTHRES |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | FALSE | FALSE | FALSE | 1843200 | 3600 | True | Size_1024 | None | 30 | 0 | 20 | 80 | 70 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DFBITCLEAR | 清除分片标记位 | 可选必选说明：可选参数<br>参数含义：清除分片标记位。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| FRAGBEFOREENCR | 加密前分片 | 可选必选说明：可选参数<br>参数含义：加密前分片。<br>数据来源：本端规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| TRAFFSADISFLG | 流量方式触发SA过期标记位 | 可选必选说明：可选参数<br>参数含义：流量方式触发SA过期。<br>数据来源：本端规划<br>取值范围：<br>- FALSE（FALSE）<br>- TRUE（TRUE）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| TRAFFICSADURTN | 流量数 (kbyte) | 可选必选说明：该参数在"TRAFFSADISFLG"配置为"FALSE"时为条件可选参数。<br>参数含义：流量方式触发SA过期的流量数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是8000~200000000，单位是千字节。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| TIMESADURTN | 时间间隔 (s) | 可选必选说明：可选参数<br>参数含义：时间方式触发SA过期的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是480~604800，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| ANTIREPLFLG | 抗重放 | 可选必选说明：可选参数<br>参数含义：抗重放功能开关。<br>数据来源：本端规划<br>取值范围：<br>- False（False）<br>- True（True）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| WINDOWSIZE | 窗口大小 | 可选必选说明：该参数在"ANTIREPLFLG"配置为"True"时为条件可选参数。<br>参数含义：抗重放窗口的大小，超过这个流量的报文会被丢弃。<br>数据来源：本端规划<br>取值范围：<br>- “Size_32（全局窗口大小32Kb）”：全局窗口大小32Kb<br>- “Size_64（全局窗口大小64Kb）”：全局窗口大小64Kb<br>- “Size_128（全局窗口大小128Kb）”：全局窗口大小128Kb<br>- “Size_256（全局窗口大小256Kb）”：全局窗口大小256Kb<br>- “Size_512（全局窗口大小512Kb）”：全局窗口大小512Kb<br>- “Size_1024（全局窗口大小1024Kb）”：全局窗口大小1024Kb<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| LOCALNAME | 本地名称 | 可选必选说明：可选参数<br>参数含义：本地的名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：<br>输入单空格将删除该参数已有配置项。 |
| DPDTYPE | DPD类型 | 可选必选说明：可选参数<br>参数含义：DPD类型。<br>数据来源：本端规划<br>取值范围：<br>- None（无）<br>- “Periodic（周期性检测）”：周期性检测<br>- “Ondemand（按需检测）”：按需检测<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| DPDINTERVAL | DPD检查间隔 (s) | 可选必选说明：该参数在"DPDTYPE"配置为"Periodic"、"Ondemand"时为条件必选参数。<br>参数含义：DPD间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~3600，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| DPDRETRYINTRVL | DPD重试间隔 (s) | 可选必选说明：该参数在"DPDTYPE"配置为"Periodic"、"Ondemand"时为条件可选参数。<br>参数含义：DPD消息重发的间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是2~60，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| NUMBER | 历史信息记录条数 | 可选必选说明：可选参数<br>参数含义：历史信息记录条数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是30~1024。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| DOSTHRESHOLD | 安全日志阈值 | 可选必选说明：可选参数<br>参数含义：安全日志阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~200。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：<br>输入0将删除该参数已有配置项。 |
| NATKLI | NAT保活时间间隔 (s) | 可选必选说明：可选参数<br>参数含义：发送NAT保活报文的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~300，单位是秒。<br>默认值：20。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：<br>在IPSec使能NAT穿越功能时，该参数才有效。 |
| CPUREPORTTHRES | IPSEC转发CPU过载告警上报阈值 (%) | 可选必选说明：可选参数<br>参数含义：IPSEC转发CPU过载告警上报阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| CPUCLEARTHRES | IPSEC转发CPU过载告警恢复阈值 (%) | 可选必选说明：可选参数<br>参数含义：IPSEC转发CPU过载告警恢复阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~100，单位是百分比。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| UIKECHECKTIME | UIKE主动核查时间 | 可选必选说明：可选参数<br>参数含义：UIKE主动向AMUP发起核查的时间。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~23，65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：<br>输入0-23之间的整数时，将核查时间调整到对应整点。<br>输入65535时，关闭UIKE向AMUP的主动核查机制。 |
| FLOWCTRLSTHRES | IPsec跟踪的开启流控的CPU阈值（%） | 可选必选说明：可选参数<br>参数含义：该参IPsec跟踪的开启流控的CPU阈值。如果IPsec转发使用的CPU的占用超过本参数配置的阈值，将开启跟踪流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |
| FLOWCTRLRTHRES | IPsec跟踪的恢复流控的CPU阈值（%） | 可选必选说明：可选参数<br>参数含义：该参数表示IPsec跟踪的恢复流控的CPU阈值。如果IPsec流控在开启状态中，然后IPsec转发使用的CPU占用恢复到本参数配置的阈值以下，将恢复流控。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是50~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IKEGLOBALCONFIG查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IKEGLOBALCONFIG]] · IKE全局配置（IKEGLOBALCONFIG）

## 关联任务

- [[UDG@20.15.2@Task@0-00217]]

## 使用实例

使能加密前分片：

```
SET IKEGLOBALCONFIG:FRAGBEFOREENCR=TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-IKEGLOBALCONFIG.md`
