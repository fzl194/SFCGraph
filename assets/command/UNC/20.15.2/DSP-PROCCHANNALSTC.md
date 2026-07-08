---
id: UNC@20.15.2@MMLCommand@DSP PROCCHANNALSTC
type: MMLCommand
name: DSP PROCCHANNALSTC（查询逻辑链路统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PROCCHANNALSTC
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

# DSP PROCCHANNALSTC（查询逻辑链路统计信息）

## 功能

该命令用于查询逻辑链路统计信息。

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

- [[configobject/UNC/20.15.2/PROCCHANNALSTC]] · 逻辑链路统计信息（PROCCHANNALSTC）

## 使用实例

显示资源逻辑链路信息：

```
DSP PROCCHANNALSTC:SRCPROCID=4,PLANEID=0
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
平面ID   源端进程ID   目的端进程ID   链路状态   发送的报文数量   接收到的报文数量   链路重置次数   发送队列消息   乱序队列消息   发送队列的最大长度   发送队列的平均长度   报文发送最大时延（ms）   报文发送最小时延（ms）   报文发送平均时延（ms）   发送失败次数   重传请求次数
0        4            1000           正常       579              458                8              2              1              100                  58                   0                        0                        0                        5              41
0        4            1001           正常       511              450                8              2              1              100                  58                   0                        0                        0                        6              35
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PROCCHANNALSTC.md`
