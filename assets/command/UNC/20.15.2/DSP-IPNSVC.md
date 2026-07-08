---
id: UNC@20.15.2@MMLCommand@DSP IPNSVC
type: MMLCommand
name: DSP IPNSVC（显示IP网络NSVC配置表）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: IPNSVC
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb over IP管理
- IP网络NSVC链路管理
status: active
---

# DSP IPNSVC（显示IP网络NSVC配置表）

## 功能

**适用网元：SGSN**

该命令用于查询IP网络NS-VC链路配置。NS-VC是NS对等层之间的端到端的虚连接链路，两端配置必须一致，通过配置NS-VC建立链路使NS对等层之间能够进行通信。

## 注意事项

目前暂不支持IPv6；

命令中的RU名称、进程号两个参数共有两种组合方式：输入RU名称查指定RU的IPNSVC；输入RU名称进程号查询指定RU上的进程的IPNSVC。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSVCI | NSVC标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSVC标识。<br>取值范围：0～65535<br>默认值：无 |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于设置此NSVC所在的网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无<br>说明：NSVC所在GBP进程的RU名称。 |
| PRON | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSVC所在的GBP进程的进程号。<br>取值范围：0～20<br>默认值：无<br>说明：NSVC所在GBP进程的进程号。 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LIPV4 | 本端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置本端Gb接口IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时才生效。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LIPV6 | 本端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置本端Gb接口IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时才生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LUP | 本端UDP端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置本端UDP端口号。<br>取值范围：1024～65535<br>默认值：无 |
| RIPV4 | 对端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置对端BSS使用的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时才生效。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| RIPV6 | 对端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置对端BSS使用的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时才生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| RUP | 对端UDP端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于设置对端BSS使用的UDP端口号。<br>取值范围：0～65535<br>默认值：无 |
| NSVCSTATE | NSVC状态 | 可选必选说明：可选参数<br>参数含义：该参数用于设置NSVC的状态。<br>取值范围：<br>- “NONOPERATIONAL(不可操作)”<br>- “OPERATIONAL(可操作)”<br>默认值：无 |

## 操作的配置对象

- [IP网络NSVC配置表（IPNSVC）](configobject/UNC/20.15.2/IPNSVC.md)

## 使用实例

查询IP网络NSVC配置表：

DSP IPNSVC:;

```
%%DSP IPNSVC:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
NSVC标识   NSE标识   RU名称            进程号         IP地址类型         本地IP地址          本端UDP端口号     对端IP地址            对端UDP端口号      NSVC状态     

2049       14904     USN_SP_RU_0066    0              IPv4               192.168.49.18       14904             192.168.49.1          11494              可操作
1          14908     USN_SP_RU_0066    1              IPv4               192.168.49.17       11498             192.168.49.1          11498              可操作
0          14907     USN_SP_RU_0066    2              IPv4               192.168.49.17       11497             192.168.49.1          11497              可操作
0          14906     USN_SP_RU_0066    3              IPv4               192.168.49.17       11496             192.168.49.1          11496              可操作
0          14905     USN_SP_RU_0066    4              IPv4               192.168.49.17       11495             192.168.49.1          11495              可操作
0          14902     USN_SP_RU_0066    0              IPv4               192.168.49.18       11492             192.168.49.1          11492              可操作
0          14901     USN_SP_RU_0066    1              IPv4               192.168.49.17       11491             192.168.49.1          11491              可操作
仍有后续报告输出
---    END

%%DSP IPNSVC:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
链路总数  =  7
(结果个数 = 8)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示IP网络NSVC配置表(DSP-IPNSVC)_72345609.md`
