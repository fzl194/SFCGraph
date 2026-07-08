---
id: UNC@20.15.2@MMLCommand@SET NFUPDATE
type: MMLCommand
name: SET NFUPDATE（设置NF更新方式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NFUPDATE
command_category: 配置类
applicable_nf:
- AMF
- SMF
- NRF
- NSSF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 本地NRF功能管理
- NF更新管理
status: active
---

# SET NFUPDATE（设置NF更新方式）

## 功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG**

该命令用于设置NF信息更新推送到NRF的方式。

- 设置Patch更新缓存最大数量为N，如果NF的Patch更新在缓存中累计的次数到达N，则会立即将NF的更新信息推送到NRF，否则，更新信息缓存起来不推送。
- 设置Patch更新定时推送任务时长(分钟)为L，Patch更新在缓存中停留L时长后会被推送到NRF，L为0表示不使用定时推送。
- Patch更新缓存限制数量与Patch更新定时推送任务时长(分钟)中任意一个条件满足都会进行Patch更新推送。

## 注意事项

- 一个Patch更新定时会在推送任务时长(分钟)（CACHETIMERLEN）内生效

- Patch更新缓存最大数量大于1时，Patch更新定时推送任务时长（分钟）必须大于0。
- Patch更新定时推送任务时长（分钟）大于0时，Patch更新缓存限制数量必须大于1。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| CACHENUM | CACHETIMERLEN |
| --- | --- |
| 120 | 2 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CACHENUM | Patch更新缓存最大数量 | 可选必选说明：可选参数<br>参数含义：当Patch更新缓存数量达到该参数表示的值，会向NRF推送缓存的更新请求。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~127。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFUPDATE查询当前参数配置值。<br>配置原则：无 |
| CACHETIMERLEN | Patch更新缓存定时器时长(分钟) | 可选必选说明：可选参数<br>参数含义：Patch更新缓存的定时推送任务会按照该参数表示的时间间隔向NRF推送缓存中的更新信息。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~127，单位是分钟。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NFUPDATE查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [更新NF注册信息（NFUPDATE）](configobject/UNC/20.15.2/NFUPDATE.md)

## 使用实例

设置NF部分更新方式，NF部分更新数据会先进行缓存，当NF部分更新次数达到5次时，统一向NRF推送；缓存中的NF部分更新数据，10分钟向NRF推送一次。

```
SET NFUPDATE: CACHENUM=5, CACHETIMERLEN=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NF更新方式（SET-NFUPDATE）_09651782.md`
