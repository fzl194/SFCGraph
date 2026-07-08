---
id: UNC@20.15.2@MMLCommand@SET DDNTIMEOUTCTRL
type: MMLCommand
name: SET DDNTIMEOUTCTRL（设置DDN定时器超时参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DDNTIMEOUTCTRL
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 流控管理
- DDN消息无响应处理策略
status: active
---

# SET DDNTIMEOUTCTRL（设置DDN定时器超时参数）

## 功能

**适用NF：SGW-C**

该命令用于设置DDN消息无响应时是否进行用户延时删除处理以及延时删除用户的随机定时器时长。

## 注意事项

- 该命令执行后立即生效。

- 默认开启DDN无响应延时删除用户功能，避免因DDN无响应导致大量用户同时去激活而引发信令风暴。如果确认不需要该功能，可选择关闭。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DELAYSUBDELSW | MINDELAYTIMER | MAXDELAYTIMER |
| --- | --- | --- |
| ENABLE | 30 | 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DELAYSUBDELSW | 用户延时删除开关 | 可选必选说明：必选参数<br>参数含义：该参数用于设置用户延时删除开关。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（使能）<br>- DISABLE（不使能）<br>默认值：无。<br>配置原则：无 |
| MINDELAYTIMER | 延时定时器时长下限值(分钟) | 可选必选说明：该参数在"DELAYSUBDELSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置延时定时器时长下限值，取延时定时器时长下限值到上限值的随机值作为延时删除用户的定时器时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~120，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNTIMEOUTCTRL查询当前参数配置值。<br>配置原则：无 |
| MAXDELAYTIMER | 延时定时器时长上限值(分钟) | 可选必选说明：该参数在"DELAYSUBDELSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置延时定时器时长上限值，取延时定时器时长下限值到上限值的随机值作为延时删除用户的定时器时长。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~120，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNTIMEOUTCTRL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [DDN定时器超时参数（DDNTIMEOUTCTRL）](configobject/UNC/20.15.2/DDNTIMEOUTCTRL.md)

## 使用实例

当运营商希望开启DDN消息无响应延时删除用户功能，配置用户延时删除定时器时长区间值执行：

```
SET DDNTIMEOUTCTRL: DELAYSUBDELSW=ENABLE, MINDELAYTIMER=40, MAXDELAYTIMER=70;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置DDN定时器超时参数（SET-DDNTIMEOUTCTRL）_46314493.md`
