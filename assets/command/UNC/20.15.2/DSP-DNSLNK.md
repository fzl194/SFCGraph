---
id: UNC@20.15.2@MMLCommand@DSP DNSLNK
type: MMLCommand
name: DSP DNSLNK（显示DNS服务器链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DNSLNK
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 系统管理
- DNS维护管理
- 查询DNS Link
status: active
---

# DSP DNSLNK（显示DNS服务器链路状态）

## 功能

**适用网元：SGSN、MME**

该命令用于查看DNS服务器链路的状态。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>SPU<br>资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>数据来源：整网规划<br>取值范围：1~63 位字符串<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定DNS链路的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定DNS客户端IPV4地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4(IPV4)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端DNS服务器IPv4地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV4(IPV4)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定DNS客户端IPV6地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定对端DNS服务器IPv6地址。<br>前提条件：当<br>“IP地址类型”<br>设置为<br>“IPV6(IPV6)”<br>时，该参数有效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNSLNK]] · DNS服务器链路状态（DNSLNK）

## 使用实例

查询USN_SP_RU_0064的DNS服务器链路信息：

DSP DNSLNK:RUNAME="USN_SP_RU_0064";

```
%%DSP DNSLNK:RUNAME="USN_SP_RU_0064";%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
RU名称                IP地址类型    本端IPv4地址         对端IPv4地址          本地端口号      DNS链路类型      DNS链路状态

USN_SP_RU_0064        IPV4         192.168.97.27        192.168.97.76         15001           TCP传输模式      DNS链路正常
USN_SP_RU_0064        IPV4         192.168.97.27        192.168.97.76         15001           UDP传输模式      DNS链路正常
USN_SP_RU_0064        IPV4         192.168.97.27        192.168.97.77         15001           TCP传输模式      DNS链路正常
USN_SP_RU_0064        IPV4         192.168.97.27        192.168.97.77         15001           UDP传输模式      DNS链路正常
(结果个数 = 4)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DNSLNK.md`
