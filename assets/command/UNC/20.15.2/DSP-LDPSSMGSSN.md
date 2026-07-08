---
id: UNC@20.15.2@MMLCommand@DSP LDPSSMGSSN
type: MMLCommand
name: DSP LDPSSMGSSN（显示LDP的会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPSSMGSSN
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

# DSP LDPSSMGSSN（显示LDP的会话信息）

## 功能

该命令用于显示LDP的会话信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_ |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LDPSSMGSSN]] · LDP的会话信息（LDPSSMGSSN）

## 使用实例

显示LDP的会话信息：

```
DSP LDPSSMGSSN:VRFNAME="_public_";
```

```

RETCODE = 0  操作成功。

结果如下
--------
                                VPN实例名称  =  _public_
                             对等体的LSR ID  =  10.10.10.10
                              LDP会话版本号  =  0
                                LDP会话类型  =  本地
                                LDP会话角色  =  被动端
                             对等体备份状态  =  LDP会话已经备份成功
                           通告业务管理状态  =  LDP会话已经备份成功
                                   协商状态  =  建立成功状态
                                   会话状态  =  LDP会话已经创建成功
                                   IP地址族  =  IPv4地址族
                        LDP本端的配置版本号  =  1
                        LDP本端的协议版本号  =  1
                 LDP本端的保活定时器值（s）  =  45
         LDP本端的保活消息发送时间间隔（s）  =  3
                       LDP本端的最大PDU长度  =  4100
           LDP本端建立TCP连接使用的传输地址  =  10.10.10.3
                      LDP对等体的配置版本号  =  1
                      LDP对等体的协议版本号  =  1
               LDP对等体的保活定时器值（s）  =  45
                     LDP对等体的最大PDU长度  =  4096
                       LDP对等体的GR FT标志  =  对等体关闭LDP GR功能
                 LDP对等体的重连接时间（s）  =  0
                   LDP对等体的恢复时间（s）  =  0
         LDP对等体建立TCP连接使用的传输地址  =  10.10.10.10
                     LDP会话协商的GR FT标志  =  LDP GR功能关闭
                                 定时器类型  =  无定时器
                  LDP重连接的剩余时间（ms）  =  0
               LDP会话慢删除定时器的值（s）  =  5
                   LDP协商的重连接时间（s）  =  0
                     LDP协商的恢复时间（s）  =  0
                    LDP与IGP联动的时间（s）  =  10
               LDP与IGP联动的剩余时间（ms）  =  0
 LDP建立会话失败后的指数回退定时器的值（s）  =  15
LDP建立会话失败后的指数回退的剩余时间（ms）  =  0
                     LDP保活定时器的值（s）  =  45
                    LDP保活的剩余时间（ms）  =  39000
             LDP发送保活消息的定时器值（s）  =  0
            LDP发送保活消息的剩余时间（ms）  =  0
                       LDP协商的最大PDU长度  =  4096
                      LDP水平分割策略的标识  =  水平分割功能关闭
                  LDP水平分割配置结点的标识  =  水平分割配置结点未完成
                    LDP远端对等体策略的标识  =  远端策略关闭
            LDP远端对等体策略配置结点的标识  =  远端策略未配置
                         LDP与IGP联动的标识  =  IGP已同步
                          LDP会话的删除原因  =  其他类原因
                          LDP会话的错误状态  =  成功
                  LDP会话发送的通告消息状态  =  成功
                         Socket返回的错误码  =  0
                    LDP主备组件间的定界标志  =  0
                      LDP与Socket的定界标志  =  15
                          LDP会话的侦听标志  =  64
                    LDP会话的备份平滑版本号  =  1
              LDP与协议管理之间的平滑版本号  =  1
              LDP与业务管理之间的平滑版本号  =  1
                    LDP分布式整数形式的编号  =  0
                     会话协商的标签发布模式  =  DU
                 处理标签发布模式变更的标识  =  处理标签发布模式未改变
                               远端会话类型  =  自动创建
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPSSMGSSN.md`
