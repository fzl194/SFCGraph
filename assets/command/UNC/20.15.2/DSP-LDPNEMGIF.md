---
id: UNC@20.15.2@MMLCommand@DSP LDPNEMGIF
type: MMLCommand
name: DSP LDPNEMGIF（显示LDP的接口信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPNEMGIF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPNEMGIF（显示LDP的接口信息）

## 功能

该命令用于显示LDP邻居管理的接口信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| IFNAME | 接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示LDP邻居的接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPNEMGIF]] · LDP的接口信息（LDPNEMGIF）

## 使用实例

显示LDP的接口信息：

```
DSP LDPNEMGIF:;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                   VPN实例名称  =  _public_
                    接口索引值  =  10
                      接口名称  =  Ethernet66/0/7
            使用传输地址的次数  =  0
                      传输地址  =  10.10.10.10
                    配置序列号  =  1
     发送Hello消息的时长（ms）  =  5000
  Hello消息发送的间隔时间（s）  =  0
      Hello消息保持的时间（s）  =  15
协商的保持Hello消息的时间（s）  =  15
     发送保活消息时间间隔（s）  =  0
                 保活时间（s）  =  45
              加入多播的返回码  =  0
            加入多播的状态标识  =  加入多播成功
          加入或退出多播的标志  =  0
                  等待加入组播  =  0
                    订阅的状态  =  订阅成功
                 LDP接口的标志  =  17
                  备份的版本号  =  30
           接收Hello消息的数量  =  18249
           发送Hello消息的数量  =  22029
                      地址数量  =  1
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPNEMGIF.md`
