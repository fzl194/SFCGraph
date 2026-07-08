---
id: UNC@20.15.2@MMLCommand@SET NSSFFUNCSWITCH
type: MMLCommand
name: SET NSSFFUNCSWITCH（设置NSSF功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFFUNCSWITCH
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能开关配置
status: active
---

# SET NSSFFUNCSWITCH（设置NSSF功能开关）

## 功能

**适用NF：NSSF**

该命令用于设置NSSF功能开关的状态。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CFGWITHSUBSW | NSREQCHKESW | NSMATCHPLYESW |
| --- | --- | --- |
| FUNC_OFF | FUNC_ON | FUNC_ON |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CFGWITHSUBSW | 按签约分配Configured切片开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定按签约分配Configured切片开关的状态。开关打开时，切片选择结果中的Configured切片为签约切片；开关关闭时，切片选择结果中的Configured切片为签约切片与ADD CFGSNSSAI配置的交集。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFFUNCSWITCH查询当前参数配置值。<br>配置原则：无 |
| NSREQCHKESW | 切片选择请求合法性判断增强开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置切片选择请求合法性判断的增强开关。开关设置为“FUNC_ON”，AMF发送给NSSF的切片选择请求中请求切片与签约切片均不合法时，返回403错误码；开关设置为“FUNC_OFF”，AMF发送给NSSF的切片选择请求中请求切片不合法时，返回403错误码。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFFUNCSWITCH查询当前参数配置值。<br>配置原则：无 |
| NSMATCHPLYESW | 切片选择匹配策略增强开关 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSSF切片选择匹配策略的增强开关。开关设置为“FUNC_ON”，切片选择流程中，当请求切片与签约切片交集无法下发allowed切片时，使用签约切片重新匹配下发；开关设置为“FUNC_OFF”，切片选择流程中，当请求切片与签约切片交集无法下发allowed切片时，不使用签约切片重新匹配，返回结果为空。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFFUNCSWITCH查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFUNCSWITCH]] · NSSF功能开关（NSSFFUNCSWITCH）

## 使用实例

当运营商希望使用NSSF的某项功能，例如按签约分配Configured切片时，需要通过该命令打开对应开关项：

```
SET NSSFFUNCSWITCH: CFGWITHSUBSW=FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NSSFFUNCSWITCH.md`
