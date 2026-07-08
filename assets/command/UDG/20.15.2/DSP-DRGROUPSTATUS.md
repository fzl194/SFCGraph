---
id: UDG@20.15.2@MMLCommand@DSP DRGROUPSTATUS
type: MMLCommand
name: DSP DRGROUPSTATUS（显示容灾组的运行状态信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: DRGROUPSTATUS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP DRGROUPSTATUS（显示容灾组的运行状态信息）

## 功能

该命令用于显示容灾组的运行状态信息以及容灾控制通道状态。

> **说明**
> - 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
> - 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于表示容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：<br>可使用<br>[**LST DRGROUPINFO**](查询容灾组信息（LST DRGROUPINFO）_74835153.md)<br>返回的DRGROUPID作为参数输入。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@DRGROUPSTATUS]] · 容灾组的运行状态信息（DRGROUPSTATUS）

## 使用实例

显示容灾组的运行状态信息，以及心跳探测结果：

```
%%DSP DRGROUPSTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
                容灾组标识  =  1
                容灾组名称  =  HafGTnGrp
          本端容灾实例标识  =  222
      本端容灾实例运行状态  =  容灾实例运行状态为备
主备容灾实例之间的心跳状态  =  主备容灾实例之间握手成功，处于连接状态
      最近一次链接建立时间  =  2022-07-31 22:36:05
      最近一次链接断开时间  =  NULL
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-DRGROUPSTATUS.md`
