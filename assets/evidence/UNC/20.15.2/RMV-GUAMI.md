# 删除AMF全局标识（RMV GUAMI）

- [命令功能](#ZH-CN_MMLREF_0209652172__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652172__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652172__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652172__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652172)

![](删除AMF全局标识（RMV GUAMI）_09652172.assets/notice_3.0-zh-cn_2.png)

执行本命令将触发AMF到NG-RAN的AMF Configuration Update流程，以及AMF到NRF的NF Profile Update流程，从而会导致用户的Inter-AMF注册成功率、被叫成功率大幅下降。故建议在执行本命令前通过STR OFFLOADAMF将用户迁移到Pool内其它AMF。

**适用NF：AMF**

该命令用于删除AMF全局标识符。

## [注意事项](#ZH-CN_MMLREF_0209652172)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209652172)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652172)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INDEX | GUAMI索引 | 可选必选说明：必选参数<br>参数含义：该参数用以在UNC系统内唯一标识某个GUAMI，一个AMF可以最多定义256个GUAMI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0209652172)

删除本AMF与指定GUAMI（索引为9）之间的关联关系，执行如下命令：

```
RMV GUAMI: INDEX=9;
```
