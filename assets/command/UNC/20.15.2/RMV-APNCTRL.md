---
id: UNC@20.15.2@MMLCommand@RMV APNCTRL
type: MMLCommand
name: RMV APNCTRL（删除APN控制参数配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNCTRL
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- 基于APN的MM拥塞控制_流控_寻呼优化配置
status: active
---

# RMV APNCTRL（删除APN控制参数配置）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一条或多条APN信令拥塞控制和固定终端寻呼优化的APN控制参数配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令中如果输入了“SUBSCRIBEDAPN（签约APN）”，则删除指定APN对应的配置；如果没有输入“SUBSCRIBEDAPN（签约APN）”，则删除所有的APN控制参数配置，此时基于APN的信令拥塞控制和固定终端寻呼优化相关的控制全部解除，可能无法对网络中的拥塞进行控制。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBEDAPN | 签约APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>“签约APN”<br>。<br>取值范围：1~62位字符串<br>默认值：无<br>说明：“SUBSCRIBEDAPN（签约APN）”<br>（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCTRL]] · APN控制参数配置（APNCTRL）

## 使用实例

删除一条 “签约APN” 为 “huawei.com” 的APN控制参数配置：

RMV APNCTRL: SUBSCRIBEDAPN="huawei.com";

删除全部的APN控制参数配置：

RMV APNCTRL:;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNCTRL.md`
