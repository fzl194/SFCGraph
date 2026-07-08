---
id: UNC@20.15.2@MMLCommand@MOD 5GCQOSACTION
type: MMLCommand
name: MOD 5GCQOSACTION（修改5GC QoS控制动作配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: 5GCQOSACTION
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC QoS控制动作
status: active
---

# MOD 5GCQOSACTION（修改5GC QoS控制动作配置）

## 功能

**适用NF：SMF**

该命令用于修改5G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

## 注意事项

- 命令执行后只对新接入用户生效。

- 当5QI值配置为GBR 5QI时，带宽参数才会生效，GBR 5QI取值参考协议23501以及STDQOSID配置。
- 带宽取值为0时，表示无效值。
- 上行保证带宽不能大于上行最大带宽。
- 下行保证带宽不能大于下行最大带宽。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定QoS Profile的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |
| FIVEQI | 5QI值 | 可选必选说明：必选参数<br>参数含义：该参数表示5G QoS identifier。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~255。<br>默认值：无<br>配置原则：无 |
| GFBRDL | 下行保证带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于配置保证的下行流比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20000000。<br>默认值：无<br>配置原则：无 |
| GFBRUL | 上行保证带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于配置保证的上行流比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20000000。<br>默认值：无<br>配置原则：无 |
| MFBRDL | 下行最大带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于配置最大的下行流比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20000000。<br>默认值：无<br>配置原则：无 |
| MFBRUL | 上行最大带宽(千比特/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于配置最大的上行流比特率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~20000000。<br>默认值：无<br>配置原则：无 |
| GFBRDLACTION | 超过下行GFBR的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于配置超过下行GFBR的处理行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别大于配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| GFBRULACTION | 超过上行GFBR的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于配置超过上行GFBR的处理行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别大于配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| MFBRDLACTION | 超过下行MFBR的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于配置超过下行MFBR的处理行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别大于配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |
| MFBRULACTION | 超过上行MFBR的处理 | 可选必选说明：可选参数<br>参数含义：该参数用于配置超过上行MFBR的处理行为。<br>数据来源：本端规划<br>取值范围：<br>- “DEGRADE（降级）”：表示如果请求的级别大于配置最高级别，则请求的级别自动降为配置的最高级别。<br>- “REJECT（拒绝）”：表示如果请求的级别超过配置的最高级别，则协商结束，激活失败。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@5GCQOSACTION]] · 5GC QoS控制动作配置（5GCQOSACTION）

## 使用实例

修改QoS Profile名称为“test”，5QI值为2的5GC QoS Action配置，修改下行保证带宽为2222千比特/秒，超过下行GFBR的处理为降级：

```
MOD 5GCQOSACTION:QOSPROFILENAME="test",FIVEQI=2,GFBRDL=2222,GFBRDLACTION=DEGRADE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-5GCQOSACTION.md`
