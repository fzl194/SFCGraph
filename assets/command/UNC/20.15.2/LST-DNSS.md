---
id: UNC@20.15.2@MMLCommand@LST DNSS
type: MMLCommand
name: LST DNSS（查询DNS服务器）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNSS
command_category: 查询类
applicable_nf:
- SGSN
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- GTP-C接口管理
- DNS
- DNS服务器管理
status: active
---

# LST DNSS（查询DNS服务器）

## 功能

**适用网元：SGSN、MME** **、AMF**

该命令用于查看配置的DNS服务器信息，DNS服务器是网络中专门提供域名解析服务的服务器。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入参数，则查询所有记录。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GRPID | 服务器组ID | 可选必选说明：可选参数<br>参数含义：该参数用于指示DNS服务器组ID。<br>数据来源：整网规划<br>取值范围：0~37<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：IP地址类型。<br>数据来源：整网规划<br>取值范围：<br>- IPV4(IPV4)<br>- IPV6(IPV6)<br>默认值：无 |
| IP | IP地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指示DNS服务器IP地址。<br>该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV4(IPV4)”<br>后生效。<br>数据来源：整网规划<br>取值范围：0.0.0.0~255.255.255.255<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：DNS服务器IPv6地址。<br>该参数在<br>“IP地址类型”<br>参数配置为<br>“IPV6(IPV6)”<br>后生效。<br>数据来源：整网规划<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DNSS]] · DNS服务器（DNSS）

## 使用实例

查询所有DNS服务器：

LST DNSS:;

```
%%LST DNSS:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
 服务器组ID    IP地址类型    IP地址     域名服务器优先级    DNS服务器名称    DNS服务器承载协议

0             IPV4          10.141.149.100    优先级1             NULL             UDP_TCP传输模式  
0             IPV4          10.141.149.101    优先级1             NULL             UDP_TCP传输模式  
仍有后续报告输出
---    END

%%LST DNSS:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
服务器组ID    IP地址类型    IPv6地址                          域名服务器优先级    DNS服务器名称    DNS服务器承载协议

0             IPV6          2001:db8:10:19:44:55:10:12        优先级1             NULL             UDP_TCP传输模式  
0             IPV6          2001:db8:10:19:44:55:10:13        优先级1             NULL             UDP_TCP传输模式  
(结果个数 = 4)
共有2个报告
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-DNSS.md`
