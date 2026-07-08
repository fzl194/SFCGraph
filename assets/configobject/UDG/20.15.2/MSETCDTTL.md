---
id: UDG@20.15.2@ConfigObject@MSETCDTTL
type: ConfigObject
name: MSETCDTTL（租约时长）
nf: UDG
version: 20.15.2
object_name: MSETCDTTL
object_kind: global_setting
status: active
---

# MSETCDTTL（租约时长）

## 说明

![](设置租约时长（SET MSETCDTTL）_48332255.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，频繁配置或配置时长不当会导致CPU升高，请谨慎使用并联系华为技术支持协助操作。

该命令用于设置租约时长。

> **说明**
> - 该命令执行后立即生效。
>
> - 为避免频繁执行对系统性能产生冲击，该命令在三分钟之内只能执行一次。
> - 该命令使用后可以使用[**DSP ETCDTTL**](查询用于仲裁目的的key的租约信息（DSP ETCDTTL）_94730406.md): TYPE=MicroserviceSide;命令查询对租约时长的修改是否生效。
> - 若查询结果和预期不一致，则5min后再查询，若查询结果仍不一致，则需联系华为技术人员定位。
> - 注意：Key值项的构成为"haf/A|B/"或"haf/A|B/C/"，Key值项中A处数字为1~30(包含1和30)，122~128(包含122和128)，大于4096的ETCDTTL不受此命令控制。
>
> - 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：
>
> | TTL |
> | --- |
> | 3 |

## 操作本对象的命令

- [LST MSETCDTTL](command/UDG/20.15.2/LST-MSETCDTTL.md)
- [SET MSETCDTTL](command/UDG/20.15.2/SET-MSETCDTTL.md)

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询租约时长（LST-MSETCDTTL）_48332253.md`
- 原始手册：`evidence/UDG/20.15.2/设置租约时长（SET-MSETCDTTL）_48332255.md`
