---
id: UNC@20.15.2@MMLCommand@LST GBIPLOCENDPT
type: MMLCommand
name: LST GBIPLOCENDPT（查询本端端点配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBIPLOCENDPT
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
- 本端IP端点配置
status: active
---

# LST GBIPLOCENDPT（查询本端端点配置）

## 功能

**适用网元：SGSN**

该命令用于在GB OVER IP查询本端端点配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定端点所在的网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| LIPV4 | 本端IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本端使用的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时才生效。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无 |
| LIPV6 | 本端IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定本端PCU使用的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时才生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| LUP | 本端UDP端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端使用的UDP端口号。<br>取值范围：1024～65535<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GBIPLOCENDPT]] · 本地端点配置（GBIPLOCENDPT）

## 使用实例

查询所有的Gb接口本端端点：

LST GBIPLOCENDPT:;

```
%%LST GBIPLOCENDPT:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
本端实体标识    NSE标识    NSE中的端点编号    IP地址类型    本地IP地址    本端UDP端口号    信令权重    数据权重    描述      vpn名称

0               600        0                  IPv4          192.168.2.1   2001             255         255         FOR BSC1  _abc_    
1               601        0                  IPv4          192.168.2.2   2002             255         255         FOR BSC2  _abc_    
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GBIPLOCENDPT.md`
