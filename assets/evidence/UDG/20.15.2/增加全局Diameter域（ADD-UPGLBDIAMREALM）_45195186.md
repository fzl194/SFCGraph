# 增加全局Diameter域（ADD UPGLBDIAMREALM）

- [命令功能](#ZH-CN_CONCEPT_0000206145195186__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000206145195186__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000206145195186__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000206145195186__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000206145195186__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000206145195186)

**适用NF：UPF**

该配置基于某种应用类型生效。

#### [注意事项](#ZH-CN_CONCEPT_0000206145195186)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为1024。

#### [操作用户权限](#ZH-CN_CONCEPT_0000206145195186)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000206145195186)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPLICATION | Diameter应用 | 可选必选说明：必选参数<br>参数含义：该参数用于指定全局Diameter域所属的Diameter应用。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- SWM：SWM接口应用。<br>默认值：无<br>配置原则：根据实际应用场景选择对应的枚举值。 |
| CONSTBYIMSISW | 根据IMSI构造归属地Realm开关 | 可选必选说明：必选参数<br>参数含义：该参数用于指定是否使能根据IMSI构造Peer的归属地Diameter域名。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：当选择ENABLE时，将通过IMSI构造Diameter域，构造格式为“epc.mnc<MNC>.mcc<MCC>.3gppnetwork.org”。 |
| REALM | Diameter域名 | 可选必选说明：条件必选参数<br>前提条件：该参数在“CONSTBYIMSISW”配置为“DISABLE”时为必选参数。<br>参数含义：该参数用于指定与号段绑定的Diameter域名或者缺省的Diameter域名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT2670控制是否区分大小写。<br>默认值：无<br>配置原则：<br>- 当根据IMSI构造归属地Realm开关设置为ENABLE时，该参数无效。<br>- 当根据IMSI构造归属地Realm开关设置为DISABLE时，必须手动指定Diameter域。 |

#### [使用实例](#ZH-CN_CONCEPT_0000206145195186)

如果希望开启全局缺省Diameter域aaa.huawei.com，可以按以下方式配置：

```
ADD UPGLBDIAMREALM:APPLICATION=SWM,CONSTBYIMSISW=DISABLE,REALM="aaa.huawei.com";
```
