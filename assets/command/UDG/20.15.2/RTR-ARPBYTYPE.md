---
id: UDG@20.15.2@MMLCommand@RTR ARPBYTYPE
type: MMLCommand
name: RTR ARPBYTYPE（根据ARP表项类型清除ARP表项）
nf: UDG
version: 20.15.2
verb: RTR
object_keyword: ARPBYTYPE
command_category: 动作类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- ARP管理
- ARP表项统计查询
status: active
---

# RTR ARPBYTYPE（根据ARP表项类型清除ARP表项）

## 功能

![](根据ARP表项类型清除ARP表项（RTR ARPBYTYPE）_50280966.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除设备上的动态表项。当非法用户发送大量ARP报文攻击目标设备时，会导致设备在短时间学习到大量的ARP信息，导致ARP表项缓存溢出，影响合法用户使用网络。为了解决这样的问题，用户可以执行此命令对ARP表项进行维护，重新建立ARP表项，从而保证合法用户正常使用网络。

## 注意事项

- 该命令执行后立即生效。
- 该操作会清除所有动态ARP表项，可能导致业务中断。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CLEARARPTYPE | 清除类型 | 可选必选说明：必选参数<br>参数含义：清除ARP表项的类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ClearDynamicArp：清除所有动态表项。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ARPBYTYPE]] · 根据ARP表项类型清除ARP表项（ARPBYTYPE）

## 使用实例

清除设备上的ARP动态表项：

```
RTR ARPBYTYPE:CLEARARPTYPE=ClearDynamicArp;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/根据ARP表项类型清除ARP表项（RTR-ARPBYTYPE）_50280966.md`
