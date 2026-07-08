# 设置QosGlobal配置（SET QOSGLOBAL）

- [命令功能](#ZH-CN_CONCEPT_0182837660__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0182837660__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0182837660__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0182837660__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0182837660__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0182837660)

**适用NF：UPF**

该命令设置QosGlobal配置。用来设置全局的QoS信息，包括QoS功能配置，上下行带宽比，具有最高优先级的non-GBR QCI值以及QoS Profile名。

#### [注意事项](#ZH-CN_CONCEPT_0182837660)

- 为了防止频繁刷新规则对系统造成性能影响，识别规则添加、修改、删除后，不会立即生效，当最后一次执行本命令90秒后所有规则才生效。
- 该命令最大记录数为1。
- 该命令配置当前不支持。2、开启后将导致性能下降。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | QOSFUNCTION | DOWNUPBWRATIO | HIGHESTNGBRQCI | QOSPROFILENAME | HIGPTTNGBRQCI |
| --- | --- | --- | --- | --- | --- |
| 初始值 | DISABLE | 3 | 5 | globalqos | 69 |

#### [操作用户权限](#ZH-CN_CONCEPT_0182837660)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0182837660)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSFUNCTION | QoS功能开关 | 可选必选说明：可选参数<br>参数含义：该参数配置整机使能和去使能用户QoS功能。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不使能。<br>- ENABLE：使能。<br>默认值：无<br>配置原则：无 |
| DOWNUPBWRATIO | 下行与上行带宽比例 | 可选必选说明：可选参数<br>参数含义：该参数是下行与上行带宽比例。例如取值为2则表示下行与上行带宽的比例为2:1。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为2～10。<br>默认值：无<br>配置原则：无 |
| HIGHESTNGBRQCI | 具有最高优先级的non-GBR QCI值 | 可选必选说明：可选参数<br>参数含义：该参数表示具有最高优先级的non-GBR QCI值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为5～9。<br>默认值：无<br>配置原则：无 |
| QOSPROFILENAME | QoS Profile名 | 可选必选说明：可选参数<br>参数含义：该参数是QoS模板名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：输入单空格将删除该参数已有配置项。 |
| HIGPTTNGBRQCI | 具有最高优先级的non-GBR PTT QCI值 | 可选必选说明：可选参数<br>参数含义：该参数表示具有最高优先级的non-GBR PTT QCI值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围为69～70。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0182837660)

假设运营商需要配置QoS功能开启，上下行带宽比以及具有最高优先级的non-GBR QCI值时，设置QosGlobal配置：

```
SET QOSGLOBAL:QOSFUNCTION=ENABLE,DOWNUPBWRATIO=3,HIGHESTNGBRQCI=5,QOSPROFILENAME="test";
```
