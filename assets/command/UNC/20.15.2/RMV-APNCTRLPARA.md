---
id: UNC@20.15.2@MMLCommand@RMV APNCTRLPARA
type: MMLCommand
name: RMV APNCTRLPARA（删除基于APN的信令控制参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: APNCTRLPARA
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- M2M管理
- 基于APN的信令控制参数
status: active
---

# RMV APNCTRLPARA（删除基于APN的信令控制参数）

## 功能

**适用网元：SGSN**

该命令用于删除基于APN的信令控制参数。

指定APN组删除信令控制参数以后，该APN组中的用户信令控制功能关闭。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APNGRPID | APNNI组号 | 可选必选说明：必选参数<br>参数含义：本参数用于指定开启APN信令控制功能的APNNI组号。<br>数据来源：全网规划<br>取值范围：0～15<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNCTRLPARA]] · 基于APN的信令控制参数（APNCTRLPARA）

## 使用实例

删除 “APNNI组号” 为 “0” 的信令控制参数：

RMV APNCTRLPARA: APNGRPID=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNCTRLPARA.md`
