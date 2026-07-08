---
id: UNC@20.15.2@MMLCommand@LST GBIPRMTENDPT
type: MMLCommand
name: LST GBIPRMTENDPT（查询对端端点配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBIPRMTENDPT
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
- 对端IP端点配置
status: active
---

# LST GBIPRMTENDPT（查询对端端点配置）

## 功能

**适用网元：SGSN**

该命令用于查询Gb接口对端端点。对端端点权重表用来配置对端IP端点的数据权重和信令权重，在IP网络NSVC链路负荷分担时根据数据权重或者信令权重来选择对端IP端点。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IPT | IP地址类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定IP地址类型。<br>取值范围：<br>- “IPV4(IPv4)”<br>- “IPV6(IPv6)”<br>默认值：无 |
| RIPV4 | 对端IPv4地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端PCU使用的IPv4地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV4(IPv4)”<br>时才生效。<br>取值范围：0.0.0.0～255.255.255.255<br>默认值：无<br>配置原则：IPv4地址不能为0.0.0.0，255.255.255.255 |
| RIPV6 | 对端IPv6地址 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端PCU使用的IPv6地址。<br>前提条件：该参数在<br>“IP地址类型”<br>设置为<br>“IPV6(IPv6)”<br>时才生效。<br>取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF<br>默认值：无 |
| RUP | 对端UDP端口号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定对端PCU使用的UDP端口号。<br>取值范围：0～65535<br>默认值：无 |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定端点所在的网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GBIPRMTENDPT]] · 对端端点配置（GBIPRMTENDPT）

## 使用实例

1. 查询所有的Gb接口对端端点：
  LST GBIPRMTENDPT:;
  ```
  %%LST GBIPRMTENDPT:;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ----------------
  IP地址类型  对端IP地址    对端UDP端口号  NSE标识  数据权重  信令权重  描述

  IPv4        172.22.44.66  4000           200      50        100       FOR BSC1
  IPv4        172.22.44.88  2000           200      255       255       noname
  (结果个数 = 2)
  ---    END
  ```
2. 查询IPv4地址为"172.22.44.66"、UDP端口号为4000的对端端点信息：
  LST GBIPRMTENDPT: IPT=IPV4, RIPV4="172.22.44.66", RUP=4000;
  ```
  %%LST GBIPRMTENDPT: IPT=IPV4, RIPV4="172.22.44.66", RUP=4000;%%
  RETCODE = 0  执行成功。

  操作结果如下
  ----------------
     IP地址类型  =  IPv4
     对端IP地址  =  172.22.44.66
  对端UDP端口号  =  4000
        NSE标识  =  200
       数据权重  =  50
       信令权重  =  100
           描述  =  FOR BSC1
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GBIPRMTENDPT.md`
