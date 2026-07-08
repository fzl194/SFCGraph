---
id: UDG@20.15.2@MMLCommand@DSP SDRSTOKEN
type: MMLCommand
name: DSP SDRSTOKEN（显示SDRS中的TOKEN信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SDRSTOKEN
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRSTOKEN（显示SDRS中的TOKEN信息）

## 功能

该命令用于查询SDRS中指定APP的TOKEN策略信息。

> **说明**
> 无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | app类型 | 可选必选说明：必选参数<br>参数含义：参数标识下发APP路由策略的APP类型，可以使用<br>[**DSP SDRSAPPTYPE**](显示SDRS中的APPTYPE信息（DSP SDRSAPPTYPE）_05545720.md)<br>命令获取。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| CELLID | Cell ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定SDR调试消息发送的CELLID，可以通过使用命令<br>[**DSP MSPROCESS**](../../可靠性管理/微服务可靠性管理/显示微服务进程信息（DSP MSPROCESS）_09587887.md)<br>获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~127。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SDRSTOKEN]] · SDRS中的TOKEN信息（SDRSTOKEN）

## 使用实例

使用如下命令查询SDRS中缓存的TOKEN策略信息：

```
%%DSP SDRSTOKEN: APPTYPE=1003, CELLID="vusn-pod-5bccb87b-d4d4v10-30-0-111__103__0";%%
RETCODE = 0  操作成功
结果如下
--------
令牌组数量  令牌组  根令牌  主链路链路实例是否故障  主实例ID               新主实例ID            版本号        推送状态  app类型   Cell ID
100         0       0       0                       11880498179773072535   11880498179773072535  551885032     0         1003      vusn-pod-5bccb87b-d4d4v10-30-0-111__103__0
100         0       1       0                       11880498179773072535   11880498179773072535  551885032     0         1003      vusn-pod-5bccb87b-d4d4v10-30-0-111__103__0
100         0       2       0                       11880498179773072535   11880498179773072535  551885032     0         1003      vusn-pod-5bccb87b-d4d4v10-30-0-111__103__0
100         0       3       0                       11880498179773072535   11880498179773072535  551885032     0         1003      vusn-pod-5bccb87b-d4d4v10-30-0-111__103__0
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-SDRSTOKEN.md`
