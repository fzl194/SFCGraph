# 配置base链路亚健康信息（SET BASESUBHEALTH）

- [命令功能](#ZH-CN_CONCEPT_0000001097738016__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001097738016__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001097738016__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001097738016__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001097738016__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001097738016)

该命令用于配置base亚健康信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001097738016)

- 该命令执行后立即生效。
- 如果带检查周期、统计周期、通信亚健康阈值参数下发去使能命令时，只有去使能生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| DETECTINTERVAL | STATISINTERVAL | THRESHOLD | ENABLEFLAG |
| --- | --- | --- | --- |
| 1 | 30 | 50 | Enable |

#### [操作用户权限](#ZH-CN_CONCEPT_0000001097738016)

G_1，管理员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001097738016)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DETECTINTERVAL | 检测周期 (s) | 可选必选说明：可选参数<br>参数含义：base面亚健康探测报文检测周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10，单位是秒。<br>默认值：无 |
| STATISINTERVAL | 统计周期 (s) | 可选必选说明：可选参数<br>参数含义：base面亚健康探测统计周期。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为10～180，单位是秒。<br>默认值：无 |
| THRESHOLD | 亚健康阈值 (千分比) | 可选必选说明：可选参数<br>参数含义：base面亚健康告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～1000。<br>默认值：无 |
| ENABLEFLAG | 使能标志 | 可选必选说明：必选参数<br>参数含义：亚健康使能标志。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Disable：去使能。<br>- Enable：使能。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001097738016)

配置base亚健康信息：

```
SET BASESUBHEALTH:ENABLEFLAG=Enable, DETECTINTERVAL=5, STATISINTERVAL=45, THRESHOLD=80
,SERVICEINSTANCE="vnfc"
;
```
