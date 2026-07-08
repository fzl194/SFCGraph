# 删除cdf token权重（RMV CDFTOKENWEIGHT）

- [命令功能](#ZH-CN_MMLREF_0000001339919397__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001339919397__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001339919397__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001339919397__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001339919397)

![](删除cdf token权重（RMV CDFTOKENWEIGHT）_39919397.assets/notice_3.0-zh-cn_2.png)

当CDFTOKENPOLICY开关配置为使能且删除cdf token权重配置时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于删除cdf token权重配置。

## [注意事项](#ZH-CN_MMLREF_0000001339919397)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001339919397)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001339919397)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | pod 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于描述pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001339919397)

当删除pod名称为cgfb-pod-0上的cdf token权重配置：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-06-11 15:20:20+8:00
O&M    #3546
%%RMV CDFTOKENWEIGHT: PODNAME="cgfb-pod-0", CONFIRM=Y;%%
RETCODE = 0  操作成功

---    END
```
