---
id: UNC@20.15.2@MMLCommand@DSP HTTPLINKHISTORY
type: MMLCommand
name: DSP HTTPLINKHISTORY（显示HTTP历史链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: HTTPLINKHISTORY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- HTTP功能管理
- HTTP管理
- HTTP链路管理
status: active
---

# DSP HTTPLINKHISTORY（显示HTTP历史链路状态）

## 功能

该命令用于显示HTTP历史链路状态。

## 注意事项

每个进程可以查询最多50条历史记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定HTTP链路所在的POD名称。该POD名称可通过<br>[**DSP HTTPPROCESS**](../HTTP进程状态管理/显示HTTP进程信息（DSP HTTPPROCESS）_29053327.md)<br>命令查询获取。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@HTTPLINKHISTORY]] · HTTP历史链路状态（HTTPLINKHISTORY）

## 使用实例

查询HTTP历史链路信息，可以执行下面的命令。

```
%%DSP HTTPLINKHISTORY:;%%
RETCODE = 0  操作成功

结果如下
--------
POD名称                    进程标识  源IPv4地址  目的IPv4地址  源IPv6地址          目的IPv6地址          接口类型  状态变更  时间戳                

sbim-pod-569958b9c5-4sk5b  17        NULL        NULL          [fe80::]:31000  [fe80::5]:50112     SBI       DOWN->UP  08:29:24  2021/07/24  
sbim-pod-569958b9c5-4sk5b  20        NULL        NULL          [fe80::]:31000  [fe80::5]:50112     SBI       DOWN->UP  08:28:44  2021/07/24  
sbim-pod-569958b9c5-4sk5b  20        NULL        NULL          [fe80::]:31000  [fe80::5]:50112     SBI       UP->DOWN  08:29:24  2021/07/24  
sbim-pod-569958b9c5-4blqr  20        NULL        NULL          [fe80::]:31000  [fe80::5]:50151     SBI       DOWN->UP  08:27:36  2021/07/24  
sbim-pod-569958b9c5-4blqr  20        NULL        NULL          [fe80::]:31000  [fe80::5]:49109     SBI       DOWN->UP  08:28:45  2021/07/24   

共有5个结果
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-HTTPLINKHISTORY.md`
