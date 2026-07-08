---
id: UNC@20.15.2@MMLCommand@DSP GTPUINTFATTR
type: MMLCommand
name: DSP GTPUINTFATTR（显示GTP-U IP地址接口属性）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GTPUINTFATTR
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
- GTP-U接口管理
- GTP-U接口类型属性
status: active
---

# DSP GTPUINTFATTR（显示GTP-U IP地址接口属性）

## 功能

**适用网元：SGSN、MME**

- 该命令用于查询指定用户范围的某接口使用的GTPU IP地址。
- 该命令可用于SPP进程。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBRANGE | 用户范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的用户范围。<br>数据来源：本端规划<br>取值范围：<br>- “ALL_USER(所有用户)”<br>- “SPECIAL_IMSIPRE(指定IMSI前缀)”<br>- “SPECIAL_NOID(指定运营商)”<br>默认值：无 |
| NOID | 运营商标识 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定运营商标识。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_NOID(指定运营商)"后生效。<br>数据来源：本端规划<br>取值范围：0～64，128～254<br>默认值：无 |
| IMSIPRE_DSP | IMSI前缀 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI前缀。使用时按照输入IMSI最长匹配进行查询，输出包含最长匹配IMSI前缀的记录。<br>前提条件：该参数在"用户范围"参数配置为"SPECIAL_IMSIPRE(指定IMSI前缀)"后生效。<br>数据来源：本端规划<br>取值范围：1~15位十进制字符串<br>默认值：无 |
| INTFTP1 | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTPU IP地址适用的接口类型。<br>数据来源：全网规划<br>取值范围：<br>- “ALL_INTERFACE(所有接口)”<br>- “GN-GGSN/GP(Gn-GGSN/Gp)”<br>- “GN-SGSN/S16(Gn-SGSN/S16)”<br>- “Iu(IU)”<br>- “S11(S11)”<br>- “S4(S4)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GTPUINTFATTR]] · GTP-U IP地址接口属性（GTPUINTFATTR）

## 使用实例

查询所有用户使用的Gn-GGSN/Gp接口使用的GTPU IP地址信息：

DSP GTPUINTFATTR: SUBRANGE=ALL_USER, INTFTP1=GN-GGSN/GP;

```
%%DSP GTPUINTFATTR: SUBRANGE=ALL_USER, INTFTP1=GN-GGSN/GP;%%
RETCODE = 0  操作成功。

输出结果如下
------------------------
    用户范围  =  所有用户
  运营商标识  =  NULL
    IMSI前缀  =  NULL
    接口类型  =  Gn-GGSN/Gp
        组号  =  1
  IP地址类型  =  IPv4
    IPv4地址  =  10.141.149.100
    IPv6地址  =  2001:db8:10:19:44:55:10:12
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GTPUINTFATTR.md`
