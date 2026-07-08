---
id: UNC@20.15.2@MMLCommand@SET UERADIOCAPLEN
type: MMLCommand
name: SET UERADIOCAPLEN（设置UE Radio Capability信元信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UERADIOCAPLEN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- UE无线能力控制策略
status: active
---

# SET UERADIOCAPLEN（设置UE Radio Capability信元信息）

## 功能

![](设置UE Radio Capability信元信息（SET UERADIOCAPLEN）_24956656.assets/notice_3.0-zh-cn_2.png)

如果设置UE Radio Capability信元长度上限过小，AMF无法存储UE Radio Capability信元内容，反之，AMF的内存有增大的风险。执行此命令前，请通过DSP UERADIOCAPLEN获取UE Radio Capability信元长度信息并联系华为技术支持协助配置。

**适用NF：AMF**

该命令用于设置AMF上存储UE Radio Capability到数据库的信元长度上限和不同IMEI设备型号核准号码的最大个数，设置存储UE Radio Capability到内存的开关及参数信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行前需要根据现网UE Radio Capability信元长度适度配置。如配置过小，AMF无法存储UE Radio Capability信元内容。如配置过大，AMF的内存有增大的风险。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UERADIOCAPLEN | MAXIMEITACNUM | SAVMEMSW | SAVMEMRADIO | SAVMEMMAXLEN | MEMTHRD | REPORTALM |
| --- | --- | --- | --- | --- | --- | --- |
| 4096 | 1024 | OFF | 20 | 32 | 200 | 95 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UERADIOCAPLEN | UE Radio Capability信元长度上限 | 可选必选说明：可选参数<br>参数含义：该参数表示AMF上能存储的UE Radio Capability信元的最大长度。当UE上报的消息中包含UE Radio Capability信元，且此信元长度超过此参数设置的值时，则UE上报的UE Radio Capability信元内容不会被存储在AMF的数据库中。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是512~5120。如果需要扩展支持5120-12288则需要设置 DWORD33。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：无 |
| MAXIMEITACNUM | 不同IMEI设备型号核准号码的最大个数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示单进程存储不同IMEI设备型号核准号码（TAC）的最大个数。TAC由IMEI的前8位数字组成，用来标识某一型号的手机。存储时不同TAC对应不同的UE Radio Capability长度记录，当接入到系统里的不同TAC超过此参数配置的数值，MML命令DSP UERADIOCAPLEN查询到的结果不全。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~4096。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：无 |
| SAVMEMSW | 保存到内存开关 | 可选必选说明：可选参数<br>参数含义：该参数用于配置UE无线能力保存到内存的开关，当UE无线能力长度大于参数“UERADIOCAPLEN”配置的上限，则将UE无线能力保存到内存中。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（开启）”：开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：<br>如果设置为“ON”，则符合该配置的UE无线能力将保存到内存中；如果设置为“OFF”，则符合该配置的UE无线能力将保存到数据库中。<br>说明：进程复位时，内存数据会丢失。 |
| SAVMEMRADIO | 保存到内存的用户数百分比 | 可选必选说明：该参数在"SAVMEMSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数表示AMF上保存UE Radio Capability信元到内存的用户数占总用户数的最大百分比。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：无 |
| SAVMEMMAXLEN | 最大长度(KB) | 可选必选说明：该参数在"SAVMEMSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数表示AMF上支持保存到内存的最大UE Radio Capability信元长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~32。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：无 |
| MEMTHRD | 内存配额(MB) | 可选必选说明：该参数在"SAVMEMSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数表示AMF上保存UE Radio Capability信元的内存上限阈值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~1024。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：无 |
| REPORTALM | 上报告警百分比 | 可选必选说明：该参数在"SAVMEMSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数表示上报5G UE无线能力处理超出上限告警的百分比。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~100。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UERADIOCAPLEN查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UERADIOCAPLEN]] · UE Radio Capability信元长度（UERADIOCAPLEN）

## 使用实例

设置AMF上能存储的UE Radio Capability信元长度上限为4096，不同IMEI设备型号核准号码的最大个数为1024，执行如下命令：

```
SET UERADIOCAPLEN:UERADIOCAPLEN=4096,MAXIMEITACNUM=1024;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置UE-Radio-Capability信元信息（SET-UERADIOCAPLEN）_24956656.md`
