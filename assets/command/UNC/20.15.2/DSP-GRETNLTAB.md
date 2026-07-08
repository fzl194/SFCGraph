---
id: UNC@20.15.2@MMLCommand@DSP GRETNLTAB
type: MMLCommand
name: DSP GRETNLTAB（查询GRE隧道信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GRETNLTAB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- GRE调测
status: active
---

# DSP GRETNLTAB（查询GRE隧道信息）

## 功能

该命令用于查询GRE隧道信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLNAME | 隧道名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定隧道接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无 |

## 操作的配置对象

- [GRE隧道信息（GRETNLTAB）](configobject/UNC/20.15.2/GRETNLTAB.md)

## 使用实例

查询GRE隧道信息：

```
DSP GRETNLTAB:TNLNAME="tunnel1";
```

```

        RETCODE = 0  操作成功。

        结果如下
        --------
                      隧道名称 = Tunnel1
                    源IPv4地址 = 10.3.3.11
                    源IPv6地址 = ::
                      源接口名 = LoopBack1
                        源类型 = 接口名称
                   源VPN实例名 = _public_
                  目的IPv4地址 = 10.4.4.11
                  目的IPv6地址 = ::
                 目的VPN实例名 = _public_
                  保活定时器ID = 0
                  保活重试次数 = 0
                      保活标识 = 0
                      承载协议 = IPv4
                 隧道VPN实例名 = _public_
             隧道MTU值（byte） = 1500
                    IP地址状态 = 1
                      管理状态 = 1
        同源同目的地址冲突状态 = 0
                       VPN状态 = 1
            源地址路由可达标记 = 1
          目的地址路由可达标记 = 1
                    Socket状态 = 1
                      保活状态 = 0
              源目的IP不同状态 = 0
                源接口嵌套标记 = 0
                      产品状态 = 1
             源接口绑定GRE标记 = 0
            隧道上次DOWN的原因 = 源地址或接口、目的地址、VPN冲突检查失败
            隧道上次DOWN的时间 = [11 02:26:06:907]
            隧道历史DOWN的原因 = 源地址或接口、目的地址、VPN冲突检查失败
            隧道历史DOWN的时间 = [11 02:25:54:530]
            隧道历史DOWN的原因 = 源地址或接口、目的地址、VPN冲突检查失败
            隧道历史DOWN的时间 = [11 02:25:49:374]
            隧道历史DOWN的原因 = 源地址或接口、目的地址、VPN冲突检查失败
            隧道历史DOWN的时间 = [11 02:25:42:785]
            隧道历史DOWN的原因 = 源地址或接口、目的地址、VPN冲突检查失败
            隧道历史DOWN的时间 = [11 02:25:37:785]

        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GRE隧道信息（DSP-GRETNLTAB）_00840669.md`
