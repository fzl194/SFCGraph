---
id: UNC@20.15.2@MMLCommand@DSP LDPLSPMGOUTSEG
type: MMLCommand
name: DSP LDPLSPMGOUTSEG（显示LDP LSP管理组件Outsegment转发表项）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LDPLSPMGOUTSEG
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

# DSP LDPLSPMGOUTSEG（显示LDP LSP管理组件Outsegment转发表项）

## 功能

该命令用于显示LDP LSP管理组件的Outsegment转发表项。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| FECADDR | 目的地址 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无<br>配置原则：当“PREFIXLENGTH”参数被输入的时候，该参数也必须输入。 |
| PREFIXLENGTH | 前缀长度 | 可选必选说明：可选参数<br>参数含义：该参数用于表示目的地址的前缀长度。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～32。<br>默认值：无<br>配置原则：当“FECADDR”参数被输入的时候，该参数也必须输入。 |
| PEERID | 对等体的LSR ID | 可选必选说明：可选参数<br>参数含义：该参数用于表示对等体的LSR ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LDPLSPMGOUTSEG]] · LDP LSP管理组件Outsegment转发表项（LDPLSPMGOUTSEG）

## 使用实例

显示LDP LSP管理组件Outsegment转发表项：

```
DSP LDPLSPMGOUTSEG:VRFNAME="_public_",FECADDR="192.168.1.1",PREFIXLENGTH=32;
```

```

RETCODE = 0  操作成功。

结果如下
--------
                      VPN实例名称  =  _public_
                         目的地址  =  192.168.1.1
                         前缀长度  =  32
                   对等体的LSR ID  =  192.168.1.1
                           下一跳  =  192.168.1.5
                           出接口  =  Ethernet66/0/4
                         主备角色  =  主路径
                   Outsegment索引  =  5008194
                           XC索引  =  5000066
                           出标签  =  3
                   LSP最大传输单元 =  1500
                  下转发成功的角色 =  入口和中间节点且优选
                 下转发失败的角色  =  空
                       老化标志位  =  FALSE
                          等待删除 =  FALSE
             是否是新建Outsegment  =  FALSE
               路由下一跳是否存在  =  TRUE
                       备份版本号  =  1
                       会话版本号  =  1
        上次更新到现在的时间（s）  =  422
                        LDP误码率  =  0e-0
                    自动恢复的状态 =  None
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-LDPLSPMGOUTSEG.md`
