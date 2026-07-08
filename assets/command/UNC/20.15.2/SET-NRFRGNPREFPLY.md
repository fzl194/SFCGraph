---
id: UNC@20.15.2@MMLCommand@SET NRFRGNPREFPLY
type: MMLCommand
name: SET NRFRGNPREFPLY（设置NRF区域优选策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFRGNPREFPLY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF区域优选管理
status: active
---

# SET NRFRGNPREFPLY（设置NRF区域优选策略）

## 功能

**适用NF：NRF**

该命令用于设置NRF区域优选策略。该命令功能暂不生效。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DNNIRGNPREFSW | DNAIRGNPREFSW | REQIDSTART | REQIDLENGTH |
| --- | --- | --- | --- |
| FUNC_OFF | FUNC_OFF | 0 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNNIRGNPREFSW | DNNI区域优选功能开关 | 可选必选说明：可选参数<br>参数含义：该参数表示NRF是否开启DNNI区域优选功能。该功能需要和命令NRFDNNIPREFRULE配合使用。开关打开时，若NF支持区域优选能力，NRF根据NF携带的服务发现参数或订阅参数和配置的优选目的NF区域规则，在服务发现响应或通知请求中携带此优选区域信息。开关关闭时，NRF在服务发现响应或通知请求中不携带优选区域信息。该参数功能暂不生效。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFRGNPREFPLY查询当前参数配置值。<br>配置原则：无 |
| DNAIRGNPREFSW | DNAI区域优选功能开关 | 可选必选说明：可选参数<br>参数含义：该参数表示NRF是否开启DNAI区域优选功能。该功能需要和命令NRFDNAIPREFRULE配合使用。开关打开时，若NF支持区域优选能力，NRF根据NF携带的服务发现参数或订阅参数和配置的优选目的NF区域规则，在服务发现响应或通知请求中携带此优选区域信息。开关关闭时，NRF在服务发现响应或通知请求中不携带优选区域信息。该参数功能暂不生效。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFRGNPREFPLY查询当前参数配置值。<br>配置原则：无 |
| REQIDSTART | 实例标识中区域信息起始位 | 可选必选说明：可选参数<br>参数含义：该参数表示请求NF实例标识中区域信息的起始位置。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~35。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFRGNPREFPLY查询当前参数配置值。<br>配置原则：无 |
| REQIDLENGTH | 实例标识中区域信息长度 | 可选必选说明：可选参数<br>参数含义：该参数表示请求NF实例标识中区域信息的长度。该参数功能暂不生效。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~36。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFRGNPREFPLY查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFRGNPREFPLY]] · NRF区域优选策略（NRFRGNPREFPLY）

## 使用实例

设置打开DNNI区域优选功能和DNAI区域优选功能，请求NF实例标识中区域信息起始位置为26，信息长度为2：

```
SET NRFRGNPREFPLY: DNNIRGNPREFSW=FUNC_ON, DNAIRGNPREFSW=FUNC_ON, REQIDSTART=26, REQIDLENGTH=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFRGNPREFPLY.md`
