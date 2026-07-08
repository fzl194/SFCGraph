---
id: UNC@20.15.2@MMLCommand@DSP PROCCHANNALEVENT
type: MMLCommand
name: DSP PROCCHANNALEVENT（查询逻辑链路事件）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PROCCHANNALEVENT
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 进程和组件信息
status: active
---

# DSP PROCCHANNALEVENT（查询逻辑链路事件）

## 功能

该命令用于查询逻辑链路事件。

## 注意事项

- 该命令执行后立即生效。
- 该命令需要在UIPC协议的环境上使用。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PLANEID | 平面ID | 可选必选说明：必选参数<br>参数含义：该参数表示平面ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～3。<br>默认值：无 |
| SRCPROCID | 源端进程ID | 可选必选说明：必选参数<br>参数含义：该参数表示源端进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| DSTPROCID | 目的端进程ID | 可选必选说明：可选参数<br>参数含义：该参数表示目的端进程ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PROCCHANNALEVENT]] · 逻辑链路事件（PROCCHANNALEVENT）

## 使用实例

显示资源逻辑链路事件，指定目的端进程最多查询最近5条记录：

```
DSP PROCCHANNALEVENT:SRCPROCID=10002,PLANEID=0,DSTPROCID=10001
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
平面ID  源端进程ID  目的端进程ID   事件发生时间                    事件类型            原因值                         
0       10002       10001          2014-10-1 18：32：12            发生故障            心跳丢失                         
0       10002       10001          2014-10-1 18：32：13            链路恢复            收到复位消息

(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询逻辑链路事件（DSP-PROCCHANNALEVENT）_59103397.md`
