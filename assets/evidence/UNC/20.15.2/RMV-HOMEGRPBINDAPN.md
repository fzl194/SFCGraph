# 删除Home Group和APN的绑定关系（RMV HOMEGRPBINDAPN）

- [命令功能](#ZH-CN_MMLREF_0000001142853268__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001142853268__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001142853268__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001142853268__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001142853268)

**适用NF：PGW-C、GGSN**

该命令用于删除APN与Home Group的绑定关系。

## [注意事项](#ZH-CN_MMLREF_0000001142853268)

- 该命令执行后立即生效。

- 该命令不指定Home Group时，表示解除指定APN与所有已绑定Home Group的绑定关系。
- 该命令指定Home Group时，表示解除指定APN与指定Home Group的绑定关系。

#### [操作用户权限](#ZH-CN_MMLREF_0000001142853268)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001142853268)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN实例名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>该参数使用ADD APN命令配置生成。 |
| HOMEGROUPINDX | Home Group编号 | 可选必选说明：可选参数<br>参数含义：该参数用来设置Home Group的编号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：<br>该参数使用ADD HOMEGROUP命令配置生成。 |

## [使用实例](#ZH-CN_MMLREF_0000001142853268)

- 删除“APN”为“huawei.com”，“Home Group编号”为“1”的Home Group和APN的绑定关系配置：
  ```
  LST HOMEGRPBINDAPN: APN="huaweit.com", HOMEGROUPINDX=1;
  ```
- 删除“APN”为“huawei.com”的全部Home Group和APN的绑定关系配置：
  ```
  LST HOMEGRPBINDAPN: APN="huaweit.com";
  ```
