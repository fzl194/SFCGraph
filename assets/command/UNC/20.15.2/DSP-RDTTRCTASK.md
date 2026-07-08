---
id: UNC@20.15.2@MMLCommand@DSP RDTTRCTASK
type: MMLCommand
name: DSP RDTTRCTASK（显示重定向跟踪任务）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: RDTTRCTASK
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 跟踪配置管理
- 跟踪重定向管理
- 跟踪重定向查询
status: active
---

# DSP RDTTRCTASK（显示重定向跟踪任务）

## 功能

**适用网元：SGSN、MME**

该命令用于查询指定VNFC下已经建立的重定向跟踪任务信息。其中重定向跟踪任务为用户在跟踪建立时选择了重定向标记并指定重定向索引的跟踪任务，系统中存在该类任务会主动将跟踪上报消息以Pcap格式上报到第三方服务器。

## 注意事项

- 该命令执行后立即生效。
- 当不指定跟踪类型时，将显示指定VNFC下所有的重定向跟踪任务信息。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRCTYPE | 跟踪类型 | 可选必选说明：可选参数。<br>参数含义：该参数表示重定向跟踪任务的类型。<br>数据来源：本端规划。<br>取值范围：<br>- GaInterfaceTrc(Ga接口跟踪)。<br>- GbInterfaceTrc(Gb接口跟踪)。<br>- GrInterfaceTrc(Gr接口跟踪)。<br>- IuInterfaceTrc（Iu接口跟踪）。<br>- S6a/S6dInterfaceTrc(S6a/S6d接口跟踪)。<br>- S13InterfaceTrc(S13接口跟踪)。<br>- SGsInterfaceTrc(SGs接口跟踪)。<br>- S1InterfaceTrc(S1接口跟踪)。<br>- GTPCTrc(GTPC跟踪)。<br>- UserTrc(用户跟踪)。<br>默认值：无 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数。<br>参数含义：VNFC名称。<br>数据来源：本端规划。<br>取值范围：输入长度范围为1~31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDTTRCTASK]] · 重定向跟踪任务（RDTTRCTASK）

## 使用实例

1.显示Gb接口跟踪重定向跟踪任务信息：

DSP RDTTRCTASK: TRCTYPE=GbInterfaceTrc, SERVICETYPE="GB_VNFC";

```
%%DSP RDTTRCTASK: TRCTYPE=GbInterfaceTrc, 
SERVICETYPE="GB_VNFC"
;%%
RETCODE = 0  操作成功。

Gb接口跟踪重定向跟踪任务信息如下：
-------------------------
 跟踪任务ID      NSEI号            小区号
 0              250              12545
 1              5421             789445
(结果个数 = 2)

---    END
```

2.显示GB_VNFC下的所有的重定向跟踪任务信息：

```
%%DSP RDTTRCTASK: 
SERVICETYPE="GB_VNFC"
;%%
RETCODE = 0  操作成功。

Gb接口跟踪重定向跟踪任务信息如下：
-------------------------
 跟踪任务ID      NSEI号            小区号
 0              250              12545
 1              5421             789445
仍有后续报告输出
---    END
```

```
%%DSP RDTTRCTASK: 
SERVICETYPE="GB_VNFC"
;%%
RETCODE = 0  操作成功。

用户跟踪重定向跟踪任务信息如下：
-------------------------
跟踪任务ID     ID类型       IMSI               MSISDN             IMEI 
7             IMSI        213368768686       NULL               NULL
8             MSISDN      NULL               4434431514464      NULL
（结果个数 = 4）
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-RDTTRCTASK.md`
