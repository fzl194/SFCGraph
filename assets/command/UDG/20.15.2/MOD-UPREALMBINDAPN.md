---
id: UDG@20.15.2@MMLCommand@MOD UPREALMBINDAPN
type: MMLCommand
name: MOD UPREALMBINDAPN（修改APN与Diameter Realm关联关系）
nf: UDG
version: 20.15.2
verb: MOD
object_keyword: UPREALMBINDAPN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: true
category_path:
- 用户面服务管理
- Diameter管理
- Diameter Realm
- Realm绑定APN
status: active
---

# MOD UPREALMBINDAPN（修改APN与Diameter Realm关联关系）

## 功能

**适用NF：UPF**

![](修改APN与Diameter Realm关联关系（MOD UPREALMBINDAPN）_45432702.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，该操作会修改APN与Diameter Realm的关联关系，可能会影响DRA的选择。

该命令用于修改APN对应的Diameter域信息，或指定根据IMSI构造Diameter域信息。

## 注意事项

该命令执行后只对新激活用户生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定要与Diameter域绑定的APN实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN绑定Diameter域的Diameter应用类型。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：根据实际应用场景选择对应的枚举值。 |
| CONSTBYIMSISW | 根据IMSI构造归属地Realm开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能根据IMSI构造Peer的归属地域名。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：当选择ENABLE时，将通过IMSI构造Diameter域，构造格式为“epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。 |
| REALMNAME | Realm名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONSTBYIMSISW”配置为“DISABLE”时为必选参数。<br>参数含义：该参数用于指定与APN关联的Diameter域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT2670控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 当根据IMSI构造归属地Realm开关设置为ENABLE时，该参数无效。<br>- 当根据IMSI构造归属地Realm开关设置为DISABLE时，必须手动指定Diameter域。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/UPREALMBINDAPN]] · APN与Diameter Realm关联关系（UPREALMBINDAPN）

## 使用实例

因为网络布局改变，之前指定的Diameter域已经不存在，新策略是根据IMSI来作为Diameter域，因此修改APN isp下的SWM应用根据IMSI构造归属地Diameter域名：

```
MOD UPREALMBINDAPN: APN="isp", APPLICATION=SWM, CONSTBYIMSISW=ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/修改APN与Diameter-Realm关联关系（MOD-UPREALMBINDAPN）_45432702.md`
