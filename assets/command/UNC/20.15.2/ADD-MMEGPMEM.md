---
id: UNC@20.15.2@MMLCommand@ADD MMEGPMEM
type: MMLCommand
name: ADD MMEGPMEM（增加MME群组成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MMEGPMEM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 1024
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组成员配置
status: active
---

# ADD MMEGPMEM（增加MME群组成员）

## 功能

**适用网元：MME**

此命令用于为 [**ADD MMEGP**](../MME群组配置/增加MME群组(ADD MMEGP)_72225301.md) 增加的MME群组添加一条成员记录。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为1024。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无<br>配置原则：<br>- “MME群组索引”已在[**ADD MMEGP**](../MME群组配置/增加MME群组(ADD MMEGP)_72225301.md)中配置。 |
| MMEC | MME编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME组内的MME编码。<br>前提条件：无<br>数据来源：全网规划<br>取值范围：2位16进制编码<br>默认值：无<br>配置原则：<br>- 每个“MME群组索引”下最多配置32个MMEC。<br>- 每个“MME群组索引”下配置的MMEC不能重复。 |
| CAP | 设备能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME负荷能力在MME群组中的相对权重值。权重值越大优先级越高。<br>前提条件：无<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：255<br>配置原则：<br>- MME群组中的MME成员的设备能力可以根据此参数进行调节。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MMEGPMEM]] · MME群组成员（MMEGPMEM）

## 使用实例

1. 增加MME群组索引 =1，MME编码 =11，设备能力 =255的记录。
  ADD MMEGPMEM: MMEGPIDX=1, MMEC="11";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-MMEGPMEM.md`
