---
id: UDG@20.15.2@MMLCommand@SET TOHVXLANPARA
type: MMLCommand
name: SET TOHVXLANPARA（设置家庭网关业务使用VXLAN隧道传输业务参数配置）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOHVXLANPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 路径管理
- VXLAN路径管理
- 家庭网关VXLAN隧道参数
status: active
---

# SET TOHVXLANPARA（设置家庭网关业务使用VXLAN隧道传输业务参数配置）

## 功能

**适用NF：UPF**

![](设置家庭网关业务使用VXLAN隧道传输业务参数配置（SET TOHVXLANPARA）_78279090.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改SRCINTF和SRCMAC可能会导致家庭网关业务不通。

该命令用于设置家庭网关业务使用VXLAN隧道传输业务参数配置。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 如果未配置VXLAN链路源端逻辑接口，则默认使用逻辑口swuif1/0/0，并且心跳检测功能自动关闭。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | VXLANTNLSW |
| --- | --- |
| 初始值 | DISABLE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VXLANTNLSW | VXLAN隧道开关 | 可选必选说明：必选参数<br>参数含义：该参数用于是配置家庭网关业务使用VXLAN隧道进行数据报文传输的开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| SRCINTF | VXLAN隧道源接口 | 可选必选说明：条件可选参数<br>前提条件：该参数在“VXLANTNLSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置VXLAN链路源端逻辑接口名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD LOGICINF命令配置生成。<br>- 该参数不配置时默认使用逻辑口swuif1/0/0。 |
| SRCMAC | VXLAN隧道源端MAC地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“VXLANTNLSW”配置为“ENABLE”时为必选参数。<br>参数含义：该参数用于配置VXLAN链路源端MAC地址。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度为17位。字符串应符合MAC地址格式，如11-11-11-11-11-11。<br>默认值：无<br>配置原则：建议该逻辑接口对应的物理接口的MAC地址作为VXLAN隧道源端的MAC地址，以免MAC地址冲突。 |
| VGWIPV4ADDR | 虚拟网关IPv4地址 | 可选必选说明：条件可选参数<br>前提条件：该参数在“VXLANTNLSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于配置虚拟网关IPv4地址，用于向家庭网关发送免费ARP时作为虚拟网关地址携带。<br>数据来源：全网规划<br>取值范围：该虚拟网关地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。该地址必须是A、B或者C类地址。<br>默认值：无<br>配置原则：当UPF与家庭网关（FTTR）之间进行使用VxLAN隧道传输业务时，需要配置该虚拟网关地址，该IP地址会在家庭网关设备（FTTR）作为数据转发的下一跳地址进行配置，需要运营商统一规划，建议在用户IP地址池中预留。 |
| SENDARPTIMER | 免费ARP发送定时器时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“VXLANTNLSW”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于控制发送免费ARP的定时器时长。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为60～86400。单位是秒。<br>默认值：270<br>配置原则：无 |
| HEARTBEAT | 心跳检测开关 | 可选必选说明：条件可选参数<br>前提条件：该参数在“VXLANTNLSW”配置为“ENABLE”时为可选参数。<br>参数含义：VXLAN隧道端点心跳检测开关。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：ENABLE<br>配置原则：无 |
| TIMETHRESHOLD | 时间阈值（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEARTBEAT”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置两次心跳检测间的时间阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～60，单位是秒。<br>默认值：6<br>配置原则：无 |
| HEARTSUCCLIMIT | 心跳检测成功次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEARTBEAT”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置VXLAN链路状态为up所需的心跳检测连续成功次数。当VXLAN链路状态为down且心跳检测连续成功次数达到这个值时，将链路的状态置为up。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：3<br>配置原则：无 |
| HEARTFAILLIMIT | 心跳检测失败次数 | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEARTBEAT”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置VXLAN链路状态为down所需的心跳检测连续失败次数。当VXLAN链路状态为up且心跳检测连续失败达到这个值时，下次发送心跳检测报文前将链路的状态置为down。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：3<br>配置原则：无 |
| TIMEOUT | Ping探测超时时长（秒） | 可选必选说明：条件可选参数<br>前提条件：该参数在“HEARTBEAT”配置为“ENABLE”时为可选参数。<br>参数含义：该参数用于设置心跳检测的超时时长，该值需要小于TIMETHRESHOLD。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～59，单位是秒。<br>默认值：2<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOHVXLANPARA]] · 家庭网关业务使用VXLAN隧道传输业务参数配置（TOHVXLANPARA）

## 使用实例

配置VXLAN隧道传输业务参数：

```
SET TOHVXLANPARA: VXLANTNLSW=ENABLE, SRCMAC="28-6E-D4-89-91-40", VGWIPV4ADDR="192.168.123.166", HEARTBEAT=DISABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置家庭网关业务使用VXLAN隧道传输业务参数配置（SET-TOHVXLANPARA）_78279090.md`
