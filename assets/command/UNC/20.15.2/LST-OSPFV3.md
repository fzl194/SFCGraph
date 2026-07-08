---
id: UNC@20.15.2@MMLCommand@LST OSPFV3
type: MMLCommand
name: LST OSPFV3（查询OSPFv3进程配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPFV3
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- OSPFv3进程配置
status: active
---

# LST OSPFV3（查询OSPFv3进程配置）

## 功能

该命令用于查询OSPFv3进程配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3进程配置（OSPFV3）](configobject/UNC/20.15.2/OSPFV3.md)

## 使用实例

查询OSPFv3进程配置：

```
LST OSPFV3:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                 OSPFv3进程号  =  1
                   路由器标识  =  10.175.11.1
                      VPN名称  =  _public_
       抑制接口收发OSPFv3报文  =  FALSE
                      使能BFD  =  FALSE
  是否配置BFD最小接收报文间隔  =  FALSE
 接收BFD包的最小时间间隔（ms） =  200
  是否配置BFD最小发送报文间隔  =  FALSE
 发送BFD包的最小时间间隔（ms） =  200
              BFD检测乘数间隔  =  3
           VPN引入路由的tag值  =  0
    计算链路开销参考值（Mbps） =  100
             使能最大重传次数  =  FALSE
                 最大重传限制  =  30
            配置Domain ID为空  =  FALSE
        去使能VPN路由环路检测  =  FALSE
       配置VPN引入路由的tag值  =  FALSE
           去使能标签环路检测  =  FALSE
            OSPFv3 Stub路由器  =  主备倒换中为Stub路由器
       On-Startup时间间隔（s） =  100
                     描述信息  =  NULL
 OSPFv3共网段虚拟系统使能标志  =  FALSE
                 IPsec SA名称  =  NULL
     SPF计算最长间隔时间（ms） =  1
     SPF计算初始间隔时间（ms） =  1
     SPF计算基数间隔时间（ms） =  1
          SPF计算延迟时间（s） =  5
      SPF计算抑制间隔时间（s） =  10
BFD会话与接口链路状态绑定标志  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPFv3进程配置（LST-OSPFV3）_00441233.md`
