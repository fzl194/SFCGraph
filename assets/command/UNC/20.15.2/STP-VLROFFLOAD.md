---
id: UNC@20.15.2@MMLCommand@STP VLROFFLOAD
type: MMLCommand
name: STP VLROFFLOAD（停止VLR迁移任务）
nf: UNC
version: 20.15.2
verb: STP
object_keyword: VLROFFLOAD
command_category: 动作类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- MSC POOL管理
- VLR迁移任务
status: active
---

# STP VLROFFLOAD（停止VLR迁移任务）

## 功能

**适用网元：SGSN、MME**

此命令用于停止与本局SGSN或MME相连的MSC POOL中VLR的迁移。

## 注意事项

- 此命令执行后立即生效。
- 如果停止VLR迁移失败，请检查是否在迁移期间执行了增加、删除或修改了VLR或LAIVLR记录的命令。如果有，请把VLR或LAIVLR记录修改为和迁移启动时一致，再尝试停止VLR迁移。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VN | VLR号 | 可选必选说明：必选参数<br>参数含义：待停止迁移的VLR号，表示VLR在移动网络中的设备号。<br>取值范围：1～15位数字<br>默认值：无 |

## 操作的配置对象

- [VLR迁移任务（VLROFFLOAD）](configobject/UNC/20.15.2/VLROFFLOAD.md)

## 使用实例

停止与本局SGSN或MME相连的MSC POOL中一个VLR的迁移，VLR号码为8613900211：

STP VLROFFLOAD: VN="8613900211";

## 证据

- 原始手册：`evidence/UNC/20.15.2/停止VLR迁移任务(STP-VLROFFLOAD)_72225103.md`
