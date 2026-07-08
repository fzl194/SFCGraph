---
id: UNC@20.15.2@MMLCommand@LST NRFGRTIMER
type: MMLCommand
name: LST NRFGRTIMER（查询NRF容灾定时器时长）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFGRTIMER
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- 定时器参数
status: active
---

# LST NRFGRTIMER（查询NRF容灾定时器时长）

## 功能

**适用NF：NRF**

该命令已废弃。

该命令用于查询NRF容灾定时器时长信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRTRAFFICTIMER | 流量统计定时器时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数表示NRF容灾流量统计定时器时长，统计的是对接到这个NRF上所有的NF的流量。NRF在该定时器时长周期内统计NF发送的注册、去注册、更新消息，用于协助NRF进行主备倒换。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~86400，单位是秒。<br>默认值：无<br>配置原则：无 |
| NRFGRFAULTTIMER | NRF故障检测时长(秒) | 可选必选说明：可选参数<br>参数含义：该参数表示主备NRF的业务故障检测时长。若NRF在检测时长周期内无法正常处理业务，则认为该NRF故障，触发NRF主备倒换协商。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是30~1800，单位是秒。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [NRF容灾定时器时长（NRFGRTIMER）](configobject/UNC/20.15.2/NRFGRTIMER.md)

## 使用实例

查询NRF容灾定时器时长信息：

```
%%LST NRFGRTIMER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
流量统计定时器时长(秒)  =  15
   NRF故障检测时长(秒)  =  300
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NRF容灾定时器时长（LST-NRFGRTIMER）_09654171.md`
