# 修改cdf token权重（MOD CDFTOKENWEIGHT）

- [命令功能](#ZH-CN_MMLREF_0000001287360196__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001287360196__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001287360196__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001287360196__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001287360196)

![](修改cdf token权重（MOD CDFTOKENWEIGHT）_87360196.assets/notice_3.0-zh-cn_2.png)

当CDFTOKENPOLICY开关配置为使能且修改cdf token权重配置时，会影响各个cgfa-pod与cgfb-pod或cgfa2-pod与cgfb2-pod之间的token权重分配，从而影响话务量均衡。

**适用NF：NCG**

该命令用于修改cdf token权重。

## [注意事项](#ZH-CN_MMLREF_0000001287360196)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001287360196)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001287360196)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | pod 名称 | 可选必选说明：必选参数<br>参数含义：该参数用于描述pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |
| TOKENWEIGHT | token权重 | 可选必选说明：必选参数<br>参数含义：该参数用于描述token权重。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~1000。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001287360196)

当修改pod名称为cgfb-pod-0上的cdf token权重为80：

```
+++    UNC/*MEID:0 MENAME:UNC_VNF_ncg001*/        2022-06-11 15:24:04+8:00
O&M    #3548
%%MOD CDFTOKENWEIGHT: PODNAME="cgfb-pod-0", TOKENWEIGHT=80, CONFIRM=Y;%%
RETCODE = 0  操作成功

---    END
```
