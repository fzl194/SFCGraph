---
id: UNC@20.15.2@MMLCommand@LST SGSNIPNUM
type: MMLCommand
name: LST SGSNIPNUM（查询SGSN控制面IP地址与SGSN号码对应关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SGSNIPNUM
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- SGSN地址和SGSN号码对照表
status: active
---

# LST SGSNIPNUM（查询SGSN控制面IP地址与SGSN号码对应关系）

## 功能

**适用网元：SGSN**

该命令用于查询SGSN控制面IP地址与SGSN号码对照表中的SGSN控制面IP地址与SGSN号码的对照关系。

## 注意事项

- 该命令执行后立即生效。
- 不输入参数时将显示本SGSN下配置的所有SGSN控制面IP地址与SGSN号码的对照关系。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型<br>取值范围：<br>- “IPV4(IPV4)”<br>- “IPV6(IPV6)”<br>默认值：无 |
| IPV4 | SGSN控制面IP地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SGSN的控制面IPv4地址。<br>前提条件：当“IP地址类型”为“IPV4(IPV4)”时，该参数有效<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：<br>- 业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。<br>- 业务地址必须是A、B或者C类地址。<br>- 该参数的掩码缺省为255.255.255.255，不可更改。 |
| IPV6 | SGSN控制面IPv6地址 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定SGSN的控制面IPv64地址。<br>前提条件：当“IP地址类型”为“IPV6(IPV6)”时，该参数有效<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无<br>配置原则：<br>- IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。<br>- 该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSNIPNUM]] · SGSN控制面IP地址与SGSN号码对应关系（SGSNIPNUM）

## 使用实例

列出SGSN中所有存在的SGSN控制面IP地址与SGSN号码的对照关系：

LST SGSNIPNUM:;

```
%%LST SGSNIPNUM:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
              IP地址类型  =  IPV4
        SGSN控制面IP地址  =  10.10.10.16
                SGSN号码  =  861390218888
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SGSNIPNUM.md`
