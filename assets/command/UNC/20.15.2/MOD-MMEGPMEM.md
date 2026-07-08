---
id: UNC@20.15.2@MMLCommand@MOD MMEGPMEM
type: MMLCommand
name: MOD MMEGPMEM（修改MME群组成员）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MMEGPMEM
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组成员配置
status: active
---

# MOD MMEGPMEM（修改MME群组成员）

## 功能

**适用网元：MME**

此命令用于修改MME群组中的成员记录。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0~63<br>默认值：无 |
| MMEC | MME编码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME编码。<br>数据来源：全网规划<br>取值范围：2位16进制编码<br>默认值：无 |
| CAP | 设备能力 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME负荷能力在MME群组中的相对权重值。权重值越大优先级越高。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |

## 操作的配置对象

- [MME群组成员（MMEGPMEM）](configobject/UNC/20.15.2/MMEGPMEM.md)

## 使用实例

1. 修改MMEGPIDX=1, MMEC="11"的设备能力为2。
  MOD MMEGPMEM: MMEGPIDX=1, MMEC="11", CAP=2;

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改MME群组成员(MOD-MMEGPMEM)_26145624.md`
