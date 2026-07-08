---
id: UDG@20.15.2@MMLCommand@ADD UPREALMBINDAPN
type: MMLCommand
name: ADD UPREALMBINDAPN（增加APN与Diameter Realm关联关系）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: UPREALMBINDAPN
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新用户生效
is_dangerous: false
max_records: 10000
category_path:
- 用户面服务管理
- Diameter管理
- Diameter Realm
- Realm绑定APN
status: active
---

# ADD UPREALMBINDAPN（增加APN与Diameter Realm关联关系）

## 功能

**适用NF：UPF**

该命令用于DRA部署场景下，配置APN对应的Diameter域信息，或指定根据IMSI构造Diameter域信息。

该配置基于某种应用类型生效。

## 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 每个APN针对特定应用类型仅能配置唯一的Diameter域信息。

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

- [[UDG@20.15.2@ConfigObject@UPREALMBINDAPN]] · APN与Diameter Realm关联关系（UPREALMBINDAPN）

## 使用实例

当没有与UPF直连的Diameter AAA可用，并且通过APN isp接入的用户希望通过Diameter路由在aaa.huawei.com域里来寻找可用的Diameter AAA时，则可以为APN isp的SWM应用绑定Diameter域aaa.huawei.com来达到目的：

```
ADD UPREALMBINDAPN: APN="isp", APPLICATION=SWM, CONSTBYIMSISW=DISABLE, REALMNAME="aaa.huawei.com";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-UPREALMBINDAPN.md`
