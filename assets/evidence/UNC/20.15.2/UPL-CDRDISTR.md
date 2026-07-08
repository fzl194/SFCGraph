# 上传SFTP密钥文件到BS侧（UPL CDRDISTR）

- [命令功能](#ZH-CN_CONCEPT_0251174252__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0251174252__1.3.2.1)
- [本地用户权限](#ZH-CN_CONCEPT_0251174252__1.3.3.1)
- [网管用户权限](#ZH-CN_CONCEPT_0251174252__1.3.4.1)
- [参数说明](#ZH-CN_CONCEPT_0251174252__1.3.5.1)
- [使用实例](#ZH-CN_CONCEPT_0251174252__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0251174252)

**适用NF：NCG**

该命令用于上传SFTP公钥/私钥文件到计费中心或当前网元指定目录:

当使用SFTP协议的PUSH方式连接计费中心侧，并采用密钥方式进行认证时，需要执行此命令将SFTP公钥文件上传到计费中心侧。

密钥方式认证的完整配置过程为：

[**ADD CDRDISTR**](增加话单分发（ADD CDRDISTR）_51174254.md) 添加话单分发任务。

[**UPL CDRDISTR**](上传SFTP密钥文件到BS侧（UPL CDRDISTR）_51174252.md) 产生私钥文件和公钥文件，并将公钥文件上传到计费中心或当前网元指定目录。

#### [注意事项](#ZH-CN_CONCEPT_0251174252)

- 该命令执行后立即生效。
- 为确保系统安全，请定期通过[**UPL CDRDISTR**](上传SFTP密钥文件到BS侧（UPL CDRDISTR）_51174252.md)命令修改密钥文件。
- 密钥认证方式下，默认的私钥文件名命名规则为“私钥文件名_分发任务标识”，公钥文件名命名规则为“私钥文件名_分发任务标识.pub”。
- [**UPL CDRDISTR**](上传SFTP密钥文件到BS侧（UPL CDRDISTR）_51174252.md)命令对PULL分发无效。

#### [本地用户权限](#ZH-CN_CONCEPT_0251174252)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_CONCEPT_0251174252)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0251174252)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDISTRID | 分发任务标识 | 可选必选说明：可选参数<br>参数含义：分发任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 用于上传分发任务标识对应的公钥文件。该参数由增加话单分发([**ADD CDRDISTR**](增加话单分发（ADD CDRDISTR）_51174254.md))命令添加；可使用查询话单分发([**LST CDRDISTR**](查询话单分发（LST CDRDISTR）_51174257.md))命令查询。<br>- 不能输入的特殊字符请参考“[**特殊字符表**](增加话单分发（ADD CDRDISTR）_51174254.md#ZH-CN_CONCEPT_0251174254__table_0365FEF0)”。 |
| RUID | RU的ID | 可选必选说明：必选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| UPLMODE | 公钥上传方式 | 可选必选说明：可选参数<br>参数含义：用于指定SFTP公钥上传的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL：将SFTP公钥上传到CG_RU的“/opt/UNC/*VNFCID*/*RUID*/vrpv8/product/TransFile”目录下。<br>- REMOTE：将SFTP公钥上传到计费中心。<br>默认值：REMOTE<br>配置原则：无<br>说明：如果用户选择上传SFTP公钥到远端，系统会将生成的公钥追加到登录远端的用户的home目录的.ssh/authorized_keys。请确认远端SFTP配置文件中属性AuthorizedKeysFile的值是否为.ssh/authorized_keys，如果该属性的值为其他值则需要手动配置密钥文件。操作方法请联系华为技术支持支撑。 |

#### [使用实例](#ZH-CN_CONCEPT_0251174252)

上传RUID为64的公钥文件到计费中心：

```
UPL CDRDISTR: RUID=64;
2017-04-21 09:13:18.87  The dst_key_9 upload keyfile to 192.168.40.64 success.
Total upload  1  Successed  1  Failed  0
共有4个报告
---    END
```
