---
id: UNC@20.15.2@MMLCommand@SET AMFSBIINFCTRL
type: MMLCommand
name: SET AMFSBIINFCTRL（设置AMF的SBI接口控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFSBIINFCTRL
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- AMF服务化接口兼容性参数管理
status: active
---

# SET AMFSBIINFCTRL（设置AMF的SBI接口控制参数）

## 功能

**适用NF：AMF**

该命令用于设置AMF的SBI接口控制参数。

若期望AMF向周边网元携带信元location及callbackUri中的Schema可基于对端请求的Schema或所选定的服务Schema动态设置，可通过本命令开启Schema自适应功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SCHEMAADAPTSW | SCHEMAUDMPLCY | SCHEMAPCFPLCY |
| --- | --- | --- |
| OFF | HTTP_FIRST | HTTP_FIRST |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCHEMAADAPTSW | Schema自适应开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制AMF是否支持Schema自适应功能。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。<br>配置原则：无 |
| SCHEMAUDMPLCY | ModelD模式UDM Schema填充策略 | 可选必选说明：该参数在"SCHEMAADAPTSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置ModelD模式下AMF与UDM网元交互时Schema的填充策略。<br>ModelD模式下，AMF无法感知对端UDM支持的Schema类型，通过本参数可以灵活调整AMF与UDM网元交互时Schema的填充策略。<br>ModelD模式下，建议AMF与对端UDM的Schema策略均设置一致；若AMF与对端UDM的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与UDM通信。<br>数据来源：全网规划<br>取值范围：<br>- HTTP_FIRST（HTTP优先）<br>- HTTPS_FIRST（HTTPS优先）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。<br>配置原则：无 |
| SCHEMAPCFPLCY | ModelD模式PCF Schema填充策略 | 可选必选说明：该参数在"SCHEMAADAPTSW"配置为"ON"时为条件可选参数。<br>参数含义：该参数用于设置ModelD模式下AMF与PCF网元交互时Schema的填充策略。<br>ModelD模式下，AMF无法感知对端PCF支持的Schema类型，通过本参数可以灵活调整AMF与PCF网元交互时Schema的填充策略。<br>ModelD模式下，建议AMF与对端PCF的Schema策略均设置一致；若AMF与对端PCF的Schema策略配置不一致时，则需要SCP同时配置两种Schema策略，否则会影响后续AMF与PCF通信。<br>数据来源：全网规划<br>取值范围：<br>- HTTP_FIRST（HTTP优先）<br>- HTTPS_FIRST（HTTPS优先）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBIINFCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFSBIINFCTRL]] · AMF的SBI接口控制参数（AMFSBIINFCTRL）

## 使用实例

开启Schema自适应功能，执行如下命令：

```
SET AMFSBIINFCTRL:SCHEMAADAPTSW=ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFSBIINFCTRL.md`
