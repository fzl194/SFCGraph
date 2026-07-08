---
id: UNC@20.15.2@MMLCommand@RMV LOCALHLR
type: MMLCommand
name: RMV LOCALHLR（删除本地HLR）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LOCALHLR
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
- 网络管理
- LOCALHLR管理
status: active
---

# RMV LOCALHLR（删除本地HLR）

## 功能

**适用网元：SGSN、MME**

该命令用于删除一条本地HLR。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HLRIDX | 本地HLR索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定HLR索引。<br>数据来源：整网规划<br>取值范围：1~256<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LOCALHLR]] · 本地HLR（LOCALHLR）

## 使用实例

删除索引为1的本地HLR信息:

RMV LOCALHLR: HLRIDX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LOCALHLR.md`
