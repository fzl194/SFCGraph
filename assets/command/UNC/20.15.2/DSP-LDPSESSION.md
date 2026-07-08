---
id: UNC@20.15.2@MMLCommand@DSP LDPSESSION
type: MMLCommand
name: DSP LDPSESSION（显示LDP会话）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPSESSION
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP会话
status: active
---

# DSP LDPSESSION（显示LDP会话）

## 功能

该命令用于显示LDP会话。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| PEERLSRID | 邻居LDP ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LDP标识符，格式为<LSR ID>：<标签空间>。标签空间取值： “0”表示全局标签空间。 “1”表示接口标签空间。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPSESSION]] · LDP会话（LDPSESSION）

## 使用实例

显示LDP会话：

```
DSP LDPSESSION:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                      VPN实例名称  =  _public_
                       邻居LDP ID  =  192.168.195.195:0
                       本地LDP ID  =  192.168.196.196:0
                        TCP源地址  =  192.168.196.196
                      TCP目的地址  =  192.168.195.195
                         会话状态  =  建立成功状态
                         会话角色  =  主动端
                         会话类型  =  本地
          KA保持定时器协商值（s）  =  45
                       KA发送计数  =  17
                       KA接收计数  =  17
                     标签发布模式  =  DU
                 邻居标签可用状态  =  可用
                       当前FT标记  =  FALSE
                      当前MD5标记  =  FALSE
         reconnect定时器的值（s）  =  NULL
          recovery定时器的值（s）  =  NULL
  session建立的时长（DDDD:HH:MM）  =  0000:00:03
                 会话动态通告能力  =  ENABLE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPSESSION.md`
