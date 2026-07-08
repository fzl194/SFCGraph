---
id: UNC@20.15.2@MMLCommand@SET SMFUDMRESET
type: MMLCommand
name: SET SMFUDMRESET（设置SMF的UDM故障处理策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMFUDMRESET
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- UDM故障处理策略管理
status: active
---

# SET SMFUDMRESET（设置SMF的UDM故障处理策略）

## 功能

**适用NF：SMF**

该命令用于设置SMF的UDM故障处理策略。

## 注意事项

- 该命令执行后在下次UDM故障时生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RECOVCHANGE | LINKDOWNORDEREG | SCANRATE |
| --- | --- | --- |
| OFF | OFF | 1 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RECOVCHANGE | recoveryTime变化时重选UDM开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UDM的recoveryTime变化时是否重选UDM。UDM的recoveryTime改变时，会发NFUpdate消息给NRF，携带改变后的recoveryTime信元，然后NRF发NFStatusNotify消息给SMF。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| LINKDOWNORDEREG | 链路故障或者去注册时重选UDM开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SMF和UDM的链路持续故障、或者UDM的状态更新为去注册时是否重选UDM。<br>数据来源：全网规划<br>取值范围：<br>- “OFF（关闭）”：关闭<br>- “ON（打开）”：打开<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMRESET查询当前参数配置值。<br>配置原则：无 |
| SCANRATE | 扫描速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要重选UDM时，每个DS每秒扫描多少个用户，扫描到后对符合重选UDM条件的用户立即重选UDM。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~20，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMFUDMRESET查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFUDMRESET]] · SMF的UDM故障重选策略（SMFUDMRESET）

## 使用实例

设置UDM的recoveryTime变化时重选UDM，UDM的链路故障或者去注册时不重选UDM，重选UDM的扫描速率为5。

```
SET SMFUDMRESET:RECOVCHANGE=ON,LINKDOWNORDEREG=OFF,SCANRATE=5;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SMFUDMRESET.md`
