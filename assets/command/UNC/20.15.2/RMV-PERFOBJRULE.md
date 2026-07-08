---
id: UNC@20.15.2@MMLCommand@RMV PERFOBJRULE
type: MMLCommand
name: RMV PERFOBJRULE（删除性能对象规则）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFOBJRULE
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
- 操作维护
- 性能管理
- 性能对象规则管理
status: active
---

# RMV PERFOBJRULE（删除性能对象规则）

## 功能

**适用网元：SGSN、MME**

本命令用于删除特定对象的统计规则，当前仅支持TAI组规则。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MOC | 测量对象类型 | 可选必选说明：必选参数<br>参数含义：待删除规则的测量统计对象类型。<br>取值范围：<br>- “TAIGP(TAI组)”<br>默认值：无 |
| TAIGPRULEIDX | TAI组规则索引 | 可选必选说明：条件必选参数<br>参数含义：待删除的TAI组规则的索引。<br>前提条件：该参数在<br>“MOC(测量对象类型)”<br>参数设置为<br>“TAIGP(TAI组)”<br>时，才需要配置。<br>取值范围：1~1500<br>默认值：无<br>配置原则：TAI组规则索引，可以通过<br>[**LST PERFOBJRULE**](查询性能对象规则(LST PERFOBJRULE)_26146196.md)<br>命令查询。<br>说明：执行删除规则操作后，符合该规则的当前系统存在的TAI，将会增加为自动统计的TAI对象。系统最多能支持1500个TAI组对象的统计，当自动统计的TAI对象超出该规格后，将无法添加。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFOBJRULE]] · 性能对象规则（PERFOBJRULE）

## 使用实例

删除规则索引为1的TAI组规则：

RMV PERFOBJRULE: MOC=TAIGP, TAIGPRULEIDX=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFOBJRULE.md`
