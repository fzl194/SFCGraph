# 修改UE USAGE TYPE群组(MOD UEUSGTYPEGP)

- [命令功能](#ZH-CN_MMLREF_0000001126305630__1.3.1.1)
- [注意事项](#ZH-CN_MMLREF_0000001126305630__1.3.2.1)
- [本地用户权限](#ZH-CN_MMLREF_0000001126305630__1.3.3.1)
- [网管用户权限](#ZH-CN_MMLREF_0000001126305630__1.3.4.1)
- [参数说明](#ZH-CN_MMLREF_0000001126305630__1.3.5.1)
- [使用实例](#ZH-CN_MMLREF_0000001126305630__1.3.6.1)

#### [命令功能](#ZH-CN_MMLREF_0000001126305630)

**适用网元：MME**

该命令用于修改UE USAGE TYPE群组的描述信息。

#### [注意事项](#ZH-CN_MMLREF_0000001126305630)

该命令执行后立即生效。

#### [本地用户权限](#ZH-CN_MMLREF_0000001126305630)

manage-ug；system-ug

#### [网管用户权限](#ZH-CN_MMLREF_0000001126305630)

G_1，管理员级别命令组；G_2，操作员级别命令组

#### [参数说明](#ZH-CN_MMLREF_0000001126305630)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组标识。<br>数据来源：本端规划<br>取值范围：0～1023<br>默认值：无 |
| DESC | 描述 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UE USAGE TYPE群组的描述信息。<br>数据来源：本端规划<br>取值范围：1～32位字符串<br>默认值：无 |

#### [使用实例](#ZH-CN_MMLREF_0000001126305630)

修改 “UE USAGE TYPE群组标识” 为 “0” 的UE USAGE TYPE群组描述信息：

MOD UEUSGTYPEGP: UEUSGTYPEGPID=0, DESC="NB-IoT";
