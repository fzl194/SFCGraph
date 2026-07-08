---
id: UNC@20.15.2@MMLCommand@LST OSPF
type: MMLCommand
name: LST OSPF（查询OSPF进程配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OSPF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF进程配置
status: active
---

# LST OSPF（查询OSPF进程配置）

## 功能

该命令用于查询OSPF特性的进程的相关配置。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@OSPF]] · OSPF进程配置（OSPF）

## 使用实例

查询OSPF特性的进程的相关配置：

```
LST OSPF:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                                 进程号  =  1
                                VPN名称  =  _public_
                   抑制接口收发OSPF报文  =  FALSE
                                使能BFD  =  FALSE
            是否配置BFD最小接收报文间隔  =  FALSE
           接收BFD包的最小时间间隔（ms） =  200
            是否配置BFD最小发送报文间隔  =  FALSE
           发送BFD包的最小时间间隔（ms） =  200
                            BFD检测乘数  =  3
                            兼容RFC1583  =  TRUE
                     VPN引入路由的tag值  =  0
              计算链路开销参考值（Mbps） =  100
                         使能最大重传数  =  FALSE
                           最大重传限制  =  30
                         Opaque LSA能力  =  FALSE
                         使能可达性抑制  =  FALSE
                      接收时间间隔（ms） =  800
                  接收最长间隔时间（ms） =  1000
                  接收初始间隔时间（ms） =  500
                  接收基数间隔时间（ms） =  500
取消使用智能定时器配置LSA接收的间隔时间  =  FALSE
                       更新时间间隔（s） =  5
                  更新最长间隔时间（ms） =  5000
                  更新初始间隔时间（ms） =  500
                  更新基数间隔时间（ms） =  1000
           是否指定LSA更新的时间间隔为0  =  FALSE
                  去使能VPN路由环路检测  =  FALSE
                             Stub路由器  =  不配置
                 On-Startup时间间隔（s） =  500
                               安全同步  =  FALSE
                 配置VPN引入路由的tag值  =  FALSE
                    SPF计算间隔时间（s） =  0
                   SPF计算间隔时间（ms） =  0
               SPF计算最长间隔时间（ms） =  10000
               SPF计算初始间隔时间（ms） =  500
               SPF计算基数间隔时间（ms） =  1000
                    禁止使用tag检测环路  =  FALSE
                        使能ECA路由类型  =  FALSE
                      配置Domain ID为空  =  FALSE
                             路由器标识  =  NULL
                               描述信息  =  NULL
                        SPF正常模式标志  =  FALSE
                         使能Sham-hello  =  FALSE
               是否自动使能MPLS LDP功能  =  去使能
             OSPF共网段虚拟系统使能标志  =  FALSE
          BFD会话与接口链路状态绑定标志  =  FALSE
           是否为Stub链路发布最大开销值  =  FALSE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OSPF.md`
