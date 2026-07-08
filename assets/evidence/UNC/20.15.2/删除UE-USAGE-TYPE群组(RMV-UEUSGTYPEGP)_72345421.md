# 删除UE USAGE TYPE群组(RMV UEUSGTYPEGP)

- [命令功能](#ZH-CN_MMLREF_0000001172345421__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001172345421__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001172345421__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001172345421__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001172345421__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001172345421__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001172345421)

**适用网元：MME**

该命令用于删除UE USAGE TYPE群组记录。

#### [注意事项](#ZH-CN_MMLREF_0000001172345421)

- 该命令执行后立即生效。
- 删除UE USAGE TYPE群组时必须保证相关表中不存在该UE USAGE TYPE群组的相关记录，可执行[**LST DNSN**](../../../GTP-C接口管理/DNS/DNS NAPTR管理/查询DNS NAPTR记录(LST DNSN)_26145892.md)查看相关记录。
- 删除UE USAGE TYPE群组时必须首先删除该UE USAGE TYPE群组下的所有成员，可执行[**RMV UEUSGTYPEGPMEM**](../UE USAGE TYPE群组成员管理/删除UE USAGE TYPE群组成员(RMV UEUSGTYPEGPMEM)_72345423.md)命令进行删除。

#### [本地用户权限](#ZH-CN_MMLREF_0000001172345421)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001172345421)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001172345421)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0～1023<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001172345421)

删除一个 “UEUSGTYPEGPID” 为 “0” 的UE USAGE TYPE群组：

RMV UEUSGTYPEGP: UEUSGTYPEGPID=0;
