---
id: UNC@20.15.2@MMLCommand@DSP DRDCI
type: MMLCommand
name: DSP DRDCI（显示DC间通信通道运行状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DRDCI
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP DRDCI（显示DC间通信通道运行状态）

## 功能

该命令用于查询DC间通信通道运行状态。

## 注意事项

- 该命令只用于在UEG-L/UEN网元采用主备（冷备）容灾模式下执行。
- 该命令只用于在UEG-M/UEG网元采用主备（热备）容灾模式下执行。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DRGROUPID | 容灾组标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定容灾组标识。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~8。<br>默认值：无<br>配置原则：<br>可使用<br>[**LST DRGROUPINFO**](查询容灾组信息（LST DRGROUPINFO）_74835153.md)<br>返回的DRGROUPID作为参数输入。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DRDCI]] · DC间通信通道信息（DRDCI）

## 使用实例

查询DC间通信通道运行状态。

```
%%DSP DRDCI:;%%
RETCODE = 0  操作成功
结果如下
--------
容灾组标识      隧道组索引     DC间通信通道状态
1               1              主备容灾实例之间握手成功，处于连接状态                                                              
1               2              主备容灾实例之间握手失败，处于断连状态                                                                                                                         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DRDCI.md`
