---
id: UDG@20.15.2@MMLCommand@DSP RMPRODUCERDETAIL
type: MMLCommand
name: DSP RMPRODUCERDETAIL（查询路由管理生产者详细信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RMPRODUCERDETAIL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 路由基础调测
- 查询路由管理伙伴信息
status: active
---

# DSP RMPRODUCERDETAIL（查询路由管理生产者详细信息）

## 功能

该命令用来查询路由管理生产者详细信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>- ipv6unicast：IPv6单播。<br>默认值：无 |
| PARTNER | Partner ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示Partner ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |
| VPNNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| VRFINDEX | VRF索引 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VRF索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| ALL | 所有实例 | 可选必选说明：可选参数<br>参数含义：该参数用于表示所有实例。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |
| VPID | VP ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示VP ID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RMPRODUCERDETAIL]] · 路由管理生产者详细信息（RMPRODUCERDETAIL）

## 使用实例

查询路由管理生产者详细信息：

```
DSP RMPRODUCERDETAIL:ADDRESSFAMILY=ipv4unicast,VRFINDEX=1;
```

```

RETCODE = 0  操作成功。

结果如下
--------
            Partner ID  =  0x6F0005
                 VP ID  =  0x1
               VRF索引  =  1
                拓扑ID  =  0
                表名字  =  base
            协议进程ID  =  0
              协议类型  =  1
              平滑状态  =  Normal(0x5)
          当前平滑阶段  =  1
              服务类型  =  Smooth1/Unlimited(0x80000001)
              服务标志  =  Null
          是否正在老化  =  FALSE
              引用计数  =  3
        序列号错误次数  =  0
          平滑服务类型  =  1
          平滑间隔（s） =  2400
                事物号  =  0
                版本号  =  1
    是否处于系统级平滑  =  FALSE
              前缀总数  =  4
          添加的前缀数  =  4
          删除的前缀数  =  0
              路由总数  =  4
    生产者添加的路由数  =  4
    生产者修改的路由数  =  0
    生产者删除的路由数  =  0
    生产者丢弃的路由数  =  0
      平滑期间路由数量  =  3
              老化总数  =  0
          上一次老化数  =  0
          老化开始时间  =  2016-11-11 07:41:04
          老化结束时间  =  2016-11-11 07:41:04
            下一跳总数  =  3
  生产者添加的下一跳数  =  3
  生产者修改的下一跳数  =  3
  生产者删除的下一跳数  =  0
  生产者老化的下一跳数  =  0
       上一次老化IID数  =  0
       IID老化开始时间  =  2016-11-11 07:41:04
       IID老化结束时间  =  2016-11-11 07:41:04
          路由属性总数  =  0
生产者添加的路由属性数  =  0
生产者修改的路由属性数  =  0
生产者删除的路由属性数  =  0
生产者老化的路由属性数  =  0
  上一次老化路由属性数  =  0
  路由属性老化开始时间  =  2016-11-11 07:41:04
  路由属性老化结束时间  =  2016-11-11 07:41:04
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询路由管理生产者详细信息（DSP-RMPRODUCERDETAIL）_50281046.md`
