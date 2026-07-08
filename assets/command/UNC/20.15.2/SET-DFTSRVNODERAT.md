---
id: UNC@20.15.2@MMLCommand@SET DFTSRVNODERAT
type: MMLCommand
name: SET DFTSRVNODERAT（设置默认RAT类型）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DFTSRVNODERAT
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入控制
- 获取RAT管理
- 全局RAT配置
status: active
---

# SET DFTSRVNODERAT（设置默认RAT类型）

## 功能

**适用NF：GGSN**

该命令用来设置默认的RAT类型。获取RAT类型用于从虚拟APN映射到真实APN、匹配user-profile进行业务、计费控制。当SGSN IP在表中没有匹配项并且消息中没有携带RAT Type信元时，会用这个默认的RAT类型作为它对应的RAT类型。当要配置该表的默认表项时，使用这条命令。

## 注意事项

- 该命令执行后立即生效。

- 若系统中尚未配置默认RAT类型，执行命令增加默认RAT类型；若系统中已配置默认RAT类型，执行本命令则修改已配置的默认RAT类型。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NODETYPE | RATTYPE |
| --- | --- |
| GGSN | NONE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NODETYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数表示当前配置的网元类型。<br>数据来源：本端规划<br>取值范围：<br>- GGSN（GGSN）<br>默认值：无。<br>配置原则：无 |
| RATTYPE | RAT类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定默认的RAT类型。<br>数据来源：全网规划<br>取值范围：<br>- “NONE（NONE）”：表示尚未配置默认的RAT类型。即没有RAT类型。<br>- “UTRAN（UTRAN）”：表示默认RAT类型为UTRAN。<br>- “GERAN（GERAN）”：表示默认RAT类型为GERAN。<br>- “WLAN（WLAN）”：表示默认RAT类型为WLAN。<br>- “GAN（GAN）”：表示默认RAT类型为GAN。<br>- “EUTRAN（EUTRAN）”：表示默认RAT类型为EUTRAN。<br>- “UNSPECIFIED（UNSPECIFIED）”：表示默认RAT类型未知。即没有RAT类型。<br>- “EUTRAN_NB_IOT（EUTRAN_NB_IOT）”：表示默认RAT类型为EUTRAN-NB-IoT。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTSRVNODERAT查询当前参数配置值。<br>配置原则：<br>当RATTYPE配置成“UNSPECIFIED”时，DWORD1021 BIT29 控制GGSN-C从读取配置后返回SMFCOMMONDEFAULTRAT_TYPEUNSPECIFIED还是nil。 |

## 操作的配置对象

- [默认RAT类型（DFTSRVNODERAT）](configobject/UNC/20.15.2/DFTSRVNODERAT.md)

## 使用实例

当设置SGSN默认的RAT类型为WLAN时，可按如下配置：

```
SET DFTSRVNODERAT:NODETYPE=GGSN, RATTYPE=WLAN;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置默认RAT类型（SET-DFTSRVNODERAT）_09653166.md`
