---
id: UDG@20.15.2@MMLCommand@DSP WLRTBLSMTHINFO
type: MMLCommand
name: DSP WLRTBLSMTHINFO（显示基于表无线路由平滑统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: WLRTBLSMTHINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 无线路由调测
- 显示无线路由统计信息
status: active
---

# DSP WLRTBLSMTHINFO（显示基于表无线路由平滑统计信息）

## 功能

该命令用于显示基于表无线路由统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。区分大小写。<br>默认值：_public_ |
| AFTYPE | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |

## 操作的配置对象

- [基于表无线路由平滑统计信息（WLRTBLSMTHINFO）](configobject/UDG/20.15.2/WLRTBLSMTHINFO.md)

## 使用实例

显示基于表无线路由平滑统计信息：

```
DSP WLRTBLSMTHINFO:AFTYPE=ipv4unicast;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
     VPN实例名称  =  _public_
    序列号错误数  =  0
          对帐数  =  0
      前缀超限数  =  0
          平滑数  =  1
        最后原因  =  smooth
    最后开始时间  =  2017-03-21 19:52:26
    最后结束时间  =  2017-03-21 19:52:26
      批量前缀数  =  0
       批量IID数  =  0
        批量属性  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示基于表无线路由平滑统计信息（DSP-WLRTBLSMTHINFO）_50280746.md`
