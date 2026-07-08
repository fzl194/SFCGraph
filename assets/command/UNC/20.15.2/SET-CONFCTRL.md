---
id: UNC@20.15.2@MMLCommand@SET CONFCTRL
type: MMLCommand
name: SET CONFCTRL（设置冲突控制参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: CONFCTRL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 会话协议参数管理
- 会话流程控制管理
- 会话流程冲突控制
status: active
---

# SET CONFCTRL（设置冲突控制参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于设置冲突场景下，低优先级流程消息的缓存重发次数和缓存重发时间间隔。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| EPSRETRYTIMES | EPSTIMEOUT | NRRETRYTIMES | NRTIMEOUT |
| --- | --- | --- | --- |
| 3 | 2 | 3 | 2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EPSRETRYTIMES | EPS消息缓存重发的次数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置冲突场景下，Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的缓存次数，次数达到设置值时，消息将被丢弃。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CONFCTRL查询当前参数配置值。<br>配置原则：无 |
| EPSTIMEOUT | EPS消息缓存重发的时间间隔(s) | 可选必选说明：可选参数<br>参数含义：该参数用于设置冲突场景下，从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CONFCTRL查询当前参数配置值。<br>配置原则：无 |
| NRRETRYTIMES | NR消息缓存重发的次数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置冲突场景下，缓存网络侧触发的Session Modify流程的次数，次数达到设置值时，消息将被丢弃。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~15。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CONFCTRL查询当前参数配置值。<br>配置原则：无 |
| NRTIMEOUT | NR消息缓存重发的时间间隔(s) | 可选必选说明：可选参数<br>参数含义：该参数用于设置冲突场景下，缓存的网络侧触发的Session Modify流程重发的时间间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CONFCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [查看冲突控制参数（CONFCTRL）](configobject/UNC/20.15.2/CONFCTRL.md)

## 使用实例

设置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发次数为3次，缓存时长为2秒，Sesssoin Modify流程缓存重发次数为3次，缓存时长为2秒：

```
SET CONFCTRL: EPSRETRYTIMES=3, EPSTIMEOUT=2, NRRETRYTIMES=3, NRTIMEOUT=2;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置冲突控制参数（SET-CONFCTRL）_09651408.md`
