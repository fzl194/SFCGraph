---
id: UNC@20.15.2@MMLCommand@SET DEACTIVERATE
type: MMLCommand
name: SET DEACTIVERATE（设置去激活用户承载的速率）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DEACTIVERATE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- 去活PDP速率
status: active
---

# SET DEACTIVERATE（设置去激活用户承载的速率）

## 功能

![](设置去激活用户承载的速率（SET DEACTIVERATE）_09652156.assets/notice_3.0-zh-cn_2.png)

如果配置速率过低，则用户去活时间较长，如果配置速率过高，会导致UNC负荷过高，CPU占用率升高，影响用户业务恢复。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于配置UNC主动触发去激活用户的速率，包括但不限于周边NF复位、链路故障、OM或会话空闲定时器超时等场景。

## 注意事项

- 该命令执行后立即生效。

- 当配置用户去活速率为5000（个/秒）时，执行去激活任务会使CPU占用率上升约6%。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| RATE |
| --- |
| 1000 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RATE | 去活速率(个/秒) | 可选必选说明：可选参数<br>参数含义：该参数用于指定整系统每秒钟去活的承载数，对于2、3G接入表示承载数，对于4、5G接入表示会话数。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是100~5000，单位是个每秒。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DEACTIVERATE查询当前参数配置值。<br>配置原则：<br>该参数描述的是整系统的去活承载速率，每个POD实际去活承载的速率=RATE/POD个数，并向上取整，所以存在实际去活速率略大于本设置值的可能。POD数为包含ContainerSm的POD数，可以通过DSP PODINFO进行查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DEACTIVERATE]] · 去激活用户承载的速率（DEACTIVERATE）

## 使用实例

运营商需要配置UNC主动触发去激活用户承载的速率时，使用该命令。配置用户去激活速率为1000：

```
SET DEACTIVERATE:RATE=1000;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置去激活用户承载的速率（SET-DEACTIVERATE）_09652156.md`
