---
id: UNC@20.15.2@MMLCommand@SET SMSFSOFTPARA
type: MMLCommand
name: SET SMSFSOFTPARA（设置SMSF软参）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SMSFSOFTPARA
command_category: 配置类
applicable_nf:
- SMSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 软件参数管理
status: active
---

# SET SMSFSOFTPARA（设置SMSF软参）

## 功能

**适用NF：SMSF**

该命令用于设置SMSF的软件参数信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

> **说明**
> 此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| DT | DWORDNUM | DWORDVALUE |
| --- | --- | --- |
| Dw | 1 | 0 |
| Dw | 2 | 0 |
| Dw | 3 | 0 |
| Dw | 4 | 0 |
| Dw | 5 | 0 |
| Dw | 6 | 0 |
| Dw | 7 | 0 |
| Dw | 8 | 0 |
| Dw | 9 | 0 |
| Dw | 10 | 0 |
| Dw | 11 | 0 |
| Dw | 12 | 0 |
| Dw | 13 | 0 |
| Dw | 14 | 0 |
| Dw | 15 | 0 |
| Dw | 16 | 0 |
| Dw | 17 | 0 |
| Dw | 18 | 0 |
| Dw | 19 | 0 |
| Dw | 20 | 0 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DT | 数据类型 | 可选必选说明：必选参数<br>参数含义：该参数表示软件参数的数据类型。<br>数据来源：本端规划<br>取值范围：<br>- Dw（双字）<br>- Byte（字节）<br>默认值：无。<br>配置原则：<br>DT参数暂不支持Byte（字节）。 |
| DWORDNUM | Dword索引 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1500。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFSOFTPARA查询当前参数配置值。<br>配置原则：无 |
| DWORDVALUE | Dword值 | 可选必选说明：该参数在"DT"配置为"Dw"时为条件必选参数。<br>参数含义：该参数表示Dword类型软件参数的值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMSFSOFTPARA查询当前参数配置值。<br>配置原则：<br>当数据类型为Dword，Dword索引为1时， Dword值表示NRF主备场景下，NRF上报流量事件的阈值百分比，在流量统计周期内，当（NRF上收到的NF管理请求消息数）/（NRF上保存的全部NF实例数）x 100大于Dword值，该NRF上报流量产生事件，否则上报流量消失事件。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMSFSOFTPARA]] · SMSF软参（SMSFSOFTPARA）

## 使用实例

设置SMSF软件参数，数据类型是“Dw”，Dword索引是“1”，Dword值是“3”

```
SET SMSFSOFTPARA: DT=Dw, DWORDNUM=1, DWORDVALUE=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SMSFSOFTPARA.md`
