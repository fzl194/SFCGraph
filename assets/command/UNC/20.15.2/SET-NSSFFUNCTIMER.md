---
id: UNC@20.15.2@MMLCommand@SET NSSFFUNCTIMER
type: MMLCommand
name: SET NSSFFUNCTIMER（设置NSSF功能时长）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFFUNCTIMER
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能时长管理
status: active
---

# SET NSSFFUNCTIMER（设置NSSF功能时长）

## 功能

**适用NF：NSSF**

该命令用于配置NSSF功能的时长类信息。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| TPSSMOTIMER |
| --- |
| 30 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TPSSMOTIMER | TPS平滑取值周期数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NSSF上报TPS（每秒事务数）时的平滑取值周期数，NSSF每秒事务数上报周期为2秒，取上报前TPSSMOTIMER *2秒时间内的TPS平均值作为上报值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFFUNCTIMER查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFUNCTIMER]] · NSSF功能时长（NSSFFUNCTIMER）

## 使用实例

配置NSSF上报TPS平滑取值周期数为10个上报周期（20秒）：

```
SET NSSFFUNCTIMER: TPSSMOTIMER=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NSSF功能时长（SET-NSSFFUNCTIMER）_22836795.md`
