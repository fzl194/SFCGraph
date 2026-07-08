---
id: UNC@20.15.2@MMLCommand@DSP GTPCSTATUSINFO
type: MMLCommand
name: DSP GTPCSTATUSINFO（显示GTP-C路径当前及历史状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPCSTATUSINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- AMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- GTP-C接口配置管理
- GTP-C路径维护
status: active
---

# DSP GTPCSTATUSINFO（显示GTP-C路径当前及历史状态）

## 功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于查询GTP-C路径当前及历史状态记录，包括接口类型、路径状态变更、变更时间戳、以及本端对端地址等信息。当前支持每个进程最多显示100条历史路径。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指示POD名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。该参数通过命令DSP POD查询。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTPCSTATUSINFO]] · GTP-C路径当前及历史状态（GTPCSTATUSINFO）

## 使用实例

查询所有路径状态。 DSP GTPCSTATUSINFO:;

```
%%DSP GTPCSTATUSINFO: ;%%
RETCODE = 0  操作成功

结果如下
------------------------
               POD名称 = uncpod-0
              接口类型  =  S11
          本端IPv4地址  =  10.2.102.17
          本端IPv6地址  =  ::
          对端IPv4地址  =  192.168.208.11
          对端IPv6地址  =  ::
          路径状态变更  =  UP->DOWN
      状态变更时间戳  =  09:30:05 06/04/2021
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTPCSTATUSINFO.md`
