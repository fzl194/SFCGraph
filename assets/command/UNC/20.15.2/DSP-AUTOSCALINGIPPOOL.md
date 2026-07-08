---
id: UNC@20.15.2@MMLCommand@DSP AUTOSCALINGIPPOOL
type: MMLCommand
name: DSP AUTOSCALINGIPPOOL（显示自动化配置地址池信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: AUTOSCALINGIPPOOL
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- 地址池信息
status: active
---

# DSP AUTOSCALINGIPPOOL（显示自动化配置地址池信息）

## 功能

该命令用于显示地址池使用情况。

## 注意事项

- 该命令执行后立即生效。
- 当配置为DHCP时，地址池信息为0.0.0.0-0.0.0.0。
- 当配置为DHCPv6时，地址池信息为::-::。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定接口自动化配置服务模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无 |
| POOLTYPE | 地址池类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定地址池类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- External：该自动化配置地址池是外联口地址池。<br>- Loopback：该自动化配置地址池是环回口地址池。<br>默认值：无 |

## 操作的配置对象

- [自动化配置地址池信息（AUTOSCALINGIPPOOL）](configobject/UNC/20.15.2/AUTOSCALINGIPPOOL.md)

## 使用实例

- 显示地址池信息，“SERVICENAME”为“service4”：
  ```
  DSP AUTOSCALINGIPPOOL:SERVICENAME="service4";
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
        服务名称  =  service4
      地址池类型  =  External
     VPN实例名称  =  vpn4
          地址族  =  IPv4地址族
    IP地址池信息  =  10.1.1.1-10.1.1.10
  地址池掩码长度  =  24
          最大值  =  10
    已使用的数量  =  1
  (结果个数 = 1)
  ---    END
  ```
- 显示地址池信息，“SERVICENAME”为“service6”：
  ```
  DSP AUTOSCALINGIPPOOL:SERVICENAME="service6";
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
        服务名称  =  service6
      地址池类型  =  External
     VPN实例名称  =  vpn6
          地址族  =  IPv6地址族
    IP地址池信息  =  2001:db8::1-2001:db8::10
  地址池掩码长度  =  64
          最大值  =  16
    已使用的数量  =  0
  (结果个数 = 1)
  ---    END
  ```
- 显示所有的地址池信息：
  ```
  DSP AUTOSCALINGIPPOOL:;
  ```
  ```

  RETCODE = 0  操作成功

  结果如下
  -------------------------
  服务名称    地址池类型    VPN实例名称    地址族          IP地址池信息                地址池掩码长度    最大值    已使用的数量

  service4    External      vpn4        IPv4地址族     10.1.1.1-10.1.1.10          24                10         1
  service6    External      vpn6        IPv6地址族     2001:db8::1-2001:db8::10    64                16         0
  (结果个数 = 2)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示自动化配置地址池信息（DSP-AUTOSCALINGIPPOOL）_49961602.md`
