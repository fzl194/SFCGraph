---
id: UNC@20.15.2@MMLCommand@DSP GTPUPATH
type: MMLCommand
name: DSP GTPUPATH（显示GTP-U路径）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPUPATH
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
- 数据转发管理
- GTP-U
- GTP-U路径管理
status: active
---

# DSP GTPUPATH（显示GTP-U路径）

## 功能

**适用网元：SGSN、MME**

该命令用于查询GTP-U路径信息，如果输入的路径在系统中已经存在则输出这条路径的信息。

## 注意事项

- 该命令执行后立即生效。
- 当GTP-U路径数较多时，命令执行时长可能会持续几分钟。建议通过“本端IPv4地址”/“本端IPv6地址”、“对端IPv4地址”/“对端IPv6地址”、“对端IPv4地址掩码”、“路径状态筛选”、“网元间接口类型筛选”参数的组合来进行分类查询，减少一次查询的GTP-U路径数，提高每次查询的效率。（GTP-U路径数可通过[**DSP GTPUPATHNUM**](显示GTP-U路径个数(DSP GTPUPATHNUM)_72345441.md)命令查询获得）。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称。该参数可以通过<br>**DSP RU**<br>命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PROCTP | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>数据来源：整网规划<br>取值范围：<br>- “UPP”<br>默认值：无 |
| PROCNO | 进程序号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的序号。<br>数据来源：整网规划<br>取值范围：0~20<br>默认值：0 |
| GTPVER | GTP版本 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-U路径的协议版本。<br>数据来源：整网规划<br>取值范围：<br>- “GTPv0（GTPv0）”<br>- “GTPv1（GTPv1）”<br>默认值：无 |
| IPTYPE | IP地址类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-U路径的IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| LOCIPV4ADDR | 本端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP-U路径的本端IPv4地址。<br>数据来源：整网规划<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：若本参数没有输入，则不以本参数作为筛选条件来查询所有的GTP-U路径。若本参数输入，则以输入的值作为筛选条件来查询所有的GTP-U路径。<br>GTP-U路径的本端IPv4地址可以使用<br>[**LST GTPULE**](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)<br>查询。 |
| PEERIPV4ADDR | 对端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP-U路径的对端IPv4地址，与<br>“对端IPv4地址掩码”<br>参数一起指定查询GTP-U路径的对端IPv4地址的网段。<br>数据来源：整网规划<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无<br>说明：若本参数没有输入，则不以本参数作为筛选条件来查询所有的GTP-U路径。若本参数输入，则以输入的值与<br>“对端IPv4地址掩码”<br>组成的网段作为筛选条件来查询所有的GTP-U路径。 |
| PEERIPV4MSK | 对端IPv4地址掩码 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP-U路径的对端IPv4地址的掩码，与<br>“对端IPv4地址”<br>参数一起指定查询GTP-U路径的对端IPv4地址的网段。<br>数据来源：整网规划<br>前提条件：当<br>“IP类型”<br>设置为<br>“IPV4(IPV4)”<br>时此参数有效。<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：255.255.255.255 |
| LOCIPV6ADDR | 本端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTPU路径的本端IPv6地址。<br>数据来源：整网规划<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：若本参数没有输入，则不以本参数作为筛选条件来查询所有的GTP-U路径。若本参数输入，则以输入的值作为筛选条件来查询所有的GTP-U路径。<br>GTP-U路径的本端IPv6地址可以使用<br>[**LST GTPULE**](../../../GTP-U接口管理/Gtpu本端实体管理/查询GTP-U本地实体(LST GTPULE)_26305792.md)<br>查询。 |
| PEERIPV6ADDR | 对端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定GTP-U路径的对端IPv6地址。<br>数据来源：整网规划<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时有效。<br>取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>说明：若本参数没有输入，则不以本参数作为筛选条件来查询所有的GTP-U路径。若本参数输入，则以输入的值作为筛选条件来查询所有的GTP-U路径。 |
| MAXDSPNUM | 最大显示路径数目 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询结果最大显示的路径数目。若实际匹配的查询路径数大于指定的最大显示路径条目，多出的路径数不会显示。<br>数据来源：整网规划<br>取值范围：1~8000<br>默认值：5000<br>说明：当GTP-U路径数较多时，本参数的取值越大，命令执行的时长越长。建议保持系统默认值不变。 |
| PATHST | 路径状态筛选 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询GTP-U路径的状态。<br>数据来源：整网规划<br>取值范围：<br>- “NORMAL（正常）”<br>- “ERROR（故障）”<br>- “ALL（所有）”<br>默认值：<br>“ERROR(故障)”<br>说明：若本参数没有输入，系统缺省查询<br>“ERROR（故障）”<br>状态的GTP-U路径。 |
| PEERINTF | 网元间接口类型筛选 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询GTP-U路径的网元间接口类型。<br>数据来源：整网规划<br>取值范围：Gn（Gn），Gp（Gp），S4（S4），S16（S16），Iu（Iu），S11(S11)<br>默认值：无<br>说明：若本参数没有输入，系统缺省查询所有网元间接口类型的GTP-U路径。若GTP-U路径同时存在多个网元间接口类型时，输出结果为包含指定输入的网元间接口类型的GTP-U路径。<br>举例：GTP-U路径上同时存在“Gn”、“S16”接口类型，输入“Gn”筛选条件可以查询，输入“S16”筛选条件也可以查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUPATH]] · GTP-U路径（GTPUPATH）

## 使用实例

1. 查询资源单元为USN_SP_RU_0066上的GTP-U路径信息：
  ```
  %%DSP GTPUPATH: RUNAME="USN_SP_RU_0066", GTPVER=GTPv1, IPTYPE=IPV4;%%
  RETCODE = 0  操作成功。

  操作结果如下:
  -------------------------
    资源单元名称 = USN_SP_RU_0066
        进程类型 = UPP
        进程序号 = 0
  To be continued...
  ---    END

  %%DSP GTPUPATH: RUNAME="USN_SP_RU_0066", GTPVER=GTPv1, IPTYPE=IPV4;%%
  RETCODE = 0  操作成功。

  操作结果如下:
  -------------------------
  GTP路径数目  =  1
  To be continued...
  ---    END

  %%DSP GTPUPATH: RUNAME="USN_SP_RU_0066", GTPVER=GTPv1, IPTYPE=IPV4;%%
  RETCODE = 0  操作成功。

  操作结果如下:
  -------------------------
             GTP版本 = GTPv1
          本端IP地址 = 192.168.9.20
          对端IP地址 = 192.168.14.20
         GTP路径状态 = 故障
         GTP路径属性 = 路径管理
      GTP路径上PDP数 = 0
  剩余生存时间（秒） = 955
    PLMN网元间的接口 = Gn接口
  (结果数目 = 3)
  共有3个报告
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示GTP-U路径(DSP-GTPUPATH)_26305650.md`
