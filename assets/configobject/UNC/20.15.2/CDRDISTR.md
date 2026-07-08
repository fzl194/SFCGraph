---
id: UNC@20.15.2@ConfigObject@CDRDISTR
type: ConfigObject
name: CDRDISTR（上传SFTP密钥文件到BS侧）
nf: UNC
version: 20.15.2
object_name: CDRDISTR
object_kind: entity
applicable_nf:
- NCG
status: active
---

# CDRDISTR（上传SFTP密钥文件到BS侧）

## 说明

**适用NF：NCG**

该命令用于配置第二份最终话单的分发任务，包括话单分发的方式、采用的协议、计费中心（本文档中又称BS（Billing System））IP地址等信息。

CG支持PULL和PUSH两种方式分发话单到计费中心（本文档中又称BS（Billing System））。

- PULL方式
  在CG的每对RU上开放第二份最终话单文件的存放目录给计费中心获取。大多数情况下，CG开放第二份最终话单的默认存储目录给计费中心获取。少数情况下，有局点要求在本地磁盘上新建一个目录，将默认存储路径下的第二份最终话单先备份到该目录下，然后开放此目录给计费中心获取。
- PUSH方式
  CG采用FTP或者SFTP协议主动将话单分发到计费中心指定目录下。

不同的分发方式的准备工作，请参见 [表1](#ZH-CN_CONCEPT_0251174254__table_038FF8DB) 。

*表1 配置话单分发任务的准备工作*

| 传输协议 | 传输方式 | 传输方式 | CG侧的准备工作 | BS侧的准备工作 |
| --- | --- | --- | --- | --- |
| FTP | PULL | PULL | CG作为FTP的服务器端。需准备的工作如下：<br>- 根据现网规划，获取CG每对RU上用于提供给计费中心取话单的IP地址。<br>- 开放给BS的用户名、密码、开放给BS的路径，然后知会BS。 | BS作为FTP的客户端。 |
| FTP | PUSH | PUSH | CG作为FTP的客户端。需准备的工作如下：<br>- 根据现网规划，获取CG每对RU上用于分发话单的主IP地址。<br>- 获取BS侧的FTP用户和密码。<br>- 获取当前局点的特殊分发要求。例如，不同通道下的话单有不同的分发规则，或者各通道下的话单是否分发到不同的BS。此要求确定了CG每对RU上的分发任务个数。 | BS作为FTP的服务器端。需准备的工作如下：<br>- 根据现网规划，BS侧开放主IP地址供CG分发话单。<br>- 开放一个话单存放目录给CG。<br>- 创建一个FTP用户，并设置此用户的主目录为话单存放目录，具备读写权限。CG采用此用户分发话单到BS的相应目录下。<br>说明：要求FTP服务器端的连接超时时长大于等于900秒。 |
| SFTP | PULL | 密码方式 | CG作为SFTP的服务器端。需准备的工作如下：<br>- 根据现网规划，获取CG每对RU上用于提供给计费中心取话单的IP地址。<br>- 开放给BS的用户名、密码、开放给BS的路径，然后知会BS。 | BS作为SFTP的客户端。 |
| SFTP | PULL | 密钥方式 | CG作为SFTP的服务器端。需准备的工作如下：<br>- 根据现网规划，获取CG每对RU上用于提供给计费中心取话单的IP地址。<br>- 开放给BS的用户名、密码、开放给BS的路径，然后知会BS。<br>- 根据UNC（NCG）产品文档中的“计费中心为Linux环境时SFTP密钥方式PULL分发任务配置指南”生成密钥文件，并完成公钥文件的追加。 | BS作为SFTP的客户端。需准备的工作如下：<br>- 获取CG生成的私钥文件。 |
| SFTP | PUSH | 密码方式 | 与FTP的PUSH方式下的准备工作相同。 | 与FTP的PUSH方式下的准备工作相同。<br>说明：要求SFTP服务器端的连接超时时长大于等于900秒。 |
| SFTP | PUSH | 密钥方式 | CG作为SFTP的客户端。需准备的工作如下：<br>- 根据现网规划，获取CG每对RU上用于分发话单的主IP地址。<br>- 获取BS侧的SFTP用户和密码。<br>- 执行“上传SFTP密钥文件到BS侧”操作。<br>- 获取当前局点的特殊分发要求。例如，不同通道下的话单有不同的分发要求，或者各通道下的话单是否分发到不同的BS。此要求确定了CG每对RU上的分发任务个数。 | BS作为SFTP的服务器端。需准备的工作如下：<br>- 根据现网规划，BS侧开放主IP地址到CG取话单。<br>- 开放一个目录给CG，此目录存放最终话单和私钥文件。<br>- 创建一个SFTP用户，并设置此用户的主目录为话单存放目录，具备读写权限。CG采用此用户分发话单到BS的相应目录下。<br>说明：要求SFTP服务器端的连接超时时长大于等于900秒。 |

## 操作本对象的命令

- [ADD CDRDISTR](command/UNC/20.15.2/ADD-CDRDISTR.md)
- [DLD CDRDISTR](command/UNC/20.15.2/DLD-CDRDISTR.md)
- [DSP CDRDISTR](command/UNC/20.15.2/DSP-CDRDISTR.md)
- [LST CDRDISTR](command/UNC/20.15.2/LST-CDRDISTR.md)
- [MOD CDRDISTR](command/UNC/20.15.2/MOD-CDRDISTR.md)
- [RMV CDRDISTR](command/UNC/20.15.2/RMV-CDRDISTR.md)
- [UPL CDRDISTR](command/UNC/20.15.2/UPL-CDRDISTR.md)

## 证据

- 原始手册：`evidence/UNC/20.15.2/上传SFTP密钥文件到BS侧（UPL-CDRDISTR）_51174252.md`
- 原始手册：`evidence/UNC/20.15.2/下载SFTP密钥文件到本端（DLD-CDRDISTR）_51174253.md`
- 原始手册：`evidence/UNC/20.15.2/修改话单分发（MOD-CDRDISTR）_51174256.md`
- 原始手册：`evidence/UNC/20.15.2/删除话单分发（RMV-CDRDISTR）_51174255.md`
- 原始手册：`evidence/UNC/20.15.2/增加话单分发（ADD-CDRDISTR）_51174254.md`
- 原始手册：`evidence/UNC/20.15.2/显示Push及Local方式下分发任务状态（DSP-CDRDISTR）_51174251.md`
- 原始手册：`evidence/UNC/20.15.2/查询话单分发（LST-CDRDISTR）_51174257.md`
