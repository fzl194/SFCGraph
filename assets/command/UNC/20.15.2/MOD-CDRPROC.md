---
id: UNC@20.15.2@MMLCommand@MOD CDRPROC
type: MMLCommand
name: MOD CDRPROC（修改话单处理）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: CDRPROC
command_category: 配置类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单处理
status: active
---

# MOD CDRPROC（修改话单处理）

## 功能

![](修改话单处理（MOD CDRPROC）_51174274.assets/notice_3.0-zh-cn_2.png)

此命令不能动态生效，需要执行“RST VNFC”重启服务，并且修改话单处理可能导致话单处理失败。

**适用NF：NCG**

该命令用于修改CG采用的格式引擎包。通常在开局配置了错误的格式引擎包或者当计费中心接口变更的时候才执行此命令。

## 注意事项

- 该命令执行后，需在“MML命令行 - UNC”窗口执行“[**RST VNFC**](../../../../../平台服务管理/单体服务公共功能管理/系统管理/复位系统/重启系统（RST VNFC）_59103634.md)”命令重新启动系统才能生效。
- 修改话单处理为危险操作，可能导致CG产生重复话单文件，不建议执行该命令；若确认一定要执行该命令，执行前，请联系华为技术支持。
- 不同的接入分组如果配置名称相同但内容不同的格式引擎包时，新的配置会覆盖老的配置，导致话单处理错误。
- 在执行此命令前，未使用U2020/MAE上传格式引擎包，则默认加载的是版本包中自带的同名格式引擎包。如果版本包中不存在该格式引擎包，则命令执行失败。
- 加载格式引擎包后，使用[**DSP FEMPACKET**](../格式引擎包/显示格式引擎配置信息（DSP FEMPACKET）_51174306.md)命令查看该格式引擎包的版本号与生成时间，用于校验格式引擎包的正确性。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：必选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：“接入网元分组标识”中只能包含数字、字母和下划线。 |
| PRFNAME | 格式引擎包名 | 可选必选说明：可选参数<br>参数含义：格式引擎包定义了CG话单处理的业务规则，主要包括话单字段过滤配置、分拣条件配置、通道配置、话单处理脚本等。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：<br>- 格式引擎包文件全名，包括后缀名。例如，“PS_R9_V940_NM_RT.tar.gz”。<br>- 不同的局点话单处理规则不同，需要根据实际情况配置相应的格式引擎包。<br>- 该参数只能由字母、数字、下划线、点组成。 |
| CDRTIMEOUT | 话单超时时间（分钟） | 可选必选说明：可选参数<br>参数含义：表示话单合并过程中能容许的超时时间。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～14400，单位是分钟。<br>默认值：无<br>配置原则：此参数如果需要修改，需要和运营商协商确定。 |
| SHAREFILECSN | 共享第二份最终话单文件序列号 | 可选必选说明：可选参数<br>参数含义：用于设置共享第二份最终话单文件序列号功能关闭或开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：<br>- 共享内存开关只能在该接入网元分组标识下仅配置一个业务模块时开启，开启后再依次添加其他业务模块。<br>- 共享内存只在该SPU的此接入网元分组标识下的多个业务模块生效。 |
| SEQNUMMODE | 序列号模式 | 可选必选说明：可选参数<br>参数含义：控制NCG回复的Cancel response和Release response的IE中携带的Sequence number来自GSN发送的Cancel request或Release request的gtp'帧的Head还是IE。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IE：序列号源自gtp'的IE。<br>- HEAD：序列号源自gtp'的Head。<br>默认值：无<br>配置原则：当GSN发送的Cancel request或者release request的IE中的Sequence number超过1个时，禁止将该参数值配置为“HEAD(序列号源自gtp'的Head)”。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRPROC]] · 话单处理（CDRPROC）

## 使用实例

修改CG话单处理采用的格式引擎包为“PS_R9_V940_NM_RT.tar.gz”，配置举例如下：

```
MOD CDRPROC: AGID="PS_GROUP_1", PRFNAME="PS_R9_V940_NM_RT.tar.gz";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改话单处理（MOD-CDRPROC）_51174274.md`
