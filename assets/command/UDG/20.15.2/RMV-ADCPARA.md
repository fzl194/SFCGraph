---
id: UDG@20.15.2@MMLCommand@RMV ADCPARA
type: MMLCommand
name: RMV ADCPARA（删除ADC参数）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: ADCPARA
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务控制策略
- ADC
- ADC参数
status: active
---

# RMV ADCPARA（删除ADC参数）

## 功能

**适用NF：PGW-U、UPF**

![](删除ADC参数（RMV ADCPARA）_01905962.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除AdcPara可能会导致用户策略获取发生变化，影响策略获取，导致用户业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除ADC参数。当运营商希望删除指定ADC应用的流信息上报开关时，则执行该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器/流过滤器组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置应用对应的流过滤器或流过滤器组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [ADC参数（ADCPARA）](configobject/UDG/20.15.2/ADCPARA.md)

## 使用实例

假设运营商需要删除指定ADC应用下的参数时，指定流过滤器名称为testflowfiltername，可以执行该命令：

```
RMV ADCPARA:FLOWFILTERNAME="testflowfiltername";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除ADC参数（RMV-ADCPARA）_01905962.md`
