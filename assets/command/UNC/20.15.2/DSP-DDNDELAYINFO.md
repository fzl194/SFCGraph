---
id: UNC@20.15.2@MMLCommand@DSP DDNDELAYINFO
type: MMLCommand
name: DSP DDNDELAYINFO（显示路径DDN Delay信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DDNDELAYINFO
command_category: 查询类
applicable_nf:
- SGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 接入管理运维
- DDN Delay管理
status: active
---

# DSP DDNDELAYINFO（显示路径DDN Delay信息）

## 功能

**适用NF：SGW-C**

该命令用来显示指定对端MME DDN Delay信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPVERSION | 对端IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端IP地址类型。<br>数据来源：本端规划<br>取值范围：<br>- IPV4（IPv4）<br>- IPV6（IPv6）<br>默认值：无<br>配置原则：无 |
| IPV4ADDRESS | 对端IPv4地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。<br>参数含义：该参数用于指定对端的IPv4地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：无 |
| IPV6ADDRESS | 对端IPv6地址 | 可选必选说明：该参数在"IPVERSION"配置为"IPV6"时为条件必选参数。<br>参数含义：该参数用于指定对端IPv6地址。<br>数据来源：本端规划<br>取值范围：IPv6地址类型。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [路径DDN Delay信息（DDNDELAYINFO）](configobject/UNC/20.15.2/DDNDELAYINFO.md)

## 使用实例

显示对端MME地址为10.194.39.226的DDN Delay信息：

```
DSP DDNDELAYINFO: IPVERSION=IPV4, IPV4ADDRESS="10.194.39.226";
RETCODE = 0  操作成功

DDN Delay Information
----------------------
                               LocalAddr = 10.135.21.2
                                PeerAddr = 10.194.39.226
                           DDN Delay(ms) = 5000
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示路径DDN-Delay信息（DSP-DDNDELAYINFO）_31700005.md`
