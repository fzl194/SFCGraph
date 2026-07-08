---
id: UNC@20.15.2@MMLCommand@SET N40MSGSTG
type: MMLCommand
name: SET N40MSGSTG（设置缓存开关、回放间隔、回放速率）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: N40MSGSTG
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费消息缓存
status: active
---

# SET N40MSGSTG（设置缓存开关、回放间隔、回放速率）

## 功能

![](设置缓存开关、回放间隔、回放速率（SET N40MSGSTG）_34667405.assets/notice_3.0-zh-cn_2.png)

当打开缓存功能后，需要使用命令SET CNVRGDCHGPARA配置参数CHGDATAREFGEN为SMF，即配置生成ChargingDataRef的方法为使用SMF生成，如果使用CHF生成ChargingDataRef时，可能导致放通用户用量丢失。

**适用NF：SMF、PGW-C**

该命令用于设置缓存开关、回放间隔、回放速率。

## 注意事项

- 该命令执行后立即生效。

- 该命令内的参数具体的生效机制，还需要参考对应的参数说明。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| STGSWITCH | REPLAYINTERVAL | REPLAYRATE | ENCRYPT | STGTXTIMER |
| --- | --- | --- | --- | --- |
| DISABLE | 30 | 500 | DISABLE | 15 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STGSWITCH | 融合计费消息缓存开关 | 可选必选说明：必选参数<br>参数含义：融合计费消息缓存开关。<br>数据来源：全网规划<br>取值范围：<br>- ENABLE（使能）<br>- DISABLE（不使能）<br>默认值：无。<br>配置原则：<br>只有在CHF支持处理SMF回放消息时，才可配置该功能使能。<br>当打开缓存功能后，需要使用命令SET CNVRGDCHGPARA配置参数CHGDATAREFGEN为SMF，即配置生成ChargingDataRef的方法为使用SMF生成。 |
| REPLAYINTERVAL | 融合计费消息回放的最小间隔(分钟) | 可选必选说明：该参数在"STGSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：融合计费消息回放的最小间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是5~1440，单位是分钟。回放间隔参数修改对应的数值后，需要加锁解锁对应的目录，修改才可生效。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGSTG查询当前参数配置值。<br>配置原则：<br>可根据现网CHF典型的故障恢复时长进行配置。 |
| REPLAYRATE | 融合计费消息回放的速率(个/秒) | 可选必选说明：该参数在"STGSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：融合计费消息回放的速率。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是10~10000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGSTG查询当前参数配置值。<br>配置原则：<br>融合计费缓存消息回放速率 <= CHF的信令处理能力 - 正常情况下SMF发送融合计费消息的峰值速率。 |
| ENCRYPT | 加密开关 | 可选必选说明：该参数在"STGSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于指定被缓存的融合计费消息是否被加密。<br>数据来源：本端规划<br>取值范围：<br>- ENABLE（使能）<br>- DISABLE（不使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGSTG查询当前参数配置值。<br>配置原则：<br>计费消息的加密存储会增加额外的性能开销，开启加密功能前请联系华为技术服务评估当前系统是否满足开启条件。 |
| STGTXTIMER | 缓存Tx定时器时长(秒) | 可选必选说明：该参数在"STGSWITCH"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置融合计费缓存服务等待CHF响应消息的时长，当超过该时长，则认为融合计费缓存服务等待CHF消息响应失败。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~20，单位是秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGSTG查询当前参数配置值。<br>配置原则：<br>只有在融合计费消息缓存开关（STGSWITCH）打开时，该配置参数才生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/N40MSGSTG]] · 缓存开关、回放间隔、回放速率（N40MSGSTG）

## 使用实例

设置缓存开关打开、回放间隔20分钟、回放速率600个/秒

```
SET N40MSGSTG: STGSWITCH=ENABLE, REPLAYINTERVAL=20, REPLAYRATE=600;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-N40MSGSTG.md`
