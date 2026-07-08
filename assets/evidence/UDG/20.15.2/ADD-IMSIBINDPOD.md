# 增加IMSI和Pod绑定关系（ADD IMSIBINDPOD）

- [命令功能](#ZH-CN_CONCEPT_0264015275__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0264015275__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0264015275__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0264015275__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0264015275__1.3.5.1)

#### [命令功能](#ZH-CN_CONCEPT_0264015275)

**适用NF：SGW-U、PGW-U、UPF**

用于将某IMSI的用户绑定到特定的POD上激活。

本命令通常是在现网扩容需要测试新扩容的POD是否能够正常工作时使用，不建议用于日常场景。

#### [注意事项](#ZH-CN_CONCEPT_0264015275)

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10。
- 配置的POD不存在或异常时，用户会激活失败。
- 拨测完毕需要手动删除拨测配置。
- 只支持绑定spu-pod或isu-pod。

#### [操作用户权限](#ZH-CN_CONCEPT_0264015275)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0264015275)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSI | IMSI | 可选必选说明：必选参数<br>参数含义：用户的IMSI信息。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。<br>默认值：无<br>配置原则：无 |
| PODNAME | Pod 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

#### [使用实例](#ZH-CN_CONCEPT_0264015275)

当需要添加IMSI 1234567890与ssgpod-0的绑定关系时，进行如下设置：

```
ADD IMSIBINDPOD: IMSI="123456789", PODNAME="ssgpod-0";
```
