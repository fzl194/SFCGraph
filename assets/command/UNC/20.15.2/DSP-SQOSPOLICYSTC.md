---
id: UNC@20.15.2@MMLCommand@DSP SQOSPOLICYSTC
type: MMLCommand
name: DSP SQOSPOLICYSTC（查看端口流量策略报文统计）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SQOSPOLICYSTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 端口统计
status: active
---

# DSP SQOSPOLICYSTC（查看端口流量策略报文统计）

## 功能

该命令用来查看端口流量策略报文统计。

## 注意事项

- 计数统计需要在流策略使能流策略的统计功能后使用。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定接口。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：与设备接口名称保持一致，下发本MML命令前可使用LST INTERFACE查看设备接口。 |
| DIRECTION | 方向 | 可选必选说明：必选参数<br>参数含义：该参数用来指定应用流策略的方向。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- inbound：入方向。<br>- outbound：出方向。<br>默认值：无 |

## 操作的配置对象

- [查看端口流量策略报文统计（SQOSPOLICYSTC）](configobject/UNC/20.15.2/SQOSPOLICYSTC.md)

## 使用实例

查看Ethernet66/0/2端口流量策略报文统计：

```
DSP SQOSPOLICYSTC:IFNAME="Ethernet66/0/2",DIRECTION=inbound;
```

```
RETCODE = 0  操作成功

结果如下
--------
                       接口名称  =  Ethernet66/0/2
                           方向  =  入方向
                       策略名称  =  p1
                           模式  =  共享模式
                   统计使能标志  =  使能
               统计状态改变时间  =  2017-08-11 20:54:17
                   策略应用时间  =  2017-08-11 20:49:12
                   统计清除时间  =  NULL
                     IPV4的数量  =  1
                     IPV6的数量  =  1
                     匹配的包数  =  0
                   匹配的字节数  =  0
                     通过的包数  =  0
                   通过的字节数  =  0
                     丢弃的包数  =  0
                   丢弃的字节数  =  0
                     忽略的包数  =  0
                   忽略的字节数  =  0
            匹配的包速率（pps）  =  0
          匹配的字节速率（bps）  =  0
            通过的包速率（pps）  =  0
          通过的字节速率（bps）  =  0
            丢弃的包速率（pps）  =  0
          丢弃的字节速率（bps）  =  0
            忽略的包速率（pps）  =  0
          忽略的字节速率（bps）  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查看端口流量策略报文统计（DSP-SQOSPOLICYSTC）_00866685.md`
