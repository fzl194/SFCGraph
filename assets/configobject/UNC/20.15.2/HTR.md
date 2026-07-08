---
id: UNC@20.15.2@ConfigObject@HTR
type: ConfigObject
name: HTR（HTR功能）
nf: UNC
version: 20.15.2
object_name: HTR
object_kind: global_setting
applicable_nf:
- SGSN
status: active
---

# HTR（HTR功能）

## 说明

**适用网元：SGSN**

此命令用于设置HTR（Hard to Reach）流控功能的相关参数。当Gr或者Ge口出现拥塞时需要进行流控。

Gr口拥塞的表现和控制场景：

- 场景1：SGSN与HLR之间直连链路拥塞，此时进行自动启控。
- 场景2：HLR过载，此时进行手工启控。
- 场景3：STP到HLR链路拥塞，此时进行手工启控。
- 场景4：STP过载，此时进行手工启控。
- 场景5：SGSN与STP之间直连链路拥塞，此时进行自动启控。

HTR功能提供如下配置功能：

- 运营商可以通过调整HTR流控启动阈值决定低于什么样的成功率启动HTR流控，通过调整HTR流控恢复阈值决定流控目标成功率。
- 在非SGSN直连链路拥塞场景下如果要进行HTR流控可以打开HTR功能手工开关。
- HTR流控的对象可以使用配置的HTR局向（使用命令[**ADD HTROFC**](../配置局向/增加HTR局向(ADD HTROFC)_72345753.md)）也可以使用系统自动生成的HTR局向，HTR功能手工开关关闭时必须使用系统自动生成局向，HTR功能手工开关打开时可以使用配置局向或系统自动生成局向，但不能既使用配置局向又使用系统自动生成局向。自动生成的局向是指SGSN通过SCCP GT翻译后获取的局向，例如，如果SGSN通过STP和多个HLR连接，而STP采用GT寻址转发消息则自动局向只能生成到STP的局向，通过配置局向可以精确到每个HLR，流控对象更准确，流控效果会更好。
- HTR流控功能同时适用于Gr和Ge接口，Ge接口不支持运营商配置HTR局向，即不支持命令[**ADD HTROFC**](../配置局向/增加HTR局向(ADD HTROFC)_72345753.md)配置Ge接口的HTR局向。
- 只有在直连场景下，HTR流控功能才适用于Ge接口。

## 操作本对象的命令

- [[command/UNC/20.15.2/LST-HTR]] · LST HTR
- [[command/UNC/20.15.2/SET-HTR]] · SET HTR

## 证据

- 原始手册：`evidence/UNC/20.15.2/HTR.md`
- 原始手册：`evidence/UNC/20.15.2/HTR.md`
