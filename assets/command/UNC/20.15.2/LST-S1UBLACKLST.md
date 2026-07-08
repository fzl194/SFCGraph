---
id: UNC@20.15.2@MMLCommand@LST S1UBLACKLST
type: MMLCommand
name: LST S1UBLACKLST（查询S1-U IP地址黑名单记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1UBLACKLST
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1-U黑名单管理
- S1-U黑名单维护
status: active
---

# LST S1UBLACKLST（查询S1-U IP地址黑名单记录）

## 功能

**适用网元：MME**

暂不支持本命令。该命令用于查询S1-U IP地址黑名单记录。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPTYPE | IP类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型，标识S1-U黑名单IP地址的类型。<br>数据来源：整网规划<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| IPV4 | IPv4地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定需要配置的S1-U IPv4黑名单地址。<br>前提条件：该参数在"IP类型"参数配置为"IPV4"后生效。<br>数据来源：整网规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| IPV6 | IPv6地址 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定需要配置的S1-U IPv6黑名单地址。<br>前提条件：该参数在"IP类型"参数配置为"IPV6"后生效。<br>数据来源：整网规划<br>取值范围：IPv6地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1UBLACKLST]] · S1-U IP地址黑名单记录（S1UBLACKLST）

## 使用实例

查询S1-U黑名单记录：

LST S1UBLACKLST:;

```
%%LST S1UBLACKLST:;%% 
RETCODE = 0  操作成功  

IPv4地址信息： 
--------------  
IP类型  IPv4地址
   
IPv4    10.16.3.4  
IPv4    10.3.5.6 
(结果个数 = 2)  

---    END
```

**输出结果说明**

参见 **[ADD S1UBLACKLST](增加S1-U IP地址黑名单记录(ADD S1UBLACKLST)_24385877.md)** 的参数说明。

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1-U-IP地址黑名单记录(LST-S1UBLACKLST)_89144234.md`
