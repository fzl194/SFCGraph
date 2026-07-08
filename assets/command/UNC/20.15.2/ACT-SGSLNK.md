---
id: UNC@20.15.2@MMLCommand@ACT SGSLNK
type: MMLCommand
name: ACT SGSLNK（激活SGs链路）
nf: UNC
version: 20.15.2
verb: ACT
object_keyword: SGSLNK
command_category: 动作类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路管理
status: active
---

# ACT SGSLNK（激活SGs链路）

## 功能

**适用网元：MME**

此命令用于激活指定的SGs链路。当需要恢复被 [**DEA SGSLNK**](去活SGs链路(DEA SGSLNK)_72225117.md) 命令去激活的SGs链路时，可以通过此命令进行重新激活。

## 注意事项

- 此命令执行后立即生效。
- 激活链路前请通过[**DSP SGSLNK**](显示SGs链路状态(DSP SGSLNK)_72345033.md)查询链路状态。
- 链路只有通过[**DEA SGSLNK**](去活SGs链路(DEA SGSLNK)_72225117.md)命令去活后处于去激活状态时，才能进行激活操作。链路处于激活态时，禁止执行该操作。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNK | 链路索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待激活链路的索引。<br>取值范围：0~511<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSLNK]] · SGs链路（SGSLNK）

## 使用实例

激活链路索引为1的SGs链路：

ACT SGSLNK: LNK=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ACT-SGSLNK.md`
