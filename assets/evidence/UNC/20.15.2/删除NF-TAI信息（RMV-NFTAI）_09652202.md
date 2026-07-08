# 删除NF TAI信息（RMV NFTAI）

- [命令功能](#ZH-CN_MMLREF_0209652202__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652202__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652202__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652202__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652202)

**适用NF：SMF**

该命令用于删除NF实例的TAI信息。当NF实例不再支持为某个TAI服务时，需要对TAI进行删除。当删除完一个NFINSTANCE关联的所有的NFTAI和TAIRANGELIST后，该NF将会通配支持所有TAI。

## [注意事项](#ZH-CN_MMLREF_0209652202)

- 该命令执行后立即生效。

- 当不输入BINDSMFINFOID时，将删除所有与NFINSTANCENAME，MCC，MNC，TAC匹配的配置。
- 当期望精确删除某一条配置时，BINDSMFINFOID不能为空。

#### [操作用户权限](#ZH-CN_MMLREF_0209652202)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652202)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |
| MCC | 移动国家代码 | 可选必选说明：必选参数<br>参数含义：本参数用于指定TAI的移动国家代码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：<br>本参数由3个十进制数字组成。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：本参数用于指定TAI的移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：<br>本参数由2~3个十进制数字组成。 |
| TAC | 跟踪区域码 | 可选必选说明：必选参数<br>参数含义：本参数用于指定跟踪区域码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是4~6。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>本参数的构成字符只能是字母A～F或a～f、数字0～9。 |
| BINDSMFINFOID | 绑定的SMFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的SMFINFOEXT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>BINDSMFINFOID需要与SMFINFOEXT中的SMFINFOID一致。 |
| BINDNWDAFINFOID | 绑定的NWDAFINFO ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定绑定的NWDAFINFOEXT记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>BINDNWDAFINFOID需要与NWDAFINFOEXT中的ID一致。 |

## [使用实例](#ZH-CN_MMLREF_0209652202)

运营商A需要在标识为SMF_Instance_0的NF实例下删除MCC为460，MNC为01，TAC为000001的TAI信息。

```
RMV NFTAI: NFINSTANCENAME="SMF_Instance_0", MCC="460", MNC="01", TAC="000001";
```
