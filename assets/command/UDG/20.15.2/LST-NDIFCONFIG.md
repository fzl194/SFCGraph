---
id: UDG@20.15.2@MMLCommand@LST NDIFCONFIG
type: MMLCommand
name: LST NDIFCONFIG（查询IPv6 ND接口配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: NDIFCONFIG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv6管理
- IPv6 ND接口配置
status: active
---

# LST NDIFCONFIG（查询IPv6 ND接口配置）

## 功能

该命令用于IPv6接口下ND配置的查询。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IFNAME | 接口名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@NDIFCONFIG]] · IPv6 ND接口配置（NDIFCONFIG）

## 使用实例

查询IPv6 ND接口下的配置：

```
LST NDIFCONFIG:IFNAME="Ethernet65/0/8";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                     接口名  =  Ethernet65/0/8
         RA报文抑制开关标记  =  关闭
           管理地址配置标记  =  关闭
         其他状态化配置标记  =  关闭
                   探测次数  =  1
                       跳限  =  128
             重传间隔（ms）  =  4222323423
          NUD可达时间（ms）  =  0
              最大间隔（s）  =  600
              最小间隔（s）  =  200
        RA报文存活时间（s）  =  1800
                   RA优先级  =  中
                 NB表项限制  =  0
                 ND安全模式  =  关闭
         RSA最小长度（bit）  =  512
         RSA最大长度（bit）  =  3072
ND报文收发时刻最大差值（s）  =  300
        时间戳模糊因素（s）  =  1
      时间戳漂移（percent）  =  1
                RA前缀标记   =  开启
                RA MTU标记   =  开启
              失效时间（s）  =  111
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-NDIFCONFIG.md`
