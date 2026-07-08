---
id: UNC@20.15.2@MMLCommand@SET SCTPINITFLOW
type: MMLCommand
name: SET SCTPINITFLOW（设置SCTP接入流控）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCTPINITFLOW
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# SET SCTPINITFLOW（设置SCTP接入流控）

## 功能

**适用NF：MME、AMF**

该命令用于设置系统中SCTP接入流控参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug;system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCH | 流控开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否开启S1和N2接口SCTP接入流控“固定速率流控”功能。<br>数据来源：整网规划<br>取值范围：<br>- ON（开启）<br>- OFF（关闭）<br>系统初始设置值：ON（开启） |
| CTHD | S1固定流控速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在开启S1和N2接口SCTP接入流控功能后，接入4G基站时整系统每秒SCTP建链数量。<br>数据来源：整网规划<br>取值范围：整数类型，取值范围为1~1000000。<br>系统初始设置值：2000 |
| CTHDN2 | N2固定流控速率 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在开启S1和N2接口SCTP接入流控功能后，接入5G基站时整系统每秒SCTP建链数量。<br>数据来源：整网规划<br>取值范围：整数类型，取值范围为1~1000000。<br>系统初始设置值：2000 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPINITFLOW]] · SCTP接入流控（SCTPINITFLOW）

## 使用实例

设置SCTP接入流控参数，指定流控开关为开启，S1固定流控速率为2000，N2固定流控速率为2000：

```
SET SCTPINITFLOW: SWITCH=ON, CTHD=2000, CTHDN2=2000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SCTPINITFLOW.md`
