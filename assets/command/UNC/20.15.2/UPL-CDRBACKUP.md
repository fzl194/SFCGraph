---
id: UNC@20.15.2@MMLCommand@UPL CDRBACKUP
type: MMLCommand
name: UPL CDRBACKUP（上传SFTP密钥文件到第三方服务器）
nf: UNC
version: 20.15.2
verb: UPL
object_keyword: CDRBACKUP
command_category: 动作类
applicable_nf:
- NCG
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单备份
status: active
---

# UPL CDRBACKUP（上传SFTP密钥文件到第三方服务器）

## 功能

**适用NF：NCG**

该命令用于将SFTP的公钥文件上传到第三方服务器、UDN服务器或当前网元指定目录。

当局点配置话单备份到UDN服务器时，此时UDN作为第三方服务器，NCG可以根据需要，执行此命令将公钥文件上传到UDN服务器。

当使用SFTP协议连接第三方服务器，并采用密钥方式进行认证时，需要使用此命令。

密钥方式认证的完整配置过程为：

[**ADD CDRBACKUP**](增加话单备份（ADD CDRBACKUP）_51174244.md) 添加话单备份任务。

[**UPL CDRBACKUP**](上传SFTP密钥文件到第三方服务器（UPL CDRBACKUP）_51174249.md) 产生私钥文件和公钥文件，并将公钥文件上传到第三方服务器或当前网元指定目录。

## 注意事项

- 该命令执行后立即生效。
- 为确保系统安全，请定期通过[**UPL CDRBACKUP**](上传SFTP密钥文件到第三方服务器（UPL CDRBACKUP）_51174249.md)命令修改密钥文件。
- 密钥认证方式下，默认的私钥文件名命名规则为“私钥文件名_备份任务标识”，公钥文件名命名规则为“私钥文件名_备份任务标识.pub”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BACKUPID | 备份任务标识 | 可选必选说明：可选参数<br>参数含义：备份任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：<br>- 该参数只能由字母、数字、下划线、中划线组成。<br>- 用于上传备份任务标识对应的公钥文件。该参数由增加话单备份([**ADD CDRBACKUP**](增加话单备份（ADD CDRBACKUP）_51174244.md))命令定义。 |
| RUID | RU的ID | 可选必选说明：必选参数<br>参数含义：RU的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为64～4294967294。<br>默认值：无<br>配置原则：该值需要执行<br>[**LST SERVICERUSTATE**](../../../../../平台服务管理/单体服务编排功能管理/系统管理/资源管理/RU信息/查询RU的信息(LST SERVICERUSTATE)_29626965.md)<br>命令，查询出存在的RU ID进行填写。 |
| UPLMODE | 公钥上传方式 | 可选必选说明：可选参数<br>参数含义：用于指定SFTP公钥上传的方式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL：将SFTP公钥上传到CG_RU的“/opt/UNC/*VNFCID*/*RUID*/vrpv8/product/TransFile”目录下。<br>- REMOTE：将SFTP公钥上传到计费中心。<br>默认值：REMOTE<br>配置原则：无<br>说明：如果用户选择上传SFTP公钥到远端，系统会将生成的公钥追加到登录远端的用户的home目录的.ssh/authorized_keys。请确认远端SFTP配置文件中属性AuthorizedKeysFile的值是否为.ssh/authorized_keys，如果该属性的值为其他值则需要手动配置密钥文件。操作方法请联系华为技术支持支撑。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRBACKUP]] · 上传SFTP密钥文件到第三方服务器（CDRBACKUP）

## 使用实例

上传RUID为64的公钥文件到计费中心：

```
UPL CDRBACKUP: RUID=64;
2017-04-21 09:14:18.77  The cbk_key_5 upload keyfile to 192.168.40.64 success.
Total upload  1  Successed  1  Failed  0
共有4个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/UPL-CDRBACKUP.md`
