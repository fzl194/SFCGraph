---
id: UNC@20.15.2@MMLCommand@RMV ADCPARA
type: MMLCommand
name: RMV ADCPARA（删除ADC参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: ADCPARA
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- PCC管理
- ADC
- ADC参数
status: active
---

# RMV ADCPARA（删除ADC参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除ADC参数。当运营商希望删除指定ADC应用的流信息上报开关和重定向信息时，则执行该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置应用对应的流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ADCPARA]] · ADC参数（ADCPARA）

## 使用实例

假设运营商不希望ADC应用对应的流过滤器名称为testflowfiltername的应用进行流信息上报，可以执行该命令：

```
RMV ADCPARA:FLOWFILTERNAME="testflowfiltername";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除ADC参数（RMV-ADCPARA）_65997000.md`
