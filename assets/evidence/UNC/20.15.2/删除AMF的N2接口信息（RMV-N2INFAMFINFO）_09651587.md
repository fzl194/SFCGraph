# 删除AMF的N2接口信息（RMV N2INFAMFINFO）

- [命令功能](#ZH-CN_MMLREF_0209651587__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209651587__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209651587__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209651587__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209651587)

**适用NF：AMF**

该命令用于删除当前AMF的N2接口信息。

## [注意事项](#ZH-CN_MMLREF_0209651587)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0209651587)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209651587)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |

## [使用实例](#ZH-CN_MMLREF_0209651587)

运营商A需要删掉当前AMF的N2接口信息。

```
RMV N2INFAMFINFO: NFINSTANCENAME="AMF_Instance_0";
```
